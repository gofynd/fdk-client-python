"""User Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import UserValidator

class User:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def getCustomers(self, q=None, page_size=None, page_no=None, request_headers:Dict={}):
        """Retrieve details of users registered in the sales channel
        :param q : The search query. Mobile number or email ID of a customer. : type string
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no

        # Parameter validation
        schema = UserValidator.getCustomers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/list", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", q=q, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(q=q, page_size=page_size, page_no=page_no)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/list", q=q, page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomerListResponseSchema
            schema = CustomerListResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomers")
                print(e)

        return response
    
    async def searchUsers(self, q=None, query=None, request_headers:Dict={}):
        """Search and filter users details registered in the sales channel
        :param q : The search query. Mobile number or email ID of a customer. : type string
        :param query : The search queries. Mobile numbers or email IDs of customers. : type array
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = UserValidator.searchUsers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/search", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"string"}},{"name":"query","in":"query","description":"The search queries. Mobile numbers or email IDs of customers.","required":false,"schema":{"type":"array","items":{"type":"string"}}}],"query":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"string"}},{"name":"query","in":"query","description":"The search queries. Mobile numbers or email IDs of customers.","required":false,"schema":{"type":"array","items":{"type":"string"}}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", q=q, query=query)
        query_string = await create_query_string(q=q, query=query)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/search", q=q, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserSearchResponseSchema
            schema = UserSearchResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for searchUsers")
                print(e)

        return response
    
    async def createUser(self, body="", request_headers:Dict={}):
        """Register and add a new user to the sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.createUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUserRequestSchema
        schema = CreateUserRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateUserResponseSchema
            schema = CreateUserResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createUser")
                print(e)

        return response
    
    async def blockOrUnblockUsers(self, body="", request_headers:Dict={}):
        """Manage user access by blocking or unblocking their accounts, restricting login for blocked accounts and allowing login for unblocked accounts.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.blockOrUnblockUsers()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BlockUserRequestSchema
        schema = BlockUserRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/activation", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/activation", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BlockUserSuccess
            schema = BlockUserSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for blockOrUnblockUsers")
                print(e)

        return response
    
    async def unDeleteUser(self, body="", request_headers:Dict={}):
        """Restore a previously deleted user account.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.unDeleteUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UnDeleteUserRequestSchema
        schema = UnDeleteUserRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/undelete", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/undelete", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UnDeleteUserSuccess
            schema = UnDeleteUserSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for unDeleteUser")
                print(e)

        return response
    
    async def getUserTimeline(self, user_id=None, request_headers:Dict={}):
        """Fetches the timeline for the user who has made a data erase request. The timeline will show when the request was raised and when the request will be completed. It will also show if request has been cancelled before completion.
        :param user_id : User ID : type string
        """
        payload = {}
        
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = UserValidator.getUserTimeline()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/{user_id}/timeline", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"user_id","in":"path","description":"User ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"user_id","in":"path","description":"User ID","required":true,"schema":{"type":"string"}}]}""", serverType="platform", user_id=user_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/{user_id}/timeline", user_id=user_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetUserTimeline
            schema = GetUserTimeline()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserTimeline")
                print(e)

        return response
    
    async def updateUser(self, user_id=None, body="", request_headers:Dict={}):
        """Modify and update user profile information.
        :param user_id : User ID : type string
        """
        payload = {}
        
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = UserValidator.updateUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateUserRequestSchema
        schema = UpdateUserRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/{user_id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"user_id","in":"path","description":"User ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"user_id","in":"path","description":"User ID","required":true,"schema":{"type":"string"}}]}""", serverType="platform", user_id=user_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/{user_id}", user_id=user_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateUserResponseSchema
            schema = CreateUserResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateUser")
                print(e)

        return response
    
    async def createUserSession(self, body="", request_headers:Dict={}):
        """Create session for user interactions
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.createUserSession()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUserSessionRequestSchema
        schema = CreateUserSessionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/session", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/session", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateUserSessionResponseSchema
            schema = CreateUserSessionResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createUserSession")
                print(e)

        return response
    
    async def deleteSession(self, id=None, session_id=None, reason=None, request_headers:Dict={}):
        """Terminate an active user session.
        :param id : ID of a customer. : type string
        :param session_id : Session ID of a customer. : type string
        :param reason : Reason for deleting session. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if session_id is not None:
            payload["session_id"] = session_id
        if reason is not None:
            payload["reason"] = reason

        # Parameter validation
        schema = UserValidator.deleteSession()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/session", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"session_id","in":"query","description":"Session ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"reason","in":"query","description":"Reason for deleting session.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"session_id","in":"query","description":"Session ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"reason","in":"query","description":"Reason for deleting session.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id, session_id=session_id, reason=reason)
        query_string = await create_query_string(id=id, session_id=session_id, reason=reason)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/session", id=id, session_id=session_id, reason=reason), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SessionDeleteResponseSchema
            schema = SessionDeleteResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSession")
                print(e)

        return response
    
    async def getActiveSessions(self, id=None, request_headers:Dict={}):
        """Retrieve a list of currently active user sessions.
        :param id : ID of a customer. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = UserValidator.getActiveSessions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/sessions", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string(id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/sessions", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SessionListResponseSchema
            schema = SessionListResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getActiveSessions")
                print(e)

        return response
    
    async def deleteActiveSessions(self, id=None, reason=None, request_headers:Dict={}):
        """Terminate all active user sessions.
        :param id : ID of a customer. : type string
        :param reason : Reason to delete sessions. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if reason is not None:
            payload["reason"] = reason

        # Parameter validation
        schema = UserValidator.deleteActiveSessions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/sessions", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"reason","in":"query","description":"Reason to delete sessions.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"id","in":"query","description":"ID of a customer.","required":true,"schema":{"type":"string"}},{"name":"reason","in":"query","description":"Reason to delete sessions.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id, reason=reason)
        query_string = await create_query_string(id=id, reason=reason)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/sessions", id=id, reason=reason), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SessionsDeleteResponseSchema
            schema = SessionsDeleteResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteActiveSessions")
                print(e)

        return response
    
    async def archiveUser(self, body="", request_headers:Dict={}):
        """Delete user from sales channel, allowing re-registration with the same mobile/email for a new user account.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.archiveUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ArchiveUserRequestSchema
        schema = ArchiveUserRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/archive", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/archive", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ArchiveUserSuccess
            schema = ArchiveUserSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for archiveUser")
                print(e)

        return response
    
    async def getPlatformConfig(self, request_headers:Dict={}):
        """Retrieve platform sales channel authentication configuration.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.getPlatformConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformSchema
            schema = PlatformSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPlatformConfig")
                print(e)

        return response
    
    async def updatePlatformConfig(self, body="", request_headers:Dict={}):
        """Modify and update platform sales channel authentication configuration.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.updatePlatformConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformSchema
        schema = PlatformSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformSchema
            schema = PlatformSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePlatformConfig")
                print(e)

        return response
    
    async def createUserGroup(self, body="", request_headers:Dict={}):
        """Form and add a new user group.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.createUserGroup()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUserGroup
        schema = CreateUserGroup()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_group", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_group", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserGroupResponseSchema
            schema = UserGroupResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createUserGroup")
                print(e)

        return response
    
    async def getUserGroups(self, page_no=None, page_size=None, name=None, type=None, status=None, group_uid=None, request_headers:Dict={}):
        """Retrieve a list of user groups.
        :param page_no : page number for pagination result : type string
        :param page_size : page size for pagination result : type string
        :param name : to search for User Groups which contains given string in their name : type string
        :param type : to search for User Groups with given type : type string
        :param status : to get User Groups with given status : type string
        :param group_uid : to get User Groups with given uid : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if name is not None:
            payload["name"] = name
        if type is not None:
            payload["type"] = type
        if status is not None:
            payload["status"] = status
        if group_uid is not None:
            payload["group_uid"] = group_uid

        # Parameter validation
        schema = UserValidator.getUserGroups()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_group", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"page number for pagination result","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"page size for pagination result","required":false,"schema":{"type":"string"}},{"name":"name","in":"query","description":"to search for User Groups which contains given string in their name","required":false,"schema":{"type":"string"}},{"name":"type","in":"query","description":"to search for User Groups with given type","required":false,"schema":{"type":"string","enum":["bulk","conditional"]}},{"name":"status","in":"query","description":"to get User Groups with given status","required":false,"schema":{"type":"string"}},{"name":"group_uid","in":"query","description":"to get User Groups with given uid","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page_no","in":"query","description":"page number for pagination result","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"page size for pagination result","required":false,"schema":{"type":"string"}},{"name":"name","in":"query","description":"to search for User Groups which contains given string in their name","required":false,"schema":{"type":"string"}},{"name":"type","in":"query","description":"to search for User Groups with given type","required":false,"schema":{"type":"string","enum":["bulk","conditional"]}},{"name":"status","in":"query","description":"to get User Groups with given status","required":false,"schema":{"type":"string"}},{"name":"group_uid","in":"query","description":"to get User Groups with given uid","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, name=name, type=type, status=status, group_uid=group_uid)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, name=name, type=type, status=status, group_uid=group_uid)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_group", page_no=page_no, page_size=page_size, name=name, type=type, status=status, group_uid=group_uid), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserGroupListResponseSchema
            schema = UserGroupListResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserGroups")
                print(e)

        return response
    
    async def updateUserGroup(self, group_id=None, body="", request_headers:Dict={}):
        """Modify and update user group details.
        :param group_id : Numeric ID allotted to a User Group : type string
        """
        payload = {}
        
        if group_id is not None:
            payload["group_id"] = group_id

        # Parameter validation
        schema = UserValidator.updateUserGroup()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateUserGroupSchema
        schema = UpdateUserGroupSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_group/{group_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"group_id","in":"path","description":"Numeric ID allotted to a User Group","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"group_id","in":"path","description":"Numeric ID allotted to a User Group","required":true,"schema":{"type":"string"}}]}""", serverType="platform", group_id=group_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_group/{group_id}", group_id=group_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserGroupResponseSchema
            schema = UserGroupResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateUserGroup")
                print(e)

        return response
    
    async def getUserGroupById(self, group_id=None, request_headers:Dict={}):
        """Retrieve a user group by its unique identifier.
        :param group_id : Numeric ID allotted to a User Group : type string
        """
        payload = {}
        
        if group_id is not None:
            payload["group_id"] = group_id

        # Parameter validation
        schema = UserValidator.getUserGroupById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_group/{group_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"group_id","in":"path","description":"Numeric ID allotted to a User Group","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"group_id","in":"path","description":"Numeric ID allotted to a User Group","required":true,"schema":{"type":"string"}}]}""", serverType="platform", group_id=group_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_group/{group_id}", group_id=group_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserGroupResponseSchema
            schema = UserGroupResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserGroupById")
                print(e)

        return response
    
    async def updateUserGroupPartially(self, group_id=None, body="", request_headers:Dict={}):
        """Update user group partially on the platform.
        :param group_id : Numeric ID allotted to a User Group : type string
        """
        payload = {}
        
        if group_id is not None:
            payload["group_id"] = group_id

        # Parameter validation
        schema = UserValidator.updateUserGroupPartially()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PartialUserGroupUpdateSchema
        schema = PartialUserGroupUpdateSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_group/{group_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"group_id","in":"path","description":"Numeric ID allotted to a User Group","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"group_id","in":"path","description":"Numeric ID allotted to a User Group","required":true,"schema":{"type":"string"}}]}""", serverType="platform", group_id=group_id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_group/{group_id}", group_id=group_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserGroupResponseSchema
            schema = UserGroupResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateUserGroupPartially")
                print(e)

        return response
    
    async def createUserAttributeDefinition(self, body="", request_headers:Dict={}):
        """Create a new User Attribute Definition
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.createUserAttributeDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUserAttributeDefinition
        schema = CreateUserAttributeDefinition()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserAttributeDefinitionDetails
            schema = UserAttributeDefinitionDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createUserAttributeDefinition")
                print(e)

        return response
    
    async def getUserAttributeDefinitions(self, excluding_ids=None, slug=None, type=None, customer_editable=None, encrypted=None, pinned=None, pin_order=None, is_locked=None, name=None, page_size=None, page_no=None, request_headers:Dict={}):
        """Retrieve user attribute definitions.
        :param excluding_ids : Exclude attribute definitions by Ids : type string
        :param slug : Filter by attribute slug. : type string
        :param type : Filter by attribute type. : type string
        :param customer_editable : Filter by customer_editable status. : type boolean
        :param encrypted : Filter by encrypted status. : type boolean
        :param pinned : Filter by pinned status. : type boolean
        :param pin_order : Filter by pin order. : type integer
        :param is_locked : Filter by locked status. : type boolean
        :param name : Filter by attribute name using a case-insensitive regex. : type string
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        """
        payload = {}
        
        if excluding_ids is not None:
            payload["excluding_ids"] = excluding_ids
        if slug is not None:
            payload["slug"] = slug
        if type is not None:
            payload["type"] = type
        if customer_editable is not None:
            payload["customer_editable"] = customer_editable
        if encrypted is not None:
            payload["encrypted"] = encrypted
        if pinned is not None:
            payload["pinned"] = pinned
        if pin_order is not None:
            payload["pin_order"] = pin_order
        if is_locked is not None:
            payload["is_locked"] = is_locked
        if name is not None:
            payload["name"] = name
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no

        # Parameter validation
        schema = UserValidator.getUserAttributeDefinitions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"excluding_ids","schema":{"type":"string"},"description":"Exclude attribute definitions by Ids"},{"in":"query","name":"slug","schema":{"type":"string"},"description":"Filter by attribute slug."},{"in":"query","name":"type","schema":{"type":"string"},"description":"Filter by attribute type."},{"in":"query","name":"customer_editable","schema":{"type":"boolean"},"description":"Filter by customer_editable status."},{"in":"query","name":"encrypted","schema":{"type":"boolean"},"description":"Filter by encrypted status."},{"in":"query","name":"pinned","schema":{"type":"boolean"},"description":"Filter by pinned status."},{"in":"query","name":"pin_order","schema":{"type":"integer"},"description":"Filter by pin order."},{"in":"query","name":"is_locked","schema":{"type":"boolean"},"description":"Filter by locked status."},{"in":"query","name":"name","schema":{"type":"string"},"description":"Filter by attribute name using a case-insensitive regex."},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"query":[{"in":"query","name":"excluding_ids","schema":{"type":"string"},"description":"Exclude attribute definitions by Ids"},{"in":"query","name":"slug","schema":{"type":"string"},"description":"Filter by attribute slug."},{"in":"query","name":"type","schema":{"type":"string"},"description":"Filter by attribute type."},{"in":"query","name":"customer_editable","schema":{"type":"boolean"},"description":"Filter by customer_editable status."},{"in":"query","name":"encrypted","schema":{"type":"boolean"},"description":"Filter by encrypted status."},{"in":"query","name":"pinned","schema":{"type":"boolean"},"description":"Filter by pinned status."},{"in":"query","name":"pin_order","schema":{"type":"integer"},"description":"Filter by pin order."},{"in":"query","name":"is_locked","schema":{"type":"boolean"},"description":"Filter by locked status."},{"in":"query","name":"name","schema":{"type":"string"},"description":"Filter by attribute name using a case-insensitive regex."},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", excluding_ids=excluding_ids, slug=slug, type=type, customer_editable=customer_editable, encrypted=encrypted, pinned=pinned, pin_order=pin_order, is_locked=is_locked, name=name, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(excluding_ids=excluding_ids, slug=slug, type=type, customer_editable=customer_editable, encrypted=encrypted, pinned=pinned, pin_order=pin_order, is_locked=is_locked, name=name, page_size=page_size, page_no=page_no)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition", excluding_ids=excluding_ids, slug=slug, type=type, customer_editable=customer_editable, encrypted=encrypted, pinned=pinned, pin_order=pin_order, is_locked=is_locked, name=name, page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def updateUserAttributeDefinition(self, attribute_def_id=None, body="", request_headers:Dict={}):
        """Update an existing user attribute definition.
        :param attribute_def_id : The unique identifier of the attribute definition to update. : type string
        """
        payload = {}
        
        if attribute_def_id is not None:
            payload["attribute_def_id"] = attribute_def_id

        # Parameter validation
        schema = UserValidator.updateUserAttributeDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUserAttributeDefinition
        schema = CreateUserAttributeDefinition()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}", """{"required":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition to update."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition to update."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}]}""", serverType="platform", attribute_def_id=attribute_def_id, )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}", attribute_def_id=attribute_def_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserAttributeDefinition
            schema = UserAttributeDefinition()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateUserAttributeDefinition")
                print(e)

        return response
    
    async def deleteUserAttributeDefinitionById(self, attribute_def_id=None, request_headers:Dict={}):
        """Delete a user attribute definition by its unique identifier.
        :param attribute_def_id : The unique identifier of the attribute definition to delete. : type string
        """
        payload = {}
        
        if attribute_def_id is not None:
            payload["attribute_def_id"] = attribute_def_id

        # Parameter validation
        schema = UserValidator.deleteUserAttributeDefinitionById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}", """{"required":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition to delete."},{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition to delete."},{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", attribute_def_id=attribute_def_id, )
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}", attribute_def_id=attribute_def_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessage
            schema = SuccessMessage()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteUserAttributeDefinitionById")
                print(e)

        return response
    
    async def getUserAttributeDefinitionById(self, attribute_def_id=None, request_headers:Dict={}):
        """Get a user attribute definition by its unique identifier.
        :param attribute_def_id : The unique identifier of the attribute definition to retrieve. : type string
        """
        payload = {}
        
        if attribute_def_id is not None:
            payload["attribute_def_id"] = attribute_def_id

        # Parameter validation
        schema = UserValidator.getUserAttributeDefinitionById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}", """{"required":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition to retrieve."},{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition to retrieve."},{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", attribute_def_id=attribute_def_id, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}", attribute_def_id=attribute_def_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserAttributeDefinition
            schema = UserAttributeDefinition()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserAttributeDefinitionById")
                print(e)

        return response
    
    async def updateUserAttribute(self, attribute_def_id=None, user_id=None, body="", request_headers:Dict={}):
        """Update Or Create User Attribute
        :param attribute_def_id : The unique identifier of the attribute definition to update. : type string
        :param user_id : The unique identifier of the user to update. : type string
        """
        payload = {}
        
        if attribute_def_id is not None:
            payload["attribute_def_id"] = attribute_def_id
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = UserValidator.updateUserAttribute()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUserAttribute
        schema = CreateUserAttribute()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}/user/{user_id}", """{"required":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition to update."},{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user to update."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition to update."},{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user to update."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}]}""", serverType="platform", attribute_def_id=attribute_def_id, user_id=user_id, )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}/user/{user_id}", attribute_def_id=attribute_def_id, user_id=user_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserAttribute
            schema = UserAttribute()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateUserAttribute")
                print(e)

        return response
    
    async def getUserAttribute(self, attribute_def_id=None, user_id=None, request_headers:Dict={}):
        """Get User Attribute
        :param attribute_def_id : The unique identifier of the attribute definition. : type string
        :param user_id : The unique identifier of the user. : type string
        """
        payload = {}
        
        if attribute_def_id is not None:
            payload["attribute_def_id"] = attribute_def_id
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = UserValidator.getUserAttribute()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}/user/{user_id}", """{"required":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition."},{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition."},{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}]}""", serverType="platform", attribute_def_id=attribute_def_id, user_id=user_id, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}/user/{user_id}", attribute_def_id=attribute_def_id, user_id=user_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserAttribute
            schema = UserAttribute()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserAttribute")
                print(e)

        return response
    
    async def deleteUserAttribute(self, attribute_def_id=None, user_id=None, request_headers:Dict={}):
        """Delete User Attribute
        :param attribute_def_id : The unique identifier of the attribute definition. : type string
        :param user_id : The unique identifier of the user. : type string
        """
        payload = {}
        
        if attribute_def_id is not None:
            payload["attribute_def_id"] = attribute_def_id
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = UserValidator.deleteUserAttribute()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}/user/{user_id}", """{"required":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition."},{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"attribute_def_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute definition."},{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}]}""", serverType="platform", attribute_def_id=attribute_def_id, user_id=user_id, )
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/definition/{attribute_def_id}/user/{user_id}", attribute_def_id=attribute_def_id, user_id=user_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessage
            schema = SuccessMessage()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteUserAttribute")
                print(e)

        return response
    
    async def getUserAttributesForUser(self, user_id=None, page_size=None, page_no=None, request_headers:Dict={}):
        """Retrieve all user attributes for a specific user
        :param user_id : The unique identifier of the user to update. : type string
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        """
        payload = {}
        
        if user_id is not None:
            payload["user_id"] = user_id
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no

        # Parameter validation
        schema = UserValidator.getUserAttributesForUser()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/user/{user_id}", """{"required":[{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user to update."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user to update."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}]}""", serverType="platform", user_id=user_id, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(page_size=page_size, page_no=page_no)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/user/{user_id}", user_id=user_id, page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def updateUserAttributes(self, user_id=None, body="", request_headers:Dict={}):
        """This API is used to create or update multiple user attribute values for the specified user ID.
        :param user_id : The unique identifier of the user. : type string
        """
        payload = {}
        
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = UserValidator.updateUserAttributes()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateBulkUserAttribute
        schema = CreateBulkUserAttribute()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/user/{user_id}", """{"required":[{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"The unique identifier of the application."},{"in":"path","name":"company_id","schema":{"type":"integer"},"required":true,"description":"The unique identifier of the company."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"The unique identifier of the application."},{"in":"path","name":"company_id","schema":{"type":"integer"},"required":true,"description":"The unique identifier of the company."}]}""", serverType="platform", user_id=user_id, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/user/{user_id}", user_id=user_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkUserAttribute
            schema = BulkUserAttribute()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateUserAttributes")
                print(e)

        return response
    
    async def deleteUserAttributesInBulk(self, user_id=None, body="", request_headers:Dict={}):
        """This request deletes attribute values for a single user based on the provided user attribute definition. Each user attribute definition represents a distinct attribute, and for each definition, a user can have one corresponding value.
        :param user_id : The unique identifier of the user to update. : type string
        """
        payload = {}
        
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = UserValidator.deleteUserAttributesInBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DeleteBulkUserAttribute
        schema = DeleteBulkUserAttribute()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/user/{user_id}", """{"required":[{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user to update."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"The unique identifier of the application."},{"in":"path","name":"company_id","schema":{"type":"integer"},"required":true,"description":"The unique identifier of the company."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"user_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the user to update."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"The unique identifier of the application."},{"in":"path","name":"company_id","schema":{"type":"integer"},"required":true,"description":"The unique identifier of the company."}]}""", serverType="platform", user_id=user_id, )
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/user/{user_id}", user_id=user_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessage
            schema = SuccessMessage()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteUserAttributesInBulk")
                print(e)

        return response
    
    async def getUserAttributeById(self, attribute_id=None, request_headers:Dict={}):
        """Retrieve User Attribute details by ID.
        :param attribute_id : The unique identifier of the attribute to get. : type string
        """
        payload = {}
        
        if attribute_id is not None:
            payload["attribute_id"] = attribute_id

        # Parameter validation
        schema = UserValidator.getUserAttributeById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/attribute/{attribute_id}", """{"required":[{"in":"path","name":"attribute_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute to get."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"attribute_id","required":true,"schema":{"type":"string"},"description":"The unique identifier of the attribute to get."},{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}]}""", serverType="platform", attribute_id=attribute_id, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/attribute/{attribute_id}", attribute_id=attribute_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserAttribute
            schema = UserAttribute()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserAttributeById")
                print(e)

        return response
    
    async def bulkImportStoreFrontUsers(self, body="", request_headers:Dict={}):
        """The API allows bulk import of storefront customers using CSV or XLSX files.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.bulkImportStoreFrontUsers()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateStoreFrontUsersPayload
        schema = CreateStoreFrontUsersPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/jobs/import", """{"required":[{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/jobs/import", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkActionModel
            schema = BulkActionModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkImportStoreFrontUsers")
                print(e)

        return response
    
    async def getBulkImportUsersList(self, page_no=None, page_size=None, search=None, start_date=None, end_date=None, status=None, file_format=None, request_headers:Dict={}):
        """This API allows fetching the list of bulk user imports for a specific application and company.
It supports pagination and filtering based on various parameters.

        :param page_no : page number for pagination result : type string
        :param page_size : page size for pagination result : type string
        :param search : The search queries based on job name. : type string
        :param start_date : Start date : type string
        :param end_date : End date : type string
        :param status : Status of the Import Documents : type string
        :param file_format : Filter data based on file format eg csv or xlsx : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if search is not None:
            payload["search"] = search
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date
        if status is not None:
            payload["status"] = status
        if file_format is not None:
            payload["file_format"] = file_format

        # Parameter validation
        schema = UserValidator.getBulkImportUsersList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/jobs/import", """{"required":[{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}],"optional":[{"name":"page_no","in":"query","description":"page number for pagination result","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"page size for pagination result","required":false,"schema":{"type":"string"}},{"name":"search","in":"query","description":"The search queries based on job name.","required":false,"schema":{"type":"string"}},{"name":"start_date","in":"query","required":false,"schema":{"type":"string","format":"date-time"},"description":"Start date"},{"name":"end_date","in":"query","required":false,"schema":{"type":"string","format":"date-time"},"description":"End date"},{"name":"status","in":"query","required":false,"schema":{"type":"string","enum":["inprogress","failed","complete","partial"]},"description":"Status of the Import Documents"},{"name":"file_format","in":"query","description":"Filter data based on file format eg csv or xlsx","required":false,"schema":{"type":"string","enum":["csv","xlsx"]}}],"query":[{"name":"page_no","in":"query","description":"page number for pagination result","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"page size for pagination result","required":false,"schema":{"type":"string"}},{"name":"search","in":"query","description":"The search queries based on job name.","required":false,"schema":{"type":"string"}},{"name":"start_date","in":"query","required":false,"schema":{"type":"string","format":"date-time"},"description":"Start date"},{"name":"end_date","in":"query","required":false,"schema":{"type":"string","format":"date-time"},"description":"End date"},{"name":"status","in":"query","required":false,"schema":{"type":"string","enum":["inprogress","failed","complete","partial"]},"description":"Status of the Import Documents"},{"name":"file_format","in":"query","description":"Filter data based on file format eg csv or xlsx","required":false,"schema":{"type":"string","enum":["csv","xlsx"]}}],"headers":[],"path":[{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}]}""", serverType="platform", page_no=page_no, page_size=page_size, search=search, start_date=start_date, end_date=end_date, status=status, file_format=file_format)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, search=search, start_date=start_date, end_date=end_date, status=status, file_format=file_format)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/jobs/import", page_no=page_no, page_size=page_size, search=search, start_date=start_date, end_date=end_date, status=status, file_format=file_format), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkActionPaginationSchema
            schema = BulkActionPaginationSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkImportUsersList")
                print(e)

        return response
    
    async def createBulkExportUsers(self, body="", request_headers:Dict={}):
        """This API allows bulk export of storefront users by requesting files in CSV or XLSX format.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.createBulkExportUsers()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkUserExportSchema
        schema = BulkUserExportSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/jobs/export", """{"required":[{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/jobs/export", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkActionModel
            schema = BulkActionModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createBulkExportUsers")
                print(e)

        return response
    
    async def getBulkExportUsersList(self, page_no=None, page_size=None, file_format=None, search=None, start_date=None, end_date=None, status=None, request_headers:Dict={}):
        """This API allows fetching the list of bulk user exports for a specific application and company.
It supports pagination and filtering based on various parameters.

        :param page_no : page number for pagination result : type string
        :param page_size : page size for pagination result : type string
        :param file_format : Filter data based on file format eg csv or xlsx : type string
        :param search : The search queries based on job name. : type string
        :param start_date : Start date : type string
        :param end_date : End date : type string
        :param status : Status of the Import Documents : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if file_format is not None:
            payload["file_format"] = file_format
        if search is not None:
            payload["search"] = search
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date
        if status is not None:
            payload["status"] = status

        # Parameter validation
        schema = UserValidator.getBulkExportUsersList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/jobs/export", """{"required":[{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}],"optional":[{"name":"page_no","in":"query","description":"page number for pagination result","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"page size for pagination result","required":false,"schema":{"type":"string"}},{"name":"file_format","in":"query","description":"Filter data based on file format eg csv or xlsx","required":false,"schema":{"type":"string","enum":["csv","xlsx"]}},{"name":"search","in":"query","description":"The search queries based on job name.","required":false,"schema":{"type":"string"}},{"name":"start_date","in":"query","required":false,"schema":{"type":"string","format":"date-time"},"description":"Start date"},{"name":"end_date","in":"query","required":false,"schema":{"type":"string","format":"date-time"},"description":"End date"},{"name":"status","in":"query","required":false,"schema":{"type":"string","enum":["inprogress","failed","complete","partial"]},"description":"Status of the Import Documents"}],"query":[{"name":"page_no","in":"query","description":"page number for pagination result","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"page size for pagination result","required":false,"schema":{"type":"string"}},{"name":"file_format","in":"query","description":"Filter data based on file format eg csv or xlsx","required":false,"schema":{"type":"string","enum":["csv","xlsx"]}},{"name":"search","in":"query","description":"The search queries based on job name.","required":false,"schema":{"type":"string"}},{"name":"start_date","in":"query","required":false,"schema":{"type":"string","format":"date-time"},"description":"Start date"},{"name":"end_date","in":"query","required":false,"schema":{"type":"string","format":"date-time"},"description":"End date"},{"name":"status","in":"query","required":false,"schema":{"type":"string","enum":["inprogress","failed","complete","partial"]},"description":"Status of the Import Documents"}],"headers":[],"path":[{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"Application ID."},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"Company ID."}]}""", serverType="platform", page_no=page_no, page_size=page_size, file_format=file_format, search=search, start_date=start_date, end_date=end_date, status=status)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, file_format=file_format, search=search, start_date=start_date, end_date=end_date, status=status)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/jobs/export", page_no=page_no, page_size=page_size, file_format=file_format, search=search, start_date=start_date, end_date=end_date, status=status), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkActionPaginationSchema
            schema = BulkActionPaginationSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkExportUsersList")
                print(e)

        return response
    
    async def getUsersJobByJobId(self, job_id=None, request_headers:Dict={}):
        """This endpoint retrieves the details of a specific user's import and export related jobs associated with a given `job_id`, `application_id`, and `company_id`.

        :param job_id : The unique identifier of the job. This is used to fetch the details of the specific job.
 : type string
        """
        payload = {}
        
        if job_id is not None:
            payload["job_id"] = job_id

        # Parameter validation
        schema = UserValidator.getUsersJobByJobId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/jobs/{job_id}", """{"required":[{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"The unique identifier of the application. This is required to identify the application context for the job.\n"},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"The unique identifier of the company. This helps in scoping the request to the specific company.\n"},{"in":"path","name":"job_id","schema":{"type":"string"},"required":true,"description":"The unique identifier of the job. This is used to fetch the details of the specific job.\n"}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"application_id","schema":{"type":"string"},"required":true,"description":"The unique identifier of the application. This is required to identify the application context for the job.\n"},{"in":"path","name":"company_id","schema":{"type":"string"},"required":true,"description":"The unique identifier of the company. This helps in scoping the request to the specific company.\n"},{"in":"path","name":"job_id","schema":{"type":"string"},"required":true,"description":"The unique identifier of the job. This is used to fetch the details of the specific job.\n"}]}""", serverType="platform", job_id=job_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/jobs/{job_id}", job_id=job_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkActionModel
            schema = BulkActionModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUsersJobByJobId")
                print(e)

        return response
    
    async def filterUsersByAttributes(self, body="", request_headers:Dict={}):
        """Returns a filtered list of users based on user attribute conditions and along with details of definition Ids.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.filterUsersByAttributes()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UserAttributeFilter
        schema = UserAttributeFilter()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/users", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/user_attribute/users", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserAttributeFiltered
            schema = UserAttributeFiltered()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for filterUsersByAttributes")
                print(e)

        return response
    