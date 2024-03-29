"""Inventory Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import InventoryValidator

class Inventory:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getJobsByCompany(self, page_no=None, page_size=None, request_headers:Dict={}):
        """REST Endpoint that returns all job configs for a company
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = InventoryValidator.getJobsByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeListJobConfigRawDTO
            schema = ResponseEnvelopeListJobConfigRawDTO()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobsByCompany")
                print(e)

        return response
    
    async def updateJob(self, body="", request_headers:Dict={}):
        """REST Endpoint that updates a job config
        """
        payload = {}
        

        # Parameter validation
        schema = InventoryValidator.updateJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import JobConfigDTO
        schema = JobConfigDTO()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeString
            schema = ResponseEnvelopeString()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateJob")
                print(e)

        return response
    
    async def createJob(self, body="", request_headers:Dict={}):
        """REST Endpoint that creates a new job config
        """
        payload = {}
        

        # Parameter validation
        schema = InventoryValidator.createJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import JobConfigDTO
        schema = JobConfigDTO()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeString
            schema = ResponseEnvelopeString()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createJob")
                print(e)

        return response
    
    async def suppressStores(self, body="", request_headers:Dict={}):
        """REST Endpoint that returns all configuration detail of a company
        """
        payload = {}
        

        # Parameter validation
        schema = InventoryValidator.suppressStores()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SuppressStorePayload
        schema = SuppressStorePayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/kafka/suppressStore", """{"required":[{"name":"company_id","in":"path","description":"Company id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/kafka/suppressStore", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeKafkaResponse
            schema = ResponseEnvelopeKafkaResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for suppressStores")
                print(e)

        return response
    
    async def getConfigByCompany(self, request_headers:Dict={}):
        """REST Endpoint that returns all configuration detail of a company
        """
        payload = {}
        

        # Parameter validation
        schema = InventoryValidator.getConfigByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/slingshot", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/slingshot", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeListSlingshotConfigurationDetail
            schema = ResponseEnvelopeListSlingshotConfigurationDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getConfigByCompany")
                print(e)

        return response
    
    async def getJobSteps(self, job_id=None, request_headers:Dict={}):
        """REST Endpoint that returns Inventory Job Steps
        :param job_id : Job Id : type integer
        """
        payload = {}
        
        if job_id is not None:
            payload["job_id"] = job_id

        # Parameter validation
        schema = InventoryValidator.getJobSteps()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/steps/{job_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"job_id","in":"path","description":"Job Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"job_id","in":"path","description":"Job Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", job_id=job_id)
        query_string = await create_query_string(job_id=job_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/steps/{job_id}", job_id=job_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeListJobStepsDTO
            schema = ResponseEnvelopeListJobStepsDTO()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobSteps")
                print(e)

        return response
    
    async def getJobByCompanyAndIntegration(self, integration_id=None, page_no=None, page_size=None, request_headers:Dict={}):
        """REST Endpoint that returns all job configs by company And integration
        :param integration_id : Integration Id : type string
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        """
        payload = {}
        
        if integration_id is not None:
            payload["integration_id"] = integration_id
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = InventoryValidator.getJobByCompanyAndIntegration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/integration/{integration_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"Integration Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"Integration Id","required":true,"schema":{"type":"string"}}]}""", integration_id=integration_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(integration_id=integration_id, page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/integration/{integration_id}", integration_id=integration_id, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeListJobConfigDTO
            schema = ResponseEnvelopeListJobConfigDTO()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobByCompanyAndIntegration")
                print(e)

        return response
    
    async def disable(self, integration_id=None, request_headers:Dict={}):
        """REST Endpoint that disables Inventory Job Config
        :param integration_id : IntegrationId : type string
        """
        payload = {}
        
        if integration_id is not None:
            payload["integration_id"] = integration_id

        # Parameter validation
        schema = InventoryValidator.disable()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/disable/integration/{integration_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"IntegrationId","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"IntegrationId","required":true,"schema":{"type":"string"}}]}""", integration_id=integration_id)
        query_string = await create_query_string(integration_id=integration_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/disable/integration/{integration_id}", integration_id=integration_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeString
            schema = ResponseEnvelopeString()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for disable")
                print(e)

        return response
    
    async def getJobConfigDefaults(self, request_headers:Dict={}):
        """REST Endpoint that returns default fields job configs by company And integration
        """
        payload = {}
        

        # Parameter validation
        schema = InventoryValidator.getJobConfigDefaults()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/defaults", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/defaults", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeJobConfigDTO
            schema = ResponseEnvelopeJobConfigDTO()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobConfigDefaults")
                print(e)

        return response
    
    async def getJobByCode(self, code=None, request_headers:Dict={}):
        """REST Endpoint that returns job config by code
        :param code : Job Code : type string
        """
        payload = {}
        
        if code is not None:
            payload["code"] = code

        # Parameter validation
        schema = InventoryValidator.getJobByCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/{code}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"code","in":"path","description":"Job Code","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"code","in":"path","description":"Job Code","required":true,"schema":{"type":"string"}}]}""", code=code)
        query_string = await create_query_string(code=code)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/{code}", code=code), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeJobConfigDTO
            schema = ResponseEnvelopeJobConfigDTO()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobByCode")
                print(e)

        return response
    
    async def getJobCodeMetrics(self, code=None, page_no=None, page_size=None, status=None, date=None, request_headers:Dict={}):
        """REST Endpoint that returns Inventory Run History For A Job Code
        :param code : Code : type string
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param status : Status : type string
        :param date : From Date : type string
        """
        payload = {}
        
        if code is not None:
            payload["code"] = code
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if status is not None:
            payload["status"] = status
        if date is not None:
            payload["date"] = date

        # Parameter validation
        schema = InventoryValidator.getJobCodeMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/{code}/metrics", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"code","in":"path","description":"Code","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"status","in":"query","description":"Status","required":false,"schema":{"type":"string"}},{"name":"date","in":"query","description":"From Date","required":false,"schema":{"type":"string","format":"date-time"}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"status","in":"query","description":"Status","required":false,"schema":{"type":"string"}},{"name":"date","in":"query","description":"From Date","required":false,"schema":{"type":"string","format":"date-time"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"code","in":"path","description":"Code","required":true,"schema":{"type":"string"}}]}""", code=code, page_no=page_no, page_size=page_size, status=status, date=date)
        query_string = await create_query_string(code=code, page_no=page_no, page_size=page_size, status=status, date=date)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/{code}/metrics", code=code, page_no=page_no, page_size=page_size, status=status, date=date), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeJobMetricsDto
            schema = ResponseEnvelopeJobMetricsDto()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobCodeMetrics")
                print(e)

        return response
    
    async def getJobCodesByCompanyAndIntegration(self, integration_id=None, page_no=None, page_size=None, request_headers:Dict={}):
        """REST Endpoint that returns all job codes by company And integration
        :param integration_id : Integration Id : type string
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        """
        payload = {}
        
        if integration_id is not None:
            payload["integration_id"] = integration_id
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = InventoryValidator.getJobCodesByCompanyAndIntegration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/integration/{integration_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"Integration Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"Integration Id","required":true,"schema":{"type":"string"}}]}""", integration_id=integration_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(integration_id=integration_id, page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/integration/{integration_id}", integration_id=integration_id, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeListJobConfigListDTO
            schema = ResponseEnvelopeListJobConfigListDTO()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobCodesByCompanyAndIntegration")
                print(e)

        return response
    