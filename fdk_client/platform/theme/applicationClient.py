

"""Theme Platform Client"""

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
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getAllPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AllAvailablePageSchema
            schema = AllAvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllPages")
                print(e)

        

        return response
    
    async def createPage(self, theme_id=None, body=""):
        """Use this API to create a page for a theme by its ID.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPage")
                print(e)

        

        return response
    
    async def updateMultiplePages(self, theme_id=None, body=""):
        """Use this API to update multiple pages of a theme by its ID.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AllAvailablePageSchema
            schema = AllAvailablePageSchema()
            try:
                schema.load(response["json"])
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
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        if page_value is not None:
            payload["page_value"] = page_value
        

        # Parameter validation
        schema = ThemeValidator.getPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id, page_value=page_value)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id, page_value=page_value)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
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
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        if page_value is not None:
            payload["page_value"] = page_value
        

        # Parameter validation
        schema = ThemeValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id, page_value=page_value)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
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
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if page_no is not None:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = ThemeValidator.getThemeLibrary()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/library", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", page_size=page_size, page_no=page_no)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DummyResponse
            schema = DummyResponse()
            try:
                schema.load(response["json"])
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/library", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", )
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DummyResponse
            schema = DummyResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addToThemeLibrary")
                print(e)

        

        return response
    
    async def getPublicThemes(self, page_size=None, page_no=None):
        """Use this API to get a list of free themes that you can apply to your website.
        :param page_size : The number of items to retrieve in each page. Default value is 10.  : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        """
        payload = {}
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if page_no is not None:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = ThemeValidator.getPublicThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/list/public", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", page_size=page_size, page_no=page_no)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DummyResponse
            schema = DummyResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPublicThemes")
                print(e)

        

        return response
    
    async def getFonts(self, ):
        """Font is a collection of characters with a similar design. Use this API to retrieve a list of website fonts.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getFonts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/fonts", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", )
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import FontsSchema
            schema = FontsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFonts")
                print(e)

        

        return response
    
    async def publishTheme(self, theme_id=None):
        """Use this API to publish a theme that is either newly created or edited.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.publishTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/publish", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DummyResponse
            schema = DummyResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for publishTheme")
                print(e)

        

        return response
    
    async def unpublishTheme(self, theme_id=None):
        """Use this API to remove an existing theme from the list of available themes.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.unpublishTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/unpublish", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DummyResponse
            schema = DummyResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for unpublishTheme")
                print(e)

        

        return response
    
    async def archiveTheme(self, theme_id=None):
        """Use this API to store an existing theme but not delete it so that it can be used in future if required. 
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.archiveTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/archive", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DummyResponse
            schema = DummyResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for archiveTheme")
                print(e)

        

        return response
    
    async def unarchiveTheme(self, theme_id=None):
        """Use this API to restore an archived theme and bring it back for editing or publishing. 
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.unarchiveTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/unarchive", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DummyResponse
            schema = DummyResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for unarchiveTheme")
                print(e)

        

        return response
    
    async def getApplicationThemes(self, ):
        """Get all the themes for a specific application
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getApplicationThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/themes", """{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer"},"examples":{"example1":{"summary":"Example 1 - Company ID","value":19243},"example2":{"summary":"Example 2 - Company ID","value":98765}}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string"},"examples":{"example1":{"summary":"Example 1 - Application ID","value":"6487ea376e1442284917c44e"},"example2":{"summary":"Example 2 - Application ID","value":"7487ea376e1442284917c44e"}}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer"},"examples":{"example1":{"summary":"Example 1 - Company ID","value":19243},"example2":{"summary":"Example 2 - Company ID","value":98765}}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string"},"examples":{"example1":{"summary":"Example 1 - Application ID","value":"6487ea376e1442284917c44e"},"example2":{"summary":"Example 2 - Application ID","value":"7487ea376e1442284917c44e"}}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/themes", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        return response
    
    async def getApplicationThemesCount(self, ):
        """Get the count of themes for a specific application
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getApplicationThemesCount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/application_themes_count", """{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/application_themes_count", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        return response
    
    async def getThemeById(self, theme_id=None):
        """Get Theme By Theme Id
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getThemeById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"64be4423bc7b28003211322e"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"64be4423bc7b28003211322e"}}]}""", theme_id=theme_id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getThemeById")
                print(e)

        

        return response
    
    async def updateTheme(self, theme_id=None, body=""):
        """Update theme for a specific company and application
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"in":"path","name":"company_id","schema":{"type":"integer","example":19243},"required":true,"description":"The ID of the company."},{"in":"path","name":"application_id","schema":{"type":"string","example":"6487ea376e1442284917c44e"},"required":true,"description":"The ID of the application."},{"in":"path","name":"theme_id","schema":{"type":"string","example":"64be4423bc7b28003211322e"},"required":true,"description":"The ID of the theme."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","schema":{"type":"integer","example":19243},"required":true,"description":"The ID of the company."},{"in":"path","name":"application_id","schema":{"type":"string","example":"6487ea376e1442284917c44e"},"required":true,"description":"The ID of the application."},{"in":"path","name":"theme_id","schema":{"type":"string","example":"64be4423bc7b28003211322e"},"required":true,"description":"The ID of the theme."}]}""", theme_id=theme_id)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateTheme")
                print(e)

        

        return response
    
    async def deleteTheme(self, theme_id=None):
        """This endpoint is used to delete a theme from the specified company and application.
        :param theme_id : The ID of the theme to be deleted. : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.deleteTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"name":"theme_id","in":"path","required":true,"schema":{"type":"string","example":"64be4423bc7b28003211322e"},"description":"The ID of the theme to be deleted."}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"name":"theme_id","in":"path","required":true,"schema":{"type":"string","example":"64be4423bc7b28003211322e"},"description":"The ID of the theme to be deleted."}]}""", theme_id=theme_id)
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
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteTheme")
                print(e)

        

        return response
    
    async def addThemeToApplication(self, body=""):
        """Add a theme to an application by providing the marketplace theme ID.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.addThemeToApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ThemeReq
        schema = ThemeReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addThemeToApplication")
                print(e)

        

        return response
    
    async def updateThemeName(self, theme_id=None, body=""):
        """Update the name of a theme for a specific company and application.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/name", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"in":"path","name":"application_id","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"in":"path","name":"theme_id","required":true,"schema":{"type":"string"},"description":"The ID of the theme to be updated."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"in":"path","name":"application_id","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"in":"path","name":"theme_id","required":true,"schema":{"type":"string"},"description":"The ID of the theme to be updated."}]}""", theme_id=theme_id)
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
        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/name", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateThemeName")
                print(e)

        

        return response
    
    async def applyTheme(self, theme_id=None):
        """Apply theme to a specific application by providing company_id, application_id, and theme_id.
        :param theme_id : The ID of the apply : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.applyTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/apply", """{"required":[{"in":"path","name":"company_id","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","description":"The ID of the apply","required":true,"schema":{"type":"string"},"examples":{"example1":{"summary":"Example 1 - Theme ID","value":"648832dcb99296ab200fbaaa"},"example2":{"summary":"Example 2 - Theme ID","value":"64b91fe317422a1e1392f85b"}}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","description":"The ID of the apply","required":true,"schema":{"type":"string"},"examples":{"example1":{"summary":"Example 1 - Theme ID","value":"648832dcb99296ab200fbaaa"},"example2":{"summary":"Example 2 - Theme ID","value":"64b91fe317422a1e1392f85b"}}}]}""", theme_id=theme_id)
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
        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/apply", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for applyTheme")
                print(e)

        

        return response
    
    async def duplicateTheme(self, theme_id=None):
        """This endpoint duplicates a Theme in the specified application.
        :param theme_id : The ID of the theme to be duplicated : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.duplicateTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/duplicate", """{"required":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"The ID of the theme to be duplicated","required":true,"schema":{"type":"string"},"examples":{"example1":{"summary":"Example 1 - Theme ID","value":"648832dcb99296ab200fbaaa"},"example2":{"summary":"Example 2 - Theme ID","value":"64b91fe317422a1e1392f85b"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"The ID of the theme to be duplicated","required":true,"schema":{"type":"string"},"examples":{"example1":{"summary":"Example 1 - Theme ID","value":"648832dcb99296ab200fbaaa"},"example2":{"summary":"Example 2 - Theme ID","value":"64b91fe317422a1e1392f85b"}}}]}""", theme_id=theme_id)
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/duplicate", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for duplicateTheme")
                print(e)

        

        return response
    
    async def getAppliedTheme(self, ):
        """Get Applied Theme of an Application by Application Id
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getAppliedTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}", """{"required":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppliedTheme")
                print(e)

        

        return response
    
    async def getThemeForPreview(self, theme_id=None):
        """Get Theme Preview By Theme Id
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getThemeForPreview()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/preview", """{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"6487ea376e1442284917c44e"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"6487ea376e1442284917c44e"}}]}""", theme_id=theme_id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/preview", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getThemeForPreview")
                print(e)

        

        return response
    
    async def getThemeLastModified(self, theme_id=None):
        """Use this API to fetch Last-Modified timestamp in header metadata.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getThemeLastModified()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/polling", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
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
        response = await AiohttpHelper().aiohttp_request("HEAD", url_with_params, headers=get_headers_with_signature(self._conf.domain, "head", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/polling", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        return response
    
    async def isUpgradable(self, theme_id=None):
        """This API endpoint checks if the theme is upgradable for a specific company and application.
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.isUpgradable()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgradable", """{"required":[{"name":"company_id","in":"path","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"648832dcb99296ab200fbaaa"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"648832dcb99296ab200fbaaa"}}]}""", theme_id=theme_id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgradable", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemeUpgradableResponse
            schema = ThemeUpgradableResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for isUpgradable")
                print(e)

        

        return response
    
    async def upgradeTheme(self, theme_id=None):
        """This endpoint allows you to upgrade an application.
        :param theme_id : The ID of the upgrade : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.upgradeTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgrade", """{"required":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"The ID of the upgrade","required":true,"schema":{"type":"string","example":"64883302baad790ae4898314"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"The ID of the company","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"The ID of the application","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"The ID of the upgrade","required":true,"schema":{"type":"string","example":"64883302baad790ae4898314"}}]}""", theme_id=theme_id)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgrade", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for upgradeTheme")
                print(e)

        

        return response
    

