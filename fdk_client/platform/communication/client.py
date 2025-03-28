"""Communication Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import CommunicationValidator

class Communication:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getSystemNotifications(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieve system notifications related to communication.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type string
        :param query : To search based on plain text : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getSystemNotifications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/notification/system-notifications", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/notification/system-notifications", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SystemNotifications
            schema = SystemNotifications()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSystemNotifications")
                print(e)

        return response
    