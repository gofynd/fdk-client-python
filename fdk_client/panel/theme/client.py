

"""Theme Panel Client"""

from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import ThemeValidator

class Theme:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getMarketplaceThemes": "/service/panel/theme/v1.0/marketplace/themes",
            "getMarketplaceThemeBySlug": "/service/panel/theme/v1.0/marketplace/theme/{slug_name}",
            "getMarketplaceThemeVersions": "/service/panel/theme/v1.0/marketplace/theme/{slug_name}/versions"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getMarketplaceThemes(self, page_size=None, page_no=None, body=""):
        """This API use to get list of pulished marketplace themes
        :param page_size : Number of themes per page : type integer
        :param page_no : Page number to retrieve : type integer
        """
        payload = {}
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        # Parameter validation
        schema = ThemeValidator.getMarketplaceThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getMarketplaceThemes"], proccessed_params="""{"required":[],"optional":[{"name":"page_size","in":"query","description":"Number of themes per page","required":false,"schema":{"type":"integer","example":6}},{"name":"page_no","in":"query","description":"Page number to retrieve","required":false,"schema":{"type":"integer","example":2}}],"query":[{"name":"page_size","in":"query","description":"Number of themes per page","required":false,"schema":{"type":"integer","example":6}},{"name":"page_no","in":"query","description":"Page number to retrieve","required":false,"schema":{"type":"integer","example":2}}],"headers":[],"path":[]}""", page_size=page_size, page_no=page_no)
        query_string = await create_query_string(page_size=page_size, page_no=page_no)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getMarketplaceThemes"]).netloc, "get", await create_url_without_domain("/service/panel/theme/v1.0/marketplace/themes", page_size=page_size, page_no=page_no), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceThemeResponseBody
            schema = MarketplaceThemeResponseBody()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMarketplaceThemes")
                print(e)

        

        return response
    
    async def getMarketplaceThemeBySlug(self, slug_name=None, body=""):
        """Fetches the theme details by slug
        :param slug_name : Slug of marketplace theme : type string
        """
        payload = {}
        
        if slug_name is not None:
            payload["slug_name"] = slug_name
        
        # Parameter validation
        schema = ThemeValidator.getMarketplaceThemeBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getMarketplaceThemeBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug_name","schema":{"type":"string","example":"emrge"},"required":true,"description":"Slug of marketplace theme"}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug_name","schema":{"type":"string","example":"emrge"},"required":true,"description":"Slug of marketplace theme"}]}""", slug_name=slug_name)
        query_string = await create_query_string(slug_name=slug_name)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getMarketplaceThemeBySlug"]).netloc, "get", await create_url_without_domain("/service/panel/theme/v1.0/marketplace/theme/{slug_name}", slug_name=slug_name), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemeSlugResponse
            schema = ThemeSlugResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMarketplaceThemeBySlug")
                print(e)

        

        return response
    
    async def getMarketplaceThemeVersions(self, slug_name=None, body=""):
        """This API use to get list of theme published theme versions
        :param slug_name : Slug of theme : type string
        """
        payload = {}
        
        if slug_name is not None:
            payload["slug_name"] = slug_name
        
        # Parameter validation
        schema = ThemeValidator.getMarketplaceThemeVersions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getMarketplaceThemeVersions"], proccessed_params="""{"required":[{"in":"path","name":"slug_name","schema":{"type":"string","example":"emerge"},"required":true,"description":"Slug of theme"}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug_name","schema":{"type":"string","example":"emerge"},"required":true,"description":"Slug of theme"}]}""", slug_name=slug_name)
        query_string = await create_query_string(slug_name=slug_name)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getMarketplaceThemeVersions"]).netloc, "get", await create_url_without_domain("/service/panel/theme/v1.0/marketplace/theme/{slug_name}/versions", slug_name=slug_name), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemeAndUserDetailsResponse
            schema = ThemeAndUserDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMarketplaceThemeVersions")
                print(e)

        

        return response
    

