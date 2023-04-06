

"""Theme Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import ThemeValidator

class Theme:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getAllPages(self, theme_id=None):
        """Use this API to retrieve all the available pages of a theme by its ID.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getAllPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import AllAvailablePageSchema
        schema = AllAvailablePageSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getAllPages")
            print(e)
            
        

        return response
    
    async def createPage(self, theme_id=None, body=""):
        """Use this API to create a page for a theme by its ID.
        :param theme_id : ID of the theme : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.createPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AvailablePageSchema
        schema = AvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import AvailablePageSchema
        schema = AvailablePageSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createPage")
            print(e)
            
        

        return response
    
    async def updateMultiplePages(self, theme_id=None, body=""):
        """Use this API to update multiple pages of a theme by its ID.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.updateMultiplePages()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AllAvailablePageSchema
        schema = AllAvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import AllAvailablePageSchema
        schema = AllAvailablePageSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateMultiplePages")
            print(e)
            
        

        return response
    
    async def getPage(self, theme_id=None, page_value=None):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id, page_value=page_value)
        query_string = await create_query_string(theme_id=theme_id, page_value=page_value)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import AvailablePageSchema
        schema = AvailablePageSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getPage")
            print(e)
            
        

        return response
    
    async def updatePage(self, theme_id=None, page_value=None, body=""):
        """Use this API to update a page for a theme by its ID.
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        if page_value:
            payload["page_value"] = page_value
        

        # Parameter validation
        schema = ThemeValidator.updatePage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AvailablePageSchema
        schema = AvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id, page_value=page_value)
        query_string = await create_query_string(theme_id=theme_id, page_value=page_value)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import AvailablePageSchema
        schema = AvailablePageSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updatePage")
            print(e)
            
        

        return response
    
    async def deletePage(self, theme_id=None, page_value=None):
        """Use this API to delete a page for a theme by its ID and page_value.
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        if page_value:
            payload["page_value"] = page_value
        

        # Parameter validation
        schema = ThemeValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id, page_value=page_value)
        query_string = await create_query_string(theme_id=theme_id, page_value=page_value)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import AvailablePageSchema
        schema = AvailablePageSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for deletePage")
            print(e)
            
        

        return response
    
    async def getThemeLibrary(self, page_size=None, page_no=None):
        """Theme library is a personalized collection of themes that are chosen and added from the available themes. Use this API to fetch a list of themes from the library along with their configuration details. 
        :param page_size : The number of items to retrieve in each page. Default value is 10.  : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        """
        payload = {}
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = ThemeValidator.getThemeLibrary()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/library", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_size=page_size, page_no=page_no)
        query_string = await create_query_string(page_size=page_size, page_no=page_no)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/library", page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import ThemesListingResponseSchema
        schema = ThemesListingResponseSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getThemeLibrary")
            print(e)
            
        

        return response
    
    async def addToThemeLibrary(self, body=""):
        """Theme library is a personalized collection of themes that are chosen and added from the available themes. Use this API to choose a theme and add it to the theme library.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.addToThemeLibrary()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddThemeRequestSchema
        schema = AddThemeRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/library", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/library", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for addToThemeLibrary")
            print(e)
            
        

        return response
    
    async def applyTheme(self, body=""):
        """Use this API to apply a theme to the website.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.applyTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddThemeRequestSchema
        schema = AddThemeRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/apply", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/apply", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for applyTheme")
            print(e)
            
        

        return response
    
    async def isUpgradable(self, theme_id=None):
        """There's always a possibility that new features get added to a theme. Use this API to check if the applied theme has an upgrade available.
        :param theme_id : Theme ID : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.isUpgradable()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgradable", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"Theme ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"Theme ID","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgradable", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import UpgradableThemeSchema
        schema = UpgradableThemeSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for isUpgradable")
            print(e)
            
        

        return response
    
    async def upgradeTheme(self, theme_id=None):
        """Use this API to upgrade the current theme to its latest version.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.upgradeTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgrade", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgrade", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for upgradeTheme")
            print(e)
            
        

        return response
    
    async def getPublicThemes(self, page_size=None, page_no=None):
        """Use this API to get a list of free themes that you can apply to your website.
        :param page_size : The number of items to retrieve in each page. Default value is 10.  : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        """
        payload = {}
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = ThemeValidator.getPublicThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/list/public", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_size=page_size, page_no=page_no)
        query_string = await create_query_string(page_size=page_size, page_no=page_no)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/list/public", page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import ThemesListingResponseSchema
        schema = ThemesListingResponseSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getPublicThemes")
            print(e)
            
        

        return response
    
    async def createTheme(self, body=""):
        """Themes improve the look and appearance of a website. Use this API to create a theme.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.createTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ThemesSchema
        schema = ThemesSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createTheme")
            print(e)
            
        

        return response
    
    async def getAppliedTheme(self, ):
        """Use this API to retrieve the theme that is currently applied to the website along with its details.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getAppliedTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getAppliedTheme")
            print(e)
            
        

        return response
    
    async def getFonts(self, ):
        """Font is a collection of characters with a similar design. Use this API to retrieve a list of website fonts.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getFonts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/fonts", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/fonts", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import FontsSchema
        schema = FontsSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getFonts")
            print(e)
            
        

        return response
    
    async def getThemeById(self, theme_id=None):
        """Use this API to retrieve the details of a specific theme by using its ID.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getThemeById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getThemeById")
            print(e)
            
        

        return response
    
    async def updateTheme(self, theme_id=None, body=""):
        """Use this API to edit an existing theme. You can customize the website font, sections, images, styles, and many more.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.updateTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ThemesSchema
        schema = ThemesSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateTheme")
            print(e)
            
        

        return response
    
    async def deleteTheme(self, theme_id=None):
        """Use this API to delete a theme from the theme library.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.deleteTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for deleteTheme")
            print(e)
            
        

        return response
    
    async def getThemeForPreview(self, theme_id=None):
        """A theme can be previewed before applying it. Use this API to retrieve the theme preview by using its ID.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getThemeForPreview()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/preview", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/preview", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getThemeForPreview")
            print(e)
            
        

        return response
    
    async def publishTheme(self, theme_id=None):
        """Use this API to publish a theme that is either newly created or edited.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.publishTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/publish", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/publish", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for publishTheme")
            print(e)
            
        

        return response
    
    async def unpublishTheme(self, theme_id=None):
        """Use this API to remove an existing theme from the list of available themes.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.unpublishTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/unpublish", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/unpublish", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for unpublishTheme")
            print(e)
            
        

        return response
    
    async def archiveTheme(self, theme_id=None):
        """Use this API to store an existing theme but not delete it so that it can be used in future if required. 
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.archiveTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/archive", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/archive", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for archiveTheme")
            print(e)
            
        

        return response
    
    async def unarchiveTheme(self, theme_id=None):
        """Use this API to restore an archived theme and bring it back for editing or publishing. 
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.unarchiveTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/unarchive", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/unarchive", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import ThemesSchema
        schema = ThemesSchema()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for unarchiveTheme")
            print(e)
            
        

        return response
    
    async def getThemeLastModified(self, theme_id=None):
        """Use this API to fetch Last-Modified timestamp in header metadata.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getThemeLastModified()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/polling", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("HEAD", url_with_params, headers=get_headers_with_signature(self._conf.domain, "head", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/polling", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        return response
    

