

"""Common Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import CommonValidator

class Common:
    def __init__(self, config):
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
    
    async def searchApplication(self, authorization=None, query=None, body=""):
        """Provide application name or domain url
        :param authorization :  : type string
        :param query : Provide application name : type string
        """
        payload = {}
        
        if authorization:
            payload["authorization"] = authorization
        
        if query:
            payload["query"] = query
        
        # Parameter validation
        schema = CommonValidator.searchApplication()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["searchApplication"], proccessed_params="""{"required":[],"optional":[{"in":"header","name":"authorization","schema":{"type":"string"}},{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"query":[{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"headers":[{"in":"header","name":"authorization","schema":{"type":"string"}}],"path":[]}""", authorization=authorization, query=query)
        query_string = await create_query_string(authorization=authorization, query=query)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["searchApplication"]).netloc, "get", await create_url_without_domain("/service/common/configuration/v1.0/application/search-application", authorization=authorization, query=query), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import ApplicationResponse
        schema = ApplicationResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for searchApplication")
            print(e)

        

        return response
    
    async def getLocations(self, location_type=None, id=None, body=""):
        """
        :param location_type : Provide location type to query on. Possible values : country, state, city : type string
        :param id : Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state. : type string
        """
        payload = {}
        
        if location_type:
            payload["location_type"] = location_type
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CommonValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocations"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"query":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"headers":[],"path":[]}""", location_type=location_type, id=id)
        query_string = await create_query_string(location_type=location_type, id=id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLocations"]).netloc, "get", await create_url_without_domain("/service/common/configuration/v1.0/location", location_type=location_type, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import Locations
        schema = Locations()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getLocations")
            print(e)

        

        return response
    

