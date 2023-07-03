

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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GenerateReportJson
            schema = GenerateReportJson()
            try:
                schema.load(response["json"])
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DownloadReportList
            schema = DownloadReportList()
            try:
                schema.load(response["json"])
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetEngineResponse
            schema = GetEngineResponse()
            try:
                schema.load(response["json"])
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetReasonResponse
            schema = GetReasonResponse()
            try:
                schema.load(response["json"])
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetEngineResponse
            schema = GetEngineResponse()
            try:
                schema.load(response["json"])
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAffiliateResponse
            schema = GetAffiliateResponse()
            try:
                schema.load(response["json"])
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DownloadCreditDebitNoteResponse
            schema = DownloadCreditDebitNoteResponse()
            try:
                schema.load(response["json"])
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentProcessResponse
            schema = PaymentProcessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for paymentProcess")
                print(e)

        

        return response
    
    async def creditlineDataplatform(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.creditlineDataplatform()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreditlineDataPlatformRequest
        schema = CreditlineDataPlatformRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/credit-line-data", """{"required":[{"in":"path","name":"company_id","description":"Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/credit-line-data", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CreditlineDataPlatformResponse
            schema = CreditlineDataPlatformResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for creditlineDataplatform")
                print(e)

        

        return response
    
    async def isCreditlinePlatform(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.isCreditlinePlatform()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import IsCreditlinePlatformRequest
        schema = IsCreditlinePlatformRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/creditline-opted", """{"required":[{"in":"path","name":"company_id","description":"Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/creditline-opted", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import IsCreditlinePlatformResponse
            schema = IsCreditlinePlatformResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for isCreditlinePlatform")
                print(e)

        

        return response
    
    async def invoiceType(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.invoiceType()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InvoiceTypeRequest
        schema = InvoiceTypeRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/invoice-type", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/invoice-type", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import InvoiceTypeResponse
            schema = InvoiceTypeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for invoiceType")
                print(e)

        

        return response
    
    async def invoiceListing(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.invoiceListing()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InvoiceListingRequest
        schema = InvoiceListingRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/invoice/listing", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/invoice/listing", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import InvoiceListingResponse
            schema = InvoiceListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for invoiceListing")
                print(e)

        

        return response
    
    async def invoicePDF(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.invoicePDF()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InvoicePdfRequest
        schema = InvoicePdfRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/invoice/pdf-view", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/invoice/pdf-view", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import InvoicePdfResponse
            schema = InvoicePdfResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for invoicePDF")
                print(e)

        

        return response
    
    async def asCnRefund(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.asCnRefund()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AsCnRefundRequest
        schema = AsCnRefundRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/cn-as-refund-method", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/cn-as-refund-method", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AsCnRefundResponse
            schema = AsCnRefundResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for asCnRefund")
                print(e)

        

        return response
    
    async def createSellerCreditNoteConfig(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.createSellerCreditNoteConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSellerCreditNoteConfigRequest
        schema = CreateSellerCreditNoteConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/create-update-credit-note-config", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/create-update-credit-note-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateSellerCreditNoteConfigResponse
            schema = CreateSellerCreditNoteConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSellerCreditNoteConfig")
                print(e)

        

        return response
    
    async def deleteConfig(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.deleteConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DeleteConfigRequest
        schema = DeleteConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/delete-seller-config", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/delete-seller-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteConfigResponse
            schema = DeleteConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteConfig")
                print(e)

        

        return response
    
    async def channelDisplayName(self, filter_key=None):
        """
        :param filter_key : gives display name for channel. : type string
        """
        payload = {}
        
        if filter_key is not None:
            payload["filter_key"] = filter_key
        

        # Parameter validation
        schema = FinanceValidator.channelDisplayName()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/channel-display-names", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true},{"in":"query","name":"filter_key","description":"gives display name for channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"filter_key","description":"gives display name for channel.","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", filter_key=filter_key)
        query_string = await create_query_string(filter_key=filter_key)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/channel-display-names", filter_key=filter_key), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ChannelDisplayNameResponse
            schema = ChannelDisplayNameResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for channelDisplayName")
                print(e)

        

        return response
    
    async def getPdfUrlView(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.getPdfUrlView()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetPdfUrlViewRequest
        schema = GetPdfUrlViewRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-cn-pdf-link", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-cn-pdf-link", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetPdfUrlViewResponse
            schema = GetPdfUrlViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPdfUrlView")
                print(e)

        

        return response
    
    async def creditNoteDetails(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.creditNoteDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreditNoteDetailsRequest
        schema = CreditNoteDetailsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/credit-note-details", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/credit-note-details", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CreditNoteDetailsResponse
            schema = CreditNoteDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for creditNoteDetails")
                print(e)

        

        return response
    
    async def getCustomerCreditBalance(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.getCustomerCreditBalance()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetCustomerCreditBalanceRequest
        schema = GetCustomerCreditBalanceRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/customer-credit-balance", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/customer-credit-balance", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCustomerCreditBalanceResponse
            schema = GetCustomerCreditBalanceResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomerCreditBalance")
                print(e)

        

        return response
    
    async def getCnConfig(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.getCnConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetCnConfigRequest
        schema = GetCnConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-seller-cn-config", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/get-seller-cn-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCnConfigResponse
            schema = GetCnConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCnConfig")
                print(e)

        

        return response
    
    async def generateReportCustomerCn(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.generateReportCustomerCn()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GenerateReportCustomerCnRequest
        schema = GenerateReportCustomerCnRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/generate-report-customer-cn", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/generate-report-customer-cn", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GenerateReportCustomerCnResponse
            schema = GenerateReportCustomerCnResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for generateReportCustomerCn")
                print(e)

        

        return response
    
    async def downloadReportCustomerCn(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = FinanceValidator.downloadReportCustomerCn()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DownloadReportCustomerCnRequest
        schema = DownloadReportCustomerCnRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/download-report-customer-cn", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/download-report-customer-cn", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DownloadReportCustomerCnResponse
            schema = DownloadReportCustomerCnResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for downloadReportCustomerCn")
                print(e)

        

        return response
    
    async def getReportingFilters(self, filter_key=None, affiliate_id=None):
        """
        :param filter_key : filter type. : type string
        :param affiliate_id : affiliate id. : type string
        """
        payload = {}
        
        if filter_key is not None:
            payload["filter_key"] = filter_key
        
        if affiliate_id is not None:
            payload["affiliate_id"] = affiliate_id
        

        # Parameter validation
        schema = FinanceValidator.getReportingFilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/finance/v1.0/company/{self._conf.companyId}/reporting-filters", """{"required":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true},{"in":"query","name":"filter_key","description":"filter type.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"affiliate_id","description":"affiliate id.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"filter_key","description":"filter type.","schema":{"type":"string"},"required":true},{"in":"query","name":"affiliate_id","description":"affiliate id.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID for which the data will be returned.Company_id is required.","schema":{"type":"string"},"required":true}]}""", filter_key=filter_key, affiliate_id=affiliate_id)
        query_string = await create_query_string(filter_key=filter_key, affiliate_id=affiliate_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/finance/v1.0/company/{self._conf.companyId}/reporting-filters", filter_key=filter_key, affiliate_id=affiliate_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetReportingFiltersResponse
            schema = GetReportingFiltersResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getReportingFilters")
                print(e)

        

        return response
    

