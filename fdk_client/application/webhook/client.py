"""Webhook Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import WebhookValidator

class Webhook:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "saveClickEvent": "/service/application/webhook/v1.0/click-analytics/events"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def saveClickEvent(self, body="", request_headers:Dict={}):
        """Send click events from sales channels.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.saveClickEvent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ClickEventRequest
        schema = ClickEventRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["saveClickEvent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["saveClickEvent"]).netloc, "post", await create_url_without_domain("/service/application/webhook/v1.0/click-analytics/events", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ClickEventResponse
            schema = ClickEventResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for saveClickEvent")
                print(e)

        return response
    