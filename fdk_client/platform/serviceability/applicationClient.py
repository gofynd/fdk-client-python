

"""Serviceability Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import ServiceabilityValidator

class Serviceability:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId

    
    async def getApplicationServiceability(self, ):
        """This API returns serviceability config of the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getApplicationServiceability()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/serviceability", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/serviceability", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationServiceabilityConfigResponse
            schema = ApplicationServiceabilityConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationServiceability")
                print(e)

        

        return response
    
    async def getZonesFromApplicationIdView(self, page_no=None, page_size=None, zone_id=None, q=None):
        """This API returns zones from the application_id View.
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param zone_id : list of zones to query for : type array
        :param q : search with name as a free text : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if zone_id is not None:
            payload["zone_id"] = zone_id
        
        if q is not None:
            payload["q"] = q
        

        # Parameter validation
        schema = ServiceabilityValidator.getZonesFromApplicationIdView()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/zones", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` contains a specific ID of a company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` contains a unique ID.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"zone_id","description":"list of zones to query for","schema":{"type":"array","items":{"type":"string"}}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"zone_id","description":"list of zones to query for","schema":{"type":"array","items":{"type":"string"}}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` contains a specific ID of a company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` contains a unique ID.","schema":{"type":"string"},"required":true}]}""", page_no=page_no, page_size=page_size, zone_id=zone_id, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, zone_id=zone_id, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/zones", page_no=page_no, page_size=page_size, zone_id=zone_id, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetZoneFromApplicationIdViewResponse
            schema = GetZoneFromApplicationIdViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getZonesFromApplicationIdView")
                print(e)

        

        return response
    
    async def getZoneFromPincodeView(self, body=""):
        """This API returns zone from the Pincode View.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getZoneFromPincodeView()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetZoneFromPincodeViewRequest
        schema = GetZoneFromPincodeViewRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/zones", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` contains a specific ID of a company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` contains a unique ID.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` contains a specific ID of a company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` contains a unique ID.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/zones", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetZoneFromPincodeViewResponse
            schema = GetZoneFromPincodeViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getZoneFromPincodeView")
                print(e)

        

        return response
    
    async def addAppDp(self, body=""):
        """This API add application dp data.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.addAppDp()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationCompanyDpViewRequest
        schema = ApplicationCompanyDpViewRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier of a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier of a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationCompanyDpViewResponse
            schema = ApplicationCompanyDpViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addAppDp")
                print(e)

        

        return response
    
    async def deleteAppDp(self, courier_partner_id=None):
        """This API remove application dp data.
        :param courier_partner_id : A `courier_partner_id` is a unique identifier of a particular delivery partner. : type integer
        """
        payload = {}
        
        if courier_partner_id is not None:
            payload["courier_partner_id"] = courier_partner_id
        

        # Parameter validation
        schema = ServiceabilityValidator.deleteAppDp()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/{courier_partner_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier of a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"courier_partner_id","description":"A `courier_partner_id` is a unique identifier of a particular delivery partner.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier of a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"courier_partner_id","description":"A `courier_partner_id` is a unique identifier of a particular delivery partner.","schema":{"type":"integer"},"required":true}]}""", courier_partner_id=courier_partner_id)
        query_string = await create_query_string(courier_partner_id=courier_partner_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier-partner/{courier_partner_id}", courier_partner_id=courier_partner_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationCompanyDpViewResponse
            schema = ApplicationCompanyDpViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAppDp")
                print(e)

        

        return response
    
    async def updatePincodeMopView(self, body=""):
        """This API updates Pincode method of payment.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updatePincodeMopView()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PincodeMopData
        schema = PincodeMopData()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-update", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-update", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeMOPresponse
            schema = PincodeMOPresponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePincodeMopView")
                print(e)

        

        return response
    
    async def updatePincodeBulkView(self, body=""):
        """This API constructs bulk write operations to update the MOP data for each pincode in the payload.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updatePincodeBulkView()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PincodeMopBulkData
        schema = PincodeMopBulkData()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-bulk-update", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-bulk-update", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeBulkViewResponse
            schema = PincodeBulkViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePincodeBulkView")
                print(e)

        

        return response
    
    async def updatePincodeCoDListing(self, body=""):
        """This API returns count of active pincode.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updatePincodeCoDListing()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PincodeCodStatusListingRequest
        schema = PincodeCodStatusListingRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-data", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pincode-mop-data", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeCodStatusListingResponse
            schema = PincodeCodStatusListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePincodeCoDListing")
                print(e)

        

        return response
    
    async def updatePincodeAuditHistory(self, body=""):
        """This API returns Audit logs of Pincode.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updatePincodeAuditHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PincodeMopUpdateAuditHistoryRequest
        schema = PincodeMopUpdateAuditHistoryRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/history", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/history", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeMopUpdateAuditHistoryResponseData
            schema = PincodeMopUpdateAuditHistoryResponseData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePincodeAuditHistory")
                print(e)

        

        return response
    
    async def getDpApplicationRules(self, ):
        """This API returns response of all rules of DpApplicationRules from mongo database.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getDpApplicationRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier/priority", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier/priority", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DPApplicationRuleResponse
            schema = DPApplicationRuleResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDpApplicationRules")
                print(e)

        

        return response
    
    async def upsertDpApplicationRules(self, body=""):
        """This API returns response of upsert of DpApplicationRules in mongo database.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.upsertDpApplicationRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DPApplicationRuleRequest
        schema = DPApplicationRuleRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier/priority", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular application channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/courier/priority", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DPApplicationRuleResponse
            schema = DPApplicationRuleResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for upsertDpApplicationRules")
                print(e)

        

        return response
    
