"""Serviceability Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import ServiceabilityValidator

class Serviceability:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getZones(self, page_no=None, page_size=None, is_active=None, channel_id=None, q=None, country_iso_code=None, state=None, city=None, pincode=None, sector=None, request_headers:Dict={}):
        """Retrieves a list of delivery zones.
        :param page_no : Index of the item to start returning with : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param is_active : Status of Zone (either active or inactive) : type boolean
        :param channel_id : Zones filtered by an application : type string
        :param q : Search with name as a free text : type string
        :param country_iso_code : ISO2 code of the country : type string
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
        schema = ServiceabilityValidator.getZones()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"Status of Zone (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"channel_id","description":"Zones filtered by an application","schema":{"type":"string"}},{"in":"query","name":"q","description":"Search with name as a free text","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country","schema":{"type":"string","x-not-enum":true}},{"in":"query","name":"state","description":"State name","schema":{"type":"string"}},{"in":"query","name":"city","description":"City name","schema":{"type":"string"}},{"in":"query","name":"pincode","description":"Pincode value to search zones","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector value to search zones","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"Status of Zone (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"channel_id","description":"Zones filtered by an application","schema":{"type":"string"}},{"in":"query","name":"q","description":"Search with name as a free text","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country","schema":{"type":"string","x-not-enum":true}},{"in":"query","name":"state","description":"State name","schema":{"type":"string"}},{"in":"query","name":"city","description":"City name","schema":{"type":"string"}},{"in":"query","name":"pincode","description":"Pincode value to search zones","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector value to search zones","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, is_active=is_active, channel_id=channel_id, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_active=is_active, channel_id=channel_id, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones", page_no=page_no, page_size=page_size, is_active=is_active, channel_id=channel_id, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ListViewResult
            schema = ListViewResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getZones")
                print(e)

        return response
    
    async def createZone(self, body="", request_headers:Dict={}):
        """Creates a delivery zone.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createZone()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateZoneData
        schema = CreateZoneData()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ZoneResult
            schema = ZoneResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createZone")
                print(e)

        return response
    
    async def updateZoneById(self, zone_id=None, body="", request_headers:Dict={}):
        """Update an existing delivery zone .
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones/{zone_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"required":true}]}""", serverType="platform", zone_id=zone_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones/{zone_id}", zone_id=zone_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ZoneSuccessResult
            schema = ZoneSuccessResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateZoneById")
                print(e)

        return response
    
    async def getZoneById(self, zone_id=None, request_headers:Dict={}):
        """Retrieves a single delivery zone.
        :param zone_id : A `zone_id` is a unique identifier for a particular zone. : type string
        """
        payload = {}
        
        if zone_id is not None:
            payload["zone_id"] = zone_id

        # Parameter validation
        schema = ServiceabilityValidator.getZoneById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones/{zone_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"required":true}]}""", serverType="platform", zone_id=zone_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones/{zone_id}", zone_id=zone_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Retrieves a list of locations.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getAllStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/logistics/stores", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/logistics/stores", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetStoresViewResult
            schema = GetStoresViewResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllStores")
                print(e)

        return response
    
    async def createCourierPartnerAccount(self, body="", request_headers:Dict={}):
        """Creates a courier partner account.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createCourierPartnerAccount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierAccountDetailsBody
        schema = CourierAccountDetailsBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true,"example":123}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true,"example":123}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        """Retrieves a list of courier partner accounts.
        :param page_no : Index of the item to start returning with : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param stage : Stage of the account. enabled/disabled : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"Stage of the account. enabled/disabled","schema":{"type":"string","enum":["enabled","disabled"]}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string","x-not-enum":true}}],"query":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"Stage of the account. enabled/disabled","schema":{"type":"string","enum":["enabled","disabled"]}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string","x-not-enum":true}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyCourierPartnerAccountListResult
            schema = CompanyCourierPartnerAccountListResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerAccounts")
                print(e)

        return response
    
    async def updateCourierPartnerAccount(self, account_id=None, body="", request_headers:Dict={}):
        """Updates an existing courier partner account.
        :param account_id : Unique ID of courier partner account : type string
        """
        payload = {}
        
        if account_id is not None:
            payload["account_id"] = account_id

        # Parameter validation
        schema = ServiceabilityValidator.updateCourierPartnerAccount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierAccountUpdateDetails
        schema = CourierAccountUpdateDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier partner account","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier partner account","schema":{"type":"string"},"required":true}]}""", serverType="platform", account_id=account_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", account_id=account_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierAccountResult
            schema = CourierAccountResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierPartnerAccount")
                print(e)

        return response
    
    async def getCourierPartnerAccount(self, account_id=None, request_headers:Dict={}):
        """Retrieves a single courier partner account.
        :param account_id : Unique ID of courier partner account : type string
        """
        payload = {}
        
        if account_id is not None:
            payload["account_id"] = account_id

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerAccount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier partner account","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier partner account","schema":{"type":"string"},"required":true}]}""", serverType="platform", account_id=account_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", account_id=account_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierAccountResult
            schema = CourierAccountResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerAccount")
                print(e)

        return response
    
    async def updateCompanyConfiguration(self, body="", request_headers:Dict={}):
        """Updates an existing delivery setup for a company, including the ability to adjust self-shipping preferences.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updateCompanyConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CompanyConfig
        schema = CompanyConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        """Retrieves information about the delivery setup for a company
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getCompanyConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Updates locality wise TAT(Turn Around Time) for particular courier scheme using CSV file.
Export locality wise CSV files.
        :param extension_id : Unique Identifier of courier partner extension. : type string
        :param scheme_id : Unique identifier of courier partner scheme. : type string
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
        from .models import BulkRegionJobDetails
        schema = BulkRegionJobDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", extension_id=extension_id, scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResultItemData
            schema = BulkRegionResultItemData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkTat")
                print(e)

        return response
    
    async def getBulkTat(self, extension_id=None, scheme_id=None, page_no=None, page_size=None, batch_id=None, action=None, status=None, country=None, region=None, start_date=None, end_date=None, request_headers:Dict={}):
        """Retrieves the history of changes made to TAT(Turn Around Time) for scheme.
        :param extension_id : Unique Identifier of courier partner extension. : type string
        :param scheme_id : Unique identifier of courier partner scheme. : type string
        :param page_no : Index of the item to start returning with : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param batch_id : Unique identifier of bulk job : type string
        :param action : Import or export bulk type : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"Import or export bulk type","schema":{"type":"string","enum":["import","export"]}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string","enum":["processing","failed","partial","completed"]}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string","format":"date-time"}}],"query":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"Import or export bulk type","schema":{"type":"string","enum":["import","export"]}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string","enum":["processing","failed","partial","completed"]}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string","format":"date-time"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResult
            schema = BulkRegionResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkTat")
                print(e)

        return response
    
    async def bulkServiceability(self, extension_id=None, scheme_id=None, body="", request_headers:Dict={}):
        """Bulk operations involve either new serviceability settings or updating existing ones in large quantities.
        :param extension_id : Unique Identifier of courier partner extension. : type string
        :param scheme_id : Unique identifier of courier partner scheme. : type string
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
        from .models import BulkRegionJobDetails
        schema = BulkRegionJobDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", extension_id=extension_id, scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResultItemData
            schema = BulkRegionResultItemData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkServiceability")
                print(e)

        return response
    
    async def getBulkServiceability(self, extension_id=None, scheme_id=None, page_no=None, page_size=None, batch_id=None, action=None, status=None, country=None, region=None, start_date=None, end_date=None, request_headers:Dict={}):
        """Retrieves the history of changes made to serviceability settings for a scheme.
        :param extension_id : Unique Identifier of courier partner extension. : type string
        :param scheme_id : Unique identifier of courier partner scheme. : type string
        :param page_no : Index of the item to start returning with : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param batch_id : Unique identifier of bulk job : type string
        :param action : Import or export bulk type : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"Import or export bulk type","schema":{"type":"string","enum":["import","export"]}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string","enum":["completed","failed","partial","processing"]}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string","format":"date-time"}}],"query":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"Import or export bulk type","schema":{"type":"string","enum":["import","export"]}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string","enum":["completed","failed","partial","processing"]}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string","format":"date-time"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResult
            schema = BulkRegionResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkServiceability")
                print(e)

        return response
    
    async def getServiceability(self, extension_id=None, scheme_id=None, region_id=None, request_headers:Dict={}):
        """Rerieves serviceability settings of a single courier scheme for a given locality
        :param extension_id : Unique Identifier of courier partner extension. : type string
        :param scheme_id : Unique identifier of courier partner scheme. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/region/{region_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true},{"in":"path","name":"region_id","description":"Unique identifier of a region","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true},{"in":"path","name":"region_id","description":"Unique identifier of a region","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id, region_id=region_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/region/{region_id}", extension_id=extension_id, scheme_id=scheme_id, region_id=region_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Updates serviceability settings of a single courier scheme for a given locality
        :param extension_id : Unique Identifier of courier partner extension. : type string
        :param scheme_id : Unique identifier of courier partner scheme. : type string
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/region/{region_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true},{"in":"path","name":"region_id","description":"Unique identifier of a region","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of courier partner scheme.","schema":{"type":"string"},"required":true},{"in":"path","name":"region_id","description":"Unique identifier of a region","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id, region_id=region_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/region/{region_id}", extension_id=extension_id, scheme_id=scheme_id, region_id=region_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        """Creates a packaging material
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createPackageMaterial()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PackageMaterial
        schema = PackageMaterial()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageMaterialResult
            schema = PackageMaterialResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPackageMaterial")
                print(e)

        return response
    
    async def getPackageMaterialList(self, page_no=None, page_size=None, q=None, size=None, package_type=None, request_headers:Dict={}):
        """Retrieves a list of packaging materials
        :param page_no : Index of the item to start returning with : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param q : Perform regex search on items matching name for given value : type string
        :param size : Filters items based on given size : type string
        :param package_type : Filters items based on given package_type : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"q","description":"Perform regex search on items matching name for given value","schema":{"type":"string"}},{"in":"query","name":"size","description":"Filters items based on given size","schema":{"type":"string"}},{"in":"query","name":"package_type","description":"Filters items based on given package_type","schema":{"type":"string","x-not-enum":true}}],"query":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"q","description":"Perform regex search on items matching name for given value","schema":{"type":"string"}},{"in":"query","name":"size","description":"Filters items based on given size","schema":{"type":"string"}},{"in":"query","name":"package_type","description":"Filters items based on given package_type","schema":{"type":"string","x-not-enum":true}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q, size=size, package_type=package_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, size=size, package_type=package_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", page_no=page_no, page_size=page_size, q=q, size=size, package_type=package_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Creates a packaging rule
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createPackageMaterialRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PackageRule
        schema = PackageRule()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageRuleResult
            schema = PackageRuleResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPackageMaterialRule")
                print(e)

        return response
    
    async def getPackageMaterialRules(self, page_no=None, page_size=None, is_active=None, request_headers:Dict={}):
        """Retrieve packaging rules
        :param page_no : Index of the item to start returning with : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param is_active : Filters items based on given is_active : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"Filters items based on given is_active","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"Filters items based on given is_active","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, is_active=is_active)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_active=is_active)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules", page_no=page_no, page_size=page_size, is_active=is_active), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Update an existing packaging rule
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_id=rule_id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", rule_id=rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageRuleResult
            schema = PackageRuleResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePackageMaterialRule")
                print(e)

        return response
    
    async def getPackageMaterialRule(self, rule_id=None, request_headers:Dict={}):
        """Retrieve packaging rule details.
        :param rule_id : A `package_material_rule_id` is a unique identifier for a Package Material Rule : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id

        # Parameter validation
        schema = ServiceabilityValidator.getPackageMaterialRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_id=rule_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", rule_id=rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageRuleResult
            schema = PackageRuleResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPackageMaterialRule")
                print(e)

        return response
    
    async def updatePackageMaterials(self, package_material_id=None, body="", request_headers:Dict={}):
        """Update an existing packaging material
        :param package_material_id : Unique identifier for a Package. Material : type string
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"Unique identifier for a Package. Material","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"Unique identifier for a Package. Material","schema":{"type":"string"},"required":true}]}""", serverType="platform", package_material_id=package_material_id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", package_material_id=package_material_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageMaterialResult
            schema = PackageMaterialResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePackageMaterials")
                print(e)

        return response
    
    async def getPackageMaterials(self, package_material_id=None, request_headers:Dict={}):
        """Retrieve a single packaging material
        :param package_material_id : Unique identifier for a Package. Material : type string
        """
        payload = {}
        
        if package_material_id is not None:
            payload["package_material_id"] = package_material_id

        # Parameter validation
        schema = ServiceabilityValidator.getPackageMaterials()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"Unique identifier for a Package. Material","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"Unique identifier for a Package. Material","schema":{"type":"string"},"required":true}]}""", serverType="platform", package_material_id=package_material_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", package_material_id=package_material_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageMaterialResult
            schema = PackageMaterialResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPackageMaterials")
                print(e)

        return response
    
    async def getOptimalLocations(self, body="", request_headers:Dict={}):
        """Retrieves a list selling locations which are best suited to fullfil an order for a customer.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getOptimalLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OptimlLocationsDetailsSchema
        schema = OptimlLocationsDetailsSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/optimal-locations", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/optimal-locations", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OptimalLocationsResult
            schema = OptimalLocationsResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOptimalLocations")
                print(e)

        return response
    
    async def createCourierPartnerScheme(self, body="", request_headers:Dict={}):
        """Create Scheme for courier partner extension
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createCourierPartnerScheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerSchemeV2DetailsModel
        schema = CourierPartnerSchemeV2DetailsModel()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerV2SchemeModel
            schema = CourierPartnerV2SchemeModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCourierPartnerScheme")
                print(e)

        return response
    
    async def getCourierPartnerSchemes(self, scheme_type=None, payment_mode=None, capabilities=None, scheme_ids=None, request_headers:Dict={}):
        """Get created Schemes for courier partner
        :param scheme_type : Indicates whether a scheme is created by an admin for global purposes or customized for a specific company. : type string
        :param payment_mode : Indicates payment mode for a scheme. : type string
        :param capabilities : Indicates whether the scheme possesses certain capabilities. : type array
        :param scheme_ids : List of scheme ids which need to be returned in the response. : type array
        """
        payload = {}
        
        if scheme_type is not None:
            payload["scheme_type"] = scheme_type
        if payment_mode is not None:
            payload["payment_mode"] = payment_mode
        if capabilities is not None:
            payload["capabilities"] = capabilities
        if scheme_ids is not None:
            payload["scheme_ids"] = scheme_ids

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerSchemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"scheme_type","description":"Indicates whether a scheme is created by an admin for global purposes or customized for a specific company.","schema":{"type":"string","enum":["global","custom"]},"required":false},{"in":"query","name":"payment_mode","description":"Indicates payment mode for a scheme.","schema":{"type":"string","enum":["COD","PREPAID"]},"required":false},{"in":"query","name":"capabilities","description":"Indicates whether the scheme possesses certain capabilities.","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"scheme_ids","description":"List of scheme ids which need to be returned in the response.","schema":{"type":"array","items":{"type":"string"}},"required":false}],"query":[{"in":"query","name":"scheme_type","description":"Indicates whether a scheme is created by an admin for global purposes or customized for a specific company.","schema":{"type":"string","enum":["global","custom"]},"required":false},{"in":"query","name":"payment_mode","description":"Indicates payment mode for a scheme.","schema":{"type":"string","enum":["COD","PREPAID"]},"required":false},{"in":"query","name":"capabilities","description":"Indicates whether the scheme possesses certain capabilities.","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"scheme_ids","description":"List of scheme ids which need to be returned in the response.","schema":{"type":"array","items":{"type":"string"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", scheme_type=scheme_type, payment_mode=payment_mode, capabilities=capabilities, scheme_ids=scheme_ids)
        query_string = await create_query_string(scheme_type=scheme_type, payment_mode=payment_mode, capabilities=capabilities, scheme_ids=scheme_ids)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme", scheme_type=scheme_type, payment_mode=payment_mode, capabilities=capabilities, scheme_ids=scheme_ids), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import courierPartnerSchemeV2List
            schema = courierPartnerSchemeV2List()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerSchemes")
                print(e)

        return response
    
    async def updateCourierPartnerScheme(self, scheme_id=None, body="", request_headers:Dict={}):
        """Update Scheme for courier partner extension
        :param scheme_id : Unique Identifier of Scheme : type string
        """
        payload = {}
        
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id

        # Parameter validation
        schema = ServiceabilityValidator.updateCourierPartnerScheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerSchemeV2UpdateDetails
        schema = CourierPartnerSchemeV2UpdateDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme/{scheme_id}", """{"required":[{"in":"path","name":"scheme_id","description":"Unique Identifier of Scheme","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"scheme_id","description":"Unique Identifier of Scheme","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", scheme_id=scheme_id, )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme/{scheme_id}", scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerV2SchemeModel
            schema = CourierPartnerV2SchemeModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierPartnerScheme")
                print(e)

        return response
    
    async def getCourierPartnerScheme(self, scheme_id=None, request_headers:Dict={}):
        """Update Scheme for courier partner extension by Id
        :param scheme_id : Unique Identifier of Scheme : type string
        """
        payload = {}
        
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerScheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme/{scheme_id}", """{"required":[{"in":"path","name":"scheme_id","description":"Unique Identifier of Scheme","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"scheme_id","description":"Unique Identifier of Scheme","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", scheme_id=scheme_id, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme/{scheme_id}", scheme_id=scheme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerV2SchemeModel
            schema = CourierPartnerV2SchemeModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerScheme")
                print(e)

        return response
    
    async def sampleFileServiceability(self, body="", request_headers:Dict={}):
        """Sample File Download
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.sampleFileServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRegionServiceabilityTatDetails
        schema = BulkRegionServiceabilityTatDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/bulk-sample", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/bulk-sample", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionServiceabilityTatResultItemData
            schema = BulkRegionServiceabilityTatResultItemData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sampleFileServiceability")
                print(e)

        return response
    
    async def getSampleFileServiceabilityStatus(self, page_no=None, page_size=None, batch_id=None, request_headers:Dict={}):
        """Get Serviceability TAT sample file generator status
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param batch_id : Batch id of the execution : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if batch_id is not None:
            payload["batch_id"] = batch_id

        # Parameter validation
        schema = ServiceabilityValidator.getSampleFileServiceabilityStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/bulk-sample", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Batch id of the execution","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Batch id of the execution","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, batch_id=batch_id, )
        query_string = await create_query_string(page_no=page_no, page_size=page_size, batch_id=batch_id, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/bulk-sample", page_no=page_no, page_size=page_size, batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionServiceabilityTatResult
            schema = BulkRegionServiceabilityTatResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSampleFileServiceabilityStatus")
                print(e)

        return response
    
    async def getCountries(self, onboarding=None, page_no=None, page_size=None, q=None, hierarchy=None, request_headers:Dict={}):
        """Retrieve a list of countries for logistical purposes.
        :param onboarding : Only fetch countries which allowed for onboard on Platform. : type boolean
        :param page_no : page number. : type integer
        :param page_size : page size. : type integer
        :param q : search. : type string
        :param hierarchy : fetch countries that has certain heirarchy present. : type string
        """
        payload = {}
        
        if onboarding is not None:
            payload["onboarding"] = onboarding
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if hierarchy is not None:
            payload["hierarchy"] = hierarchy

        # Parameter validation
        schema = ServiceabilityValidator.getCountries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/countries", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"onboarding","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer","default":12,"maximum":48},"required":false},{"in":"query","name":"q","description":"search.","schema":{"type":"string"},"required":false},{"in":"query","name":"hierarchy","description":"fetch countries that has certain heirarchy present.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"onboarding","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer","default":12,"maximum":48},"required":false},{"in":"query","name":"q","description":"search.","schema":{"type":"string"},"required":false},{"in":"query","name":"hierarchy","description":"fetch countries that has certain heirarchy present.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", onboarding=onboarding, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy, )
        query_string = await create_query_string(onboarding=onboarding, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/countries", onboarding=onboarding, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCountries
            schema = GetCountries()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCountries")
                print(e)

        return response
    