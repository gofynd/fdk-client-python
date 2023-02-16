

"""  Public Client."""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import InventoryValidator

class Inventory:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getJobConfigByIntegrationType": "/service/common/inventory/v1.0/company/job/config",
            "getJobCodesMetrics": "/service/common/inventory/v1.0/company/email/jobCode",
            "saveJobCodesMetrics": "/service/common/inventory/v1.0/company/email/jobCode"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getJobConfigByIntegrationType(self, integration_type=None, disable=None, body=""):
        """REST Endpoint that returns all job Configs by Integration Type
        :param integration_type : Integration Type : type string
        :param disable : JobConfig current state : type boolean
        """
        payload = {}
        
        if integration_type:
            payload["integration_type"] = integration_type
        
        if disable:
            payload["disable"] = disable
        
        # Parameter validation
        schema = InventoryValidator.getJobConfigByIntegrationType()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getJobConfigByIntegrationType"], proccessed_params="""{"required":[{"name":"integration_type","in":"query","description":"Integration Type","required":true,"schema":{"type":"string"}}],"optional":[{"name":"disable","in":"query","description":"JobConfig current state","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"name":"integration_type","in":"query","description":"Integration Type","required":true,"schema":{"type":"string"}},{"name":"disable","in":"query","description":"JobConfig current state","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[]}""", integration_type=integration_type, disable=disable)
        query_string = await create_query_string(integration_type=integration_type, disable=disable)
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getJobConfigByIntegrationType"]).netloc, "get", await create_url_without_domain("/service/common/inventory/v1.0/company/job/config", integration_type=integration_type, disable=disable), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getJobCodesMetrics(self, daily_job=None, job_code=None, body=""):
        """Endpoint to return all JobCodes present in Metrics Collection
        :param daily_job : Daily Job Flag : type boolean
        :param job_code : Email Job Code : type string
        """
        payload = {}
        
        if daily_job:
            payload["daily_job"] = daily_job
        
        if job_code:
            payload["job_code"] = job_code
        
        # Parameter validation
        schema = InventoryValidator.getJobCodesMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getJobCodesMetrics"], proccessed_params="""{"required":[],"optional":[{"name":"daily_job","in":"query","description":"Daily Job Flag","required":false,"schema":{"type":"boolean"}},{"name":"job_code","in":"query","description":"Email Job Code","required":false,"schema":{"type":"string"}}],"query":[{"name":"daily_job","in":"query","description":"Daily Job Flag","required":false,"schema":{"type":"boolean"}},{"name":"job_code","in":"query","description":"Email Job Code","required":false,"schema":{"type":"string"}}],"headers":[],"path":[]}""", daily_job=daily_job, job_code=job_code)
        query_string = await create_query_string(daily_job=daily_job, job_code=job_code)
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getJobCodesMetrics"]).netloc, "get", await create_url_without_domain("/service/common/inventory/v1.0/company/email/jobCode", daily_job=daily_job, job_code=job_code), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def saveJobCodesMetrics(self, body=""):
        """Endpoint to save JobCode Metrics
        """
        payload = {}
        
        # Parameter validation
        schema = InventoryValidator.saveJobCodesMetrics()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EmailJobMetrics import EmailJobMetrics
        schema = EmailJobMetrics()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["saveJobCodesMetrics"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["saveJobCodesMetrics"]).netloc, "post", await create_url_without_domain("/service/common/inventory/v1.0/company/email/jobCode", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

