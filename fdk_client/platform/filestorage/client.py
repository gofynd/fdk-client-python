

"""FileStorage Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import FileStorageValidator

class FileStorage:
    def __init__(self, config):
        self._conf = config

    
    async def startUpload(self, namespace=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `startUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `startUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `completeUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

        :param namespace : Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace
        

        # Parameter validation
        schema = FileStorageValidator.startUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StartRequest
        schema = StartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/start/", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", namespace=namespace, )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/start/", namespace=namespace, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import StartResponse
            schema = StartResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for startUpload")
                print(e)

        

        return response
    
    async def completeUpload(self, namespace=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `startUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `startUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `completeUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

        :param namespace : Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace
        

        # Parameter validation
        schema = FileStorageValidator.completeUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StartResponse
        schema = StartResponse()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/complete/", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", namespace=namespace, )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/complete/", namespace=namespace, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CompleteResponse
            schema = CompleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for completeUpload")
                print(e)

        

        return response
    
    async def getSignUrls(self, body=""):
        """Describe here
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.getSignUrls()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SignUrlRequest
        schema = SignUrlRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/sign-urls/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/sign-urls/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SignUrlResponse
            schema = SignUrlResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSignUrls")
                print(e)

        

        return response
    
    async def copyFiles(self, sync=None, body=""):
        """Copy Files
        :param sync : sync : type boolean
        """
        payload = {}
        
        if sync is not None:
            payload["sync"] = sync
        

        # Parameter validation
        schema = FileStorageValidator.copyFiles()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRequest
        schema = BulkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/uploads/copy/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"query":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", sync=sync, )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/uploads/copy/", sync=sync, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkUploadResponse
            schema = BulkUploadResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for copyFiles")
                print(e)

        

        return response
    
    async def browse(self, namespace=None, page_no=None):
        """Browse Files
        :param namespace : bucket name : type string
        :param page_no : page no : type integer
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace
        
        if page_no is not None:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = FileStorageValidator.browse()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/browse/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", namespace=namespace, page_no=page_no)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/browse/", namespace=namespace, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import BrowseResponse
            schema = BrowseResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for browse")
                print(e)

        

        return response
    
    async def proxy(self, url=None):
        """Proxy
        :param url : url : type string
        """
        payload = {}
        
        if url is not None:
            payload["url"] = url
        

        # Parameter validation
        schema = FileStorageValidator.proxy()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/proxy/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", url=url)
        query_string = await create_query_string(url=url)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/proxy/", url=url), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        return response
    

