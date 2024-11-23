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
    
    async def updateCourierRule(self, rule_id=None, body="", request_headers:Dict={}):
        """Updates an existing rule within the delivery configuration.
        :param rule_id : Unique identifier of the courier partner rule. : type string
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_id","description":"Unique identifier of the courier partner rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_id","description":"Unique identifier of the courier partner rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_id=rule_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_id}", rule_id=rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerRuleResult
            schema = CourierPartnerRuleResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierRule")
                print(e)

        return response
    
    async def getCourierPartnerRule(self, rule_id=None, request_headers:Dict={}):
        """Retrieves a single rule within the delivery configuration.
        :param rule_id : Unique identifier of the courier partner rule : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_id","description":"Unique identifier of the courier partner rule","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_id","description":"Unique identifier of the courier partner rule","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_id=rule_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules/{rule_id}", rule_id=rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        :param page_no : Index of the item to start returning with : type integer
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/rules", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"status","description":"Filter rules based on rule status","schema":{"type":"string","enum":[true,false]}}],"query":[{"in":"query","name":"page_no","description":"Index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"status","description":"Filter rules based on rule status","schema":{"type":"string","enum":[true,false]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, status=status)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, status=status)

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique Identifier of sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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
        from .models import SelfShipResult
        schema = SelfShipResult()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/selfship", """{"required":[{"name":"company_id","in":"path","description":"Unique identifier of the company.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"A `application_id` is a unique identifier for a particular sale channel.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Unique identifier of the company.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"A `application_id` is a unique identifier for a particular sale channel.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/selfship", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationSelfShipConfigResult
            schema = ApplicationSelfShipConfigResult()
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/selfship", """{"required":[{"name":"company_id","in":"path","description":"Unique identifier of the company.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"A `application_id` is a unique identifier for a particular sale channel.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Unique identifier of the company.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"A `application_id` is a unique identifier for a particular sale channel.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/selfship", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationSelfShipConfigResult
            schema = ApplicationSelfShipConfigResult()
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/configuration", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/configuration", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/configuration", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"status","required":false,"schema":{"type":"string","enum":["true","false","all"]}}],"query":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"status","required":false,"schema":{"type":"string","enum":["true","false","all"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, status=status)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, status=status)

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules/{rule_uid}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular rule object.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular rule object.","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_uid=rule_uid)
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/rules/{rule_uid}", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular rule object.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular rule object.","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_uid=rule_uid)
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
    