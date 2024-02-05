"""Partner Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import PartnerValidator

class Partner:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def addProxyPath(self, extension_id=None, body="", request_headers:Dict={}):
        """Use this API to generate proxy URL for the external URL
        :param extension_id : Extension id for which a proxy URL will be generated : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id

        # Parameter validation
        schema = PartnerValidator.addProxyPath()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddProxyReq
        schema = AddProxyReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id","examples":{"success":{"value":"1"},"failure":{"value":"1"}}},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id","examples":{"success":{"value":"62048f967a73bc5f868ec6fc"},"failure":{"value":"62048f967a73bc5f868ec6fc"}}},{"name":"extension_id","in":"path","description":"Extension id for which a proxy URL will be generated","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"6073280be899ea5b1150fd9d"},"failure":{"value":"6073280be899ea5b1150fd9d"}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id","examples":{"success":{"value":"1"},"failure":{"value":"1"}}},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id","examples":{"success":{"value":"62048f967a73bc5f868ec6fc"},"failure":{"value":"62048f967a73bc5f868ec6fc"}}},{"name":"extension_id","in":"path","description":"Extension id for which a proxy URL will be generated","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"6073280be899ea5b1150fd9d"},"failure":{"value":"6073280be899ea5b1150fd9d"}}}]}""", extension_id=extension_id)
        query_string = await create_query_string(extension_id=extension_id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import AddProxyResponse
            schema = AddProxyResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addProxyPath")
                print(e)

        return response
    
    async def removeProxyPath(self, extension_id=None, attached_path=None, request_headers:Dict={}):
        """Use this API to remove the proxy URL which is already generated for the external URL
        :param extension_id : Extension id for which proxy URL needs to be removed : type string
        :param attached_path : Attached path slug : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if attached_path is not None:
            payload["attached_path"] = attached_path

        # Parameter validation
        schema = PartnerValidator.removeProxyPath()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}/{attached_path}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id","examples":{"success":{"value":"1"},"failure":{"value":"1"}}},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id","examples":{"success":{"value":"6073280be8r9ea5b1150fd9f"},"failure":{"value":"6073280be8r9ea5b1150fd9f"}}},{"name":"extension_id","in":"path","description":"Extension id for which proxy URL needs to be removed","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"6073280be899ea5b1150fd9d"},"failure":{"value":"6073280be899ea5b1150fd9d"}}},{"name":"attached_path","in":"path","description":"Attached path slug","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"invalid attached path"}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id","examples":{"success":{"value":"1"},"failure":{"value":"1"}}},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id","examples":{"success":{"value":"6073280be8r9ea5b1150fd9f"},"failure":{"value":"6073280be8r9ea5b1150fd9f"}}},{"name":"extension_id","in":"path","description":"Extension id for which proxy URL needs to be removed","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"6073280be899ea5b1150fd9d"},"failure":{"value":"6073280be899ea5b1150fd9d"}}},{"name":"attached_path","in":"path","description":"Attached path slug","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"invalid attached path"}}}]}""", extension_id=extension_id, attached_path=attached_path)
        query_string = await create_query_string(extension_id=extension_id, attached_path=attached_path)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}/{attached_path}", extension_id=extension_id, attached_path=attached_path), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import RemoveProxyResponse
            schema = RemoveProxyResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeProxyPath")
                print(e)

        return response
    