"""Authorization Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import AuthorizationValidator

class Authorization:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def getApplicationStaffList(self, page_no=None, page_size=None, order_incent=None, ordering_store=None, user=None, user_name=None, request_headers:Dict={}):
        """Returns a paginated list of staff assigned to a sales channel, including each staff member's name, employee code, incentive eligibility, assigned ordering stores, and title.
        :param page_no : Page number for pagination. Defaults to 1. : type integer
        :param page_size : Number of staff members to return per page. Defaults to 10 and must not exceed 100. : type integer
        :param order_incent : Select `true` to retrieve only staff members eligible for incentives on orders. : type boolean
        :param ordering_store : Positive integer ID of the ordering store. Returns staff assigned to that store, plus application staff with the `admin` role. : type integer
        :param user : Unique ID of the user : type string
        :param user_name : Filter by the user's first or last name. : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if order_incent is not None:
            payload["order_incent"] = order_incent
        if ordering_store is not None:
            payload["ordering_store"] = ordering_store
        if user is not None:
            payload["user"] = user
        if user_name is not None:
            payload["user_name"] = user_name

        # Parameter validation
        schema = AuthorizationValidator.getApplicationStaffList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/authorization/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/staff/list", """{"required":[{"name":"company_id","in":"path","required":true,"description":"The unique identifier for the company.","schema":{"type":"integer","minimum":1}},{"name":"application_id","in":"path","required":true,"description":"Unique ID of the application","schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","required":false,"description":"Page number for pagination. Defaults to 1.","schema":{"type":"integer","minimum":1,"default":1}},{"name":"page_size","in":"query","required":false,"description":"Number of staff members to return per page. Defaults to 10 and must not exceed 100.","schema":{"type":"integer","minimum":1,"maximum":100,"default":10}},{"name":"order_incent","in":"query","required":false,"description":"Select `true` to retrieve only staff members eligible for incentives on orders.","schema":{"type":"boolean"}},{"name":"ordering_store","in":"query","required":false,"description":"Positive integer ID of the ordering store. Returns staff assigned to that store, plus application staff with the `admin` role.","schema":{"type":"integer","minimum":1}},{"name":"user","in":"query","required":false,"description":"Unique ID of the user","schema":{"type":"string"}},{"name":"user_name","in":"query","required":false,"description":"Filter by the user's first or last name.","schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","required":false,"description":"Page number for pagination. Defaults to 1.","schema":{"type":"integer","minimum":1,"default":1}},{"name":"page_size","in":"query","required":false,"description":"Number of staff members to return per page. Defaults to 10 and must not exceed 100.","schema":{"type":"integer","minimum":1,"maximum":100,"default":10}},{"name":"order_incent","in":"query","required":false,"description":"Select `true` to retrieve only staff members eligible for incentives on orders.","schema":{"type":"boolean"}},{"name":"ordering_store","in":"query","required":false,"description":"Positive integer ID of the ordering store. Returns staff assigned to that store, plus application staff with the `admin` role.","schema":{"type":"integer","minimum":1}},{"name":"user","in":"query","required":false,"description":"Unique ID of the user","schema":{"type":"string"}},{"name":"user_name","in":"query","required":false,"description":"Filter by the user's first or last name.","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"The unique identifier for the company.","schema":{"type":"integer","minimum":1}},{"name":"application_id","in":"path","required":true,"description":"Unique ID of the application","schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, order_incent=order_incent, ordering_store=ordering_store, user=user, user_name=user_name)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, order_incent=order_incent, ordering_store=ordering_store, user=user, user_name=user_name)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/authorization/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/staff/list", page_no=page_no, page_size=page_size, order_incent=order_incent, ordering_store=ordering_store, user=user, user_name=user_name), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationStaffPage
            schema = ApplicationStaffPage()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationStaffList")
                print(e)

        return response
    