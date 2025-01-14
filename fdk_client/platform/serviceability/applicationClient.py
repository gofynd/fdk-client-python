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

    
    async def getZones(self, page_no=None, page_size=None, is_active=None, q=None, country_iso_code=None, state=None, city=None, pincode=None, sector=None, request_headers:Dict={}):
        """Retrieves a list of delivery zones.
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param is_active : Status of Zone (either active or inactive) : type boolean
        :param q : search with name as a free text : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"Status of Zone (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"application_id","description":"Zones filtered by an application","schema":{"type":"string"}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country","schema":{"type":"string"}},{"in":"query","name":"state","description":"State name","schema":{"type":"string"}},{"in":"query","name":"city","description":"City name","schema":{"type":"string"}},{"in":"query","name":"pincode","description":"Pincode value to search zones","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector value to search zones","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"Status of Zone (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"application_id","description":"Zones filtered by an application","schema":{"type":"string"}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country","schema":{"type":"string"}},{"in":"query","name":"state","description":"State name","schema":{"type":"string"}},{"in":"query","name":"city","description":"City name","schema":{"type":"string"}},{"in":"query","name":"pincode","description":"Pincode value to search zones","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector value to search zones","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, is_active=is_active, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_active=is_active, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/zones", page_no=page_no, page_size=page_size, is_active=is_active, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ListViewResponse
            schema = ListViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getZones")
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-update", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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
            from .models import PincodeMOPresponse
            schema = PincodeMOPresponse()
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-bulk-update", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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
            from .models import PincodeBulkViewResponse
            schema = PincodeBulkViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePincodeBulkView")
                print(e)

        return response
    
    async def updatePincodeCoDListing(self, body="", request_headers:Dict={}):
        """Retrieves a list of pincodes along with the count based on whether cash on delivery settings.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updatePincodeCoDListing()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PincodeCodStatusListingRequest
        schema = PincodeCodStatusListingRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-data", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-data", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeCodStatusListingResponse
            schema = PincodeCodStatusListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePincodeCoDListing")
                print(e)

        return response
    
    async def updatePincodeAuditHistory(self, body="", request_headers:Dict={}):
        """Retrieves the history of changes made to cash on delivery settings for pincodes.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updatePincodeAuditHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PincodeMopUpdateAuditHistoryRequest
        schema = PincodeMopUpdateAuditHistoryRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/history", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/history", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeMopUpdateAuditHistoryResponseData
            schema = PincodeMopUpdateAuditHistoryResponseData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePincodeAuditHistory")
                print(e)

        return response
    
    async def updateCourierRule(self, rule_id=None, body="", request_headers:Dict={}):
        """Updates an existing rule within the delivery configuration.
        :param rule_id : A `rule_id` is a unique identifier for a particular Dp. : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id

        # Parameter validation
        schema = ServiceabilityValidator.updateCourierRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerRule
        schema = CourierPartnerRule()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_id","description":"A `rule_id` is a unique identifier for a particular Dp.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_id","description":"A `rule_id` is a unique identifier for a particular Dp.","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_id=rule_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_id}", rule_id=rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerRuleResponse
            schema = CourierPartnerRuleResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierRule")
                print(e)

        return response
    
    async def getCourierPartnerRule(self, rule_id=None, request_headers:Dict={}):
        """Retrieves a single rule within the delivery configuration.
        :param rule_id : A `rule_id` is a unique identifier for a rule. : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_id","description":"A `rule_id` is a unique identifier for a rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_id","description":"A `rule_id` is a unique identifier for a rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_id=rule_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_id}", rule_id=rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerRuleResponse
            schema = CourierPartnerRuleResponse()
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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
            from .models import CourierPartnerRuleResponse
            schema = CourierPartnerRuleResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCourierPartnerRule")
                print(e)

        return response
    
    async def getCourierPartnerRules(self, page_no=None, page_size=None, status=None, request_headers:Dict={}):
        """Retrieve a list of rules within the delivery configuration.
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"status","description":"Filter rules based on rule status","schema":{"type":"string","enum":[true,false]}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"status","description":"Filter rules based on rule status","schema":{"type":"string","enum":[true,false]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, status=status)
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
            from .models import CourierPartnerRulesListResponse
            schema = CourierPartnerRulesListResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerRules")
                print(e)

        return response
    
    async def updateApplicationConfiguration(self, body="", request_headers:Dict={}):
        """Updates an existing delivery setup for an application, which involves updating sorting settings or rule priorities.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updateApplicationConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationConfig
        schema = ApplicationConfig()
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
            from .models import ApplicationConfig
            schema = ApplicationConfig()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateApplicationConfiguration")
                print(e)

        return response
    
    async def getApplicationConfiguration(self, request_headers:Dict={}):
        """Retrieves information about the delivery setup for an application
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
            from .models import ApplicationConfig
            schema = ApplicationConfig()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationConfiguration")
                print(e)

        return response
    
    async def patchApplicationServiceabilitySelfShipment(self, body="", request_headers:Dict={}):
        """Updates self ship setup for an existing application
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.patchApplicationServiceabilitySelfShipment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SelfShipResponse
        schema = SelfShipResponse()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/selfship", """{"required":[{"name":"company_id","in":"path","description":"A `company_id` is a unique identifier for a particular seller account.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"A `application_id` is a unique identifier for a particular sale channel.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"A `company_id` is a unique identifier for a particular seller account.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"A `application_id` is a unique identifier for a particular sale channel.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/selfship", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationSelfShipConfigResponse
            schema = ApplicationSelfShipConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for patchApplicationServiceabilitySelfShipment")
                print(e)

        return response
    
    async def getApplicationServiceabilitySelfShipment(self, request_headers:Dict={}):
        """Retrieves the self ship setup for a single application
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getApplicationServiceabilitySelfShipment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/selfship", """{"required":[{"name":"company_id","in":"path","description":"A `company_id` is a unique identifier for a particular seller account.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"A `application_id` is a unique identifier for a particular sale channel.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"A `company_id` is a unique identifier for a particular seller account.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"A `application_id` is a unique identifier for a particular sale channel.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/selfship", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationSelfShipConfigResponse
            schema = ApplicationSelfShipConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationServiceabilitySelfShipment")
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
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param status :  : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"status","required":false,"schema":{"type":"string","enum":["true","false","all"]}}],"query":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"status","required":false,"schema":{"type":"string","enum":["true","false","all"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, status=status)
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
            from .models import GetStoreRulesApiResponse
            schema = GetStoreRulesApiResponse()
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
        from .models import CreateStoreRuleRequestSchema
        schema = CreateStoreRuleRequestSchema()
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
            from .models import StoreRuleResponseSchema
            schema = StoreRuleResponseSchema()
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
        from .models import CreateStoreRuleRequestSchema
        schema = CreateStoreRuleRequestSchema()
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
            from .models import StoreRuleUpdateResponseSchema
            schema = StoreRuleUpdateResponseSchema()
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
        from .models import RulePriorityRequest
        schema = RulePriorityRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/priority", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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
            from .models import RulePriorityResponse
            schema = RulePriorityResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierPartnerRulePriority")
                print(e)

        return response
    