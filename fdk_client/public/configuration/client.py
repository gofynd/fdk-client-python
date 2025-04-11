"""Configuration Public Client"""

from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PublicConfig import PublicConfig

from .validator import ConfigurationValidator

class Configuration:
    def __init__(self, config: PublicConfig):
        self._conf = config
        self._relativeUrls = {
            "searchApplication": "/service/public/configuration/v1.0/application/search-application",
            "getLocations": "/service/public/configuration/v1.0/location",
            "checkVersionIsUpToDate": "/service/public/configuration/v1.0/version"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def searchApplication(self, authorization=None, query=None, body="", request_headers:Dict={}):
        """Provide application name or domain url.
        :param authorization :  : type string
        :param query : Provide application name : type string
        """
        payload = {}
        
        if authorization is not None:
            payload["authorization"] = authorization
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = ConfigurationValidator.searchApplication()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["searchApplication"], proccessed_params="""{"required":[],"optional":[{"in":"header","name":"authorization","schema":{"type":"string"}},{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"query":[{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"headers":[{"in":"header","name":"authorization","schema":{"type":"string"}}],"path":[]}""", serverType="public", authorization=authorization, query=query)
        query_string = await create_query_string(query=query)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["searchApplication"]).netloc, "get", await create_url_without_domain("/service/public/configuration/v1.0/application/search-application", authorization=authorization, query=query), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        """Get Location configuration
        :param location_type : Provide location type to query on. Possible values : country, state, city : type string
        :param id : Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state. : type string
        """
        payload = {}
        
        if location_type is not None:
            payload["location_type"] = location_type
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ConfigurationValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocations"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"query":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"headers":[],"path":[]}""", serverType="public", location_type=location_type, id=id)
        query_string = await create_query_string(location_type=location_type, id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLocations"]).netloc, "get", await create_url_without_domain("/service/public/configuration/v1.0/location", location_type=location_type, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Locations
            schema = Locations()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocations")
                print(e)

        return response
    
    async def checkVersionIsUpToDate(self, body="", request_headers:Dict={}):
        """Check if the application version is up to date.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.checkVersionIsUpToDate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VersionRequestSchema
        schema = VersionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["checkVersionIsUpToDate"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["checkVersionIsUpToDate"]).netloc, "post", await create_url_without_domain("/service/public/configuration/v1.0/version", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import VersionResponseSchema
            schema = VersionResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkVersionIsUpToDate")
                print(e)

        return response
    