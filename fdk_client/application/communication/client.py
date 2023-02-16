

"""Communication Application Client"""

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
            "getCommunicationConsent": "/service/application/communication/v1.0/consent",
            "upsertCommunicationConsent": "/service/application/communication/v1.0/consent",
            "upsertAppPushtoken": "/service/application/communication/v1.0/pn-token"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getCommunicationConsent(self, body=""):
        """Use this API to retrieve the consent provided by the user for receiving communication messages over Email/SMS/WhatsApp.
        """
        payload = {}
        
        # Parameter validation
        schema = CommunicationValidator.getCommunicationConsent()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCommunicationConsent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCommunicationConsent"]).netloc, "get", await create_url_without_domain("/service/application/communication/v1.0/consent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def upsertCommunicationConsent(self, body=""):
        """Use this API to update and insert the consent provided by the user for receiving communication messages over Email/SMS/WhatsApp.
        """
        payload = {}
        
        # Parameter validation
        schema = CommunicationValidator.upsertCommunicationConsent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CommunicationConsentReq import CommunicationConsentReq
        schema = CommunicationConsentReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["upsertCommunicationConsent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["upsertCommunicationConsent"]).netloc, "post", await create_url_without_domain("/service/application/communication/v1.0/consent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def upsertAppPushtoken(self, body=""):
        """Use this API to update and insert the push token of the user.
        """
        payload = {}
        
        # Parameter validation
        schema = CommunicationValidator.upsertAppPushtoken()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PushtokenReq import PushtokenReq
        schema = PushtokenReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["upsertAppPushtoken"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["upsertAppPushtoken"]).netloc, "post", await create_url_without_domain("/service/application/communication/v1.0/pn-token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

