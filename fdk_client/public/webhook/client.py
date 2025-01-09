"""Webhook Public Client"""

from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PublicConfig import PublicConfig

from .validator import WebhookValidator

class Webhook:
    def __init__(self, config: PublicConfig):
        self._conf = config
        self._relativeUrls = {
            "fetchAllWebhookEvents": "/service/common/webhook/v1.0/events",
            "queryWebhookEventDetails": "/service/common/webhook/v1.0/events/query-event-details",
            "notifyDepricatedEvent": "/service/common/webhook/v1.0/events/depricated-event-notifier",
            "testHandlerTransformation": "/service/common/webhook/v1.0/events/transform-event",
            "validateSchema": "/service/common/webhook/v1.0/events/validate-event-schema"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def fetchAllWebhookEvents(self, body="", request_headers:Dict={}):
        """Retrieve a list of all webhook events in the public server setup.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.fetchAllWebhookEvents()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["fetchAllWebhookEvents"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["fetchAllWebhookEvents"]).netloc, "get", await create_url_without_domain("/service/common/webhook/v1.0/events", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventDetails
            schema = EventDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchAllWebhookEvents")
                print(e)

        return response
    
    async def queryWebhookEventDetails(self, body="", request_headers:Dict={}):
        """Query and obtain detailed information about webhook events in the public server configurations.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.queryWebhookEventDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["queryWebhookEventDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["queryWebhookEventDetails"]).netloc, "post", await create_url_without_domain("/service/common/webhook/v1.0/events/query-event-details", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventDetails
            schema = EventDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for queryWebhookEventDetails")
                print(e)

        return response
    
    async def notifyDepricatedEvent(self, body="", request_headers:Dict={}):
        """Notifies all the events that are subscribed and are going to deprecate or new version is available for those events
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.notifyDepricatedEvent()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["notifyDepricatedEvent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["notifyDepricatedEvent"]).netloc, "get", await create_url_without_domain("/service/common/webhook/v1.0/events/depricated-event-notifier", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventNotifier
            schema = EventNotifier()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for notifyDepricatedEvent")
                print(e)

        return response
    
    async def testHandlerTransformation(self, body="", request_headers:Dict={}):
        """Test transformation of handler
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.testHandlerTransformation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TransformEventPayload
        schema = TransformEventPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["testHandlerTransformation"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["testHandlerTransformation"]).netloc, "post", await create_url_without_domain("/service/common/webhook/v1.0/events/transform-event", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TransformEventResult
            schema = TransformEventResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for testHandlerTransformation")
                print(e)

        return response
    
    async def validateSchema(self, body="", request_headers:Dict={}):
        """Validate Schema for an event
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.validateSchema()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateSchemaPayload
        schema = ValidateSchemaPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["validateSchema"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["validateSchema"]).netloc, "post", await create_url_without_domain("/service/common/webhook/v1.0/events/validate-event-schema", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ValidateSchemaResult
            schema = ValidateSchemaResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateSchema")
                print(e)

        return response
    