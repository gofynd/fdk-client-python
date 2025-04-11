"""Communication Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import CommunicationValidator

class Communication:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "getCommunicationConsent": "/service/application/communication/v1.0/consent",
            "upsertCommunicationConsent": "/service/application/communication/v1.0/consent",
            "getCurrentCommunicationConsent": "/service/application/communication/v1.0/current/communication/consent",
            "upsertCurrentCommunicationConsent": "/service/application/communication/v1.0/current/communication/consent",
            "getOtpConfiguration": "/service/application/communication/v1.0/otp/otp-configuration"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getCommunicationConsent(self, body="", request_headers:Dict={}):
        """Get the consent provided by the user for receiving communication.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getCommunicationConsent()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCommunicationConsent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCommunicationConsent"]).netloc, "get", await create_url_without_domain("/service/application/communication/v1.0/consent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CommunicationConsent
            schema = CommunicationConsent()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCommunicationConsent")
                print(e)

        return response
    
    async def upsertCommunicationConsent(self, body="", request_headers:Dict={}):
        """Update or insert the consent provided by the user for receiving communication messages.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.upsertCommunicationConsent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CommunicationConsentReq
        schema = CommunicationConsentReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["upsertCommunicationConsent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["upsertCommunicationConsent"]).netloc, "post", await create_url_without_domain("/service/application/communication/v1.0/consent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CommunicationConsentRes
            schema = CommunicationConsentRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for upsertCommunicationConsent")
                print(e)

        return response
    
    async def getCurrentCommunicationConsent(self, body="", request_headers:Dict={}):
        """Retrieve the consent provided by the user for receiving communication messages over Email/SMS/WhatsApp. .
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getCurrentCommunicationConsent()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCurrentCommunicationConsent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCurrentCommunicationConsent"]).netloc, "get", await create_url_without_domain("/service/application/communication/v1.0/current/communication/consent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CommunicationConsent
            schema = CommunicationConsent()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCurrentCommunicationConsent")
                print(e)

        return response
    
    async def upsertCurrentCommunicationConsent(self, body="", request_headers:Dict={}):
        """Update and insert the consent provided by the user for receiving communication messages over Email/SMS/WhatsApp. .
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.upsertCurrentCommunicationConsent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CommunicationConsentReq
        schema = CommunicationConsentReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["upsertCurrentCommunicationConsent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["upsertCurrentCommunicationConsent"]).netloc, "post", await create_url_without_domain("/service/application/communication/v1.0/current/communication/consent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CommunicationConsentRes
            schema = CommunicationConsentRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for upsertCurrentCommunicationConsent")
                print(e)

        return response
    
    async def getOtpConfiguration(self, body="", request_headers:Dict={}):
        """Get otp-configuration.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getOtpConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOtpConfiguration"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOtpConfiguration"]).netloc, "get", await create_url_without_domain("/service/application/communication/v1.0/otp/otp-configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OtpConfiguration
            schema = OtpConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOtpConfiguration")
                print(e)

        return response
    