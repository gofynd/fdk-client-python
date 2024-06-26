"""Inventory Public Client"""

from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PublicConfig import PublicConfig

from .validator import InventoryValidator

class Inventory:
    def __init__(self, config: PublicConfig):
        self._conf = config
        self._relativeUrls = {
            "getJobCodesMetrics": "/service/common/inventory/v1.0/company/email/jobCode",
            "saveJobCodesMetrics": "/service/common/inventory/v1.0/company/email/jobCode",
            "getConfigByApiKey": "/service/common/inventory/v1.0/company/slingshot",
            "getApiKey": "/service/common/inventory/v1.0/company/slingshot/apikey",
            "getJobByCode": "/service/common/inventory/v1.0/company/jobs/code/{code}",
            "getJobConfigByIntegrationType": "/service/common/inventory/v1.0/company/job/config"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getJobCodesMetrics(self, daily_job=None, job_code=None, body="", request_headers:Dict={}):
        """Endpoint to return all JobCodes present in Metrics Collection
        :param daily_job : Daily Job Flag : type boolean
        :param job_code : Email Job Code : type string
        """
        payload = {}
        
        if daily_job is not None:
            payload["daily_job"] = daily_job
        if job_code is not None:
            payload["job_code"] = job_code

        # Parameter validation
        schema = InventoryValidator.getJobCodesMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getJobCodesMetrics"], proccessed_params="""{"required":[],"optional":[{"name":"daily_job","in":"query","description":"Daily Job Flag","required":false,"schema":{"type":"boolean"}},{"name":"job_code","in":"query","description":"Email Job Code","required":false,"schema":{"type":"string"}}],"query":[{"name":"daily_job","in":"query","description":"Daily Job Flag","required":false,"schema":{"type":"boolean"}},{"name":"job_code","in":"query","description":"Email Job Code","required":false,"schema":{"type":"string"}}],"headers":[],"path":[]}""", serverType="public", daily_job=daily_job, job_code=job_code)
        query_string = await create_query_string(daily_job=daily_job, job_code=job_code)

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getJobCodesMetrics"]).netloc, "get", await create_url_without_domain("/service/common/inventory/v1.0/company/email/jobCode", daily_job=daily_job, job_code=job_code), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeObject
            schema = ResponseEnvelopeObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobCodesMetrics")
                print(e)

        return response
    
    async def saveJobCodesMetrics(self, body="", request_headers:Dict={}):
        """Endpoint to save JobCode Metrics
        """
        payload = {}
        

        # Parameter validation
        schema = InventoryValidator.saveJobCodesMetrics()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailJobMetrics
        schema = EmailJobMetrics()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["saveJobCodesMetrics"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
        query_string = await create_query_string()

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["saveJobCodesMetrics"]).netloc, "post", await create_url_without_domain("/service/common/inventory/v1.0/company/email/jobCode", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeEmailJobMetrics
            schema = ResponseEnvelopeEmailJobMetrics()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for saveJobCodesMetrics")
                print(e)

        return response
    
    async def getConfigByApiKey(self, apikey=None, body="", request_headers:Dict={}):
        """REST Endpoint that returns all configuration detail of a company
        :param apikey : Api key : type string
        """
        payload = {}
        
        if apikey is not None:
            payload["apikey"] = apikey

        # Parameter validation
        schema = InventoryValidator.getConfigByApiKey()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getConfigByApiKey"], proccessed_params="""{"required":[{"name":"apikey","in":"query","description":"Api key","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"apikey","in":"query","description":"Api key","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", serverType="public", apikey=apikey)
        query_string = await create_query_string(apikey=apikey)

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getConfigByApiKey"]).netloc, "get", await create_url_without_domain("/service/common/inventory/v1.0/company/slingshot", apikey=apikey), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeSlingshotConfigurationDetail
            schema = ResponseEnvelopeSlingshotConfigurationDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getConfigByApiKey")
                print(e)

        return response
    
    async def getApiKey(self, user_name=None, password=None, body="", request_headers:Dict={}):
        """REST Endpoint that returns apikey by username by password
        :param user_name : Integration id : type string
        :param password : company/store token : type string
        """
        payload = {}
        
        if user_name is not None:
            payload["user_name"] = user_name
        if password is not None:
            payload["password"] = password

        # Parameter validation
        schema = InventoryValidator.getApiKey()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getApiKey"], proccessed_params="""{"required":[{"name":"user_name","in":"query","description":"Integration id","required":true,"schema":{"type":"string"}},{"name":"password","in":"query","description":"company/store token","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"user_name","in":"query","description":"Integration id","required":true,"schema":{"type":"string"}},{"name":"password","in":"query","description":"company/store token","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", serverType="public", user_name=user_name, password=password)
        query_string = await create_query_string(user_name=user_name, password=password)

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getApiKey"]).netloc, "get", await create_url_without_domain("/service/common/inventory/v1.0/company/slingshot/apikey", user_name=user_name, password=password), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeApikeyModel
            schema = ResponseEnvelopeApikeyModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApiKey")
                print(e)

        return response
    
    async def getJobByCode(self, code=None, body="", request_headers:Dict={}):
        """REST Endpoint that returns job config by code
        :param code : Job Code : type string
        """
        payload = {}
        
        if code is not None:
            payload["code"] = code

        # Parameter validation
        schema = InventoryValidator.getJobByCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getJobByCode"], proccessed_params="""{"required":[{"name":"code","in":"path","description":"Job Code","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"code","in":"path","description":"Job Code","required":true,"schema":{"type":"string"}}]}""", serverType="public", code=code)
        query_string = await create_query_string(code=code)

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getJobByCode"]).netloc, "get", await create_url_without_domain("/service/common/inventory/v1.0/company/jobs/code/{code}", code=code), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeJobConfigDTO
            schema = ResponseEnvelopeJobConfigDTO()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobByCode")
                print(e)

        return response
    
    async def getJobConfigByIntegrationType(self, integration_type=None, disable=None, body="", request_headers:Dict={}):
        """REST Endpoint that returns all job Configs by Integration Type
        :param integration_type : Integration Type : type string
        :param disable : JobConfig current state : type boolean
        """
        payload = {}
        
        if integration_type is not None:
            payload["integration_type"] = integration_type
        if disable is not None:
            payload["disable"] = disable

        # Parameter validation
        schema = InventoryValidator.getJobConfigByIntegrationType()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getJobConfigByIntegrationType"], proccessed_params="""{"required":[{"name":"integration_type","in":"query","description":"Integration Type","required":true,"schema":{"type":"string"}}],"optional":[{"name":"disable","in":"query","description":"JobConfig current state","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"name":"integration_type","in":"query","description":"Integration Type","required":true,"schema":{"type":"string"}},{"name":"disable","in":"query","description":"JobConfig current state","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[]}""", serverType="public", integration_type=integration_type, disable=disable)
        query_string = await create_query_string(integration_type=integration_type, disable=disable)

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getJobConfigByIntegrationType"]).netloc, "get", await create_url_without_domain("/service/common/inventory/v1.0/company/job/config", integration_type=integration_type, disable=disable), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseEnvelopeListJobConfigDTO
            schema = ResponseEnvelopeListJobConfigDTO()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobConfigByIntegrationType")
                print(e)

        return response
    