"""Theme Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import ThemeValidator

class Theme:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def getAllPages(self, theme_id=None, request_headers:Dict={}):
        """Retrieve a list of all available pages.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.getAllPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AllAvailablePageSchema
            schema = AllAvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllPages")
                print(e)

        return response
    
    async def createPage(self, theme_id=None, body="", request_headers:Dict={}):
        """Generate and add a new page to the selected theme of the Platform.
        :param theme_id : ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.createPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AvailablePageSchema
        schema = AvailablePageSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPage")
                print(e)

        return response
    
    async def updateMultiplePages(self, theme_id=None, body="", request_headers:Dict={}):
        """Modify multiple pages simultaneously of a theme.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.updateMultiplePages()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AllAvailablePageSchema
        schema = AllAvailablePageSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AllAvailablePageSchema
            schema = AllAvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateMultiplePages")
                print(e)

        return response
    
    async def getPage(self, theme_id=None, page_value=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific page of a theme.
        :param theme_id : ID of the theme to be retrieved : type string
        :param page_value : Value of the page to be retrieved : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        if page_value is not None:
            payload["page_value"] = page_value

        # Parameter validation
        schema = ThemeValidator.getPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}]}""", serverType="platform", theme_id=theme_id, page_value=page_value)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPage")
                print(e)

        return response
    
    async def updatePage(self, theme_id=None, page_value=None, body="", request_headers:Dict={}):
        """Modify and update the content of a page.
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        if page_value is not None:
            payload["page_value"] = page_value

        # Parameter validation
        schema = ThemeValidator.updatePage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AvailablePageSchema
        schema = AvailablePageSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}]}""", serverType="platform", theme_id=theme_id, page_value=page_value)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePage")
                print(e)

        return response
    
    async def deletePage(self, theme_id=None, page_value=None, request_headers:Dict={}):
        """Remove a page from a theme of the platform.
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        if page_value is not None:
            payload["page_value"] = page_value

        # Parameter validation
        schema = ThemeValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}]}""", serverType="platform", theme_id=theme_id, page_value=page_value)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deletePage")
                print(e)

        return response
    
    async def getFonts(self, request_headers:Dict={}):
        """Retrieve a list of available fonts that can be used by themes in the platform.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getFonts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/fonts", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/fonts", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FontsSchema
            schema = FontsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFonts")
                print(e)

        return response
    
    async def getApplicationThemes(self, request_headers:Dict={}):
        """Retrieve all draft themes added to sales channel from theme collection.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getApplicationThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/themes", """{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer"}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer"}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/themes", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getApplicationThemesCount(self, request_headers:Dict={}):
        """Retrieve count of all draft themes added to sales channel from theme collection.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getApplicationThemesCount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/application_themes_count", """{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/application_themes_count", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getThemeById(self, theme_id=None, request_headers:Dict={}):
        """Retrieve a theme by its unique identifier. Response contains theme template data and data stored in theme editor.
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.getThemeById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"64be4423bc7b28003211322e"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"64be4423bc7b28003211322e"}}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getThemeById")
                print(e)

        return response
    
    async def updateTheme(self, theme_id=None, body="", request_headers:Dict={}):
        """Modify and update the content and settings of a theme.
        :param theme_id : The ID of the theme. : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.updateTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateThemeRequestBody
        schema = UpdateThemeRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"in":"path","name":"company_id","schema":{"type":"integer","example":19243},"required":true,"description":"The ID of the company."},{"in":"path","name":"application_id","schema":{"type":"string","example":"6487ea376e1442284917c44e"},"required":true,"description":"The ID of the application."},{"in":"path","name":"theme_id","schema":{"type":"string","example":"64be4423bc7b28003211322e"},"required":true,"description":"The ID of the theme."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","schema":{"type":"integer","example":19243},"required":true,"description":"The ID of the company."},{"in":"path","name":"application_id","schema":{"type":"string","example":"6487ea376e1442284917c44e"},"required":true,"description":"The ID of the application."},{"in":"path","name":"theme_id","schema":{"type":"string","example":"64be4423bc7b28003211322e"},"required":true,"description":"The ID of the theme."}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateTheme")
                print(e)

        return response
    
    async def deleteTheme(self, theme_id=None, request_headers:Dict={}):
        """Remove a theme from theme drafts of a sales channel.
        :param theme_id : The ID of the theme to be deleted. : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.deleteTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"name":"theme_id","in":"path","required":true,"schema":{"type":"string","example":"64be4423bc7b28003211322e"},"description":"The ID of the theme to be deleted."}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"name":"theme_id","in":"path","required":true,"schema":{"type":"string","example":"64be4423bc7b28003211322e"},"description":"The ID of the theme to be deleted."}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteTheme")
                print(e)

        return response
    
    async def addThemeToApplication(self, body="", request_headers:Dict={}):
        """Include a theme in an application drafts from theme collection.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.addThemeToApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ThemeReq
        schema = ThemeReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addThemeToApplication")
                print(e)

        return response
    
    async def updateThemeName(self, theme_id=None, body="", request_headers:Dict={}):
        """Modify the name of the draft theme by theme Id.
        :param theme_id : The ID of the theme to be updated. : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.updateThemeName()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateThemeNameRequestBody
        schema = UpdateThemeNameRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/name", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"in":"path","name":"application_id","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"in":"path","name":"theme_id","required":true,"schema":{"type":"string"},"description":"The ID of the theme to be updated."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"in":"path","name":"application_id","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"in":"path","name":"theme_id","required":true,"schema":{"type":"string"},"description":"The ID of the theme to be updated."}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/name", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateThemeName")
                print(e)

        return response
    
    async def applyTheme(self, theme_id=None, request_headers:Dict={}):
        """Change current applied theme with new draft theme.
        :param theme_id : The ID of the apply : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.applyTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/apply", """{"required":[{"in":"path","name":"company_id","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","description":"The ID of the apply","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","description":"The ID of the apply","required":true,"schema":{"type":"string"}}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/apply", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for applyTheme")
                print(e)

        return response
    
    async def duplicateTheme(self, theme_id=None, request_headers:Dict={}):
        """Create a new copy of an existing theme by theme Id
        :param theme_id : The ID of the theme to be duplicated : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.duplicateTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/duplicate", """{"required":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"The ID of the theme to be duplicated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"The ID of the theme to be duplicated","required":true,"schema":{"type":"string"}}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/duplicate", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for duplicateTheme")
                print(e)

        return response
    
    async def getAppliedTheme(self, request_headers:Dict={}):
        """Retrieve the currently applied theme of a sales channel using application Id.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getAppliedTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}", """{"required":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppliedTheme")
                print(e)

        return response
    
    async def getThemeForPreview(self, theme_id=None, request_headers:Dict={}):
        """Retrieve a theme by its unique identifier. Response contains theme template data and data stored in theme editor.
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.getThemeForPreview()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/preview", """{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/preview", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getThemeForPreview")
                print(e)

        return response
    
    async def getThemeLastModified(self, theme_id=None, request_headers:Dict={}):
        """Retrieve the last modification of a theme used for polling and identifing cross user changes in a theme.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.getThemeLastModified()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/polling", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("HEAD", url_with_params, headers=get_headers_with_signature(self._conf.domain, "head", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/polling", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def isUpgradable(self, theme_id=None, request_headers:Dict={}):
        """Determine if a public theme is eligible for an upgrade to a new version after any new version released in marketplace. 
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.isUpgradable()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgradable", """{"required":[{"name":"company_id","in":"path","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"648832dcb99296ab200fbaaa"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"648832dcb99296ab200fbaaa"}}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgradable", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemeUpgradableResponse
            schema = ThemeUpgradableResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for isUpgradable")
                print(e)

        return response
    
    async def upgradeTheme(self, theme_id=None, request_headers:Dict={}):
        """Update a draft theme to a new version of the marketplace.
        :param theme_id : The ID of the upgrade : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.upgradeTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgrade", """{"required":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"The ID of the upgrade","required":true,"schema":{"type":"string","example":"64883302baad790ae4898314"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"The ID of the upgrade","required":true,"schema":{"type":"string","example":"64883302baad790ae4898314"}}]}""", serverType="platform", theme_id=theme_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgrade", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for upgradeTheme")
                print(e)

        return response
    
    async def getExtensionSections(self, type=None, company_mode=None, request_headers:Dict={}):
        """Retrieve the list of extension sections for a given application in the specified company.
        :param type : The type of the theme : type string
        :param company_mode : The mode of the company : type string
        """
        payload = {}
        
        if type is not None:
            payload["type"] = type
        if company_mode is not None:
            payload["company_mode"] = company_mode

        # Parameter validation
        schema = ThemeValidator.getExtensionSections()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/extension-section", """{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":1}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6399ba8924ab1be7c21314b5"}}],"optional":[{"in":"query","name":"type","required":false,"description":"The type of the theme","schema":{"type":"string","example":"react"}},{"in":"query","name":"company_mode","required":false,"description":"The mode of the company","schema":{"type":"string","example":"live"}}],"query":[{"in":"query","name":"type","required":false,"description":"The type of the theme","schema":{"type":"string","example":"react"}},{"in":"query","name":"company_mode","required":false,"description":"The mode of the company","schema":{"type":"string","example":"live"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":1}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6399ba8924ab1be7c21314b5"}}]}""", serverType="platform", type=type, company_mode=company_mode)
        query_string = await create_query_string(type=type, company_mode=company_mode)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/extension-section", type=type, company_mode=company_mode), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    