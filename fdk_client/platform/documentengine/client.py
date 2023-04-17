

""" DocumentEngine Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import DocumentEngineValidator

class DocumentEngine:
    def __init__(self, config):
        self._conf = config
    
    async def generateBulkPackageLabel(self, body=""):
        """Use this API to generate label for Packages
        """
        payload = {}
        

        # Parameter validation
        schema = DocumentEngineValidator.generateBulkPackageLabel()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GenerateBulkPackageLabel
        schema = GenerateBulkPackageLabel()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/document/v1.0/company/{self._conf.companyId}/generate-bulk-package-label", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/document/v1.0/company/{self._conf.companyId}/generate-bulk-package-label", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        
        
        from .models import SuccessResponseGenerateBulk
        schema = SuccessResponseGenerateBulk()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for generateBulkPackageLabel")
            print(e)
            
        

        return response
    
    async def generateBulkBoxLabel(self, body=""):
        """Use this API to generate label for Boxes
        """
        payload = {}
        

        # Parameter validation
        schema = DocumentEngineValidator.generateBulkBoxLabel()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GenerateBulkBoxLabel
        schema = GenerateBulkBoxLabel()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/document/v1.0/company/{self._conf.companyId}/generate-bulk-box-label", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/document/v1.0/company/{self._conf.companyId}/generate-bulk-box-label", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        
        
        from .models import SuccessResponseGenerateBulk
        schema = SuccessResponseGenerateBulk()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for generateBulkBoxLabel")
            print(e)
            
        

        return response
    
    async def generateBulkShipmentLabel(self, body=""):
        """Use this API to generate label for Shipments
        """
        payload = {}
        

        # Parameter validation
        schema = DocumentEngineValidator.generateBulkShipmentLabel()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GenerateBulkShipmentLabel
        schema = GenerateBulkShipmentLabel()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/document/v1.0/company/{self._conf.companyId}/generate-bulk-shipment-label", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/document/v1.0/company/{self._conf.companyId}/generate-bulk-shipment-label", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        
        
        from .models import SuccessResponseGenerateBulk
        schema = SuccessResponseGenerateBulk()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for generateBulkShipmentLabel")
            print(e)
            
        

        return response
    
    async def generateNoc(self, body=""):
        """Use this API to generate NOC for Seller
        """
        payload = {}
        

        # Parameter validation
        schema = DocumentEngineValidator.generateNoc()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GenerateNoc
        schema = GenerateNoc()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/document/v1.0/company/{self._conf.companyId}/generate-noc", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/document/v1.0/company/{self._conf.companyId}/generate-noc", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        
        
        from .models import SuccessResponseGenerateBulk
        schema = SuccessResponseGenerateBulk()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for generateNoc")
            print(e)
            
        

        return response
    
    async def getLabelStatus(self, uid=None):
        """Use this API to fetch status of PDF generation of Labels
        :param uid : UID given at time of generate request : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = DocumentEngineValidator.getLabelStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/document/v1.0/company/{self._conf.companyId}/get-label-list", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}},{"in":"query","name":"uid","required":true,"description":"UID given at time of generate request","schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"uid","required":true,"description":"UID given at time of generate request","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/document/v1.0/company/{self._conf.companyId}/get-label-list", uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")

        
        
        from .models import StatusSuccessResponse
        schema = StatusSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getLabelStatus")
            print(e)
            
        

        return response
    
    async def getNocStatus(self, uid=None):
        """Use this API to fetch status of PDF generation of NOC
        :param uid : UID given at time of generate request : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = DocumentEngineValidator.getNocStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/document/v1.0/company/{self._conf.companyId}/get-noc-status", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}},{"in":"query","name":"uid","required":true,"description":"UID given at time of generate request","schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"uid","required":true,"description":"UID given at time of generate request","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/document/v1.0/company/{self._conf.companyId}/get-noc-status", uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")

        
        
        from .models import StatusSuccessResponse
        schema = StatusSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getNocStatus")
            print(e)
            
        

        return response
    
    async def getPresignedURL(self, body=""):
        """Use this API to generate Presigned URLs for downloading PDFs
        """
        payload = {}
        

        # Parameter validation
        schema = DocumentEngineValidator.getPresignedURL()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InvoiceLabelPresignedRequestBody
        schema = InvoiceLabelPresignedRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/document/v1.0/company/{self._conf.companyId}/get-single-presigned-url", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/document/v1.0/company/{self._conf.companyId}/get-single-presigned-url", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        
        
        from .models import SignedSuccessResponse
        schema = SignedSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getPresignedURL")
            print(e)
            
        

        return response
    
    async def getLabelPresignedURL(self, uid=None):
        """Use this API to generate Presigned URLs for downloading labels
        :param uid : UID given at time of generate request : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = DocumentEngineValidator.getLabelPresignedURL()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/document/v1.0/company/{self._conf.companyId}/get-label-presigned-url", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}},{"in":"query","name":"uid","required":true,"description":"UID given at time of generate request","schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"uid","required":true,"description":"UID given at time of generate request","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/document/v1.0/company/{self._conf.companyId}/get-label-presigned-url", uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")

        
        
        from .models import SignedSuccessResponse
        schema = SignedSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getLabelPresignedURL")
            print(e)
            
        

        return response
    
    async def getNocPresignedURL(self, uid=None):
        """Use this API to generate Presigned URL for downloading NOC Pdf
        :param uid : UID given at time of generate request : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = DocumentEngineValidator.getNocPresignedURL()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/document/v1.0/company/{self._conf.companyId}/get-noc-presigned-url", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}},{"in":"query","name":"uid","required":true,"description":"UID given at time of generate request","schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"uid","required":true,"description":"UID given at time of generate request","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company ID","schema":{"type":"integer"}}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/document/v1.0/company/{self._conf.companyId}/get-noc-presigned-url", uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")

        
        
        from .models import SignedSuccessResponse
        schema = SignedSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getNocPresignedURL")
            print(e)
            
        

        return response
    

