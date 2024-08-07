"""Partner Public Client"""

from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PublicConfig import PublicConfig

from .validator import PartnerValidator

class Partner:
    def __init__(self, config: PublicConfig):
        self._conf = config
        self._relativeUrls = {
            "getPanelExtensionDetails": "/service/panel/partners/v1.0/extensions/{slug}"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getPanelExtensionDetails(self, slug=None, body="", request_headers:Dict={}):
        """Retrieve detailed information about panel extensions in the public server setup.
        :param slug : pass the slug of the extension : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = PartnerValidator.getPanelExtensionDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPanelExtensionDetails"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"pass the slug of the extension","required":true,"schema":{"type":"string"},"example":"example-extension-1"}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"pass the slug of the extension","required":true,"schema":{"type":"string"},"example":"example-extension-1"}]}""", serverType="public", slug=slug)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPanelExtensionDetails"]).netloc, "get", await create_url_without_domain("/service/panel/partners/v1.0/extensions/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ExtensionUsingSlug
            schema = ExtensionUsingSlug()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPanelExtensionDetails")
                print(e)

        return response
    