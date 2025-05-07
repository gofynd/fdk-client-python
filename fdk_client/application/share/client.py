"""Share Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import ShareValidator

class Share:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "getApplicationQRCode": "/service/application/share/v1.0/qr",
            "getProductQRCodeBySlug": "/service/application/share/v1.0/qr/products/{slug}",
            "getCollectionQRCodeBySlug": "/service/application/share/v1.0/qr/collection/{slug}",
            "getUrlQRCode": "/service/application/share/v1.0/qr/url",
            "createShortLink": "/service/application/share/v1.0/links/short-link",
            "getShortLinkByHash": "/service/application/share/v1.0/links/short-link/{hash}",
            "getOriginalShortLinkByHash": "/service/application/share/v1.0/links/short-link/{hash}/original"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getApplicationQRCode(self, body="", request_headers:Dict={}):
        """Generates a QR code for the application for easy sharing.
        """
        payload = {}
        

        # Parameter validation
        schema = ShareValidator.getApplicationQRCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getApplicationQRCode"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getApplicationQRCode"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import QRCodeResp
            schema = QRCodeResp()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationQRCode")
                print(e)

        return response
    
    async def getProductQRCodeBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Creates a QR code for a specific product identified by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ShareValidator.getProductQRCodeBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductQRCodeBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}]}""", serverType="application", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductQRCodeBySlug"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr/products/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import QRCodeResp
            schema = QRCodeResp()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductQRCodeBySlug")
                print(e)

        return response
    
    async def getCollectionQRCodeBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Generates a QR code for a specific product collection using its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ShareValidator.getCollectionQRCodeBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCollectionQRCodeBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}]}""", serverType="application", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCollectionQRCodeBySlug"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr/collection/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import QRCodeResp
            schema = QRCodeResp()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCollectionQRCodeBySlug")
                print(e)

        return response
    
    async def getUrlQRCode(self, url=None, body="", request_headers:Dict={}):
        """Converts a given URL into a scannable QR code.
        :param url : A link or a web address of a given URL transformed into a scannable QR code. : type string
        """
        payload = {}
        
        if url is not None:
            payload["url"] = url

        # Parameter validation
        schema = ShareValidator.getUrlQRCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUrlQRCode"], proccessed_params="""{"required":[{"name":"url","in":"query","description":"A link or a web address of a given URL transformed into a scannable QR code.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"url","in":"query","description":"A link or a web address of a given URL transformed into a scannable QR code.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", serverType="application", url=url)
        query_string = await create_query_string(url=url)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getUrlQRCode"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr/url", url=url), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import QRCodeResp
            schema = QRCodeResp()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUrlQRCode")
                print(e)

        return response
    
    async def createShortLink(self, body="", request_headers:Dict={}):
        """Creates a shortened version of a given URL for easier sharing.
        """
        payload = {}
        

        # Parameter validation
        schema = ShareValidator.createShortLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ShortLinkReq
        schema = ShortLinkReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["createShortLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["createShortLink"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/links/short-link", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShortLinkRes
            schema = ShortLinkRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createShortLink")
                print(e)

        return response
    
    async def getShortLinkByHash(self, hash=None, body="", request_headers:Dict={}):
        """Retrieves a previously created short link using its hash identifier.
        :param hash : A string value used for converting long URL to short URL and vice-versa. : type string
        """
        payload = {}
        
        if hash is not None:
            payload["hash"] = hash

        # Parameter validation
        schema = ShareValidator.getShortLinkByHash()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShortLinkByHash"], proccessed_params="""{"required":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}]}""", serverType="application", hash=hash)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getShortLinkByHash"]).netloc, "get", await create_url_without_domain("/service/application/share/v1.0/links/short-link/{hash}", hash=hash), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShortLinkRes
            schema = ShortLinkRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShortLinkByHash")
                print(e)

        return response
    
    async def getOriginalShortLinkByHash(self, hash=None, body="", request_headers:Dict={}):
        """Retrieve the original link from a short-link by using a hash value.
        :param hash : A string value used for converting long URL to short URL and vice-versa. : type string
        """
        payload = {}
        
        if hash is not None:
            payload["hash"] = hash

        # Parameter validation
        schema = ShareValidator.getOriginalShortLinkByHash()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOriginalShortLinkByHash"], proccessed_params="""{"required":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}]}""", serverType="application", hash=hash)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOriginalShortLinkByHash"]).netloc, "get", await create_url_without_domain("/service/application/share/v1.0/links/short-link/{hash}/original", hash=hash), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShortLinkRes
            schema = ShortLinkRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOriginalShortLinkByHash")
                print(e)

        return response
    