

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
        
        if namespace:
            payload["namespace"] = namespace
        

        # Parameter validation
        schema = FileStorageValidator.appStartUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StartRequest
        schema = StartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start/", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", namespace=namespace, )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start/", namespace=namespace, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import StartResponse
        schema = StartResponse()
        try:
            schema.dump(schema.load(response))
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
        
        if namespace:
            payload["namespace"] = namespace
        

        # Parameter validation
        schema = FileStorageValidator.appCompleteUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StartResponse
        schema = StartResponse()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete/", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", namespace=namespace, )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete/", namespace=namespace, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import CompleteResponse
        schema = CompleteResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for appCompleteUpload")
            print(e)

        

        return response
    
    async def appCopyFiles(self, sync=None, body=""):
        """Copy Files
        :param sync : sync : type boolean
        """
        payload = {}
        
        if sync:
            payload["sync"] = sync
        

        # Parameter validation
        schema = FileStorageValidator.appCopyFiles()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRequest
        schema = BulkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/uploads/copy/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"query":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application_id","required":true,"schema":{"type":"integer"}}]}""", sync=sync, )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/uploads/copy/", sync=sync, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import BulkUploadResponse
        schema = BulkUploadResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for appCopyFiles")
            print(e)

        

        return response
    
    async def appbrowse(self, namespace=None, page_no=None):
        """Browse Files
        :param namespace : bucket name : type string
        :param page_no : page no : type integer
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = FileStorageValidator.appbrowse()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application_id","required":true,"schema":{"type":"integer"}}]}""", namespace=namespace, page_no=page_no)
        query_string = await create_query_string(namespace=namespace, page_no=page_no)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse/", namespace=namespace, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import BrowseResponse
        schema = BrowseResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for appbrowse")
            print(e)

        

        return response
    

