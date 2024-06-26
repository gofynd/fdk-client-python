"""Billing Public Client"""

from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PublicConfig import PublicConfig

from .validator import BillingValidator

class Billing:
    def __init__(self, config: PublicConfig):
        self._conf = config
        self._relativeUrls = {
            "getStandardPlans": "/service/public/billing/v1.0/plan/detailed-list"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getStandardPlans(self, platform=None, body="", request_headers:Dict={}):
        """Get Standard/Public Plans.

        :param platform : The type of platform for which plans are requested. : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = BillingValidator.getStandardPlans()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getStandardPlans"], proccessed_params="""{"required":[{"name":"platform","in":"query","description":"The type of platform for which plans are requested.","required":true,"schema":{"type":"string","example":"mobile/web/both"}}],"optional":[],"query":[{"name":"platform","in":"query","description":"The type of platform for which plans are requested.","required":true,"schema":{"type":"string","example":"mobile/web/both"}}],"headers":[],"path":[]}""", serverType="public", platform=platform)
        query_string = await create_query_string(platform=platform)

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getStandardPlans"]).netloc, "get", await create_url_without_domain("/service/public/billing/v1.0/plan/detailed-list", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DetailList
            schema = DetailList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStandardPlans")
                print(e)

        return response
    