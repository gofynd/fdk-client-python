

"""Theme Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import ThemeValidator

class Theme:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getAllPages": "/service/application/theme/v1.0/{theme_id}/page",
            "getPage": "/service/application/theme/v1.0/{theme_id}/{page_value}",
            "getAppliedTheme": "/service/application/theme/v1.0/applied-theme",
            "getThemeForPreview": "/service/application/theme/v1.0/{theme_id}/preview"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getAllPages(self, theme_id=None, body=""):
        """Use this API to retrieve all the available pages of a theme by its ID.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        # Parameter validation
        schema = ThemeValidator.getAllPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAllPages"], proccessed_params="""{"required":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAllPages"]).netloc, "get", await create_url_without_domain("/service/application/theme/v1.0/{theme_id}/page", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPage(self, theme_id=None, page_value=None, body=""):
        """Use this API to retrieve a page of a theme.
        :param theme_id : ID of the theme to be retrieved : type string
        :param page_value : Value of the page to be retrieved : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        if page_value:
            payload["page_value"] = page_value
        
        # Parameter validation
        schema = ThemeValidator.getPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPage"], proccessed_params="""{"required":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id, page_value=page_value)
        query_string = await create_query_string(theme_id=theme_id, page_value=page_value)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPage"]).netloc, "get", await create_url_without_domain("/service/application/theme/v1.0/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAppliedTheme(self, body=""):
        """An application has multiple themes, but only one theme can be applied at a time. Use this API to retrieve the theme currently applied to the application.
        """
        payload = {}
        
        # Parameter validation
        schema = ThemeValidator.getAppliedTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAppliedTheme"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAppliedTheme"]).netloc, "get", await create_url_without_domain("/service/application/theme/v1.0/applied-theme", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getThemeForPreview(self, theme_id=None, body=""):
        """A theme can be previewed before applying it. Use this API to retrieve the preview of a theme by its ID.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        # Parameter validation
        schema = ThemeValidator.getThemeForPreview()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getThemeForPreview"], proccessed_params="""{"required":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getThemeForPreview"]).netloc, "get", await create_url_without_domain("/service/application/theme/v1.0/{theme_id}/preview", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
