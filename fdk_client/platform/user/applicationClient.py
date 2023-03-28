

"""User Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import UserValidator

class User:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getCustomers(self, q=None, page_size=None, page_no=None):
        """Use this API to retrieve a list of customers who have registered in the application.
        :param q : The search query. Mobile number or email ID of a customer. : type object
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        """
        payload = {}
        
        if q:
            payload["q"] = q
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = UserValidator.getCustomers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/list", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"object"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"object"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", q=q, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(q=q, page_size=page_size, page_no=page_no)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/list", q=q, page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def searchUsers(self, q=None):
        """Use this API to retrieve an existing user from a list.
        :param q : The search query. Mobile number or email ID of a customer. : type string
        """
        payload = {}
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = UserValidator.searchUsers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/search", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"string"}}],"query":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", q=q)
        query_string = await create_query_string(q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/search", q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createUser(self, body=""):
        """Create user
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.createUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUserRequestSchema
        schema = CreateUserRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def blockOrUnblockUsers(self, body=""):
        """Block/Unblock user
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.blockOrUnblockUsers()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BlockUserRequestSchema
        schema = BlockUserRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/activation", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/activation", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def archiveUser(self, body=""):
        """archive user
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.archiveUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ArchiveUserRequestSchema
        schema = ArchiveUserRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/archive", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/archive", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def unDeleteUser(self, body=""):
        """undelete user who deleted from application and have not elapsed the platform configured delete days
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.unDeleteUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UnDeleteUserRequestSchema
        schema = UnDeleteUserRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/undelete", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/undelete", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateUser(self, user_id=None, body=""):
        """Use this API to update user details, Note: Existing emails and phone numbers of user will be replaced directly if phone_numbers or emails field sent in request data.
        :param user_id : User ID : type string
        """
        payload = {}
        
        if user_id:
            payload["user_id"] = user_id
        

        # Parameter validation
        schema = UserValidator.updateUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateUserRequestSchema
        schema = UpdateUserRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/{user_id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"user_id","in":"path","description":"User ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"user_id","in":"path","description":"User ID","required":true,"schema":{"type":"string"}}]}""", user_id=user_id)
        query_string = await create_query_string(user_id=user_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/{user_id}", user_id=user_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def createUserSession(self, body=""):
        """Create user session
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.createUserSession()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUserSessionRequestSchema
        schema = CreateUserSessionRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/session", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/session", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteSession(self, id=None, session_id=None, reason=None):
        """Use this API to Delete a session of customers who have registered in the application.
        :param id : ID of a customer. : type string
        :param session_id : Session ID of a customer. : type string
        :param reason : Reason for deleting session. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if session_id:
            payload["session_id"] = session_id
        
        if reason:
            payload["reason"] = reason
        

        # Parameter validation
        schema = UserValidator.deleteSession()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/session", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"session_id","in":"query","description":"Session ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"reason","in":"query","description":"Reason for deleting session.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"session_id","in":"query","description":"Session ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"reason","in":"query","description":"Reason for deleting session.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", id=id, session_id=session_id, reason=reason)
        query_string = await create_query_string(id=id, session_id=session_id, reason=reason)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/session", id=id, session_id=session_id, reason=reason), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getActiveSessions(self, id=None):
        """Use this API to retrieve a list of session with info of customers who have registered in the application.
        :param id : ID of a customer. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = UserValidator.getActiveSessions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/sessions", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/sessions", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def deleteActiveSessions(self, id=None, reason=None):
        """Use this API to Delete a list of session of customers who have registered in the application.
        :param id : ID of a customer. : type string
        :param reason : Reason to delete sessions. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if reason:
            payload["reason"] = reason
        

        # Parameter validation
        schema = UserValidator.deleteActiveSessions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/sessions", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"reason","in":"query","description":"Reason to delete sessions.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"reason","in":"query","description":"Reason to delete sessions.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", id=id, reason=reason)
        query_string = await create_query_string(id=id, reason=reason)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/sessions", id=id, reason=reason), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getPlatformConfig(self, ):
        """Use this API to get all the platform configurations such as mobile image, desktop image, social logins, and all other text.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.getPlatformConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updatePlatformConfig(self, body=""):
        """Use this API to edit the existing platform configurations such as mobile image, desktop image, social logins, and all other text.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.updatePlatformConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformSchema
        schema = PlatformSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

