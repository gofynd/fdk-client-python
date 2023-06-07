

"""FileStorage Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import FileStorageValidator

class FileStorage:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "startUpload": "/service/application/assets/v1.0/namespaces/{namespace}/upload/start/",
            "completeUpload": "/service/application/assets/v1.0/namespaces/{namespace}/upload/complete/",
            "signUrls": "/service/application/assets/v1.0/sign-urls/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def startUpload(self, namespace=None, body=""):
        """Use this API to perform the first step of uploading (i.e. **Start**) an arbitrarily sized buffer or blob.

The three major steps are:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `startUpload`.
It returns a storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `startUpload` API with the file (Buffer or Blob) in the request body.

### Complete
After successfully upload, call the `completeUpload` API to finish the upload process.
This operation will return the URL of the uploaded file.

        :param namespace : Segregation of different types of files(prodcuts, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["startUpload"], proccessed_params="""{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(prodcuts, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(prodcuts, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}}]}""", namespace=namespace)
        query_string = await create_query_string(namespace=namespace)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["startUpload"]).netloc, "post", await create_url_without_domain("/service/application/assets/v1.0/namespaces/{namespace}/upload/start/", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
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
        """Use this API to perform the third step of uploading (i.e. **Complete**) an arbitrarily sized buffer or blob.

The three major steps are:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `startUpload`.
It returns a storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `startUpload` API with the file (Buffer or Blob) in the request body.

### Complete
After successfully upload, call the `completeUpload` API to finish the upload process.
This operation will return the URL of the uploaded file.

        :param namespace : Segregation of different types of files(prodcuts, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket. : type string
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["completeUpload"], proccessed_params="""{"required":[{"name":"namespace","in":"path","description":"Segregation of different types of files(prodcuts, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Segregation of different types of files(prodcuts, orders, logistics etc), Required for validating the data of the file being uploaded, decides where exactly the file will be stored inside the storage bucket.","required":true,"schema":{"type":"string"}}]}""", namespace=namespace)
        query_string = await create_query_string(namespace=namespace)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["completeUpload"]).netloc, "post", await create_url_without_domain("/service/application/assets/v1.0/namespaces/{namespace}/upload/complete/", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CompleteResponse
            schema = CompleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for completeUpload")
                print(e)

        

        return response
    
    async def signUrls(self, body=""):
        """Describe here
        """
        payload = {}
        
        # Parameter validation
        schema = FileStorageValidator.signUrls()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SignUrlRequest
        schema = SignUrlRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["signUrls"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["signUrls"]).netloc, "post", await create_url_without_domain("/service/application/assets/v1.0/sign-urls/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import SignUrlResponse
            schema = SignUrlResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for signUrls")
                print(e)

        

        return response
    

