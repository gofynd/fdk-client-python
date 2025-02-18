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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", namespace=namespace, )
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", namespace=namespace, )
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", namespace=namespace, page=page, limit=limit, search=search)
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}},{"name":"search","in":"query","description":"Search","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", namespace=namespace, page=page, limit=limit, search=search)
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
    