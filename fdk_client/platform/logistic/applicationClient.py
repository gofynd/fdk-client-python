

"""Logistic Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import LogisticValidator

class Logistic:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getApplicationServiceability(self, ):
        """This API returns serviceability config of the application.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.getApplicationServiceability()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/serviceability", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/serviceability", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def upsertZoneControllerView(self, body=""):
        """This API returns zone from the Pincode View.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.upsertZoneControllerView()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.GetZoneFromPincodeViewRequest import GetZoneFromPincodeViewRequest
        schema = GetZoneFromPincodeViewRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/zones", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` contains a specific ID of a company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` contains a unique ID.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` contains a specific ID of a company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` contains a unique ID.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/zones", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

