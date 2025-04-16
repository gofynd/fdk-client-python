"""Content Public Client"""

from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PublicConfig import PublicConfig

from .validator import ContentValidator

class Content:
    def __init__(self, config: PublicConfig):
        self._conf = config
        self._relativeUrls = {
            "getCredentialsByEntity": "/service/public/content/credentials/{entity}"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getCredentialsByEntity(self, entity=None, body="", request_headers:Dict={}):
        """Get credentials for support system
        :param entity : Server Type : type string
        """
        payload = {}
        
        if entity is not None:
            payload["entity"] = entity

        # Parameter validation
        schema = ContentValidator.getCredentialsByEntity()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCredentialsByEntity"], proccessed_params="""{"required":[{"in":"path","name":"entity","description":"Server Type","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"entity","description":"Server Type","required":true,"schema":{"type":"string"}}]}""", serverType="public", entity=entity)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCredentialsByEntity"]).netloc, "get", await create_url_without_domain("/service/public/content/credentials/{entity}", entity=entity), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CredentialsSchema
            schema = CredentialsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCredentialsByEntity")
                print(e)

        return response
    