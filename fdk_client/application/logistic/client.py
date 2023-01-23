

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
            "getPincodeZones": "/service/application/logistics/v1.0/pincode/zones",
            "upsertZoneControllerView": "/service/application/logistics/v1.0/assign_stores"
            
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
        
        if pincode:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPincodeCity"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/pincode/{pincode}", pincode=pincode), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
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
    
    async def upsertZoneControllerView(self, company_id=None, application_id=None, body=""):
        """This API returns zone from the Pincode View.
        :param company_id : A `company_id` contains a specific ID of a company. : type integer
        :param application_id : A `application_id` contains a unique ID. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        # Parameter validation
        schema = LogisticValidator.upsertZoneControllerView()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AssignStoreRequest import AssignStoreRequest
        schema = AssignStoreRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["upsertZoneControllerView"], proccessed_params="""{"required":[{"in":"path","name":"company_id","description":"A `company_id` contains a specific ID of a company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` contains a unique ID.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` contains a specific ID of a company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` contains a unique ID.","schema":{"type":"string"},"required":true}]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["upsertZoneControllerView"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/assign_stores", company_id=company_id, application_id=application_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

