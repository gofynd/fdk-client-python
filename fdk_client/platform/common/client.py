"""Common Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import CommonValidator

class Common:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def searchApplication(self, authorization=None, query=None, request_headers:Dict={}):
        """This API retrieves details for a specific sales channel based on the provided search criteria. The search can be performed using the name of the sales channel
        :param authorization :  : type string
        :param query : Provide application name : type string
        """
        payload = {}
        
        if authorization is not None:
            payload["authorization"] = authorization
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommonValidator.searchApplication()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/common/configuration/v1.0/application/search-application", """{"required":[],"optional":[{"in":"header","name":"authorization","schema":{"type":"string"}},{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"query":[{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"headers":[{"in":"header","name":"authorization","schema":{"type":"string"}}],"path":[]}""", serverType="platform", authorization=authorization, query=query)
        query_string = await create_query_string(authorization=authorization, query=query)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/common/configuration/v1.0/application/search-application", authorization=authorization, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationResponse
            schema = ApplicationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for searchApplication")
                print(e)

        return response
    
    async def getLocations(self, location_type=None, id=None, request_headers:Dict={}):
        """Retrieve a list of locations associated with the company.
        :param location_type :  : type string
        :param id : Field is optional when location_type is country. If querying for state, provide id of the country. If querying for city, provide id of the state. : type string
        """
        payload = {}
        
        if location_type is not None:
            payload["location_type"] = location_type
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommonValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/common/configuration/v1.0/location", """{"required":[],"optional":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]}},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of the country. If querying for city, provide id of the state."}],"query":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]}},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of the country. If querying for city, provide id of the state."}],"headers":[],"path":[]}""", serverType="platform", location_type=location_type, id=id)
        query_string = await create_query_string(location_type=location_type, id=id)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/common/configuration/v1.0/location", location_type=location_type, id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Locations
            schema = Locations()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocations")
                print(e)

        return response
    