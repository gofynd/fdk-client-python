

"""Partner Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import PartnerValidator

class Partner:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def addProxyPath(self, extension_id=None, body=""):
        """Use this API to generate proxy URL for the external URL
        :param extension_id : Extension id for which proxy URL will be generated : type string
        """
        payload = {}
        
        if extension_id:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = PartnerValidator.addProxyPath()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddProxyReq
        schema = AddProxyReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"extension_id","in":"path","description":"Extension id for which proxy URL will be generated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"extension_id","in":"path","description":"Extension id for which proxy URL will be generated","required":true,"schema":{"type":"string"}}]}""", extension_id=extension_id)
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import AddProxyResponse
        schema = AddProxyResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for addProxyPath")
            print(e)
            
        

        return response
    
    async def removeProxyPath(self, extension_id=None, attached_path=None):
        """Use this API to remove the proxy URL which is already generated for the external URL
        :param extension_id : Extension id for which proxy URL needs to be removed : type string
        :param attached_path : Attachaed path slug : type string
        """
        payload = {}
        
        if extension_id:
            payload["extension_id"] = extension_id
        
        if attached_path:
            payload["attached_path"] = attached_path
        

        # Parameter validation
        schema = PartnerValidator.removeProxyPath()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}/{attached_path}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"extension_id","in":"path","description":"Extension id for which proxy URL needs to be removed","required":true,"schema":{"type":"string"}},{"name":"attached_path","in":"path","description":"Attachaed path slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"extension_id","in":"path","description":"Extension id for which proxy URL needs to be removed","required":true,"schema":{"type":"string"}},{"name":"attached_path","in":"path","description":"Attachaed path slug","required":true,"schema":{"type":"string"}}]}""", extension_id=extension_id, attached_path=attached_path)
        query_string = await create_query_string(extension_id=extension_id, attached_path=attached_path)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}/{attached_path}", extension_id=extension_id, attached_path=attached_path), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import RemoveProxyResponse
        schema = RemoveProxyResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for removeProxyPath")
            print(e)
            
        

        return response
    

