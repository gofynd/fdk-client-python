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
        """Start uploading a file from an application and returns a storage link in response.
        :param namespace : Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace

        # Parameter validation
        schema = FileStorageValidator.appStartUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import FileUploadStart
        schema = FileUploadStart()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}]}""", serverType="platform", namespace=namespace, )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FileUpload
            schema = FileUpload()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for appStartUpload")
                print(e)

        return response
    
    async def appCompleteUpload(self, namespace=None, body="", request_headers:Dict={}):
        """Finish uploading a file from an application.
        :param namespace : Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace

        # Parameter validation
        schema = FileStorageValidator.appCompleteUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import FileUpload
        schema = FileUpload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}]}""", serverType="platform", namespace=namespace, )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FileUploadComplete
            schema = FileUploadComplete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for appCompleteUpload")
                print(e)

        return response
    
    async def appCopyFiles(self, sync=None, body="", request_headers:Dict={}):
        """Copy files from an application to another location.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/uploads/copy", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}],"optional":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"query":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}]}""", serverType="platform", sync=sync, )
        query_string = await create_query_string(sync=sync, )
        if query_string:
            url_with_params += "?" + query_string

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
        """Browse files within an application.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}]}""", serverType="platform", namespace=namespace, page=page, limit=limit, search=search)
        query_string = await create_query_string(page=page, limit=limit, search=search)
        if query_string:
            url_with_params += "?" + query_string

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
        """Browse Files
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}]}""", serverType="platform", namespace=namespace, page=page, limit=limit, search=search)
        query_string = await create_query_string(page=page, limit=limit, search=search)
        if query_string:
            url_with_params += "?" + query_string

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
    
    async def getPdfTypes(self, country_code=None, store_os=None, request_headers:Dict={}):
        """Get all the supported invoice pdf types such as Invoice, Label, Delivery challan
        :param country_code : Country code used to filter data displayed on the UI. : type string
        :param store_os : Identifies whether the store OS determines the PDF generator flow displayed on the UI. : type boolean
        """
        payload = {}
        
        if country_code is not None:
            payload["country_code"] = country_code
        if store_os is not None:
            payload["store_os"] = store_os

        # Parameter validation
        schema = FileStorageValidator.getPdfTypes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/types", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"store_os","in":"query","required":true,"description":"Identifies whether the store OS determines the PDF generator flow displayed on the UI.","schema":{"type":"boolean","description":"Identifies whether the store OS invoices need to be displayed on the PDF generator flow displayed on the UI."}}],"optional":[{"name":"country_code","in":"query","description":"Country code used to filter data displayed on the UI.","schema":{"type":"string","x-not-enum":true,"description":"Country code used to filter data displayed on the UI."}}],"query":[{"name":"country_code","in":"query","description":"Country code used to filter data displayed on the UI.","schema":{"type":"string","x-not-enum":true,"description":"Country code used to filter data displayed on the UI."}},{"name":"store_os","in":"query","required":true,"description":"Identifies whether the store OS determines the PDF generator flow displayed on the UI.","schema":{"type":"boolean","description":"Identifies whether the store OS invoices need to be displayed on the PDF generator flow displayed on the UI."}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}]}""", serverType="platform", country_code=country_code, store_os=store_os)
        query_string = await create_query_string(country_code=country_code, store_os=store_os)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/types", country_code=country_code, store_os=store_os), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InvoiceTypes
            schema = InvoiceTypes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPdfTypes")
                print(e)

        return response
    
    async def fetchPdfTypeById(self, id=None, request_headers:Dict={}):
        """Get the pdf types of PDF formats for filter
        :param id : Unique identifier for the PDF type. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = FileStorageValidator.fetchPdfTypeById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/types/{id}", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier for the PDF type.","schema":{"type":"string","description":"Unique identifier for the PDF type."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier for the PDF type.","schema":{"type":"string","description":"Unique identifier for the PDF type."}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/types/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PdfTypeByIdDetails
            schema = PdfTypeByIdDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchPdfTypeById")
                print(e)

        return response
    
    async def getDefaultPdfData(self, pdf_type_id=None, country_code=None, request_headers:Dict={}):
        """Retrieve default data for PDF generation.
        :param pdf_type_id : Unique identifier for the invoice type. : type integer
        :param country_code : Country code used to filter data displayed on the UI. : type string
        """
        payload = {}
        
        if pdf_type_id is not None:
            payload["pdf_type_id"] = pdf_type_id
        if country_code is not None:
            payload["country_code"] = country_code

        # Parameter validation
        schema = FileStorageValidator.getDefaultPdfData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/mapper", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"pdf_type_id","in":"query","required":true,"description":"Unique identifier for the invoice type.","schema":{"type":"integer","description":"Unique identifier for the invoice type."}}],"optional":[{"name":"country_code","in":"query","description":"Country code used to filter data displayed on the UI.","schema":{"type":"string","x-not-enum":true,"description":"Country code used to filter data displayed on the UI."}}],"query":[{"name":"pdf_type_id","in":"query","required":true,"description":"Unique identifier for the invoice type.","schema":{"type":"integer","description":"Unique identifier for the invoice type."}},{"name":"country_code","in":"query","description":"Country code used to filter data displayed on the UI.","schema":{"type":"string","x-not-enum":true,"description":"Country code used to filter data displayed on the UI."}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}]}""", serverType="platform", pdf_type_id=pdf_type_id, country_code=country_code)
        query_string = await create_query_string(pdf_type_id=pdf_type_id, country_code=country_code)
        if query_string:
            url_with_params += "?" + query_string

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
            from .models import PdfDataItemsDetails
            schema = PdfDataItemsDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDefaultPdfData")
                print(e)

        return response
    
    async def getPdfPayloadById(self, id=None, request_headers:Dict={}):
        """Retrieve default data for PDF generation.
        :param id : Unique identifier associated with the PDF payload, used for retrieving or processing PDF-related data. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = FileStorageValidator.getPdfPayloadById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/mapper/{id}", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier associated with the PDF payload, used for retrieving or processing PDF-related data.","schema":{"type":"string","description":"Unique identifier associated with the PDF payload, used for retrieving or processing PDF-related data."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier associated with the PDF payload, used for retrieving or processing PDF-related data.","schema":{"type":"string","description":"Unique identifier associated with the PDF payload, used for retrieving or processing PDF-related data."}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/mapper/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MapperDetails
            schema = MapperDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPdfPayloadById")
                print(e)

        return response
    
    async def getConfigHtmlTemplateById(self, id=None, request_headers:Dict={}):
        """Update html template for invoice such as Invoice, Label, Deliver challan
        :param id : Unique identifier for fetching PDF configuration details. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = FileStorageValidator.getConfigHtmlTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config/{id}", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier for fetching PDF configuration details.","schema":{"type":"string","description":"Unique identifier for fetching PDF configuration details."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier for fetching PDF configuration details.","schema":{"type":"string","description":"Unique identifier for fetching PDF configuration details."}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def updateHtmlTemplate(self, id=None, body="", request_headers:Dict={}):
        """Update the HTML Template.
        :param id : Unique identifier used for operations. : type string
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config/{id}", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier used for operations.","schema":{"type":"string","description":"Unique identifier used for operations."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier used for operations.","schema":{"type":"string","description":"Unique identifier used for operations."}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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
    
    async def deletePdfGeneratorConfig(self, id=None, request_headers:Dict={}):
        """Deletes a specific PDF generator configuration based on the provided id.
        :param id : Unique identifier used for operations. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = FileStorageValidator.deletePdfGeneratorConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config/{id}", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier used for operations.","schema":{"type":"string","description":"Unique identifier used for operations."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier used for operations.","schema":{"type":"string","description":"Unique identifier used for operations."}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getHtmlTemplateConfig(self, pdf_type_id=None, format=None, country_code=None, request_headers:Dict={}):
        """Get default html template for invoice or label
        :param pdf_type_id : Unique identifier for the invoice type. : type integer
        :param format : Specifies the invoice document format (e.g., A4, A6, POS, A3). : type string
        :param country_code : Country code used to filter data displayed on the UI. : type string
        """
        payload = {}
        
        if pdf_type_id is not None:
            payload["pdf_type_id"] = pdf_type_id
        if format is not None:
            payload["format"] = format
        if country_code is not None:
            payload["country_code"] = country_code

        # Parameter validation
        schema = FileStorageValidator.getHtmlTemplateConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"pdf_type_id","in":"query","required":true,"description":"Unique identifier for the invoice type.","schema":{"type":"integer","description":"Unique identifier for the invoice type."}},{"name":"format","in":"query","required":true,"description":"Specifies the invoice document format (e.g., A4, A6, POS, A3).","schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"Specifies the invoice document format (e.g., A4, A6, POS, A3)."}}],"optional":[{"name":"country_code","in":"query","description":"Country code used to filter data displayed on the UI.","schema":{"type":"string","x-not-enum":true,"description":"Country code used to filter data displayed on the UI."}}],"query":[{"name":"pdf_type_id","in":"query","required":true,"description":"Unique identifier for the invoice type.","schema":{"type":"integer","description":"Unique identifier for the invoice type."}},{"name":"format","in":"query","required":true,"description":"Specifies the invoice document format (e.g., A4, A6, POS, A3).","schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"Specifies the invoice document format (e.g., A4, A6, POS, A3)."}},{"name":"country_code","in":"query","description":"Country code used to filter data displayed on the UI.","schema":{"type":"string","x-not-enum":true,"description":"Country code used to filter data displayed on the UI."}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}]}""", serverType="platform", pdf_type_id=pdf_type_id, format=format, country_code=country_code)
        query_string = await create_query_string(pdf_type_id=pdf_type_id, format=format, country_code=country_code)
        if query_string:
            url_with_params += "?" + query_string

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
                print("Response Validation failed for getHtmlTemplateConfig")
                print(e)

        return response
    
    async def saveHtmlTemplate(self, body="", request_headers:Dict={}):
        """Store an HTML template.
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.saveHtmlTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PdfConfig
        schema = PdfConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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
        """Retrieve the default PDF template.
        :param pdf_type_id : Unique identifier for the invoice type. : type integer
        :param format : Specifies the invoice document format (e.g., A4, A6, POS, A3). : type string
        :param country_code : Country code used to filter data displayed on the UI. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/default-template", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"pdf_type_id","in":"query","required":true,"description":"Unique identifier for the invoice type.","schema":{"type":"integer","description":"Unique identifier for the invoice type."}},{"name":"format","in":"query","required":true,"description":"Specifies the invoice document format (e.g., A4, A6, POS, A3).","schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"Specifies the invoice document format (e.g., A4, A6, POS, A3)."}}],"optional":[{"name":"country_code","in":"query","description":"Country code used to filter data displayed on the UI.","schema":{"type":"string","x-not-enum":true,"description":"Country code used to filter data displayed on the UI."}}],"query":[{"name":"pdf_type_id","in":"query","required":true,"description":"Unique identifier for the invoice type.","schema":{"type":"integer","description":"Unique identifier for the invoice type."}},{"name":"format","in":"query","required":true,"description":"Specifies the invoice document format (e.g., A4, A6, POS, A3).","schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"Specifies the invoice document format (e.g., A4, A6, POS, A3)."}},{"name":"country_code","in":"query","description":"Country code used to filter data displayed on the UI.","schema":{"type":"string","x-not-enum":true,"description":"Country code used to filter data displayed on the UI."}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}]}""", serverType="platform", pdf_type_id=pdf_type_id, format=format, country_code=country_code)
        query_string = await create_query_string(pdf_type_id=pdf_type_id, format=format, country_code=country_code)
        if query_string:
            url_with_params += "?" + query_string

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/payment-receipt", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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
    
    async def fetchPdfDefaultTemplateById(self, id=None, request_headers:Dict={}):
        """get default html template for invoice such as Invoice, Label, Deliver challan
        :param id : Unique identifier for the default PDF template. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = FileStorageValidator.fetchPdfDefaultTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/default-template/{id}", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier for the default PDF template.","schema":{"type":"string","description":"Unique MongoDB identifier for the default PDF template."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"id","in":"path","required":true,"description":"Unique identifier for the default PDF template.","schema":{"type":"string","description":"Unique MongoDB identifier for the default PDF template."}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/default-template/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PdfDefaultTemplateById
            schema = PdfDefaultTemplateById()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchPdfDefaultTemplateById")
                print(e)

        return response
    