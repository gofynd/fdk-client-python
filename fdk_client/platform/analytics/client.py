

""" Analytics Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import AnalyticsValidator

class Analytics:
    def __init__(self, config):
        self._conf = config
    
    async def createExportJob(self, export_type=None, body=""):
        """Create data export job in required format
        :param export_type : Export type / format : type string
        """
        payload = {}
        
        if export_type:
            payload["export_type"] = export_type
        

        # Parameter validation
        schema = AnalyticsValidator.createExportJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ExportJobReq
        schema = ExportJobReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/export/{export_type}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"export_type","in":"path","description":"Export type / format","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"export_type","in":"path","description":"Export type / format","required":true,"schema":{"type":"string"}}]}""", export_type=export_type)
        query_string = await create_query_string(export_type=export_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/export/{export_type}", export_type=export_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getExportJobStatus(self, export_type=None, job_id=None):
        """Get data export job status
        :param export_type : Export type / format : type string
        :param job_id : Export job id : type string
        """
        payload = {}
        
        if export_type:
            payload["export_type"] = export_type
        
        if job_id:
            payload["job_id"] = job_id
        

        # Parameter validation
        schema = AnalyticsValidator.getExportJobStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/export/{export_type}/job/{job_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"export_type","in":"path","description":"Export type / format","required":true,"schema":{"type":"string"}},{"name":"job_id","in":"path","description":"Export job id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"export_type","in":"path","description":"Export type / format","required":true,"schema":{"type":"string"}},{"name":"job_id","in":"path","description":"Export job id","required":true,"schema":{"type":"string"}}]}""", export_type=export_type, job_id=job_id)
        query_string = await create_query_string(export_type=export_type, job_id=job_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/export/{export_type}/job/{job_id}", export_type=export_type, job_id=job_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getLogsList(self, log_type=None, page_no=None, page_size=None, body=""):
        """Get logs list
        :param log_type : Log type : type string
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        """
        payload = {}
        
        if log_type:
            payload["log_type"] = log_type
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = AnalyticsValidator.getLogsList()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetLogsListReq
        schema = GetLogsListReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/logs/{log_type}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"log_type","in":"path","description":"Log type","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"log_type","in":"path","description":"Log type","required":true,"schema":{"type":"string"}}]}""", log_type=log_type, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(log_type=log_type, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/logs/{log_type}", log_type=log_type, page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def searchLogs(self, page_no=None, page_size=None, log_type=None, body=""):
        """Search logs
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        :param log_type : Log type : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if log_type:
            payload["log_type"] = log_type
        

        # Parameter validation
        schema = AnalyticsValidator.searchLogs()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SearchLogReq
        schema = SearchLogReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/logs/{log_type}/search", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"log_type","in":"path","description":"Log type","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"log_type","in":"path","description":"Log type","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, log_type=log_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, log_type=log_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/logs/{log_type}/search", page_no=page_no, page_size=page_size, log_type=log_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

