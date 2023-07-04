

"""  Public Client."""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import WebhookValidator

class Webhook:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "fetchAllWebhookEvents": "/service/common/webhook/v1.0/events",
            "queryWebhookEventDetails": "/service/common/webhook/v1.0/events/query-event-details"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def fetchAllWebhookEvents(self, body=""):
        """Get All Webhook Events
        """
        payload = {}
        
        # Parameter validation
        schema = WebhookValidator.fetchAllWebhookEvents()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["fetchAllWebhookEvents"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["fetchAllWebhookEvents"]).netloc, "get", await create_url_without_domain("/service/common/webhook/v1.0/events", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def queryWebhookEventDetails(self, body=""):
        """Get Webhook Event Details for provided events
        """
        payload = {}
        
        # Parameter validation
        schema = WebhookValidator.queryWebhookEventDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["queryWebhookEventDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["queryWebhookEventDetails"]).netloc, "post", await create_url_without_domain("/service/common/webhook/v1.0/events/query-event-details", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

