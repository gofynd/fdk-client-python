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
        """Inititates the process of uploading a file to storage location, and returns a storage link in response.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v2.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/start", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}]}""", serverType="platform", namespace=namespace, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v2.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/start", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FileUpload
            schema = FileUpload()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for startUpload")
                print(e)

        return response
    
    async def completeUpload(self, namespace=None, body="", request_headers:Dict={}):
        """Starts the process of uploading a file to storage location, and returns a storage link in response.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v2.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/complete", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}]}""", serverType="platform", namespace=namespace, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v2.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/complete", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FileUploadComplete
            schema = FileUploadComplete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for completeUpload")
                print(e)

        return response
    
    async def getSignUrls(self, body="", request_headers:Dict={}):
        """Retrieve signed URLs for file access.
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.getSignUrls()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SignUrl
        schema = SignUrl()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/sign-urls", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/sign-urls", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SignUrlResult
            schema = SignUrlResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSignUrls")
                print(e)

        return response
    
    async def copyFiles(self, sync=None, body="", request_headers:Dict={}):
        """Duplicate files to another location.
        :param sync : Determines whether the copy files operation should run in synchronous mode. : type boolean
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/uploads/copy", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}],"optional":[{"name":"sync","in":"query","required":false,"description":"Determines whether the copy files operation should run in synchronous mode.","schema":{"type":"boolean"}}],"query":[{"name":"sync","in":"query","required":false,"description":"Determines whether the copy files operation should run in synchronous mode.","schema":{"type":"boolean"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}]}""", serverType="platform", sync=sync, )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/uploads/copy", sync=sync), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def browse(self, namespace=None, page=None, limit=None, request_headers:Dict={}):
        """View and navigate through available files.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}]}""", serverType="platform", namespace=namespace, page=page, limit=limit)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/browse", namespace=namespace, page=page, limit=limit), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def proxy(self, url=None, request_headers:Dict={}):
        """Access files through a proxy.
        :param url : url : type string
        """
        payload = {}
        
        if url is not None:
            payload["url"] = url

        # Parameter validation
        schema = FileStorageValidator.proxy()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/proxy", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}]}""", serverType="platform", url=url)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/proxy", url=url), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProxyFileAccess
            schema = ProxyFileAccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for proxy")
                print(e)

        return response
    