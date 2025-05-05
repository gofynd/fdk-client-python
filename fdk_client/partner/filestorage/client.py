"""FileStorage Partner Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PartnerConfig import PartnerConfig

from .validator import FileStorageValidator

class FileStorage:
    def __init__(self, config: PartnerConfig):
        self._conf = config

    
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
        from .models import FileUpload
        schema = FileUpload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v2.0/organization/{self._conf.organizationId}/namespaces/{namespace}/upload/complete", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}}]}""", serverType="partner", namespace=namespace, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/assets/v2.0/organization/{self._conf.organizationId}/namespaces/{namespace}/upload/complete", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FileUploadComplete
            schema = FileUploadComplete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for completeUpload")
                print(e)

        return response
    
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
        from .models import FileUploadStart
        schema = FileUploadStart()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v2.0/organization/{self._conf.organizationId}/namespaces/{namespace}/upload/start", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}}]}""", serverType="partner", namespace=namespace, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/assets/v2.0/organization/{self._conf.organizationId}/namespaces/{namespace}/upload/start", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FileUpload
            schema = FileUpload()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for startUpload")
                print(e)

        return response
    
    async def browseFiles(self, namespace=None, page=None, limit=None, request_headers:Dict={}):
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
        schema = FileStorageValidator.browseFiles()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}}]}""", serverType="partner", namespace=namespace, page=page, limit=limit)
        query_string = await create_query_string(page=page, limit=limit)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/namespaces/{namespace}/browse", namespace=namespace, page=page, limit=limit), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def fetchProxy(self, url=None, request_headers:Dict={}):
        """Proxy
        :param url : url : type string
        """
        payload = {}
        
        if url is not None:
            payload["url"] = url

        # Parameter validation
        schema = FileStorageValidator.fetchProxy()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/proxy/fetch", """{"required":[{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}},{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}}]}""", serverType="partner", url=url)
        query_string = await create_query_string(url=url)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/proxy/fetch", url=url), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FetchProxyDetails
            schema = FetchProxyDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchProxy")
                print(e)

        return response
    
    async def saveProxyDetails(self, body="", request_headers:Dict={}):
        """Proxy
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.saveProxyDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProxyFile
        schema = ProxyFile()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/proxy/fetch", """{"required":[{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}}]}""", serverType="partner", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/proxy/fetch", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SaveProxy
            schema = SaveProxy()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for saveProxyDetails")
                print(e)

        return response
    
    async def signUrls(self, body="", request_headers:Dict={}):
        """Generates secure, signed URLs that is valid for certain expiry time for accessing stored files.
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.signUrls()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SignUrl
        schema = SignUrl()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/sign-urls", """{"required":[{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","required":true,"schema":{"type":"string","description":"This is organization id"}}]}""", serverType="partner", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/sign-urls", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SignUrlResult
            schema = SignUrlResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for signUrls")
                print(e)

        return response
    