"""FileStorage Partner Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PartnerConfig import PartnerConfig

from .validator import FileStorageValidator

class FileStorage:
    def __init__(self, config: PartnerConfig):
        self._conf = config

    
    async def getAllNamespaceDetails(self, request_headers:Dict={}):
        """Retrieve information about all available namespaces
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.getAllNamespaceDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/namespaces", """{"required":[{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}]}""", serverType="partner", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/namespaces", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AllNamespaceDetails
            schema = AllNamespaceDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllNamespaceDetails")
                print(e)

        return response
    
    async def getNamespaceDetail(self, namespace=None, request_headers:Dict={}):
        """Retrieve information about a specific namespace
        :param namespace : Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace

        # Parameter validation
        schema = FileStorageValidator.getNamespaceDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/namespaces/{namespace}", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}]}""", serverType="partner", namespace=namespace, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/namespaces/{namespace}", namespace=namespace), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import NamespaceDetails
            schema = NamespaceDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNamespaceDetail")
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
        from .models import FileUpload
        schema = FileUpload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v2.0/organization/{self._conf.organizationId}/namespaces/{namespace}/upload/complete", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}]}""", serverType="partner", namespace=namespace, )
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v2.0/organization/{self._conf.organizationId}/namespaces/{namespace}/upload/start", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}]}""", serverType="partner", namespace=namespace, )
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
    
    async def browse(self, namespace=None, application_id=None, company_id=None, page=None, limit=None, request_headers:Dict={}):
        """Browse Files
        :param namespace : Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
        :param application_id : Unique identifier for the application. : type string
        :param company_id : Unique numeric identifier for the company. : type integer
        :param page : page no : type integer
        :param limit : Limit : type integer
        """
        payload = {}
        
        if namespace is not None:
            payload["namespace"] = namespace
        if application_id is not None:
            payload["application_id"] = application_id
        if company_id is not None:
            payload["company_id"] = company_id
        if page is not None:
            payload["page"] = page
        if limit is not None:
            payload["limit"] = limit

        # Parameter validation
        schema = FileStorageValidator.browse()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}]}""", serverType="partner", namespace=namespace, application_id=application_id, company_id=company_id, page=page, limit=limit)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/namespaces/{namespace}/browse", namespace=namespace, application_id=application_id, company_id=company_id, page=page, limit=limit), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/namespaces/{namespace}/browse", """{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}],"optional":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page","in":"query","description":"page no","required":false,"schema":{"type":"integer"}},{"name":"limit","in":"query","description":"Limit","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(products, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}},{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}]}""", serverType="partner", namespace=namespace, page=page, limit=limit)
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
    
    async def organizationLevelFetchProxy(self, application_id=None, company_id=None, url=None, request_headers:Dict={}):
        """Proxy
        :param application_id : Unique identifier for the application. : type string
        :param company_id : Unique numeric identifier for the company. : type integer
        :param url : url : type string
        """
        payload = {}
        
        if application_id is not None:
            payload["application_id"] = application_id
        if company_id is not None:
            payload["company_id"] = company_id
        if url is not None:
            payload["url"] = url

        # Parameter validation
        schema = FileStorageValidator.organizationLevelFetchProxy()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/proxy/fetch", """{"required":[{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}},{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}]}""", serverType="partner", application_id=application_id, company_id=company_id, url=url)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/proxy/fetch", application_id=application_id, company_id=company_id, url=url), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FetchProxyDetails
            schema = FetchProxyDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for organizationLevelFetchProxy")
                print(e)

        return response
    
    async def saveOrganizationLevelProxy(self, application_id=None, company_id=None, body="", request_headers:Dict={}):
        """Proxy
        :param application_id : Unique identifier for the application. : type string
        :param company_id : Unique numeric identifier for the company. : type integer
        """
        payload = {}
        
        if application_id is not None:
            payload["application_id"] = application_id
        if company_id is not None:
            payload["company_id"] = company_id

        # Parameter validation
        schema = FileStorageValidator.saveOrganizationLevelProxy()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProxyFile
        schema = ProxyFile()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/proxy/fetch", """{"required":[{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}},{"name":"application_id","in":"path","required":true,"description":"Unique identifier for the application.","schema":{"type":"string","description":"Unique identifier for the application."}},{"name":"company_id","in":"path","required":true,"description":"Unique numeric identifier for the company.","schema":{"type":"integer","description":"Unique numeric identifier for the company."}}]}""", serverType="partner", application_id=application_id, company_id=company_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/proxy/fetch", application_id=application_id, company_id=company_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SaveProxy
            schema = SaveProxy()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for saveOrganizationLevelProxy")
                print(e)

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/proxy/fetch", """{"required":[{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}},{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}]}""", serverType="partner", url=url)
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/assets/v1.0/organization/{self._conf.organizationId}/proxy/fetch", """{"required":[{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","description":"Unique identifier for the organization, used to specify the organization scope in API requests.","in":"path","required":true,"schema":{"type":"string","description":"Unique identifier for the organization, used to specify the organization scope in API requests."}}]}""", serverType="partner", )
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
    