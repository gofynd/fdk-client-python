"""FileStorage Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import FileStorageValidator

class FileStorage:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def startUpload(self, namespace=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/start", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}}]}""", namespace=namespace, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/start", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import StartResponse
            schema = StartResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for startUpload")
                print(e)

        return response
    
    async def completeUpload(self, namespace=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/complete", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}}]}""", namespace=namespace, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/complete", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CompleteResponse
            schema = CompleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for completeUpload")
                print(e)

        return response
    
    async def getSignUrls(self, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/sign-urls", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/sign-urls", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import SignUrlResponse
            schema = SignUrlResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSignUrls")
                print(e)

        return response
    
    async def copyFiles(self, sync=None, body="", request_headers:Dict={}):
        """Copy Files
        :param sync :  : type boolean
        """
        payload = {}
        
        if sync is not None:
            payload["sync"] = sync

        # Parameter validation
        schema = FileStorageValidator.copyFiles()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CopyFiles
        schema = CopyFiles()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/uploads/copy", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}}],"optional":[{"name":"sync","in":"query","required":false,"schema":{"type":"boolean","description":"Copy files operation should run in sync mode or not"},"examples":{"syncMode":{"value":true}}}],"query":[{"name":"sync","in":"query","required":false,"schema":{"type":"boolean","description":"Copy files operation should run in sync mode or not"},"examples":{"syncMode":{"value":true}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}}]}""", sync=sync, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/uploads/copy", sync=sync), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkUploadSyncMode
            schema = BulkUploadSyncMode()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for copyFiles")
                print(e)

        return response
    
    async def browse(self, namespace=None, page=None, limit=None, request_headers:Dict={}):
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
        schema = FileStorageValidator.browse()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":16}}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":16}}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"},"failure":{"value":"test123"}}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}}]}""", namespace=namespace, page=page, limit=limit)
        query_string = await create_query_string(namespace=namespace, page=page, limit=limit)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/browse", namespace=namespace, page=page, limit=limit), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import BrowseResponse
            schema = BrowseResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for browse")
                print(e)

        return response
    
    async def proxy(self, url=None, request_headers:Dict={}):
        """Proxy
        :param url : url : type string
        """
        payload = {}
        
        if url is not None:
            payload["url"] = url

        # Parameter validation
        schema = FileStorageValidator.proxy()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/proxy", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}},{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"https://hdn-1.fynd.com/platform/pictures/free-logo/original/7qdHNTFe--platform-logo.png"},"failure":{"value":"platform/pictures/free-logo/original/7qdHNTFe--platform-logo.png"}}}],"optional":[],"query":[{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"https://hdn-1.fynd.com/platform/pictures/free-logo/original/7qdHNTFe--platform-logo.png"},"failure":{"value":"platform/pictures/free-logo/original/7qdHNTFe--platform-logo.png"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":2}}}]}""", url=url)
        query_string = await create_query_string(url=url)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/proxy", url=url), query_string, headers, "", exclude_headers=exclude_headers), data="")

        return response
    