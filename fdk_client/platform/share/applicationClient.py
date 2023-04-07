

"""Share Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import ShareValidator

class Share:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def createShortLink(self, body=""):
        """Create short link
        """
        payload = {}
        

        # Parameter validation
        schema = ShareValidator.createShortLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ShortLinkReq
        schema = ShortLinkReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getShortLinks(self, page_no=None, page_size=None, created_by=None, active=None, q=None):
        """Get short links
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        :param created_by : Short link creator : type string
        :param active : Short link active status : type string
        :param q : Search text for original and short url : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if created_by:
            payload["created_by"] = created_by
        
        if active:
            payload["active"] = active
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ShareValidator.getShortLinks()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"default":1,"type":"integer"}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"default":10,"type":"integer"}},{"name":"created_by","in":"query","description":"Short link creator","required":false,"schema":{"type":"string","enum":["team"]}},{"name":"active","in":"query","description":"Short link active status","required":false,"schema":{"type":"string","enum":[true,false]}},{"name":"q","in":"query","description":"Search text for original and short url","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"default":1,"type":"integer"}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"default":10,"type":"integer"}},{"name":"created_by","in":"query","description":"Short link creator","required":false,"schema":{"type":"string","enum":["team"]}},{"name":"active","in":"query","description":"Short link active status","required":false,"schema":{"type":"string","enum":[true,false]}},{"name":"q","in":"query","description":"Search text for original and short url","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, created_by=created_by, active=active, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, created_by=created_by, active=active, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/", page_no=page_no, page_size=page_size, created_by=created_by, active=active, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getShortLinkByHash(self, hash=None):
        """Get short link by hash
        :param hash : Hash of short url : type string
        """
        payload = {}
        
        if hash:
            payload["hash"] = hash
        

        # Parameter validation
        schema = ShareValidator.getShortLinkByHash()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{hash}/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"hash","in":"path","description":"Hash of short url","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"hash","in":"path","description":"Hash of short url","required":true,"schema":{"type":"string"}}]}""", hash=hash)
        query_string = await create_query_string(hash=hash)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{hash}/", hash=hash), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateShortLinkById(self, id=None, body=""):
        """Update short link by id
        :param id : Short link document identifier : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ShareValidator.updateShortLinkById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ShortLinkReq
        schema = ShortLinkReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{id}/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Short link document identifier","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Short link document identifier","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

