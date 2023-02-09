

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
            "getEntityList": "/service/application/logistics/v1.0/entity-list",
            "getPincodeZones": "/service/application/logistics/v1.0/pincode/zones",
            "assignLocations": "/service/application/logistics/v1.0/assign_stores"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getPincodeCity(self, pincode=None, country_code=None, body=""):
        """Get pincode data
        :param pincode : A `pincode` contains a specific address of a location. : type string
        :param country_code : A 3 alphabetic country code : type string
        """
        payload = {}
        
        if pincode:
            payload["pincode"] = pincode
        
        if country_code:
            payload["country_code"] = country_code
        
        # Parameter validation
        schema = LogisticValidator.getPincodeCity()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPincodeCity"], proccessed_params="""{"required":[{"in":"path","name":"pincode","description":"A `pincode` contains a specific address of a location.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"country_code","description":"A 3 alphabetic country code","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"country_code","description":"A 3 alphabetic country code","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"pincode","description":"A `pincode` contains a specific address of a location.","schema":{"type":"string"},"required":true}]}""", pincode=pincode, country_code=country_code)
        query_string = await create_query_string(pincode=pincode, country_code=country_code)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPincodeCity"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/pincode/{pincode}", pincode=pincode, country_code=country_code), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getTatProduct(self, body=""):
        """Get TAT data
        """
        payload = {}
        
        # Parameter validation
        schema = LogisticValidator.getTatProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.TATViewRequest import TATViewRequest
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getTatProduct"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getEntityList(self, page=None, limit=None, body=""):
        """Get Entity List
        :param page : Page Number. : type string
        :param limit : Limit of entity in page : type string
        """
        payload = {}
        
        if page:
            payload["page"] = page
        
        if limit:
            payload["limit"] = limit
        
        # Parameter validation
        schema = LogisticValidator.getEntityList()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EntityListRequest import EntityListRequest
        schema = EntityListRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getEntityList"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"page","description":"Page Number.","schema":{"type":"string"},"required":false},{"in":"query","name":"limit","description":"Limit of entity in page","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page","description":"Page Number.","schema":{"type":"string"},"required":false},{"in":"query","name":"limit","description":"Limit of entity in page","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", page=page, limit=limit)
        query_string = await create_query_string(page=page, limit=limit)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getEntityList"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/entity-list", page=page, limit=limit), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPincodeZones(self, body=""):
        """This API returns zone from the Pincode View.
        """
        payload = {}
        
        # Parameter validation
        schema = LogisticValidator.getPincodeZones()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.GetZoneFromPincodeViewRequest import GetZoneFromPincodeViewRequest
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPincodeZones"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/pincode/zones", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def assignLocations(self, body=""):
        """This API returns zone from the Pincode View.
        """
        payload = {}
        
        # Parameter validation
        schema = LogisticValidator.assignLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AssignStoreRequest import AssignStoreRequest
        schema = AssignStoreRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["assignLocations"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["assignLocations"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/assign_stores", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

