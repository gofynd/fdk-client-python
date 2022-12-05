"""OAuth Client."""

from threading import Timer
from typing import Dict
from urllib import parse
import base64
import asyncio

from ..common.exceptions import FDKOAuthCodeError, FDKTokenIssueError
from ..common.aiohttp_helper import AiohttpHelper
from ..common.utils import get_headers_with_signature
import time


refresh_token_request_cache = {}


class OAuthClient:
    def __init__(self, config):
        self._conf = config
        self.token = None
        self.refreshToken = None
        self.retryOAuthTokenTimer: Timer = None
        self.raw_token = None
        self.token_expires_in = None
        self.token_expires_at = 0
        self.useAutoRenewTimer = config.useAutoRenewTimer if config.useAutoRenewTimer != None else True


    # renew access token if token is about to expire in 2mins(120s) and auto renew time is not enabled
    async def getAccessToken(self):
        if (not self.useAutoRenewTimer and self.refreshToken and self.is_token_expired(120)):
            await self.renewAccessToken()
         
        # return already generated token if token is not expired
        return self.token


    # returns True if token is about to expire in "ttl" time
    def is_token_expired(self, ttl=0):
        current_timestamp = self.get_current_timestamp()
        if ((self.token_expires_at-current_timestamp)/1000 < ttl):
            return True
        return False


    # returns timestamp in milliseconds
    # JS/Java equivalent of `new Date().getTime()`
    def get_current_timestamp(self):
        return time.time_ns() // 1_000_000


    def setToken(self, token):
        self.raw_token = token
        self.token_expires_in = token.get("expires_in")
        self.token = token.get("access_token")
        self.refreshToken = token.get("refresh_token") if token.get("refresh_token") else None
        if self.refreshToken and self.useAutoRenewTimer:
            self.retryOAuthToken(token.get("expires_in"))

    def retryOAuthToken(self, expires_in):
        if self.retryOAuthTokenTimer:
            self.retryOAuthTokenTimer.cancel()
        if expires_in > 60:
            self.retryOAuthTokenTimer = Timer(float(expires_in - 60), lambda: asyncio.run(self.renewAccessToken()))
            self.retryOAuthTokenTimer.start()

    def startAuthorization(self, options: Dict):
        query = {
            "access_mode": options.get("access_mode", ""),
            "client_id": self._conf.apiKey,
            "redirect_uri": options.get("redirectUri", ""),
            "response_type": "code",
            "scope": ",".join(options.get("scope", [])),
            "state": options.get("state", "")
        }
        queryString = parse.urlencode(query)
        reqPath = f"/service/panel/authentication/v1.0/company/{self._conf.companyId}/oauth/authorize"
        signingOptions = {
          "method": "GET",
          "host": self._conf.domain,
          "path": reqPath,
          "body": None,
          "headers": {},
          "signQuery": True
        }
        queryString = asyncio.run(get_headers_with_signature(self._conf.domain, "get",
                                                            f"/service/panel/authentication/v1.0/company/"
                                                            f"{self._conf.companyId}/oauth/authorize",
                                                            queryString, {}, sign_query=True))
        return f"{self._conf.domain}{signingOptions['path']}?{queryString}"

    async def verifyCallback(self, query):
        if query.get("error"):
            raise FDKOAuthCodeError(query["error_description"])
        try:
            res = await self.getAccesstokenObj(grant_type="authorization_code", code=query.get("code", ""))
            self.setToken(res)
            self.token_expires_at = self.get_current_timestamp() + self.token_expires_in * 1000
        except Exception as e:
            raise FDKTokenIssueError(str(e))

    # cache refresh token request
    async def renewAccessToken(self, is_offline_token=False):
        if is_offline_token:
            request_cache_key = f"{self._conf.apiKey}:{self._conf.companyId}"
            if not refresh_token_request_cache[request_cache_key]:
                refresh_token_request_cache[request_cache_key] = self.getAccesstokenObj(
                    grant_type='refresh_token',
                    refresh_token=self.refreshToken
                )
            try:
                res = await refresh_token_request_cache[request_cache_key]
            except Exception as e:
                raise FDKTokenIssueError(str(e))
            finally:
                del refresh_token_request_cache[request_cache_key]

        else:
            res = await self.getAccesstokenObj(grant_type="refresh_token", refresh_token=self.refreshToken)
        
        self.setToken(res)
        self.token_expires_at = self.get_current_timestamp() + self.token_expires_in * 1000
        return res

    async def getAccesstokenObj(self, grant_type="", refresh_token="", code=""):
        reqData = {
            "grant_type": grant_type,
        }
        if grant_type == "refresh_token":
            reqData = {**reqData, "refresh_token": refresh_token}
        elif grant_type == "authorization_code":
            reqData = {**reqData, "code": code}

        token = base64.b64encode(f"{self._conf.apiKey}:{self._conf.apiSecret}".encode()).decode()
        url = f"{self._conf.domain}/service/panel/authentication/v1.0/company/{self._conf.companyId}/oauth/token"
        headers = {
            "Authorization": f"Basic {token}"
        }
        headers = await get_headers_with_signature(self._conf.domain, "post",
                                             f"/service/panel/authentication/v1.0/company/{self._conf.companyId}/oauth/token",
                                             "", headers, reqData, ["Authorization"])
        response = await AiohttpHelper().aiohttp_request("POST", url, reqData, headers)
        return response["json"]


    async def getOfflineAccessToken(self, scopes, code):
        try:
            res = await self.getOfflineAccessTokenObj(scopes, code)
            self.setToken(res)
            self.token_expires_at = self.get_current_timestamp() + self.token_expires_in * 1000
            return res
        except Exception as e:
            raise FDKTokenIssueError(str(e))

    
    async def getOfflineAccessTokenObj(self, scopes, code):
        url = f"{self._conf.domain}/servide/panel/authentication/v1.0/company/{self._conf.companyId}/oauth/offline-token"
        data = {
            "client_id": self._conf.apiKey,
            "client_secret": self._conf.apiSecret,
            "grant_type": "authorization_code",
            "scope": scopes,
            "code": code
        }
        token = base64.b64encode(f"{self._conf.apiKey}:{self._conf.apiSecret}".encode()).decode()
        headers = {
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json"
        }
        # getting x-fp-signature 
        headers = await get_headers_with_signature(
            domain=self._conf.domain,
            method="post",
            url=f"/servide/panel/authentication/v1.0/company/{self._conf.companyId}/oauth/offline-token",
            query_string="",
            headers=headers,
            body=data,
            exclude_headers=list(headers.keys())
        )
        response = await AiohttpHelper().aiohttp_request(request_type="POST", url=url, data=data, headers=headers)
        return response["json"]