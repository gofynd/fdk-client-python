

"""Partner Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import PartnerValidator

class Partner:
    def __init__(self, config):
        self._conf = config

    
    async def subscribeExtension(self, entity=None, extension_id=None, entity_id=None, body=""):
        """Use this API to select plan for paid extension
        :param entity : entity : type string
        :param extension_id : extension id : type string
        :param entity_id : entity id : type string
        """
        payload = {}
        
        if entity is not None:
            payload["entity"] = entity
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        
        if entity_id is not None:
            payload["entity_id"] = entity_id
        

        # Parameter validation
        schema = PartnerValidator.subscribeExtension()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionRequest
        schema = SubscriptionRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/extension/{extension_id}/{entity}/{entity_id}/charge_consent", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"entity","in":"path","description":"entity","required":true,"schema":{"type":"string"}},{"name":"extension_id","in":"path","description":"extension id","required":true,"schema":{"type":"string"}},{"name":"entity_id","in":"path","description":"entity id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"entity","in":"path","description":"entity","required":true,"schema":{"type":"string"}},{"name":"extension_id","in":"path","description":"extension id","required":true,"schema":{"type":"string"}},{"name":"entity_id","in":"path","description":"entity id","required":true,"schema":{"type":"string"}}]}""", entity=entity, extension_id=extension_id, entity_id=entity_id)
        query_string = await create_query_string(entity=entity, extension_id=extension_id, entity_id=entity_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/extension/{extension_id}/{entity}/{entity_id}/charge_consent", entity=entity, extension_id=extension_id, entity_id=entity_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionRes
            schema = SubscriptionRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for subscribeExtension")
                print(e)

        

        return response
    
    async def getExtensionsForCompany(self, page_size=None, tag=None, current_page=None, page_no=None, filter_by=None, query=None):
        """Use this API to get the the extensions for the company
        :param page_size : Number of records you want to get in single page : type number
        :param tag : tag : type string
        :param current_page : tag : type string
        :param page_no : Current page number : type number
        :param filter_by : Filter by : type string
        :param query : query : type string
        """
        payload = {}
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if tag is not None:
            payload["tag"] = tag
        
        if current_page is not None:
            payload["current_page"] = current_page
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if filter_by is not None:
            payload["filter_by"] = filter_by
        
        if query is not None:
            payload["query"] = query
        

        # Parameter validation
        schema = PartnerValidator.getExtensionsForCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/extensions", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_size","in":"query","description":"Number of records you want to get in single page","schema":{"type":"number"},"example":10},{"name":"tag","in":"query","description":"tag","schema":{"type":"string"}},{"name":"current_page","in":"query","description":"tag","schema":{"type":"string"}},{"name":"page_no","in":"query","description":"Current page number","schema":{"type":"number"},"example":1},{"name":"filter_by","in":"query","description":"Filter by","schema":{"type":"string"},"example":"user_specific"},{"name":"query","in":"query","description":"query","schema":{"type":"string"}}],"query":[{"name":"page_size","in":"query","description":"Number of records you want to get in single page","schema":{"type":"number"},"example":10},{"name":"tag","in":"query","description":"tag","schema":{"type":"string"}},{"name":"current_page","in":"query","description":"tag","schema":{"type":"string"}},{"name":"page_no","in":"query","description":"Current page number","schema":{"type":"number"},"example":1},{"name":"filter_by","in":"query","description":"Filter by","schema":{"type":"string"},"example":"user_specific"},{"name":"query","in":"query","description":"query","schema":{"type":"string"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", page_size=page_size, tag=tag, current_page=current_page, page_no=page_no, filter_by=filter_by, query=query)
        query_string = await create_query_string(page_size=page_size, tag=tag, current_page=current_page, page_no=page_no, filter_by=filter_by, query=query)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/extensions", page_size=page_size, tag=tag, current_page=current_page, page_no=page_no, filter_by=filter_by, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ExtensionList
            schema = ExtensionList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getExtensionsForCompany")
                print(e)

        

        return response
    
    async def getPublicExtension(self, extension_id=None):
        """Use this API to get the details of public extensions
        :param extension_id : Extension id : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = PartnerValidator.getPublicExtension()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/public-extension/{extension_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}}]}""", extension_id=extension_id)
        query_string = await create_query_string(extension_id=extension_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/public-extension/{extension_id}", extension_id=extension_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PublicExtension
            schema = PublicExtension()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPublicExtension")
                print(e)

        

        return response
    
    async def getExtensionById(self, extension_id=None):
        """Use this API to get the details of extension
        :param extension_id : Extension id : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = PartnerValidator.getExtensionById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/extension/{extension_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}}]}""", extension_id=extension_id)
        query_string = await create_query_string(extension_id=extension_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/extension/{extension_id}", extension_id=extension_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ExtensionCommon
            schema = ExtensionCommon()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getExtensionById")
                print(e)

        

        return response
    
    async def deleteExtensionById(self, extension_id=None, message=None, uninstall_reason_type=None):
        """Use this API to remove extension from yout company or channel
        :param extension_id : Extension id : type string
        :param message : Message while uninstalling extension : type string
        :param uninstall_reason_type : Reason for uninstalling extension : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        
        if message is not None:
            payload["message"] = message
        
        if uninstall_reason_type is not None:
            payload["uninstall_reason_type"] = uninstall_reason_type
        

        # Parameter validation
        schema = PartnerValidator.deleteExtensionById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/extension/{extension_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}},{"name":"message","in":"query","description":"Message while uninstalling extension","required":true,"schema":{"type":"string"},"example":"not_needed_anymore"},{"name":"uninstall_reason_type","in":"query","description":"Reason for uninstalling extension","required":true,"schema":{"type":"string"},"example":"not_needed_anymore"}],"optional":[],"query":[{"name":"message","in":"query","description":"Message while uninstalling extension","required":true,"schema":{"type":"string"},"example":"not_needed_anymore"},{"name":"uninstall_reason_type","in":"query","description":"Reason for uninstalling extension","required":true,"schema":{"type":"string"},"example":"not_needed_anymore"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}}]}""", extension_id=extension_id, message=message, uninstall_reason_type=uninstall_reason_type)
        query_string = await create_query_string(extension_id=extension_id, message=message, uninstall_reason_type=uninstall_reason_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/extension/{extension_id}", extension_id=extension_id, message=message, uninstall_reason_type=uninstall_reason_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import UninstallExtension
            schema = UninstallExtension()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteExtensionById")
                print(e)

        

        return response
    
    async def getPrivateExtensions(self, page_size=None, page_no=None, query=None):
        """Use this API to get the list of private extensions
        :param page_size : Number of records you want to get in single page : type number
        :param page_no : Number of page : type number
        :param query : Filter query which we want to pass : type object
        """
        payload = {}
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if query is not None:
            payload["query"] = query
        

        # Parameter validation
        schema = PartnerValidator.getPrivateExtensions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/private-extensions", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_size","in":"query","description":"Number of records you want to get in single page","schema":{"type":"number"},"example":10},{"name":"page_no","in":"query","description":"Number of page","schema":{"type":"number"},"example":1},{"name":"query","in":"query","description":"Filter query which we want to pass","schema":{"type":"object"},"example":{"installed":"false"}}],"query":[{"name":"page_size","in":"query","description":"Number of records you want to get in single page","schema":{"type":"number"},"example":10},{"name":"page_no","in":"query","description":"Number of page","schema":{"type":"number"},"example":1},{"name":"query","in":"query","description":"Filter query which we want to pass","schema":{"type":"object"},"example":{"installed":"false"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", page_size=page_size, page_no=page_no, query=query)
        query_string = await create_query_string(page_size=page_size, page_no=page_no, query=query)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/private-extensions", page_size=page_size, page_no=page_no, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ExtensionResponse
            schema = ExtensionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPrivateExtensions")
                print(e)

        

        return response
    
    async def getExtensionsSuggestions(self, page_size=None):
        """Use this API to get the the extensions suggestions
        :param page_size : Number of records you want to get in single page : type number
        """
        payload = {}
        
        if page_size is not None:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = PartnerValidator.getExtensionsSuggestions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/extension/suggestions", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_size","in":"query","description":"Number of records you want to get in single page","schema":{"type":"number"},"example":3}],"query":[{"name":"page_size","in":"query","description":"Number of records you want to get in single page","schema":{"type":"number"},"example":3}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", page_size=page_size)
        query_string = await create_query_string(page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/extension/suggestions", page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ExtensionSuggestionList
            schema = ExtensionSuggestionList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getExtensionsSuggestions")
                print(e)

        

        return response
    
    async def getPartnerInvites(self, request_status=None, page_size=None, page_no=None):
        """Use this API to get pending, accepted and rejected partner invites in platform
        :param request_status : status of the request : type string
        :param page_size : Number of records per page : type string
        :param page_no : Number of page the user want to fetch : type string
        """
        payload = {}
        
        if request_status is not None:
            payload["request_status"] = request_status
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if page_no is not None:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = PartnerValidator.getPartnerInvites()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/partner-request", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"request_status","in":"query","description":"status of the request","schema":{"type":"string"},"example":"pending"},{"name":"page_size","in":"query","description":"Number of records per page","schema":{"type":"string"},"example":"10"},{"name":"page_no","in":"query","description":"Number of page the user want to fetch","schema":{"type":"string"},"example":"2"}],"query":[{"name":"request_status","in":"query","description":"status of the request","schema":{"type":"string"},"example":"pending"},{"name":"page_size","in":"query","description":"Number of records per page","schema":{"type":"string"},"example":"10"},{"name":"page_no","in":"query","description":"Number of page the user want to fetch","schema":{"type":"string"},"example":"2"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", request_status=request_status, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(request_status=request_status, page_size=page_size, page_no=page_no)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/partner-request", request_status=request_status, page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PartnerRequestList
            schema = PartnerRequestList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPartnerInvites")
                print(e)

        

        return response
    
    async def getPartnerRequestDetails(self, invite_id=None):
        """Use this API to get details of pending partner request
        :param invite_id : invitation id : type string
        """
        payload = {}
        
        if invite_id is not None:
            payload["invite_id"] = invite_id
        

        # Parameter validation
        schema = PartnerValidator.getPartnerRequestDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/partner-request/{invite_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"invite_id","in":"path","description":"invitation id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"invite_id","in":"path","description":"invitation id","required":true,"schema":{"type":"string"}}]}""", invite_id=invite_id)
        query_string = await create_query_string(invite_id=invite_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/partner-request/{invite_id}", invite_id=invite_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PartnerInviteDetails
            schema = PartnerInviteDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPartnerRequestDetails")
                print(e)

        

        return response
    
    async def modifyPartnerRequest(self, invite_id=None, body=""):
        """Use this API to approve or reject the pending partner request
        :param invite_id : invitation id : type string
        """
        payload = {}
        
        if invite_id is not None:
            payload["invite_id"] = invite_id
        

        # Parameter validation
        schema = PartnerValidator.modifyPartnerRequest()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ModifyPartnerReq
        schema = ModifyPartnerReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/partner-request/{invite_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"invite_id","in":"path","description":"invitation id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"invite_id","in":"path","description":"invitation id","required":true,"schema":{"type":"string"}}]}""", invite_id=invite_id)
        query_string = await create_query_string(invite_id=invite_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/partner-request/{invite_id}", invite_id=invite_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PartnerInviteDetails
            schema = PartnerInviteDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for modifyPartnerRequest")
                print(e)

        

        return response
    
    async def setupProducts(self, request_id=None):
        """Use this API for setup
        :param request_id : extrequest id : type string
        """
        payload = {}
        
        if request_id is not None:
            payload["request_id"] = request_id
        

        # Parameter validation
        schema = PartnerValidator.setupProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/setup", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"request_id","in":"query","description":"extrequest id","schema":{"type":"string"}}],"query":[{"name":"request_id","in":"query","description":"extrequest id","schema":{"type":"string"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", request_id=request_id)
        query_string = await create_query_string(request_id=request_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/setup", request_id=request_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SetupProductRes
            schema = SetupProductRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setupProducts")
                print(e)

        

        return response
    

