"""Analytics Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import AnalyticsValidator

class Analytics:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def executeJobForProvidedParametersV2(self, body="", request_headers:Dict={}):
        """Query click events data
        """
        payload = {}
        

        # Parameter validation
        schema = AnalyticsValidator.executeJobForProvidedParametersV2()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import JobExecute
        schema = JobExecute()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/insights/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/job/execute", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"Value for the company ID"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"The application ID for the sales channel"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"Value for the company ID"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"The application ID for the sales channel"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/insights/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/job/execute", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import JobExecutionResult
            schema = JobExecutionResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for executeJobForProvidedParametersV2")
                print(e)

        return response
    
    async def startDownloadForQueryV2(self, export_type=None, body="", request_headers:Dict={}):
        """Initiates download job and returns job name
        :param export_type :  : type string
        """
        payload = {}
        
        if export_type is not None:
            payload["export_type"] = export_type

        # Parameter validation
        schema = AnalyticsValidator.startDownloadForQueryV2()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import FileDownloadRequestBody
        schema = FileDownloadRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/insights/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/job/download", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"Value for the company ID"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"The application ID for the sales channel"}},{"name":"export_type","in":"query","required":true,"schema":{"type":"string","description":"The file type for exporting your report.","enum":["csv","excel"]}}],"optional":[],"query":[{"name":"export_type","in":"query","required":true,"schema":{"type":"string","description":"The file type for exporting your report.","enum":["csv","excel"]}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"Value for the company ID"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"The application ID for the sales channel"}}]}""", serverType="platform", export_type=export_type)
        query_string = await create_query_string(export_type=export_type)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/insights/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/job/download", export_type=export_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def checkJobStatusByNameV2(self, file_name=None, request_headers:Dict={}):
        """Takes job name in path param to check the status of job Returns file URL if downloading is done else returns status of job
        :param file_name : Download job name : type string
        """
        payload = {}
        
        if file_name is not None:
            payload["file_name"] = file_name

        # Parameter validation
        schema = AnalyticsValidator.checkJobStatusByNameV2()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/insights/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/job/{file_name}/status", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"Value for the company ID"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"The application ID for the sales channel"}},{"name":"file_name","in":"path","description":"Download job name","required":true,"schema":{"type":"string","description":"File name for the job you want to know the status."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"Value for the company ID"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"The application ID for the sales channel"}},{"name":"file_name","in":"path","description":"Download job name","required":true,"schema":{"type":"string","description":"File name for the job you want to know the status."}}]}""", serverType="platform", file_name=file_name)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/insights/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/job/{file_name}/status", file_name=file_name), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import JobStatus
            schema = JobStatus()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkJobStatusByNameV2")
                print(e)

        return response
    