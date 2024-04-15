"""Communication Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import CommunicationValidator

class Communication:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getSystemNotifications(self, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve system notifications related to communication.
        :param page_no :  : type integer
        :param page_size :  : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CommunicationValidator.getSystemNotifications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/notification/system-notifications/", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}}],"optional":[{"in":"query","name":"page_no","schema":{"type":"integer","format":"int32","example":1}},{"in":"query","name":"page_size","schema":{"type":"integer","format":"int32","example":10}}],"query":[{"in":"query","name":"page_no","schema":{"type":"integer","format":"int32","example":1}},{"in":"query","name":"page_size","schema":{"type":"integer","format":"int32","example":10}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}}]}""", serverType="platform", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/notification/system-notifications/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SystemNotifications
            schema = SystemNotifications()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSystemNotifications")
                print(e)

        return response
    