

""" AuditTrail Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import AuditTrailValidator

class AuditTrail:
    def __init__(self, config):
        self._conf = config
    
    async def getAuditLogs(self, qs=None):
        """Get audit logs
        :param qs : Logs Query : type string
        """
        payload = {}
        
        if qs:
            payload["qs"] = qs
        

        # Parameter validation
        schema = AuditTrailValidator.getAuditLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", """{"required":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}},{"in":"query","name":"qs","description":"Logs Query","required":true,"schema":{"type":"string","example":"%7B%7D&limit=10&company=61&sort=%7B%22_id%22%3A-1%7D"}}],"optional":[],"query":[{"in":"query","name":"qs","description":"Logs Query","required":true,"schema":{"type":"string","example":"%7B%7D&limit=10&company=61&sort=%7B%22_id%22%3A-1%7D"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}}]}""", qs=qs)
        query_string = await create_query_string(qs=qs)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", qs=qs), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createAuditLog(self, body=""):
        """Create a Audit log
        """
        payload = {}
        

        # Parameter validation
        schema = AuditTrailValidator.createAuditLog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.RequestBodyAuditLog import RequestBodyAuditLog
        schema = RequestBodyAuditLog()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAuditLog(self, id=None):
        """Get audit logs by logs uuid
        :param id : log uuid : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = AuditTrailValidator.getAuditLog()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/{id}", """{"required":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"id","description":"log uuid","required":true,"schema":{"type":"string","example":"602a1366a7486d63f1e915b2"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"id","description":"log uuid","required":true,"schema":{"type":"string","example":"602a1366a7486d63f1e915b2"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getEntityTypes(self, ):
        """Get entity types
        """
        payload = {}
        

        # Parameter validation
        schema = AuditTrailValidator.getEntityTypes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/entity-types", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/entity-types", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

