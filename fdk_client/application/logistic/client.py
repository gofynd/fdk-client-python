

"""Logistic Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import LogisticValidator

class Logistic:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getPincodeCity": "/service/application/logistics/v1.0/pincode/{pincode}",
            "getTatProduct": "/service/application/logistics/v1.0/",
            "getAllCountries": "/service/application/logistics/v1.0/country-list",
            "getPincodeZones": "/service/application/logistics/v1.0/pincode/zones",
            "getOptimalLocations": "/service/application/logistics/v1.0/reassign_stores",
            "getCountries": "/service/application/logistics/v1.0/country",
            "getCountry": "/service/application/logistics/v1.0/country/{uid}",
            "getLocalities": "/service/application/logistics/v1.0/locality/{region}",
            "getLocality": "/service/application/logistics/v1.0/locality/{region}/{value}"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getPincodeCity(self, pincode=None, body=""):
        """Get pincode data
        :param pincode : A `pincode` contains a specific address of a location. : type string
        """
        payload = {}
        
        if pincode is not None:
            payload["pincode"] = pincode
        
        # Parameter validation
        schema = LogisticValidator.getPincodeCity()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPincodeCity"], proccessed_params="""{"required":[{"in":"path","name":"pincode","description":"A `pincode` contains a specific address of a location.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"pincode","description":"A `pincode` contains a specific address of a location.","schema":{"type":"string"},"required":true}]}""", pincode=pincode)
        query_string = await create_query_string(pincode=pincode)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPincodeCity"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/pincode/{pincode}", pincode=pincode), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeApiResponse
            schema = PincodeApiResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPincodeCity")
                print(e)

        

        return response
    
    async def getTatProduct(self, body=""):
        """Get TAT data
        """
        payload = {}
        
        # Parameter validation
        schema = LogisticValidator.getTatProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TATViewRequest
        schema = TATViewRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getTatProduct"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getTatProduct"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import TATViewResponse
            schema = TATViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTatProduct")
                print(e)

        

        return response
    
    async def getAllCountries(self, body=""):
        """Get all countries
        """
        payload = {}
        
        # Parameter validation
        schema = LogisticValidator.getAllCountries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAllCountries"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAllCountries"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/country-list", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CountryListResponse
            schema = CountryListResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllCountries")
                print(e)

        

        return response
    
    async def getPincodeZones(self, body=""):
        """This API returns zone from the Pincode View.
        """
        payload = {}
        
        # Parameter validation
        schema = LogisticValidator.getPincodeZones()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetZoneFromPincodeViewRequest
        schema = GetZoneFromPincodeViewRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPincodeZones"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPincodeZones"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/pincode/zones", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import GetZoneFromPincodeViewResponse
            schema = GetZoneFromPincodeViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPincodeZones")
                print(e)

        

        return response
    
    async def getOptimalLocations(self, body=""):
        """This API returns zone from the Pincode View.
        """
        payload = {}
        
        # Parameter validation
        schema = LogisticValidator.getOptimalLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ReAssignStoreRequest
        schema = ReAssignStoreRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOptimalLocations"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOptimalLocations"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/reassign_stores", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import ReAssignStoreResponse
            schema = ReAssignStoreResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOptimalLocations")
                print(e)

        

        return response
    
    async def getCountries(self, body=""):
        """Get countries data
        """
        payload = {}
        
        # Parameter validation
        schema = LogisticValidator.getCountries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCountries"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCountries"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/country", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import GetCountries
            schema = GetCountries()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCountries")
                print(e)

        

        return response
    
    async def getCountry(self, uid=None, body=""):
        """Get country data
        :param uid : A `uid` contains a specific unique name of a region. : type string
        """
        payload = {}
        
        if uid is not None:
            payload["uid"] = uid
        
        # Parameter validation
        schema = LogisticValidator.getCountry()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCountry"], proccessed_params="""{"required":[{"in":"path","name":"uid","description":"A `uid` contains a specific unique name of a region.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"uid","description":"A `uid` contains a specific unique name of a region.","schema":{"type":"string"},"required":true}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCountry"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/country/{uid}", uid=uid), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import GetCountry
            schema = GetCountry()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCountry")
                print(e)

        

        return response
    
    async def getLocalities(self, region=None, body=""):
        """Get Localities data
        :param region : A `region` contains a specific unique name. : type string
        """
        payload = {}
        
        if region is not None:
            payload["region"] = region
        
        # Parameter validation
        schema = LogisticValidator.getLocalities()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocalities"], proccessed_params="""{"required":[{"in":"path","name":"region","description":"A `region` contains a specific unique name.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"region","description":"A `region` contains a specific unique name.","schema":{"type":"string"},"required":true}]}""", region=region)
        query_string = await create_query_string(region=region)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLocalities"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/locality/{region}", region=region), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import GetLocalities
            schema = GetLocalities()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocalities")
                print(e)

        

        return response
    
    async def getLocality(self, region=None, value=None, body=""):
        """Get Locality data
        :param region : A `region` contains a specific unique name. : type string
        :param value : A `value` contains a specific value of the region. : type string
        """
        payload = {}
        
        if region is not None:
            payload["region"] = region
        
        if value is not None:
            payload["value"] = value
        
        # Parameter validation
        schema = LogisticValidator.getLocality()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocality"], proccessed_params="""{"required":[{"in":"path","name":"region","description":"A `region` contains a specific unique name.","schema":{"type":"string"},"required":true},{"in":"path","name":"value","description":"A `value` contains a specific value of the region.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"region","description":"A `region` contains a specific unique name.","schema":{"type":"string"},"required":true},{"in":"path","name":"value","description":"A `value` contains a specific value of the region.","schema":{"type":"string"},"required":true}]}""", region=region, value=value)
        query_string = await create_query_string(region=region, value=value)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLocality"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/locality/{region}/{value}", region=region, value=value), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import GetLocality
            schema = GetLocality()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocality")
                print(e)

        

        return response
    

