"""FileStorage Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import FileStorageValidator

class FileStorage:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def appStartUpload(self, namespace=None, body="", request_headers:Dict={}):
        """Inititates the process of uploading a file to storage location, and returns a storage link in response on platofrm at application level. Please refer group description for more details.
        :param namespace : Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace

        # Parameter validation
        schema = FileStorageValidator.appStartUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StartRequest
        schema = StartRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", namespace=namespace, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StartResponse
            schema = StartResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for appStartUpload")
                print(e)

        return response
    
    async def appCompleteUpload(self, namespace=None, body="", request_headers:Dict={}):
        """Complete the file upload and store the file details such as name, size, content type, and namespace to maintain integrity within the system's database on platform at application level
        :param namespace : Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace

        # Parameter validation
        schema = FileStorageValidator.appCompleteUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StartResponse
        schema = StartResponse()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", namespace=namespace, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CompleteResponse
            schema = CompleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for appCompleteUpload")
                print(e)

        return response
    
    async def appCopyFiles(self, sync=None, body="", request_headers:Dict={}):
        """Handle multiple file uploads, updating progress and providing detailed status reports.
        :param sync : sync : type boolean
        """
        payload = {}
        
        if sync is not None:
            payload["sync"] = sync

        # Parameter validation
        schema = FileStorageValidator.appCopyFiles()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CopyFiles
        schema = CopyFiles()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/uploads/copy", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"query":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", sync=sync, )
        query_string = await create_query_string(sync=sync, )

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/uploads/copy", sync=sync), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def appbrowse(self, namespace=None, page=None, limit=None, search=None, request_headers:Dict={}):
        """View and navigate through available files.
        :param namespace : Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
        :param page : page no : type integer
        :param limit : Limit : type integer
        :param search : Search : type string
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace
        if page is not None:
            payload["page"] = page
        if limit is not None:
            payload["limit"] = limit
        if search is not None:
            payload["search"] = search

        # Parameter validation
        schema = FileStorageValidator.appbrowse()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", namespace=namespace, page=page, limit=limit, search=search)
        query_string = await create_query_string(page=page, limit=limit, search=search)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", namespace=namespace, page=page, limit=limit, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def browsefiles(self, namespace=None, page=None, limit=None, search=None, body="", request_headers:Dict={}):
        """View and navigate through available files.
        :param namespace : Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
        :param page : page no : type integer
        :param limit : Limit : type integer
        :param search : Search : type string
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace
        if page is not None:
            payload["page"] = page
        if limit is not None:
            payload["limit"] = limit
        if search is not None:
            payload["search"] = search

        # Parameter validation
        schema = FileStorageValidator.browsefiles()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ExtensionSlug
        schema = ExtensionSlug()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", namespace=namespace, page=page, limit=limit, search=search)
        query_string = await create_query_string(page=page, limit=limit, search=search)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", namespace=namespace, page=page, limit=limit, search=search), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getPdfTypes(self, country_code=None, request_headers:Dict={}):
        """Retrieve a list of available invoice types.
        :param country_code :  : type string
        """
        payload = {}
        
        if country_code is not None:
            payload["country_code"] = country_code

        # Parameter validation
        schema = FileStorageValidator.getPdfTypes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/types", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"}}],"query":[{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", country_code=country_code)
        query_string = await create_query_string(country_code=country_code)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/types", country_code=country_code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InvoiceTypesResponse
            schema = InvoiceTypesResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPdfTypes")
                print(e)

        return response
    
    async def getDefaultPdfData(self, pdf_type_id=None, country_code=None, request_headers:Dict={}):
        """Retrieve default pdf payload data for invoice generation.
        :param pdf_type_id :  : type integer
        :param country_code :  : type string
        """
        payload = {}
        
        if pdf_type_id is not None:
            payload["pdf_type_id"] = pdf_type_id
        if country_code is not None:
            payload["country_code"] = country_code

        # Parameter validation
        schema = FileStorageValidator.getDefaultPdfData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/mapper", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"}}],"optional":[{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"}}],"query":[{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"}},{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", pdf_type_id=pdf_type_id, country_code=country_code)
        query_string = await create_query_string(pdf_type_id=pdf_type_id, country_code=country_code)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/mapper", pdf_type_id=pdf_type_id, country_code=country_code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DummyTemplateDataItems
            schema = DummyTemplateDataItems()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDefaultPdfData")
                print(e)

        return response
    
    async def updateHtmlTemplate(self, id=None, body="", request_headers:Dict={}):
        """Update the HTML Template.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = FileStorageValidator.updateHtmlTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PdfConfig
        schema = PdfConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config/{id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"This is mongo id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"This is mongo id"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PdfConfigSaveSuccess
            schema = PdfConfigSaveSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateHtmlTemplate")
                print(e)

        return response
    
    async def getDefaultHtmlTemplate(self, pdf_type_id=None, format=None, country_code=None, request_headers:Dict={}):
        """
Get the saved html template for provided sales channel

        :param pdf_type_id :  : type integer
        :param format :  : type string
        :param country_code :  : type string
        """
        payload = {}
        
        if pdf_type_id is not None:
            payload["pdf_type_id"] = pdf_type_id
        if format is not None:
            payload["format"] = format
        if country_code is not None:
            payload["country_code"] = country_code

        # Parameter validation
        schema = FileStorageValidator.getDefaultHtmlTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"}}],"optional":[{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"}}],"query":[{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"}},{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", pdf_type_id=pdf_type_id, format=format, country_code=country_code)
        query_string = await create_query_string(pdf_type_id=pdf_type_id, format=format, country_code=country_code)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", pdf_type_id=pdf_type_id, format=format, country_code=country_code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PdfConfigSuccess
            schema = PdfConfigSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDefaultHtmlTemplate")
                print(e)

        return response
    
    async def saveHtmlTemplate(self, body="", request_headers:Dict={}):
        """Save html template for provided sales channel
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.saveHtmlTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PdfConfig
        schema = PdfConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PdfConfigSaveSuccess
            schema = PdfConfigSaveSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for saveHtmlTemplate")
                print(e)

        return response
    
    async def getDefaultPdfTemplate(self, pdf_type_id=None, format=None, country_code=None, request_headers:Dict={}):
        """Retrieve to get the default Invoice template.
        :param pdf_type_id :  : type integer
        :param format :  : type string
        :param country_code :  : type string
        """
        payload = {}
        
        if pdf_type_id is not None:
            payload["pdf_type_id"] = pdf_type_id
        if format is not None:
            payload["format"] = format
        if country_code is not None:
            payload["country_code"] = country_code

        # Parameter validation
        schema = FileStorageValidator.getDefaultPdfTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/default-template", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"}}],"optional":[{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"}}],"query":[{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"}},{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", pdf_type_id=pdf_type_id, format=format, country_code=country_code)
        query_string = await create_query_string(pdf_type_id=pdf_type_id, format=format, country_code=country_code)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/default-template", pdf_type_id=pdf_type_id, format=format, country_code=country_code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PdfDefaultTemplateSuccess
            schema = PdfDefaultTemplateSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDefaultPdfTemplate")
                print(e)

        return response
    
    async def generatePaymentReceipt(self, body="", request_headers:Dict={}):
        """Generate Payment Receipt for Jiomart Digital
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.generatePaymentReceipt()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentReceiptRequestBody
        schema = PaymentReceiptRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/payment-receipt", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/payment-receipt", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    