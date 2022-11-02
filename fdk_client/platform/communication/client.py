

""" Communication Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import CommunicationValidator

class Communication:
    def __init__(self, config):
        self._conf = config
    
    async def getSystemNotifications(self, page_no=None, page_size=None):
        """Get system notifications
        :param page_no :  : type integer
        :param page_size :  : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CommunicationValidator.getSystemNotifications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/notification/system-notifications/", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}}],"optional":[{"in":"query","name":"page_no","schema":{"type":"integer","format":"int32","example":1}},{"in":"query","name":"page_size","schema":{"type":"integer","format":"int32","example":10}}],"query":[{"in":"query","name":"page_no","schema":{"type":"integer","format":"int32","example":1}},{"in":"query","name":"page_size","schema":{"type":"integer","format":"int32","example":10}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/notification/system-notifications/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
