

"""Finance Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import FinanceValidator

class Finance:
    def __init__(self, config):
        self._conf = config

    
    async def generateReport(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.generateReport()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GenerateReportRequest
        schema = GenerateReportRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/generate-report", """{"required":[{"in":"path","name":"company_id","description":"Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/generate-report", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import GenerateReportJson
        schema = GenerateReportJson()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for generateReport")
            print(e)

        

        return response
    
    async def downloadReport(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.downloadReport()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DownloadReport
        schema = DownloadReport()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/download-report", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/download-report", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import DownloadReportList
        schema = DownloadReportList()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for downloadReport")
            print(e)

        

        return response
    
    async def getData(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.getData()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetEngineRequest
        schema = GetEngineRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-data", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-data", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import GetEngineResponse
        schema = GetEngineResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getData")
            print(e)

        

        return response
    
    async def getReason(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.getReason()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetReasonRequest
        schema = GetReasonRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-reason", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-reason", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import GetReasonResponse
        schema = GetReasonResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getReason")
            print(e)

        

        return response
    
    async def getReportList(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.getReportList()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetReportListRequest
        schema = GetReportListRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-report-list", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-report-list", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import GetEngineResponse
        schema = GetEngineResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getReportList")
            print(e)

        

        return response
    
    async def getAffiliate(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.getAffiliate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetAffiliate
        schema = GetAffiliate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-affiliate-list", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is reqired.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is reqired.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-affiliate-list", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import GetAffiliateResponse
        schema = GetAffiliateResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getAffiliate")
            print(e)

        

        return response
    
    async def downloadCreditDebitNote(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.downloadCreditDebitNote()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DownloadCreditDebitNoteRequest
        schema = DownloadCreditDebitNoteRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/download-credit-debit-note", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/download-credit-debit-note", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import DownloadCreditDebitNoteResponse
        schema = DownloadCreditDebitNoteResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for downloadCreditDebitNote")
            print(e)

        

        return response
    
    async def paymentProcess(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.paymentProcess()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentProcessRequest
        schema = PaymentProcessRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/payment-process", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/payment-process", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import PaymentProcessResponse
        schema = PaymentProcessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for paymentProcess")
            print(e)

        

        return response
    

