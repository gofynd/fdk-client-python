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
        from .models import StartRequest
        schema = StartRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", namespace=namespace, )
        query_string = await create_query_string(namespace=namespace, )

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        from .models import StartResponse
        schema = StartResponse()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", namespace=namespace, )
        query_string = await create_query_string(namespace=namespace, )

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/uploads/copy", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"},"examples":{"nonSyncMode":{"value":false},"failure":{"value":true}}}],"query":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"},"examples":{"nonSyncMode":{"value":false},"failure":{"value":true}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", sync=sync, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/uploads/copy", sync=sync), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"},"examples":{"success":{"value":"test"}}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"},"examples":{"success":{"value":"test"}}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", namespace=namespace, page=page, limit=limit, search=search)
        query_string = await create_query_string(namespace=namespace, page=page, limit=limit, search=search)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", namespace=namespace, page=page, limit=limit, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="")

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"},"examples":{"success":{"value":"test"}}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"},"examples":{"success":{"value":"test"}}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", namespace=namespace, page=page, limit=limit, search=search)
        query_string = await create_query_string(namespace=namespace, page=page, limit=limit, search=search)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", namespace=namespace, page=page, limit=limit, search=search), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        return response
    
    async def getPdfTypes(self, country_code=None, request_headers:Dict={}):
        """Retrieve a list of available PDF types.
        :param country_code :  : type string
        """
        payload = {}
        
        if country_code is not None:
            payload["country_code"] = country_code

        # Parameter validation
        schema = FileStorageValidator.getPdfTypes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/types", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"},"examples":{"success":{"value":"IN"},"failure":{"value":"NA"}}}],"query":[{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"},"examples":{"success":{"value":"IN"},"failure":{"value":"NA"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", country_code=country_code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/types", country_code=country_code), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Retrieve default data for PDF generation.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/mapper", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"successEmptyValue":{"value":-1}}}],"optional":[{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"},"examples":{"success":{"value":"IN"},"failure":{"value":"NA"}}}],"query":[{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"successEmptyValue":{"value":-1}}},{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"},"examples":{"success":{"value":"IN"},"failure":{"value":"NA"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", pdf_type_id=pdf_type_id, country_code=country_code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/mapper", pdf_type_id=pdf_type_id, country_code=country_code), query_string, headers, "", exclude_headers=exclude_headers), data="")

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config/{id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"This is mongo id"},"examples":{"success":{"value":"64dfd8fc8f3b8b5ae5beb72c"},"failure":{"value":"64dfd8fc8f3b8b5a"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"This is mongo id"},"examples":{"success":{"value":"64dfd8fc8f3b8b5ae5beb72c"},"failure":{"value":"64dfd8fc8f3b8b5a"}}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Get default html template for invoice or label
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"successEmptyValue":{"value":-1}}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"},"examples":{"success":{"value":"A4"},"failure":{"value":"A3"}}}],"optional":[{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"},"examples":{"success":{"value":"IN"},"failure":{"value":"NA"}}}],"query":[{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"successEmptyValue":{"value":-1}}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"},"examples":{"success":{"value":"A4"},"failure":{"value":"A3"}}},{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"},"examples":{"success":{"value":"IN"},"failure":{"value":"NA"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", pdf_type_id=pdf_type_id, format=format, country_code=country_code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", pdf_type_id=pdf_type_id, format=format, country_code=country_code), query_string, headers, "", exclude_headers=exclude_headers), data="")

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/default-template", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"successEmptyValue":{"value":-1}}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"},"examples":{"success":{"value":"A4"},"failure":{"value":"A3"}}}],"optional":[{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"},"examples":{"success":{"value":"IN"},"failure":{"value":"NA"}}}],"query":[{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"successEmptyValue":{"value":-1}}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"},"examples":{"success":{"value":"A4"},"failure":{"value":"A3"}}},{"name":"country_code","in":"query","schema":{"type":"string","description":"This is country_code for which data needs to be displayed on UI"},"examples":{"success":{"value":"IN"},"failure":{"value":"NA"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", pdf_type_id=pdf_type_id, format=format, country_code=country_code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/default-template", pdf_type_id=pdf_type_id, format=format, country_code=country_code), query_string, headers, "", exclude_headers=exclude_headers), data="")

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/payment-receipt", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/payment-receipt", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        return response
    