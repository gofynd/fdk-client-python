"""Authorization Partner Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PartnerConfig import PartnerConfig

from .validator import AuthorizationValidator

class Authorization:
    def __init__(self, config: PartnerConfig):
        self._conf = config

    
    async def createOrganizationClient(self, body="", request_headers:Dict={}):
        """Use this Api to create a new client for an organization
        """
        payload = {}
        

        # Parameter validation
        schema = AuthorizationValidator.createOrganizationClient()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ClientData
        schema = ClientData()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/authorization/v1.0/organization/{self._conf.organizationId}/oauth/client", """{"required":[{"in":"path","name":"organization_id","schema":{"type":"string"},"description":"The unique identifier for the organization.","required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"organization_id","schema":{"type":"string"},"description":"The unique identifier for the organization.","required":true}]}""", serverType="partner", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/authorization/v1.0/organization/{self._conf.organizationId}/oauth/client", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ClientResponse
            schema = ClientResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createOrganizationClient")
                print(e)

        return response
    
    async def getOrganizationClientList(self, page_no=None, page_size=None, is_active=None, request_headers:Dict={}):
        """Get the list of organization OAuth Client
        :param page_no : Page number for pagination : type integer
        :param page_size : Number of items per page : type integer
        :param is_active : wheather to filter by active status or not : type boolean
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if is_active is not None:
            payload["is_active"] = is_active

        # Parameter validation
        schema = AuthorizationValidator.getOrganizationClientList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/authorization/v1.0/organization/{self._conf.organizationId}/oauth/client", """{"required":[{"name":"organization_id","in":"path","required":true,"schema":{"type":"string"},"description":"The ID of the organization"}],"optional":[{"name":"page_no","in":"query","required":false,"schema":{"type":"integer"},"description":"Page number for pagination"},{"name":"page_size","in":"query","required":false,"schema":{"type":"integer"},"description":"Number of items per page"},{"name":"is_active","in":"query","required":false,"schema":{"type":"boolean"},"description":"wheather to filter by active status or not"}],"query":[{"name":"page_no","in":"query","required":false,"schema":{"type":"integer"},"description":"Page number for pagination"},{"name":"page_size","in":"query","required":false,"schema":{"type":"integer"},"description":"Number of items per page"},{"name":"is_active","in":"query","required":false,"schema":{"type":"boolean"},"description":"wheather to filter by active status or not"}],"headers":[],"path":[{"name":"organization_id","in":"path","required":true,"schema":{"type":"string"},"description":"The ID of the organization"}]}""", serverType="partner", page_no=page_no, page_size=page_size, is_active=is_active)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/authorization/v1.0/organization/{self._conf.organizationId}/oauth/client", page_no=page_no, page_size=page_size, is_active=is_active), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ClientListSchema
            schema = ClientListSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrganizationClientList")
                print(e)

        return response
    
    async def getOrganizationClientById(self, client_id=None, request_headers:Dict={}):
        """Get the organization oauth client by cliend id
        :param client_id : The ID of the client : type string
        """
        payload = {}
        
        if client_id is not None:
            payload["client_id"] = client_id

        # Parameter validation
        schema = AuthorizationValidator.getOrganizationClientById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/authorization/v1.0/organization/{self._conf.organizationId}/oauth/client/{client_id}", """{"required":[{"name":"organization_id","in":"path","required":true,"schema":{"type":"string"},"description":"The ID of the organization"},{"name":"client_id","in":"path","required":true,"schema":{"type":"string"},"description":"The ID of the client"}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","required":true,"schema":{"type":"string"},"description":"The ID of the organization"},{"name":"client_id","in":"path","required":true,"schema":{"type":"string"},"description":"The ID of the client"}]}""", serverType="partner", client_id=client_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/authorization/v1.0/organization/{self._conf.organizationId}/oauth/client/{client_id}", client_id=client_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ClientResponse
            schema = ClientResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrganizationClientById")
                print(e)

        return response
    
    async def updateOrganizationClientById(self, client_id=None, body="", request_headers:Dict={}):
        """Use this Api to Update OAuth Client name and tags description
        :param client_id : The ID of the client : type string
        """
        payload = {}
        
        if client_id is not None:
            payload["client_id"] = client_id

        # Parameter validation
        schema = AuthorizationValidator.updateOrganizationClientById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateClient
        schema = UpdateClient()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/authorization/v1.0/organization/{self._conf.organizationId}/oauth/client/{client_id}", """{"required":[{"in":"path","name":"organization_id","schema":{"type":"string"},"description":"The unique identifier for the organization.","required":true},{"name":"client_id","in":"path","required":true,"schema":{"type":"string"},"description":"The ID of the client"}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"organization_id","schema":{"type":"string"},"description":"The unique identifier for the organization.","required":true},{"name":"client_id","in":"path","required":true,"schema":{"type":"string"},"description":"The ID of the client"}]}""", serverType="partner", client_id=client_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/partner/authorization/v1.0/organization/{self._conf.organizationId}/oauth/client/{client_id}", client_id=client_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ClientResponse
            schema = ClientResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateOrganizationClientById")
                print(e)

        return response
    
    async def deleteOrganizationOAuthClientById(self, client_id=None, request_headers:Dict={}):
        """This endpoint allows you to delete a specific Organization OAuth client.
        :param client_id : ID of the OAuth client : type string
        """
        payload = {}
        
        if client_id is not None:
            payload["client_id"] = client_id

        # Parameter validation
        schema = AuthorizationValidator.deleteOrganizationOAuthClientById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/authorization/v1.0/organization/{self._conf.organizationId}/oauth/client/{client_id}", """{"required":[{"name":"organization_id","in":"path","description":"ID of the organization","required":true,"schema":{"type":"string"}},{"name":"client_id","in":"path","description":"ID of the OAuth client","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"ID of the organization","required":true,"schema":{"type":"string"}},{"name":"client_id","in":"path","description":"ID of the OAuth client","required":true,"schema":{"type":"string"}}]}""", serverType="partner", client_id=client_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/partner/authorization/v1.0/organization/{self._conf.organizationId}/oauth/client/{client_id}", client_id=client_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ClientResponse
            schema = ClientResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteOrganizationOAuthClientById")
                print(e)

        return response
    