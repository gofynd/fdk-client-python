"""FileStorage Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import FileStorageValidator

class FileStorage:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "startUpload": "/service/application/assets/v2.0/namespaces/{namespace}/upload/start",
            "completeUpload": "/service/application/assets/v2.0/namespaces/{namespace}/upload/complete",
            "signUrls": "/service/application/assets/v1.0/sign-urls"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def startUpload(self, namespace=None, body="", request_headers:Dict={}):
        """Starts the process of uploading a file to storage location, and returns a signed url in response.
        :param namespace : A classification value that categorizes files based on the namespace used to determine their storage location and validate their data before upload. The namespace  also acts as a directory structure within the storage bucket and enforces file-specific rules.
Available namespaces:
  - misc: Public namespace allowing all file types up to 100Mb
  - user-profile-pic: Public namespace allowing images up to 15Mb
  - feedback-media: Public namespace allowing images and videos up to 1Gb
  - users-vto-images: Private namespace allowing images up to 40Mb
  - application-audience: Private namespace allowing images and PDFs up to 50Mb : type string
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

        url_with_params = await create_url_with_params(api_url=self._urls["startUpload"], proccessed_params="""{"required":[{"name":"namespace","in":"path","description":"A classification value that categorizes files based on the namespace used to determine their storage location and validate their data before upload. The namespace  also acts as a directory structure within the storage bucket and enforces file-specific rules.\nAvailable namespaces:\n  - misc: Public namespace allowing all file types up to 100Mb\n  - user-profile-pic: Public namespace allowing images up to 15Mb\n  - feedback-media: Public namespace allowing images and videos up to 1Gb\n  - users-vto-images: Private namespace allowing images up to 40Mb\n  - application-audience: Private namespace allowing images and PDFs up to 50Mb","required":true,"schema":{"type":"string","enum":["misc","user-profile-pic","feedback-media","users-vto-images","application-audience","test","test123"]}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"A classification value that categorizes files based on the namespace used to determine their storage location and validate their data before upload. The namespace  also acts as a directory structure within the storage bucket and enforces file-specific rules.\nAvailable namespaces:\n  - misc: Public namespace allowing all file types up to 100Mb\n  - user-profile-pic: Public namespace allowing images up to 15Mb\n  - feedback-media: Public namespace allowing images and videos up to 1Gb\n  - users-vto-images: Private namespace allowing images up to 40Mb\n  - application-audience: Private namespace allowing images and PDFs up to 50Mb","required":true,"schema":{"type":"string","enum":["misc","user-profile-pic","feedback-media","users-vto-images","application-audience","test","test123"]}}]}""", serverType="application", namespace=namespace)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["startUpload"]).netloc, "post", await create_url_without_domain("/service/application/assets/v2.0/namespaces/{namespace}/upload/start", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

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
        """
Complete the file upload and store the file details such as name, size, content type, and namespace to maintain integrity within the system's database.
        :param namespace : A classification value that categorizes files based on the namespace used to determine their storage location and validate their data before upload. The namespace  also acts as a directory structure within the storage bucket and enforces file-specific rules.
Available namespaces:
  - misc: Public namespace allowing all file types up to 100Mb
  - user-profile-pic: Public namespace allowing images up to 15Mb
  - feedback-media: Public namespace allowing images and videos up to 1Gb
  - users-vto-images: Private namespace allowing images up to 40Mb
  - application-audience: Private namespace allowing images and PDFs up to 50Mb : type string
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

        url_with_params = await create_url_with_params(api_url=self._urls["completeUpload"], proccessed_params="""{"required":[{"name":"namespace","in":"path","description":"A classification value that categorizes files based on the namespace used to determine their storage location and validate their data before upload. The namespace  also acts as a directory structure within the storage bucket and enforces file-specific rules.\nAvailable namespaces:\n  - misc: Public namespace allowing all file types up to 100Mb\n  - user-profile-pic: Public namespace allowing images up to 15Mb\n  - feedback-media: Public namespace allowing images and videos up to 1Gb\n  - users-vto-images: Private namespace allowing images up to 40Mb\n  - application-audience: Private namespace allowing images and PDFs up to 50Mb","required":true,"schema":{"type":"string","enum":["misc","user-profile-pic","feedback-media","users-vto-images","application-audience","test","test123"]}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"A classification value that categorizes files based on the namespace used to determine their storage location and validate their data before upload. The namespace  also acts as a directory structure within the storage bucket and enforces file-specific rules.\nAvailable namespaces:\n  - misc: Public namespace allowing all file types up to 100Mb\n  - user-profile-pic: Public namespace allowing images up to 15Mb\n  - feedback-media: Public namespace allowing images and videos up to 1Gb\n  - users-vto-images: Private namespace allowing images up to 40Mb\n  - application-audience: Private namespace allowing images and PDFs up to 50Mb","required":true,"schema":{"type":"string","enum":["misc","user-profile-pic","feedback-media","users-vto-images","application-audience","test","test123"]}}]}""", serverType="application", namespace=namespace)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["completeUpload"]).netloc, "post", await create_url_without_domain("/service/application/assets/v2.0/namespaces/{namespace}/upload/complete", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FileUploadComplete
            schema = FileUploadComplete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for completeUpload")
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

        url_with_params = await create_url_with_params(api_url=self._urls["signUrls"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["signUrls"]).netloc, "post", await create_url_without_domain("/service/application/assets/v1.0/sign-urls", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SignUrlResult
            schema = SignUrlResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for signUrls")
                print(e)

        return response
    