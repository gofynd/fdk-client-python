"""Share Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import ShareValidator

class Share:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def createShortLink(self, body="", request_headers:Dict={}):
        """Generate a shortened URL link for sharing.
        """
        payload = {}
        

        # Parameter validation
        schema = ShareValidator.createShortLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ShortLinkReq
        schema = ShortLinkReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"The unique identifier for the company."}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"The unique identifier for the company."}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShortLinkRes
            schema = ShortLinkRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createShortLink")
                print(e)

        return response
    
    async def getShortLinks(self, page_no=None, page_size=None, created_by=None, active=None, short_url=None, original_url=None, title=None, request_headers:Dict={}):
        """Retrieve a list of all generated short links.
        :param page_no : Current page number : type integer
        :param page_size : Number of items displayed per page : type integer
        :param created_by : Short link creator : type string
        :param active : Short link active status : type string
        :param short_url : Search for short url : type string
        :param original_url : Search for original url : type string
        :param title : Search text for title : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if created_by is not None:
            payload["created_by"] = created_by
        if active is not None:
            payload["active"] = active
        if short_url is not None:
            payload["short_url"] = short_url
        if original_url is not None:
            payload["original_url"] = original_url
        if title is not None:
            payload["title"] = title

        # Parameter validation
        schema = ShareValidator.getShortLinks()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"The unique identifier for the company."}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"Number of items displayed per page","required":false,"schema":{"type":"integer"}},{"name":"created_by","in":"query","description":"Short link creator","required":false,"schema":{"type":"string","enum":["team"]}},{"name":"active","in":"query","description":"Short link active status","required":false,"schema":{"type":"string","enum":["true","false"]}},{"name":"short_url","in":"query","description":"Search for short url","required":false,"schema":{"type":"string"}},{"name":"original_url","in":"query","description":"Search for original url","required":false,"schema":{"type":"string"}},{"name":"title","in":"query","description":"Search text for title","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"Number of items displayed per page","required":false,"schema":{"type":"integer"}},{"name":"created_by","in":"query","description":"Short link creator","required":false,"schema":{"type":"string","enum":["team"]}},{"name":"active","in":"query","description":"Short link active status","required":false,"schema":{"type":"string","enum":["true","false"]}},{"name":"short_url","in":"query","description":"Search for short url","required":false,"schema":{"type":"string"}},{"name":"original_url","in":"query","description":"Search for original url","required":false,"schema":{"type":"string"}},{"name":"title","in":"query","description":"Search text for title","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"The unique identifier for the company."}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, created_by=created_by, active=active, short_url=short_url, original_url=original_url, title=title)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, created_by=created_by, active=active, short_url=short_url, original_url=original_url, title=title)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link", page_no=page_no, page_size=page_size, created_by=created_by, active=active, short_url=short_url, original_url=original_url, title=title), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShortLinkList
            schema = ShortLinkList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShortLinks")
                print(e)

        return response
    
    async def getShortLinkByHash(self, hash=None, request_headers:Dict={}):
        """Retrieve a specific short link by its unique hash.
        :param hash :  : type string
        """
        payload = {}
        
        if hash is not None:
            payload["hash"] = hash

        # Parameter validation
        schema = ShareValidator.getShortLinkByHash()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{hash}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"The unique identifier for the company."}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"hash","in":"path","required":true,"schema":{"type":"string","description":"This is shortlink hash"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"The unique identifier for the company."}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"hash","in":"path","required":true,"schema":{"type":"string","description":"This is shortlink hash"}}]}""", serverType="platform", hash=hash)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{hash}", hash=hash), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShortLinkRes
            schema = ShortLinkRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShortLinkByHash")
                print(e)

        return response
    
    async def updateShortLinkById(self, id=None, body="", request_headers:Dict={}):
        """Update details of a specific short link by its ID.
        :param id : Document Id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ShareValidator.updateShortLinkById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ShortLinkReq
        schema = ShortLinkReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"The unique identifier for the company."}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"id","in":"path","description":"Document Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"The unique identifier for the company."}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"id","in":"path","description":"Document Id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShortLinkRes
            schema = ShortLinkRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateShortLinkById")
                print(e)

        return response
    