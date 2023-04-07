

"""Share Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import ShareValidator

class Share:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getApplicationQRCode": "/service/application/share/v1.0/qr/",
            "getProductQRCodeBySlug": "/service/application/share/v1.0/qr/products/{slug}/",
            "getCollectionQRCodeBySlug": "/service/application/share/v1.0/qr/collection/{slug}/",
            "getUrlQRCode": "/service/application/share/v1.0/qr/url/",
            "createShortLink": "/service/application/share/v1.0/links/short-link/",
            "getShortLinkByHash": "/service/application/share/v1.0/links/short-link/{hash}/",
            "getOriginalShortLinkByHash": "/service/application/share/v1.0/links/short-link/{hash}/original/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getApplicationQRCode(self, body=""):
        """Use this API to create a QR code of an app for sharing it with users who want to use the app.
        """
        payload = {}
        
        # Parameter validation
        schema = ShareValidator.getApplicationQRCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getApplicationQRCode"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getApplicationQRCode"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProductQRCodeBySlug(self, slug=None, body=""):
        """Use this API to create a QR code of a product for sharing it with users who want to view/purchase the product.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = ShareValidator.getProductQRCodeBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductQRCodeBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductQRCodeBySlug"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr/products/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCollectionQRCodeBySlug(self, slug=None, body=""):
        """Use this API to create a QR code of a collection of products for sharing it with users who want to view/purchase the collection.
        :param slug : A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = ShareValidator.getCollectionQRCodeBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCollectionQRCodeBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCollectionQRCodeBySlug"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr/collection/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getUrlQRCode(self, url=None, body=""):
        """Use this API to create a QR code of a URL for sharing it with users who want to visit the link.
        :param url : A link or a web address : type string
        """
        payload = {}
        
        if url:
            payload["url"] = url
        
        # Parameter validation
        schema = ShareValidator.getUrlQRCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUrlQRCode"], proccessed_params="""{"required":[{"name":"url","in":"query","description":"A link or a web address","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"url","in":"query","description":"A link or a web address","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", url=url)
        query_string = await create_query_string(url=url)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getUrlQRCode"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr/url/", url=url), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def createShortLink(self, body=""):
        """Use this API to create a short link that is easy to write/share/read as compared to long URLs.
        """
        payload = {}
        
        # Parameter validation
        schema = ShareValidator.createShortLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ShortLinkReq
        schema = ShortLinkReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createShortLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["createShortLink"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/links/short-link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getShortLinkByHash(self, hash=None, body=""):
        """Use this API to get a short link by using a hash value.
        :param hash : A string value used for converting long URL to short URL and vice-versa. : type string
        """
        payload = {}
        
        if hash:
            payload["hash"] = hash
        
        # Parameter validation
        schema = ShareValidator.getShortLinkByHash()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShortLinkByHash"], proccessed_params="""{"required":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}]}""", hash=hash)
        query_string = await create_query_string(hash=hash)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getShortLinkByHash"]).netloc, "get", await create_url_without_domain("/service/application/share/v1.0/links/short-link/{hash}/", hash=hash), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getOriginalShortLinkByHash(self, hash=None, body=""):
        """Use this API to retrieve the original link from a short-link by using a hash value.
        :param hash : A string value used for converting long URL to short URL and vice-versa. : type string
        """
        payload = {}
        
        if hash:
            payload["hash"] = hash
        
        # Parameter validation
        schema = ShareValidator.getOriginalShortLinkByHash()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOriginalShortLinkByHash"], proccessed_params="""{"required":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}]}""", hash=hash)
        query_string = await create_query_string(hash=hash)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOriginalShortLinkByHash"]).netloc, "get", await create_url_without_domain("/service/application/share/v1.0/links/short-link/{hash}/original/", hash=hash), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

