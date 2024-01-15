"""Serviceability Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import ServiceabilityValidator

class Serviceability:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getZones(self, page_no=None, page_size=None, is_active=None, channel_id=None, q=None, country=None, state=None, city=None, pincode=None, sector=None, request_headers:Dict={}):
        """Return the list of zones that are defined at the company level.
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param is_active : Status of Zone (either active or inactive) : type boolean
        :param channel_id : Zones filtered by an application : type string
        :param q : search with name as a free text : type string
        :param country : ISO2 code of the country : type string
        :param state : State name : type string
        :param city : City name : type string
        :param pincode : Pincode value to search zones : type string
        :param sector : Sector value to search zones : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if is_active is not None:
            payload["is_active"] = is_active
        if channel_id is not None:
            payload["channel_id"] = channel_id
        if q is not None:
            payload["q"] = q
        if country is not None:
            payload["country"] = country
        if state is not None:
            payload["state"] = state
        if city is not None:
            payload["city"] = city
        if pincode is not None:
            payload["pincode"] = pincode
        if sector is not None:
            payload["sector"] = sector

        # Parameter validation
        schema = ServiceabilityValidator.getZones()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true,"examples":{"Test Company":{"value":1}}}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"Status of Zone (either active or inactive)","schema":{"type":"boolean"},"examples":{"Active Zones":{"value":true}}},{"in":"query","name":"channel_id","description":"Zones filtered by an application","schema":{"type":"string"},"examples":{"Single application filter":{"value":"64fee4b354c2c22a822de54f"},"Multiple application filters":{"value":"64fee4b354c2c22a822de54f,6502e3b460c34d2d0fb705c8"}}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"},"examples":{"Sample query":{"value":"zone"}}},{"in":"query","name":"country","description":"ISO2 code of the country","schema":{"type":"string"},"examples":{"India":{"value":"India"}}},{"in":"query","name":"state","description":"State name","schema":{"type":"string"},"examples":{"Indian State":{"value":"Maharashtra"}}},{"in":"query","name":"city","description":"City name","schema":{"type":"string"},"examples":{"Indian City":{"value":"Mumbai"}}},{"in":"query","name":"pincode","description":"Pincode value to search zones","schema":{"type":"string"},"examples":{"Pincode":{"value":"400603"}}},{"in":"query","name":"sector","description":"Sector value to search zones","schema":{"type":"string"},"examples":{"Sector":{"value":"Abu Dhabi"}}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"Status of Zone (either active or inactive)","schema":{"type":"boolean"},"examples":{"Active Zones":{"value":true}}},{"in":"query","name":"channel_id","description":"Zones filtered by an application","schema":{"type":"string"},"examples":{"Single application filter":{"value":"64fee4b354c2c22a822de54f"},"Multiple application filters":{"value":"64fee4b354c2c22a822de54f,6502e3b460c34d2d0fb705c8"}}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"},"examples":{"Sample query":{"value":"zone"}}},{"in":"query","name":"country","description":"ISO2 code of the country","schema":{"type":"string"},"examples":{"India":{"value":"India"}}},{"in":"query","name":"state","description":"State name","schema":{"type":"string"},"examples":{"Indian State":{"value":"Maharashtra"}}},{"in":"query","name":"city","description":"City name","schema":{"type":"string"},"examples":{"Indian City":{"value":"Mumbai"}}},{"in":"query","name":"pincode","description":"Pincode value to search zones","schema":{"type":"string"},"examples":{"Pincode":{"value":"400603"}}},{"in":"query","name":"sector","description":"Sector value to search zones","schema":{"type":"string"},"examples":{"Sector":{"value":"Abu Dhabi"}}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true,"examples":{"Test Company":{"value":1}}}]}""", page_no=page_no, page_size=page_size, is_active=is_active, channel_id=channel_id, q=q, country=country, state=state, city=city, pincode=pincode, sector=sector)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_active=is_active, channel_id=channel_id, q=q, country=country, state=state, city=city, pincode=pincode, sector=sector)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones", page_no=page_no, page_size=page_size, is_active=is_active, channel_id=channel_id, q=q, country=country, state=state, city=city, pincode=pincode, sector=sector), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ListViewResponse
            schema = ListViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getZones")
                print(e)

        return response
    
    async def createZone(self, body="", request_headers:Dict={}):
        """Creates a new zone with the specified mapping. A zone enables serviceability based on given regions. By creating a zone and including specific regions, you can ensure that the stores associated with the zone are serviceable for those added regions. This functionality is particularly useful when you need to ensure serviceability for multiple regions by grouping them into a single zone.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createZone()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateZoneData
        schema = CreateZoneData()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import ZoneResponse
            schema = ZoneResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createZone")
                print(e)

        return response
    
    async def updateZoneById(self, zone_id=None, body="", request_headers:Dict={}):
        """Updates the region, application, store mapping and other details in the Zone.
        :param zone_id : A `zone_id` is a unique identifier for a particular zone. : type string
        """
        payload = {}
        
        if zone_id is not None:
            payload["zone_id"] = zone_id

        # Parameter validation
        schema = ServiceabilityValidator.updateZoneById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateZoneData
        schema = UpdateZoneData()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones/{zone_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true,"examples":{"Test Company":{"value":"1"}}},{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"examples":{"Test Zone":{"value":"64d22858f8aafe61d79f07ea"}},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true,"examples":{"Test Company":{"value":"1"}}},{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"examples":{"Test Zone":{"value":"64d22858f8aafe61d79f07ea"}},"required":true}]}""", zone_id=zone_id)
        query_string = await create_query_string(zone_id=zone_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones/{zone_id}", zone_id=zone_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import ZoneSuccessResponse
            schema = ZoneSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateZoneById")
                print(e)

        return response
    
    async def getZoneById(self, zone_id=None, request_headers:Dict={}):
        """Returns the region, application, store mapping and other details in the Zone.
        :param zone_id : A `zone_id` is a unique identifier for a particular zone. : type string
        """
        payload = {}
        
        if zone_id is not None:
            payload["zone_id"] = zone_id

        # Parameter validation
        schema = ServiceabilityValidator.getZoneById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones/{zone_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true,"examples":{"Test Company":{"value":"1"}}},{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"examples":{"Test Zone":{"value":"64d22858f8aafe61d79f07ea"}},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true,"examples":{"Test Company":{"value":"1"}}},{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"examples":{"Test Zone":{"value":"64d22858f8aafe61d79f07ea"}},"required":true}]}""", zone_id=zone_id)
        query_string = await create_query_string(zone_id=zone_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones/{zone_id}", zone_id=zone_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetZoneByIdSchema
            schema = GetZoneByIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getZoneById")
                print(e)

        return response
    
    async def getAllStores(self, request_headers:Dict={}):
        """This API returns stores data.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getAllStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/logistics/stores", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/logistics/stores", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetStoresViewResponse
            schema = GetStoresViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllStores")
                print(e)

        return response
    
    async def getOptimalLocations(self, body="", request_headers:Dict={}):
        """This API returns serviceable store of the item.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getOptimalLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ReAssignStoreRequest
        schema = ReAssignStoreRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/reassign", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/reassign", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import ReAssignStoreResponse
            schema = ReAssignStoreResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOptimalLocations")
                print(e)

        return response
    
    async def createCourierPartnerAccount(self, body="", request_headers:Dict={}):
        """This API Creates a new Courier Account
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createCourierPartnerAccount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierAccount
        schema = CourierAccount()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierAccount
            schema = CourierAccount()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCourierPartnerAccount")
                print(e)

        return response
    
    async def getCourierPartnerAccounts(self, page_no=None, page_size=None, stage=None, payment_mode=None, transport_type=None, request_headers:Dict={}):
        """This API returns Courier Account of a company.
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param stage : stage of the account. enabled/disabled : type string
        :param payment_mode : Filters dp accounts based on payment mode : type string
        :param transport_type : Filters dp accounts based on transport_type : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if stage is not None:
            payload["stage"] = stage
        if payment_mode is not None:
            payload["payment_mode"] = payment_mode
        if transport_type is not None:
            payload["transport_type"] = transport_type

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerAccounts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"stage of the account. enabled/disabled","schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"stage of the account. enabled/disabled","schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyCourierPartnerAccountListResponse
            schema = CompanyCourierPartnerAccountListResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerAccounts")
                print(e)

        return response
    
    async def updateCourierPartnerAccount(self, account_id=None, body="", request_headers:Dict={}):
        """Updates Courier Account
        :param account_id : Unique ID of courier account : type string
        """
        payload = {}
        
        if account_id is not None:
            payload["account_id"] = account_id

        # Parameter validation
        schema = ServiceabilityValidator.updateCourierPartnerAccount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierAccount
        schema = CourierAccount()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}]}""", account_id=account_id)
        query_string = await create_query_string(account_id=account_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", account_id=account_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierAccountResponse
            schema = CourierAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierPartnerAccount")
                print(e)

        return response
    
    async def getCourierPartnerAccount(self, account_id=None, request_headers:Dict={}):
        """This API returns response DpAccount of a company from mongo database.
        :param account_id : Unique ID of courier account : type string
        """
        payload = {}
        
        if account_id is not None:
            payload["account_id"] = account_id

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerAccount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}]}""", account_id=account_id)
        query_string = await create_query_string(account_id=account_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", account_id=account_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierAccountResponse
            schema = CourierAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerAccount")
                print(e)

        return response
    
    async def updateCompanyConfiguration(self, body="", request_headers:Dict={}):
        """Apply Courier Rule to company with rules priority
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updateCompanyConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CompanyConfig
        schema = CompanyConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyConfig
            schema = CompanyConfig()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCompanyConfiguration")
                print(e)

        return response
    
    async def getCompanyConfiguration(self, request_headers:Dict={}):
        """This API returns all Courier Rules applied for company.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getCompanyConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyConfig
            schema = CompanyConfig()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCompanyConfiguration")
                print(e)

        return response
    
    async def bulkTat(self, extension_id=None, scheme_id=None, body="", request_headers:Dict={}):
        """Region TAT Import or Export
        :param extension_id : Unique Identifier of CP Extension : type string
        :param scheme_id : Unique identifier of a scheme : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id

        # Parameter validation
        schema = ServiceabilityValidator.bulkTat()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRegionJobSerializer
        schema = BulkRegionJobSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", extension_id=extension_id, scheme_id=scheme_id)
        query_string = await create_query_string(extension_id=extension_id, scheme_id=scheme_id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", extension_id=extension_id, scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResponseItemData
            schema = BulkRegionResponseItemData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkTat")
                print(e)

        return response
    
    async def getBulkTat(self, extension_id=None, scheme_id=None, page_no=None, page_size=None, batch_id=None, action=None, status=None, country=None, region=None, start_date=None, end_date=None, request_headers:Dict={}):
        """Get region tat bulk history
        :param extension_id : Unique Identifier of CP Extension : type string
        :param scheme_id : Unique identifier of a scheme : type string
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param batch_id : Unique identifier of bulk job : type string
        :param action : import or export bulk type : type string
        :param status : Status of the bulk actions : type string
        :param country : Country for which bulk job is initiated : type string
        :param region : Region for which bulk job is initiated : type string
        :param start_date : Fetch job history after a particule date : type string
        :param end_date : Fetch job history before a particule date : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if batch_id is not None:
            payload["batch_id"] = batch_id
        if action is not None:
            payload["action"] = action
        if status is not None:
            payload["status"] = status
        if country is not None:
            payload["country"] = country
        if region is not None:
            payload["region"] = region
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date

        # Parameter validation
        schema = ServiceabilityValidator.getBulkTat()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-03","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-03","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
        query_string = await create_query_string(extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResponse
            schema = BulkRegionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkTat")
                print(e)

        return response
    
    async def bulkServiceability(self, extension_id=None, scheme_id=None, body="", request_headers:Dict={}):
        """Serviceability Import or Export
        :param extension_id : Unique Identifier of CP Extension : type string
        :param scheme_id : Unique identifier of a scheme : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id

        # Parameter validation
        schema = ServiceabilityValidator.bulkServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRegionJobSerializer
        schema = BulkRegionJobSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", extension_id=extension_id, scheme_id=scheme_id)
        query_string = await create_query_string(extension_id=extension_id, scheme_id=scheme_id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", extension_id=extension_id, scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResponseItemData
            schema = BulkRegionResponseItemData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkServiceability")
                print(e)

        return response
    
    async def getBulkServiceability(self, extension_id=None, scheme_id=None, page_no=None, page_size=None, batch_id=None, action=None, status=None, country=None, region=None, start_date=None, end_date=None, request_headers:Dict={}):
        """Get Region Serviceability Bulk History
        :param extension_id : Unique Identifier of CP Extension : type string
        :param scheme_id : Unique identifier of a scheme : type string
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param batch_id : Unique identifier of bulk job : type string
        :param action : import or export bulk type : type string
        :param status : Status of the bulk actions : type string
        :param country : Country for which bulk job is initiated : type string
        :param region : Region for which bulk job is initiated : type string
        :param start_date : Fetch job history after a particule date : type string
        :param end_date : Fetch job history before a particule date : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if batch_id is not None:
            payload["batch_id"] = batch_id
        if action is not None:
            payload["action"] = action
        if status is not None:
            payload["status"] = status
        if country is not None:
            payload["country"] = country
        if region is not None:
            payload["region"] = region
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date

        # Parameter validation
        schema = ServiceabilityValidator.getBulkServiceability()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-03","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-03","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
        query_string = await create_query_string(extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResponse
            schema = BulkRegionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkServiceability")
                print(e)

        return response
    
    async def getServiceability(self, extension_id=None, scheme_id=None, region_id=None, request_headers:Dict={}):
        """Get Serviceability of a region
        :param extension_id : Unique Identifier of CP Extension : type string
        :param scheme_id : Unique identifier of a scheme : type string
        :param region_id : Unique identifier of a region : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id
        if region_id is not None:
            payload["region_id"] = region_id

        # Parameter validation
        schema = ServiceabilityValidator.getServiceability()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/region/{region_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true},{"in":"path","name":"region_id","description":"Unique identifier of a region","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true},{"in":"path","name":"region_id","description":"Unique identifier of a region","schema":{"type":"string"},"required":true}]}""", extension_id=extension_id, scheme_id=scheme_id, region_id=region_id)
        query_string = await create_query_string(extension_id=extension_id, scheme_id=scheme_id, region_id=region_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/region/{region_id}", extension_id=extension_id, scheme_id=scheme_id, region_id=region_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ServiceabilityModel
            schema = ServiceabilityModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getServiceability")
                print(e)

        return response
    
    async def updateServiceability(self, extension_id=None, scheme_id=None, region_id=None, body="", request_headers:Dict={}):
        """Serviceability Update for a region
        :param extension_id : Unique Identifier of CP Extension : type string
        :param scheme_id : Unique identifier of a scheme : type string
        :param region_id : Unique identifier of a region : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id
        if region_id is not None:
            payload["region_id"] = region_id

        # Parameter validation
        schema = ServiceabilityValidator.updateServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ServiceabilityModel
        schema = ServiceabilityModel()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/region/{region_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true},{"in":"path","name":"region_id","description":"Unique identifier of a region","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true},{"in":"path","name":"region_id","description":"Unique identifier of a region","schema":{"type":"string"},"required":true}]}""", extension_id=extension_id, scheme_id=scheme_id, region_id=region_id)
        query_string = await create_query_string(extension_id=extension_id, scheme_id=scheme_id, region_id=region_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/region/{region_id}", extension_id=extension_id, scheme_id=scheme_id, region_id=region_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import ServiceabilityModel
            schema = ServiceabilityModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateServiceability")
                print(e)

        return response
    
    async def createPackageMaterial(self, body="", request_headers:Dict={}):
        """This API returns response of upsert of PackageMaterial in mongo database.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createPackageMaterial()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PackageMaterial
        schema = PackageMaterial()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageMaterialResponse
            schema = PackageMaterialResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPackageMaterial")
                print(e)

        return response
    
    async def getPackageMaterialList(self, page_no=None, page_size=None, q=None, size=None, package_type=None, request_headers:Dict={}):
        """This API returns response of PackageMaterials from mongo database.
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param q : perform regex search on items matching name for given value : type string
        :param size : filters items based on given size : type string
        :param package_type : filters items based on given package_type : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if size is not None:
            payload["size"] = size
        if package_type is not None:
            payload["package_type"] = package_type

        # Parameter validation
        schema = ServiceabilityValidator.getPackageMaterialList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"q","description":"perform regex search on items matching name for given value","schema":{"type":"string"}},{"in":"query","name":"size","description":"filters items based on given size","schema":{"type":"string"}},{"in":"query","name":"package_type","description":"filters items based on given package_type","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"q","description":"perform regex search on items matching name for given value","schema":{"type":"string"}},{"in":"query","name":"size","description":"filters items based on given size","schema":{"type":"string"}},{"in":"query","name":"package_type","description":"filters items based on given package_type","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", page_no=page_no, page_size=page_size, q=q, size=size, package_type=package_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, size=size, package_type=package_type)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", page_no=page_no, page_size=page_size, q=q, size=size, package_type=package_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageMaterialList
            schema = PackageMaterialList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPackageMaterialList")
                print(e)

        return response
    
    async def createPackageMaterialRule(self, body="", request_headers:Dict={}):
        """This API returns response of upsert of Package Material Rule in mongo database.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createPackageMaterialRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PackageRule
        schema = PackageRule()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageRuleResponse
            schema = PackageRuleResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPackageMaterialRule")
                print(e)

        return response
    
    async def getPackageMaterialRules(self, page_no=None, page_size=None, is_active=None, request_headers:Dict={}):
        """This API returns response of Package Materials Rules from mongo database.
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param is_active : filters items based on given is_active : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if is_active is not None:
            payload["is_active"] = is_active

        # Parameter validation
        schema = ServiceabilityValidator.getPackageMaterialRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"filters items based on given is_active","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"filters items based on given is_active","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", page_no=page_no, page_size=page_size, is_active=is_active)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_active=is_active)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules", page_no=page_no, page_size=page_size, is_active=is_active), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageMaterialRuleList
            schema = PackageMaterialRuleList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPackageMaterialRules")
                print(e)

        return response
    
    async def updatePackageMaterialRule(self, rule_id=None, body="", request_headers:Dict={}):
        """This API updates Package Material Rules into mongo database.
        :param rule_id : A `package_material_rule_id` is a unique identifier for a Package Material Rule : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id

        # Parameter validation
        schema = ServiceabilityValidator.updatePackageMaterialRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PackageRule
        schema = PackageRule()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}]}""", rule_id=rule_id)
        query_string = await create_query_string(rule_id=rule_id)

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", rule_id=rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageRuleResponse
            schema = PackageRuleResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePackageMaterialRule")
                print(e)

        return response
    
    async def getPackageMaterialRule(self, rule_id=None, request_headers:Dict={}):
        """This API returns response of Package Material from mongo database.
        :param rule_id : A `package_material_rule_id` is a unique identifier for a Package Material Rule : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id

        # Parameter validation
        schema = ServiceabilityValidator.getPackageMaterialRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}]}""", rule_id=rule_id)
        query_string = await create_query_string(rule_id=rule_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", rule_id=rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageRuleResponse
            schema = PackageRuleResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPackageMaterialRule")
                print(e)

        return response
    
    async def updatePackageMaterials(self, package_material_id=None, body="", request_headers:Dict={}):
        """This API updates Package Materials from into mongo database.
        :param package_material_id : A `package_material_id` is a unique identifier for a Package Material : type string
        """
        payload = {}
        
        if package_material_id is not None:
            payload["package_material_id"] = package_material_id

        # Parameter validation
        schema = ServiceabilityValidator.updatePackageMaterials()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PackageMaterial
        schema = PackageMaterial()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"A `package_material_id` is a unique identifier for a Package Material","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"A `package_material_id` is a unique identifier for a Package Material","schema":{"type":"string"},"required":true}]}""", package_material_id=package_material_id)
        query_string = await create_query_string(package_material_id=package_material_id)

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", package_material_id=package_material_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageMaterialResponse
            schema = PackageMaterialResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePackageMaterials")
                print(e)

        return response
    
    async def getPackageMaterials(self, package_material_id=None, request_headers:Dict={}):
        """This API returns response of Package Material from mongo database.
        :param package_material_id : A `package_material_id` is a unique identifier for a Package Material : type string
        """
        payload = {}
        
        if package_material_id is not None:
            payload["package_material_id"] = package_material_id

        # Parameter validation
        schema = ServiceabilityValidator.getPackageMaterials()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"A `package_material_id` is a unique identifier for a Package Material","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"A `package_material_id` is a unique identifier for a Package Material","schema":{"type":"string"},"required":true}]}""", package_material_id=package_material_id)
        query_string = await create_query_string(package_material_id=package_material_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", package_material_id=package_material_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageMaterialResponse
            schema = PackageMaterialResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPackageMaterials")
                print(e)

        return response
    