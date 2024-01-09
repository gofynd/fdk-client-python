"""AuditTrail Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import AuditTrailValidator

class AuditTrail:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getAuditLogs(self, qs=None, limit=None, sort=None, request_headers:Dict={}):
        """Get a paginated set of logs that can be filtered using the available set of parameters and get the relevant group of logs
        :param qs : Logs Query : type string
        :param limit : Current request items count : type integer
        :param sort : To sort based on _id : type object
        """
        payload = {}
        
        if qs is not None:
            payload["qs"] = qs
        if limit is not None:
            payload["limit"] = limit
        if sort is not None:
            payload["sort"] = sort

        # Parameter validation
        schema = AuditTrailValidator.getAuditLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", """{"required":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}},{"in":"query","name":"qs","description":"Logs Query","required":true,"schema":{"type":"string","example":"%7B%7D&limit=10&company=61&sort=%7B%22_id%22%3A-1%7D"}}],"optional":[{"name":"limit","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"_id":{"type":"integer","enum":[-1,1]}}},"description":"To sort based on _id"}],"query":[{"in":"query","name":"qs","description":"Logs Query","required":true,"schema":{"type":"string","example":"%7B%7D&limit=10&company=61&sort=%7B%22_id%22%3A-1%7D"}},{"name":"limit","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"_id":{"type":"integer","enum":[-1,1]}}},"description":"To sort based on _id"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}}]}""", qs=qs, limit=limit, sort=sort)
        query_string = await create_query_string(qs=qs, limit=limit, sort=sort)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", qs=qs, limit=limit, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import LogSchemaResponse
            schema = LogSchemaResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAuditLogs")
                print(e)

        return response
    
    async def createAuditLog(self, body="", request_headers:Dict={}):
        """Create a log instance that stores all the relevant info to be logged
        """
        payload = {}
        

        # Parameter validation
        schema = AuditTrailValidator.createAuditLog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RequestBodyAuditLog
        schema = RequestBodyAuditLog()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateLogResponse
            schema = CreateLogResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAuditLog")
                print(e)

        return response
    
    async def getAuditLog(self, id=None, request_headers:Dict={}):
        """Get detailed log information by their id
        :param id : log uuid : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = AuditTrailValidator.getAuditLog()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/{id}", """{"required":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"id","description":"log uuid","required":true,"schema":{"type":"string","example":"602a1366a7486d63f1e915b2"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"id","description":"log uuid","required":true,"schema":{"type":"string","example":"602a1366a7486d63f1e915b2"}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import LogSchemaResponse
            schema = LogSchemaResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAuditLog")
                print(e)

        return response
    
    async def getEntityTypes(self, request_headers:Dict={}):
        """Get a consolidated list of entity types from all the logs stored on the db, which further helps to filter the logs better
        """
        payload = {}
        

        # Parameter validation
        schema = AuditTrailValidator.getEntityTypes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/entity-types", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/entity-types", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import EntityTypesResponse
            schema = EntityTypesResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEntityTypes")
                print(e)

        return response
    