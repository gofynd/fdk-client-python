"""Serviceability Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import ServiceabilityValidator

class Serviceability:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def createZone(self, body="", request_headers:Dict={}):
        """Creates a delivery zone.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createZone()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateZoneDataSchema
        schema = CreateZoneDataSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ZoneSchema
            schema = ZoneSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createZone")
                print(e)

        return response
    
    async def getZones(self, stage=None, page_size=None, page_no=None, is_active=None, q=None, country_iso_code=None, pincode=None, state=None, city=None, sector=None, request_headers:Dict={}):
        """Retrieves a list of delivery zones.
        :param stage : Identifies the specific stage of zone bing requested. : type string
        :param page_size : Defines the number of items displayed per page. : type integer
        :param page_no : Current page number. : type integer
        :param is_active : Status of Zone (either active or inactive) : type boolean
        :param q : Used to search for matching results based on the provided input. : type string
        :param country_iso_code : ISO2 code of the country. : type string
        :param pincode : PIN Code of the country. : type string
        :param state : State of the country. : type string
        :param city : City of the country. : type string
        :param sector : Sector name of mentioned address. : type string
        """
        payload = {}
        
        if stage is not None:
            payload["stage"] = stage
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no
        if is_active is not None:
            payload["is_active"] = is_active
        if q is not None:
            payload["q"] = q
        if country_iso_code is not None:
            payload["country_iso_code"] = country_iso_code
        if pincode is not None:
            payload["pincode"] = pincode
        if state is not None:
            payload["state"] = state
        if city is not None:
            payload["city"] = city
        if sector is not None:
            payload["sector"] = sector

        # Parameter validation
        schema = ServiceabilityValidator.getZones()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"stage","description":"Identifies the specific stage of zone bing requested.","schema":{"type":"string","enum":["in_progress","failed","completed"]}},{"in":"query","name":"page_size","description":"Defines the number of items displayed per page.","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"page_no","description":"Current page number.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"is_active","description":"Status of Zone (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"q","description":"Used to search for matching results based on the provided input.","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country.","schema":{"x-not-enum":true,"type":"string"}},{"in":"query","name":"pincode","description":"PIN Code of the country.","schema":{"type":"string"}},{"in":"query","name":"state","description":"State of the country.","schema":{"type":"string"}},{"in":"query","name":"city","description":"City of the country.","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector name of mentioned address.","schema":{"type":"string"}}],"query":[{"in":"query","name":"stage","description":"Identifies the specific stage of zone bing requested.","schema":{"type":"string","enum":["in_progress","failed","completed"]}},{"in":"query","name":"page_size","description":"Defines the number of items displayed per page.","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"page_no","description":"Current page number.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"is_active","description":"Status of Zone (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"q","description":"Used to search for matching results based on the provided input.","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country.","schema":{"x-not-enum":true,"type":"string"}},{"in":"query","name":"pincode","description":"PIN Code of the country.","schema":{"type":"string"}},{"in":"query","name":"state","description":"State of the country.","schema":{"type":"string"}},{"in":"query","name":"city","description":"City of the country.","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector name of mentioned address.","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", stage=stage, page_size=page_size, page_no=page_no, is_active=is_active, q=q, country_iso_code=country_iso_code, pincode=pincode, state=state, city=city, sector=sector)
        query_string = await create_query_string(stage=stage, page_size=page_size, page_no=page_no, is_active=is_active, q=q, country_iso_code=country_iso_code, pincode=pincode, state=state, city=city, sector=sector)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones", stage=stage, page_size=page_size, page_no=page_no, is_active=is_active, q=q, country_iso_code=country_iso_code, pincode=pincode, state=state, city=city, sector=sector), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ListViewSchema
            schema = ListViewSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getZones")
                print(e)

        return response
    
    async def getZone(self, zone_id=None, request_headers:Dict={}):
        """Retrieves a single delivery zone
        :param zone_id : Unique identifier for a particular zone : type string
        """
        payload = {}
        
        if zone_id is not None:
            payload["zone_id"] = zone_id

        # Parameter validation
        schema = ServiceabilityValidator.getZone()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones/{zone_id}", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"Unique identifier for a particular zone","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"Unique identifier for a particular zone","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", zone_id=zone_id, )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones/{zone_id}", zone_id=zone_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetZoneByIdSchema
            schema = GetZoneByIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getZone")
                print(e)

        return response
    
    async def updateZone(self, zone_id=None, body="", request_headers:Dict={}):
        """Enable or Disable a Zone under that application.
        :param zone_id : Unique identifier for a particular zone : type string
        """
        payload = {}
        
        if zone_id is not None:
            payload["zone_id"] = zone_id

        # Parameter validation
        schema = ServiceabilityValidator.updateZone()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateZoneData
        schema = UpdateZoneData()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones/{zone_id}", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"Unique identifier for a particular zone","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"Unique identifier for a particular zone","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", zone_id=zone_id, )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones/{zone_id}", zone_id=zone_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ZoneUpdateSuccessResult
            schema = ZoneUpdateSuccessResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateZone")
                print(e)

        return response
    
    async def deleteZone(self, zone_id=None, request_headers:Dict={}):
        """Delete a Zone under that application.
        :param zone_id : Unique identifier for a particular zone : type string
        """
        payload = {}
        
        if zone_id is not None:
            payload["zone_id"] = zone_id

        # Parameter validation
        schema = ServiceabilityValidator.deleteZone()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones/{zone_id}", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"Unique identifier for a particular zone","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"Unique identifier for a particular zone","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", zone_id=zone_id, )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones/{zone_id}", zone_id=zone_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ZoneDeleteSuccessResult
            schema = ZoneDeleteSuccessResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteZone")
                print(e)

        return response
    
    async def createBulkExport(self, body="", request_headers:Dict={}):
        """Export zones defined at the application level.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createBulkExport()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkCreateZoneExport
        schema = BulkCreateZoneExport()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones/bulk/export", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones/bulk/export", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ZoneBulkExport
            schema = ZoneBulkExport()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createBulkExport")
                print(e)

        return response
    
    async def getBulkExport(self, batch_id=None, request_headers:Dict={}):
        """Get specific zone which is exported at the application level.
        :param batch_id : A `batch_id` is a unique identifier for a particular zone. : type string
        """
        payload = {}
        
        if batch_id is not None:
            payload["batch_id"] = batch_id

        # Parameter validation
        schema = ServiceabilityValidator.getBulkExport()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones/bulk/export/{batch_id}", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"A `batch_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"A `batch_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"required":true}]}""", serverType="platform", batch_id=batch_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/zones/bulk/export/{batch_id}", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetZoneBulkExport
            schema = GetZoneBulkExport()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkExport")
                print(e)

        return response
    
    async def createGeoArea(self, body="", request_headers:Dict={}):
        """Allows to create and manage GeoAreas, representing groups of geographic regions.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createGeoArea()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GeoAreaRequestBody
        schema = GeoAreaRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"The unique identifier for the sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"The unique identifier for the sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GeoAreaResponseBody
            schema = GeoAreaResponseBody()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createGeoArea")
                print(e)

        return response
    
    async def getGeoAreas(self, page_size=None, is_active=None, page_no=None, type=None, q=None, country_iso_code=None, state=None, city=None, pincode=None, sector=None, request_headers:Dict={}):
        """Retrieves a listing view of created GeoAreas.
        :param page_size : Determines the items to be displayed in a page : type integer
        :param is_active : Status of GeoAreas (either active or inactive) : type boolean
        :param page_no : Current page number : type integer
        :param type : To fetch the type of a specific geoarea. : type string
        :param q : Used to search for matching results based on the provided input. : type string
        :param country_iso_code : ISO2 code of the country : type string
        :param state : State name : type string
        :param city : City name : type string
        :param pincode : Pincode value to search geoareas : type string
        :param sector : Sector value to search geoareas : type string
        """
        payload = {}
        
        if page_size is not None:
            payload["page_size"] = page_size
        if is_active is not None:
            payload["is_active"] = is_active
        if page_no is not None:
            payload["page_no"] = page_no
        if type is not None:
            payload["type"] = type
        if q is not None:
            payload["q"] = q
        if country_iso_code is not None:
            payload["country_iso_code"] = country_iso_code
        if state is not None:
            payload["state"] = state
        if city is not None:
            payload["city"] = city
        if pincode is not None:
            payload["pincode"] = pincode
        if sector is not None:
            payload["sector"] = sector

        # Parameter validation
        schema = ServiceabilityValidator.getGeoAreas()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas", """{"required":[{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for an application.","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"Status of GeoAreas (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"page_no","description":"Current page number","schema":{"type":"integer"}},{"in":"query","name":"type","description":"To fetch the type of a specific geoarea.","schema":{"type":"string"}},{"in":"query","name":"q","description":"Used to search for matching results based on the provided input.","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country","schema":{"type":"string","x-not-enum":true}},{"in":"query","name":"state","description":"State name","schema":{"type":"string"}},{"in":"query","name":"city","description":"City name","schema":{"type":"string"}},{"in":"query","name":"pincode","description":"Pincode value to search geoareas","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector value to search geoareas","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"Status of GeoAreas (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"page_no","description":"Current page number","schema":{"type":"integer"}},{"in":"query","name":"type","description":"To fetch the type of a specific geoarea.","schema":{"type":"string"}},{"in":"query","name":"q","description":"Used to search for matching results based on the provided input.","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country","schema":{"type":"string","x-not-enum":true}},{"in":"query","name":"state","description":"State name","schema":{"type":"string"}},{"in":"query","name":"city","description":"City name","schema":{"type":"string"}},{"in":"query","name":"pincode","description":"Pincode value to search geoareas","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector value to search geoareas","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for an application.","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_size=page_size, is_active=is_active, page_no=page_no, type=type, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector)
        query_string = await create_query_string(page_size=page_size, is_active=is_active, page_no=page_no, type=type, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas", page_size=page_size, is_active=is_active, page_no=page_no, type=type, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GeoAreaGetResponseBody
            schema = GeoAreaGetResponseBody()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGeoAreas")
                print(e)

        return response
    
    async def getGeoArea(self, geoarea_id=None, request_headers:Dict={}):
        """This API Returns the data of the specific GeoArea which exists on the platform.
        :param geoarea_id : A unique identifier for the GeoArea. : type string
        """
        payload = {}
        
        if geoarea_id is not None:
            payload["geoarea_id"] = geoarea_id

        # Parameter validation
        schema = ServiceabilityValidator.getGeoArea()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/{geoarea_id}", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"geoarea_id","description":"A unique identifier for the GeoArea.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"The unique identifier for the sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"geoarea_id","description":"A unique identifier for the GeoArea.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"The unique identifier for the sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", geoarea_id=geoarea_id, )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/{geoarea_id}", geoarea_id=geoarea_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GeoAreaDetails
            schema = GeoAreaDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGeoArea")
                print(e)

        return response
    
    async def updateGeoArea(self, geoarea_id=None, body="", request_headers:Dict={}):
        """Updates the GeoArea with a new name, regions, etc.
        :param geoarea_id : A unique identifier for the GeoArea. : type string
        """
        payload = {}
        
        if geoarea_id is not None:
            payload["geoarea_id"] = geoarea_id

        # Parameter validation
        schema = ServiceabilityValidator.updateGeoArea()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GeoAreaRequestBody
        schema = GeoAreaRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/{geoarea_id}", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"geoarea_id","description":"A unique identifier for the GeoArea.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"The unique identifier for the sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"geoarea_id","description":"A unique identifier for the GeoArea.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"The unique identifier for the sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", geoarea_id=geoarea_id, )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/{geoarea_id}", geoarea_id=geoarea_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GeoAreaPutResponseBody
            schema = GeoAreaPutResponseBody()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateGeoArea")
                print(e)

        return response
    
    async def createBulkGeoArea(self, body="", request_headers:Dict={}):
        """Allows to create and manage GeoAreas, representing groups of geographic regions in bulk.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createBulkGeoArea()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkGeoAreaDetails
        schema = BulkGeoAreaDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/regions/bulk", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"The unique identifier for the sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"The unique identifier for the sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/regions/bulk", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkGeoAreaResult
            schema = BulkGeoAreaResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createBulkGeoArea")
                print(e)

        return response
    
    async def getBulkGeoArea(self, geoarea_id=None, request_headers:Dict={}):
        """Allows to Get GeoArea status which is created, representing groups of geographic regions in bulk.
        :param geoarea_id : A unique identifier for the GeoArea. : type string
        """
        payload = {}
        
        if geoarea_id is not None:
            payload["geoarea_id"] = geoarea_id

        # Parameter validation
        schema = ServiceabilityValidator.getBulkGeoArea()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/regions/bulk/{geoarea_id}", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"The unique identifier for the sales channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"geoarea_id","description":"A unique identifier for the GeoArea.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"The unique identifier for the sales channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"geoarea_id","description":"A unique identifier for the GeoArea.","schema":{"type":"string"},"required":true}]}""", serverType="platform", geoarea_id=geoarea_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/regions/bulk/{geoarea_id}", geoarea_id=geoarea_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkGeoAreaGetResult
            schema = BulkGeoAreaGetResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkGeoArea")
                print(e)

        return response
    
    async def updateBulkGeoArea(self, geoarea_id=None, body="", request_headers:Dict={}):
        """Update geoarea details and their associated regions through a CSV file in bulk.
        :param geoarea_id : A unique identifier for the GeoArea. : type string
        """
        payload = {}
        
        if geoarea_id is not None:
            payload["geoarea_id"] = geoarea_id

        # Parameter validation
        schema = ServiceabilityValidator.updateBulkGeoArea()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkGeoAreaDetails
        schema = BulkGeoAreaDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/regions/bulk/{geoarea_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier for the company","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique identifier for the sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"geoarea_id","description":"A unique identifier for the GeoArea.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier for the company","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique identifier for the sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"geoarea_id","description":"A unique identifier for the GeoArea.","schema":{"type":"string"},"required":true}]}""", serverType="platform", geoarea_id=geoarea_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/regions/bulk/{geoarea_id}", geoarea_id=geoarea_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkGeoAreaResult
            schema = BulkGeoAreaResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateBulkGeoArea")
                print(e)

        return response
    
    async def createGeoAreaExportJob(self, geoarea_id=None, request_headers:Dict={}):
        """Create the job for exporting the regions in Geoarea in CSV format.
        :param geoarea_id : The unique identifier of the Geoarea. : type string
        """
        payload = {}
        
        if geoarea_id is not None:
            payload["geoarea_id"] = geoarea_id

        # Parameter validation
        schema = ServiceabilityValidator.createGeoAreaExportJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/bulk/export/{geoarea_id}", """{"required":[{"name":"company_id","in":"path","required":true,"description":"The unique identifier of the company.","schema":{"type":"integer"}},{"name":"application_id","in":"path","required":true,"description":"The unique identifier of the application.","schema":{"type":"string"}},{"name":"geoarea_id","in":"path","required":true,"description":"The unique identifier of the Geoarea.","schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"The unique identifier of the company.","schema":{"type":"integer"}},{"name":"application_id","in":"path","required":true,"description":"The unique identifier of the application.","schema":{"type":"string"}},{"name":"geoarea_id","in":"path","required":true,"description":"The unique identifier of the Geoarea.","schema":{"type":"string"}}]}""", serverType="platform", geoarea_id=geoarea_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/bulk/export/{geoarea_id}", geoarea_id=geoarea_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GeoAreaBulkCreationResult
            schema = GeoAreaBulkCreationResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createGeoAreaExportJob")
                print(e)

        return response
    
    async def getGeoAreaExportJobStatus(self, geoarea_id=None, request_headers:Dict={}):
        """Get the status and details of the Geoarea bulk export process.
        :param geoarea_id : The unique identifier of the Geoarea. : type string
        """
        payload = {}
        
        if geoarea_id is not None:
            payload["geoarea_id"] = geoarea_id

        # Parameter validation
        schema = ServiceabilityValidator.getGeoAreaExportJobStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/bulk/export/{geoarea_id}", """{"required":[{"name":"company_id","in":"path","required":true,"description":"The unique identifier of the company.","schema":{"type":"integer"}},{"name":"application_id","in":"path","required":true,"description":"The unique identifier of the application.","schema":{"type":"string"}},{"name":"geoarea_id","in":"path","required":true,"description":"The unique identifier of the Geoarea.","schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"The unique identifier of the company.","schema":{"type":"integer"}},{"name":"application_id","in":"path","required":true,"description":"The unique identifier of the application.","schema":{"type":"string"}},{"name":"geoarea_id","in":"path","required":true,"description":"The unique identifier of the Geoarea.","schema":{"type":"string"}}]}""", serverType="platform", geoarea_id=geoarea_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/bulk/export/{geoarea_id}", geoarea_id=geoarea_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GeoAreaBulkExportResult
            schema = GeoAreaBulkExportResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGeoAreaExportJobStatus")
                print(e)

        return response
    
    async def updatePincodeMopView(self, body="", request_headers:Dict={}):
        """Modify and update views related to pincode MOP (Mode of Payment).
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updatePincodeMopView()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PincodeMopData
        schema = PincodeMopData()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-update", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-update", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeMOPResult
            schema = PincodeMOPResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePincodeMopView")
                print(e)

        return response
    
    async def updatePincodeBulkView(self, body="", request_headers:Dict={}):
        """Updates the cash on delivery settings for multiple specified pin codes simultaneously.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updatePincodeBulkView()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PincodeMopBulkData
        schema = PincodeMopBulkData()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-bulk-update", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-bulk-update", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeBulkViewResult
            schema = PincodeBulkViewResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePincodeBulkView")
                print(e)

        return response
    
    async def updatePincodeCoDListing(self, page_number=None, page_size=None, body="", request_headers:Dict={}):
        """Retrieves a list of pincodes along with the count based on whether cash on delivery settings.
        :param page_number : Page number to be fetched. : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        """
        payload = {}
        
        if page_number is not None:
            payload["page_number"] = page_number
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ServiceabilityValidator.updatePincodeCoDListing()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PincodeCodStatusListingDetails
        schema = PincodeCodStatusListingDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-data", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_number","description":"Page number to be fetched.","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":100}}],"query":[{"in":"query","name":"page_number","description":"Page number to be fetched.","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":100}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}]}""", serverType="platform", page_number=page_number, page_size=page_size)
        query_string = await create_query_string(page_number=page_number, page_size=page_size)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-data", page_number=page_number, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeCodStatusListingResult
            schema = PincodeCodStatusListingResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePincodeCoDListing")
                print(e)

        return response
    
    async def updatePincodeAuditHistory(self, page_number=None, page_size=None, body="", request_headers:Dict={}):
        """Retrieves the history of changes made to cash on delivery settings for pincodes.
        :param page_number : Page number to be fetched. : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        """
        payload = {}
        
        if page_number is not None:
            payload["page_number"] = page_number
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ServiceabilityValidator.updatePincodeAuditHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PincodeMopUpdateAuditHistoryDetails
        schema = PincodeMopUpdateAuditHistoryDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/history", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_number","description":"Page number to be fetched.","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":100}}],"query":[{"in":"query","name":"page_number","description":"Page number to be fetched.","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":100}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}]}""", serverType="platform", page_number=page_number, page_size=page_size)
        query_string = await create_query_string(page_number=page_number, page_size=page_size)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/history", page_number=page_number, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeMopUpdateAuditHistoryResultData
            schema = PincodeMopUpdateAuditHistoryResultData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePincodeAuditHistory")
                print(e)

        return response
    
    async def updateCourierRule(self, rule_uid=None, body="", request_headers:Dict={}):
        """Updates an existing rule within the delivery configuration.
        :param rule_uid : Unique identifier of the courier partner rule. : type string
        """
        payload = {}
        
        if rule_uid is not None:
            payload["rule_uid"] = rule_uid

        # Parameter validation
        schema = ServiceabilityValidator.updateCourierRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerRule
        schema = CourierPartnerRule()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_uid}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"Unique identifier of the courier partner rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"Unique identifier of the courier partner rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_uid=rule_uid)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_uid}", rule_uid=rule_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerRuleResult
            schema = CourierPartnerRuleResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierRule")
                print(e)

        return response
    
    async def getCourierPartnerRule(self, rule_uid=None, request_headers:Dict={}):
        """Retrieves a single rule within the delivery configuration.
        :param rule_uid : Unique identifier of the courier partner rule : type string
        """
        payload = {}
        
        if rule_uid is not None:
            payload["rule_uid"] = rule_uid

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_uid}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"Unique identifier of the courier partner rule","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"Unique identifier of the courier partner rule","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_uid=rule_uid)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_uid}", rule_uid=rule_uid), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerRuleResult
            schema = CourierPartnerRuleResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerRule")
                print(e)

        return response
    
    async def createCourierPartnerRule(self, body="", request_headers:Dict={}):
        """Creates a rule within the delivery configuration.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createCourierPartnerRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerRule
        schema = CourierPartnerRule()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerRuleResult
            schema = CourierPartnerRuleResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCourierPartnerRule")
                print(e)

        return response
    
    async def getCourierPartnerRules(self, page_no=None, page_size=None, status=None, request_headers:Dict={}):
        """Retrieve a list of rules within the delivery configuration.
        :param page_no : The current page number for paginated results. : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param status : Filter rules based on rule status : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if status is not None:
            payload["status"] = status

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"status","description":"Filter rules based on rule status","schema":{"type":"string","enum":["true","false"]}}],"query":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"status","description":"Filter rules based on rule status","schema":{"type":"string","enum":["true","false"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, status=status)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, status=status)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules", page_no=page_no, page_size=page_size, status=status), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerRulesListResult
            schema = CourierPartnerRulesListResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerRules")
                print(e)

        return response
    
    async def getCourierPartners(self, body="", request_headers:Dict={}):
        """Get all the serviceable courier partners of a destination and the shipments.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartners()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ShipmentCourierPartnerDetails
        schema = ShipmentCourierPartnerDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipment/courier-partners", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique identifier of the sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique identifier of the sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipment/courier-partners", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentCourierPartnerResult
            schema = ShipmentCourierPartnerResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartners")
                print(e)

        return response
    
    async def updateApplicationConfiguration(self, body="", request_headers:Dict={}):
        """Apply configuration to application to set DP rules and Zone configuration
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updateApplicationConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationConfigPutDetail
        schema = ApplicationConfigPutDetail()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier of company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier of sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier of company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier of sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationConfigPut
            schema = ApplicationConfigPut()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateApplicationConfiguration")
                print(e)

        return response
    
    async def getApplicationConfiguration(self, request_headers:Dict={}):
        """This API returns all the Application config that has been applied to the given company and application.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getApplicationConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier of company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier of a sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier of company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier of a sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationConfigGetResult
            schema = ApplicationConfigGetResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationConfiguration")
                print(e)

        return response
    
    async def patchApplicationConfiguration(self, body="", request_headers:Dict={}):
        """Apply configs to application. Supports patching for buybox rule config and promise config. For reference, refer to examples
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.patchApplicationConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationConfigPatch
        schema = ApplicationConfigPatch()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier of company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier of sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier of company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier of sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationConfigPatchResult
            schema = ApplicationConfigPatchResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for patchApplicationConfiguration")
                print(e)

        return response
    
    async def getApplicationConfig(self, request_headers:Dict={}):
        """Retrieves information about the order routing setup for a single application
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getApplicationConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/configuration", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreRuleConfigData
            schema = StoreRuleConfigData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationConfig")
                print(e)

        return response
    
    async def insertApplicationConfig(self, body="", request_headers:Dict={}):
        """Creates a order routing setup for an application, which involves updating sorting settings or rule priorities.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.insertApplicationConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StoreRuleConfigData
        schema = StoreRuleConfigData()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/configuration", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreRuleConfigData
            schema = StoreRuleConfigData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for insertApplicationConfig")
                print(e)

        return response
    
    async def updateStoreRulesConfig(self, body="", request_headers:Dict={}):
        """Updates an existing order routing setup for a single application, which involves updating sorting settings or rule priorities.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updateStoreRulesConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StoreRuleConfigData
        schema = StoreRuleConfigData()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/configuration", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreRuleConfigData
            schema = StoreRuleConfigData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateStoreRulesConfig")
                print(e)

        return response
    
    async def getStoreRules(self, page_no=None, page_size=None, status=None, request_headers:Dict={}):
        """Retrieves an existing order routing setup for a single application
        :param page_no : The current page number for paginated results. : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param status : Filter rules based on rule status : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if status is not None:
            payload["status"] = status

        # Parameter validation
        schema = ServiceabilityValidator.getStoreRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","required":false,"description":"The current page number for paginated results.","schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","required":false,"schema":{"type":"integer"}},{"in":"query","name":"status","required":false,"description":"Filter rules based on rule status","schema":{"type":"string","enum":["true","false","all"]}}],"query":[{"in":"query","name":"page_no","required":false,"description":"The current page number for paginated results.","schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","required":false,"schema":{"type":"integer"}},{"in":"query","name":"status","required":false,"description":"Filter rules based on rule status","schema":{"type":"string","enum":["true","false","all"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, status=status)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, status=status)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules", page_no=page_no, page_size=page_size, status=status), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetStoreRulesApiResult
            schema = GetStoreRulesApiResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStoreRules")
                print(e)

        return response
    
    async def createStoreRules(self, body="", request_headers:Dict={}):
        """Create a rule within the order routing rules
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createStoreRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateStoreRuleDetailsSchema
        schema = CreateStoreRuleDetailsSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreRuleResultSchema
            schema = StoreRuleResultSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createStoreRules")
                print(e)

        return response
    
    async def getStoreRule(self, rule_uid=None, request_headers:Dict={}):
        """Retrieves a single rule within the order routing rules
        :param rule_uid : A `rule_uid` is a unique identifier for a particular rule object. : type string
        """
        payload = {}
        
        if rule_uid is not None:
            payload["rule_uid"] = rule_uid

        # Parameter validation
        schema = ServiceabilityValidator.getStoreRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules/{rule_uid}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular rule object.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular rule object.","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_uid=rule_uid)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules/{rule_uid}", rule_uid=rule_uid), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreRuleDataSchema
            schema = StoreRuleDataSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStoreRule")
                print(e)

        return response
    
    async def updateStoreRules(self, rule_uid=None, body="", request_headers:Dict={}):
        """Updates an existing rule within the order routing rules.
        :param rule_uid : A `rule_uid` is a unique identifier for a particular rule object. : type string
        """
        payload = {}
        
        if rule_uid is not None:
            payload["rule_uid"] = rule_uid

        # Parameter validation
        schema = ServiceabilityValidator.updateStoreRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateStoreRuleDetailsSchema
        schema = CreateStoreRuleDetailsSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules/{rule_uid}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular rule object.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular rule object.","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_uid=rule_uid)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules/{rule_uid}", rule_uid=rule_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreRuleUpdateResultSchema
            schema = StoreRuleUpdateResultSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateStoreRules")
                print(e)

        return response
    
    async def updateCourierPartnerRulePriority(self, body="", request_headers:Dict={}):
        """Updates a courier partner rule priority for a single application
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updateCourierPartnerRulePriority()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RulePriorityDetails
        schema = RulePriorityDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/priority", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/priority", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RulePriorityResult
            schema = RulePriorityResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierPartnerRulePriority")
                print(e)

        return response
    
    async def updateStoreRulePriority(self, body="", request_headers:Dict={}):
        """Update Store Rule priority
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updateStoreRulePriority()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RulePriorityDetails
        schema = RulePriorityDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules/priority", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules/priority", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RulePriorityResult
            schema = RulePriorityResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateStoreRulePriority")
                print(e)

        return response
    
    async def downloadGeoareaSampleFile(self, request_headers:Dict={}):
        """Download a sample file for geoarea data.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.downloadGeoareaSampleFile()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/regions/bulk/sample", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique identifier of the sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique identifier of the sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/geoareas/regions/bulk/sample", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    