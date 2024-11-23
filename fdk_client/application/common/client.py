"""Common Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import CommonValidator

class Common:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "searchApplication": "/service/common/configuration/v1.0/application/search-application",
            "getLocations": "/service/common/configuration/v1.0/location"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def searchApplication(self, authorization=None, query=None, body="", request_headers:Dict={}):
        """Get an active sales channel based on a provided query. The query can be a valid sales channel ID or a verified domain name. If the sales channel is found, a success response is returned. If not, a 404 error response is returned.
        :param authorization : Basic auth string to access the api endpoint. : type string
        :param query : Provide application name. : type string
        """
        payload = {}
        
        if authorization is not None:
            payload["authorization"] = authorization
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommonValidator.searchApplication()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["searchApplication"], proccessed_params="""{"required":[],"optional":[{"in":"header","name":"authorization","schema":{"type":"string"},"description":"Basic auth string to access the api endpoint."},{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name."}],"query":[{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name."}],"headers":[{"in":"header","name":"authorization","schema":{"type":"string"},"description":"Basic auth string to access the api endpoint."}],"path":[]}""", serverType="application", authorization=authorization, query=query)
        query_string = await create_query_string(query=query)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["searchApplication"]).netloc, "get", await create_url_without_domain("/service/common/configuration/v1.0/application/search-application", authorization=authorization, query=query), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationResponseSchema
            schema = ApplicationResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for searchApplication")
                print(e)

        return response
    
    async def getLocations(self, location_type=None, id=None, body="", request_headers:Dict={}):
        """Get countries , state , cities data associated with the sales channel.
        :param location_type : Provide location type to query on. Possible values : country, state, city. : type string
        :param id : Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state. : type string
        """
        payload = {}
        
        if location_type is not None:
            payload["location_type"] = location_type
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommonValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocations"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city."},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"query":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city."},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"headers":[],"path":[]}""", serverType="application", location_type=location_type, id=id)
        query_string = await create_query_string(location_type=location_type, id=id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLocations"]).netloc, "get", await create_url_without_domain("/service/common/configuration/v1.0/location", location_type=location_type, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Locations
            schema = Locations()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocations")
                print(e)

        return response
    