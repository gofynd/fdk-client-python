

"""  Administrator Client."""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import CommunicationValidator

class Communication:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "sendSellerCommunicationSynchronously": "/service/___/administrator/communication/v1.0/platform/send-comms/send-instant",
            "sendSellerCommunicationAsynchronously": "/service/___/administrator/communication/v1.0/platform/send-comms/send-async"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def sendSellerCommunicationSynchronously(self, body=""):
        """Send email or sms synchronously
        """
        payload = {}
        
        # Parameter validation
        schema = CommunicationValidator.sendSellerCommunicationSynchronously()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EngineRequest
        schema = EngineRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendSellerCommunicationSynchronously"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendSellerCommunicationSynchronously"]).netloc, "post", await create_url_without_domain("/service/___/administrator/communication/v1.0/platform/send-comms/send-instant", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import EngineResponse
        schema = EngineResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for sendSellerCommunicationSynchronously")
            print(e)

        

        return response
    
    async def sendSellerCommunicationAsynchronously(self, body=""):
        """Send email or sms asynchronously
        """
        payload = {}
        
        # Parameter validation
        schema = CommunicationValidator.sendSellerCommunicationAsynchronously()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EngineRequest
        schema = EngineRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendSellerCommunicationAsynchronously"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendSellerCommunicationAsynchronously"]).netloc, "post", await create_url_without_domain("/service/___/administrator/communication/v1.0/platform/send-comms/send-async", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import EngineResponse
        schema = EngineResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for sendSellerCommunicationAsynchronously")
            print(e)

        

        return response
    

