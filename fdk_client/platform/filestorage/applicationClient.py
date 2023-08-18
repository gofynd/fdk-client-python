

"""FileStorage Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import FileStorageValidator

class FileStorage:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId

    
    async def appStartUpload(self, namespace=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `appStartUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `appStartUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `appCompleteUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", namespace=namespace, )
        query_string = await create_query_string(namespace=namespace, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start", namespace=namespace, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import StartResponse
            schema = StartResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for appStartUpload")
                print(e)

        

        return response
    
    async def appCompleteUpload(self, namespace=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `appStartUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `appStartUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `appCompleteUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", namespace=namespace, )
        query_string = await create_query_string(namespace=namespace, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete", namespace=namespace, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CompleteResponse
            schema = CompleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for appCompleteUpload")
                print(e)

        

        return response
    
    async def appCopyFiles(self, sync=None, body=""):
        """Copy Files
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/uploads/copy", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"},"examples":{"syncMode":{"value":true}}}],"query":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"},"examples":{"syncMode":{"value":true}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", sync=sync, )
        query_string = await create_query_string(sync=sync, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/uploads/copy", sync=sync, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkUploadSyncMode
            schema = BulkUploadSyncMode()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for appCopyFiles")
                print(e)

        

        return response
    
    async def appbrowse(self, namespace=None, page=None, limit=None):
        """Browse Files
        :param namespace : Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
        :param page : page no : type integer
        :param limit : Limit : type integer
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace
        
        if page is not None:
            payload["page"] = page
        
        if limit is not None:
            payload["limit"] = limit
        

        # Parameter validation
        schema = FileStorageValidator.appbrowse()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":16}}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":16}}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", namespace=namespace, page=page, limit=limit)
        query_string = await create_query_string(namespace=namespace, page=page, limit=limit)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", namespace=namespace, page=page, limit=limit), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import BrowseResponse
            schema = BrowseResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for appbrowse")
                print(e)

        

        return response
    
    async def getPdfTypes(self, ):
        """Get all the supported invoice pdf types such as Invoice, Label, Deliver challan
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.getPdfTypes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/types", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/types", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        return response
    
    async def getDefaultPdfData(self, pdf_type_id=None):
        """Get Dummy pdf data for invoice or label
        :param pdf_type_id :  : type integer
        """
        payload = {}
        
        if pdf_type_id is not None:
            payload["pdf_type_id"] = pdf_type_id
        

        # Parameter validation
        schema = FileStorageValidator.getDefaultPdfData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/mapper", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"failure":{"value":30}}}],"optional":[],"query":[{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"failure":{"value":30}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", pdf_type_id=pdf_type_id)
        query_string = await create_query_string(pdf_type_id=pdf_type_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/mapper", pdf_type_id=pdf_type_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        return response
    
    async def getDefaultHtmlTemplate(self, pdf_type_id=None, format=None):
        """Get default html template for invoice or label
        :param pdf_type_id :  : type integer
        :param format :  : type string
        """
        payload = {}
        
        if pdf_type_id is not None:
            payload["pdf_type_id"] = pdf_type_id
        
        if format is not None:
            payload["format"] = format
        

        # Parameter validation
        schema = FileStorageValidator.getDefaultHtmlTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"failure":{"value":30}}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"},"examples":{"success":{"value":"A4"},"failure":{"value":"A3"}}}],"optional":[],"query":[{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"failure":{"value":30}}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"},"examples":{"success":{"value":"A4"},"failure":{"value":"A3"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", pdf_type_id=pdf_type_id, format=format)
        query_string = await create_query_string(pdf_type_id=pdf_type_id, format=format)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", pdf_type_id=pdf_type_id, format=format), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        return response
    
    async def saveHtmlTemplate(self, body=""):
        """Update html template for invoice such as Invoice, Label, Deliver challan
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.saveHtmlTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import pdfConfig
        schema = pdfConfig()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        return response
    
    async def previewTemplate(self, body=""):
        """Rendered HTML template with dummy json data
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.previewTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import pdfRender
        schema = pdfRender()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/render", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/render", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        return response
    
    async def getDefaultPdfTemplate(self, pdf_type_id=None, format=None):
        """Get default html template data for invoice or label
        :param pdf_type_id :  : type integer
        :param format :  : type string
        """
        payload = {}
        
        if pdf_type_id is not None:
            payload["pdf_type_id"] = pdf_type_id
        
        if format is not None:
            payload["format"] = format
        

        # Parameter validation
        schema = FileStorageValidator.getDefaultPdfTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/default-template", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"failure":{"value":30}}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"},"examples":{"success":{"value":"A4"},"failure":{"value":"A3"}}}],"optional":[],"query":[{"name":"pdf_type_id","in":"query","required":true,"schema":{"type":"integer","description":"This is invoice unique id"},"examples":{"success":{"value":1},"failure":{"value":30}}},{"name":"format","in":"query","required":true,"schema":{"type":"string","enum":["A4","A6","POS","A3"],"description":"This is invoice document format such as A4, A6, POS"},"examples":{"success":{"value":"A4"},"failure":{"value":"A3"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", pdf_type_id=pdf_type_id, format=format)
        query_string = await create_query_string(pdf_type_id=pdf_type_id, format=format)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pdf/default-template", pdf_type_id=pdf_type_id, format=format), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        return response
    

