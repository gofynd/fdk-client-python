

""" Common Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import CommonValidator

class Common:
    def __init__(self, config):
        self._conf = config
    
    async def searchApplication(self, authorization=None, query=None):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/common/configuration/v1.0/application/search-application", """{"required":[],"optional":[{"in":"header","name":"authorization","schema":{"type":"string"}},{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"query":[{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"headers":[{"in":"header","name":"authorization","schema":{"type":"string"}}],"path":[]}""", authorization=authorization, query=query)
        query_string = await create_query_string(authorization=authorization, query=query)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/common/configuration/v1.0/application/search-application", authorization=authorization, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getLocations(self, location_type=None, id=None):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/common/configuration/v1.0/location", """{"required":[],"optional":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"query":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"headers":[],"path":[]}""", location_type=location_type, id=id)
        query_string = await create_query_string(location_type=location_type, id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/common/configuration/v1.0/location", location_type=location_type, id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
