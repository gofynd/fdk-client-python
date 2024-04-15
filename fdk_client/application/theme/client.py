"""Theme Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import ThemeValidator

class Theme:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "getAllPages": "/service/application/theme/v1.0/{theme_id}/page",
            "getPage": "/service/application/theme/v1.0/{theme_id}/{page_value}",
            "getAppliedTheme": "/service/application/theme/v2.0/applied-theme",
            "getThemeForPreview": "/service/application/theme/v2.0/{theme_id}/preview"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getAllPages(self, theme_id=None, body="", request_headers:Dict={}):
        """Retrieves a list of all the pages available within the applied theme.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.getAllPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAllPages"], proccessed_params="""{"required":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", serverType="application", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAllPages"]).netloc, "get", await create_url_without_domain("/service/application/theme/v1.0/{theme_id}/page", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AllAvailablePageSchema
            schema = AllAvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllPages")
                print(e)

        return response
    
    async def getPage(self, theme_id=None, page_value=None, filters=None, company=None, body="", request_headers:Dict={}):
        """Retrieve detailed information for a specific page within the theme.
        :param theme_id : ID of the theme to be retrieved : type string
        :param page_value : Value of the page to be retrieved : type string
        :param filters : Filters on sections to be applied or not : type string
        :param company : Company id of the application : type integer
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        if page_value is not None:
            payload["page_value"] = page_value
        if filters is not None:
            payload["filters"] = filters
        if company is not None:
            payload["company"] = company

        # Parameter validation
        schema = ThemeValidator.getPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPage"], proccessed_params="""{"required":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[{"name":"filters","in":"query","description":"Filters on sections to be applied or not","required":false,"schema":{"type":"string"}},{"name":"company","in":"query","description":"Company id of the application","required":false,"schema":{"type":"integer"}}],"query":[{"name":"filters","in":"query","description":"Filters on sections to be applied or not","required":false,"schema":{"type":"string"}},{"name":"company","in":"query","description":"Company id of the application","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}]}""", serverType="application", theme_id=theme_id, page_value=page_value, filters=filters, company=company)
        query_string = await create_query_string(theme_id=theme_id, page_value=page_value, filters=filters, company=company)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPage"]).netloc, "get", await create_url_without_domain("/service/application/theme/v1.0/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value, filters=filters, company=company), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPage")
                print(e)

        return response
    
    async def getAppliedTheme(self, body="", request_headers:Dict={}):
        """Gets the theme currently applied to the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getAppliedTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAppliedTheme"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAppliedTheme"]).netloc, "get", await create_url_without_domain("/service/application/theme/v2.0/applied-theme", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppliedTheme")
                print(e)

        return response
    
    async def getThemeForPreview(self, theme_id=None, body="", request_headers:Dict={}):
        """Retrieves a theme for previewing before applying it to the application.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.getThemeForPreview()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getThemeForPreview"], proccessed_params="""{"required":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", serverType="application", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getThemeForPreview"]).netloc, "get", await create_url_without_domain("/service/application/theme/v2.0/{theme_id}/preview", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getThemeForPreview")
                print(e)

        return response
    