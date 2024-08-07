"""Theme Partner Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PartnerConfig import PartnerConfig

from .validator import ThemeValidator

class Theme:
    def __init__(self, config: PartnerConfig):
        self._conf = config

    
    async def getAllPages(self, company_id=None, application_id=None, theme_id=None, request_headers:Dict={}):
        """Retrieve a list of all pages available in the partner server setup.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.getAllPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", serverType="partner", company_id=company_id, application_id=application_id, theme_id=theme_id, )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/page", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AllAvailablePageSchema
            schema = AllAvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllPages")
                print(e)

        return response
    
    async def createPage(self, company_id=None, application_id=None, theme_id=None, body="", request_headers:Dict={}):
        """Add a new page to the partner server configurations.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.createPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AvailablePageSchema
        schema = AvailablePageSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", serverType="partner", company_id=company_id, application_id=application_id, theme_id=theme_id, )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/page", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPage")
                print(e)

        return response
    
    async def updateMultiplePages(self, company_id=None, application_id=None, theme_id=None, body="", request_headers:Dict={}):
        """Modify and update multiple pages in the partner server setup.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.updateMultiplePages()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AllAvailablePageSchema
        schema = AllAvailablePageSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", serverType="partner", company_id=company_id, application_id=application_id, theme_id=theme_id, )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/page", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AllAvailablePageSchema
            schema = AllAvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateMultiplePages")
                print(e)

        return response
    
    async def getPage(self, company_id=None, application_id=None, theme_id=None, page_value=None, request_headers:Dict={}):
        """Obtain detailed information about a specific page in the partner server.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme to be retrieved : type string
        :param page_value : Value of the page to be retrieved : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id
        if theme_id is not None:
            payload["theme_id"] = theme_id
        if page_value is not None:
            payload["page_value"] = page_value

        # Parameter validation
        schema = ThemeValidator.getPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", serverType="partner", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPage")
                print(e)

        return response
    
    async def updatePage(self, company_id=None, application_id=None, theme_id=None, page_value=None, body="", request_headers:Dict={}):
        """Modify and update information related to a specific page in the partner server.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", serverType="partner", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePage")
                print(e)

        return response
    
    async def deletePage(self, company_id=None, application_id=None, theme_id=None, page_value=None, request_headers:Dict={}):
        """Remove a page from the partner server configurations.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id
        if theme_id is not None:
            payload["theme_id"] = theme_id
        if page_value is not None:
            payload["page_value"] = page_value

        # Parameter validation
        schema = ThemeValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", serverType="partner", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deletePage")
                print(e)

        return response
    
    async def getApplicationThemes(self, company_id=None, application_id=None, request_headers:Dict={}):
        """Retrieve a list of themes available for the partner server application.
        :param company_id : The ID of the company : type integer
        :param application_id : The ID of the application : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id

        # Parameter validation
        schema = ThemeValidator.getApplicationThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v2.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/themes", """{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer"}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer"}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", serverType="partner", company_id=company_id, application_id=application_id, )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/theme/v2.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/themes", company_id=company_id, application_id=application_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getThemeById(self, company_id=None, application_id=None, theme_id=None, request_headers:Dict={}):
        """Obtain detailed information about a theme using its unique ID.
        :param company_id : The ID of the company : type integer
        :param application_id : The ID of the application : type string
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.getThemeById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v2.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}", """{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"64be4423bc7b28003211322e"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"64be4423bc7b28003211322e"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", serverType="partner", company_id=company_id, application_id=application_id, theme_id=theme_id, )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/theme/v2.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getThemeById")
                print(e)

        return response
    
    async def updateTheme(self, company_id=None, application_id=None, theme_id=None, body="", request_headers:Dict={}):
        """Modify and update information related to a theme in the partner server.
        :param company_id : The ID of the company. : type integer
        :param application_id : The ID of the application. : type string
        :param theme_id : The ID of the theme. : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.updateTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateThemeRequestBody
        schema = UpdateThemeRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v2.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}", """{"required":[{"in":"path","name":"company_id","schema":{"type":"integer","example":19243},"required":true,"description":"The ID of the company."},{"in":"path","name":"application_id","schema":{"type":"string","example":"6487ea376e1442284917c44e"},"required":true,"description":"The ID of the application."},{"in":"path","name":"theme_id","schema":{"type":"string","example":"64be4423bc7b28003211322e"},"required":true,"description":"The ID of the theme."},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","schema":{"type":"integer","example":19243},"required":true,"description":"The ID of the company."},{"in":"path","name":"application_id","schema":{"type":"string","example":"6487ea376e1442284917c44e"},"required":true,"description":"The ID of the application."},{"in":"path","name":"theme_id","schema":{"type":"string","example":"64be4423bc7b28003211322e"},"required":true,"description":"The ID of the theme."},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", serverType="partner", company_id=company_id, application_id=application_id, theme_id=theme_id, )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/partner/theme/v2.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateTheme")
                print(e)

        return response
    
    async def deleteTheme(self, company_id=None, application_id=None, theme_id=None, request_headers:Dict={}):
        """Remove a theme from the partner server configurations.
        :param company_id : The ID of the company. : type integer
        :param application_id : The ID of the application. : type string
        :param theme_id : The ID of the theme to be deleted. : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.deleteTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v2.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"name":"theme_id","in":"path","required":true,"schema":{"type":"string","example":"64be4423bc7b28003211322e"},"description":"The ID of the theme to be deleted."},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"name":"theme_id","in":"path","required":true,"schema":{"type":"string","example":"64be4423bc7b28003211322e"},"description":"The ID of the theme to be deleted."},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", serverType="partner", company_id=company_id, application_id=application_id, theme_id=theme_id, )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/partner/theme/v2.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}/{theme_id}", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteTheme")
                print(e)

        return response
    
    async def getOrganizationThemes(self, status=None, page_size=None, page_no=None, request_headers:Dict={}):
        """Retrieve a list of themes associated with partner server organizations.
        :param status : The status of the theme : type string
        :param page_size : Number of themes per page : type integer
        :param page_no : Page number to retrieve : type integer
        """
        payload = {}
        
        if status is not None:
            payload["status"] = status
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no

        # Parameter validation
        schema = ThemeValidator.getOrganizationThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/themes", """{"required":[{"name":"organization_id","in":"path","description":"Id of your organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"}],"optional":[{"name":"status","in":"query","description":"The status of the theme","required":false,"schema":{"type":"string","enum":["published","submitted","in-review","rejected"]},"example":"published"},{"name":"page_size","in":"query","description":"Number of themes per page","required":false,"schema":{"type":"integer","example":6}},{"name":"page_no","in":"query","description":"Page number to retrieve","required":false,"schema":{"type":"integer","example":2}}],"query":[{"name":"status","in":"query","description":"The status of the theme","required":false,"schema":{"type":"string","enum":["published","submitted","in-review","rejected"]},"example":"published"},{"name":"page_size","in":"query","description":"Number of themes per page","required":false,"schema":{"type":"integer","example":6}},{"name":"page_no","in":"query","description":"Page number to retrieve","required":false,"schema":{"type":"integer","example":2}}],"headers":[],"path":[{"name":"organization_id","in":"path","description":"Id of your organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"}]}""", serverType="partner", status=status, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(status=status, page_size=page_size, page_no=page_no)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/themes", status=status, page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceThemeSchema
            schema = MarketplaceThemeSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrganizationThemes")
                print(e)

        return response
    
    async def getOrganizationThemeDetails(self, theme_id=None, request_headers:Dict={}):
        """Obtain detailed information about a theme within partner server organizations.
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.getOrganizationThemeDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_id}", """{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}]}""", serverType="partner", theme_id=theme_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_id}", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceTheme
            schema = MarketplaceTheme()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrganizationThemeDetails")
                print(e)

        return response
    
    async def updateDraftTheme(self, theme_id=None, body="", request_headers:Dict={}):
        """Modify and update a draft theme in partner server organizations.
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.updateDraftTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MarketplaceTheme
        schema = MarketplaceTheme()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_id}", """{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}]}""", serverType="partner", theme_id=theme_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_id}", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceTheme
            schema = MarketplaceTheme()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateDraftTheme")
                print(e)

        return response
    
    async def submitOrganizationTheme(self, theme_id=None, body="", request_headers:Dict={}):
        """Initiate the process of submitting a theme within partner server organizations.
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.submitOrganizationTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MarketplaceTheme
        schema = MarketplaceTheme()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_id}", """{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}]}""", serverType="partner", theme_id=theme_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_id}", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceTheme
            schema = MarketplaceTheme()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for submitOrganizationTheme")
                print(e)

        return response
    
    async def deleteOrganizationTheme(self, theme_id=None, request_headers:Dict={}):
        """Remove a theme from partner server organizations.
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.deleteOrganizationTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_id}", """{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string","example":"64934032f50a825d1360a4b5"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string","example":"64934032f50a825d1360a4b5"}}]}""", serverType="partner", theme_id=theme_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_id}", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceTheme
            schema = MarketplaceTheme()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteOrganizationTheme")
                print(e)

        return response
    
    async def getLatestVersionOfThemeBySlug(self, slug_name=None, request_headers:Dict={}):
        """Retrieve the most recent version of a theme using its slug.
        :param slug_name : Slug of theme : type string
        """
        payload = {}
        
        if slug_name is not None:
            payload["slug_name"] = slug_name

        # Parameter validation
        schema = ThemeValidator.getLatestVersionOfThemeBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/{slug_name}/latest", """{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"slug_name","in":"path","description":"Slug of theme","required":true,"schema":{"type":"string","example":"emerge"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"slug_name","in":"path","description":"Slug of theme","required":true,"schema":{"type":"string","example":"emerge"}}]}""", serverType="partner", slug_name=slug_name)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/{slug_name}/latest", slug_name=slug_name), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def createNewThemeInOrganization(self, slug=None, body="", request_headers:Dict={}):
        """Add a new theme to partner server organizations.
        :param slug : The slug of the theme. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ThemeValidator.createNewThemeInOrganization()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MarketplaceTheme
        schema = MarketplaceTheme()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme", """{"required":[{"in":"path","name":"organization_id","required":true,"schema":{"type":"string"},"description":"The ID of the organization"}],"optional":[{"name":"slug","in":"query","required":false,"schema":{"type":"string"},"description":"The slug of the theme."}],"query":[{"name":"slug","in":"query","required":false,"schema":{"type":"string"},"description":"The slug of the theme."}],"headers":[],"path":[{"in":"path","name":"organization_id","required":true,"schema":{"type":"string"},"description":"The ID of the organization"}]}""", serverType="partner", slug=slug)
        query_string = await create_query_string(slug=slug)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceTheme
            schema = MarketplaceTheme()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createNewThemeInOrganization")
                print(e)

        return response
    
    async def createExtensionSectionDraft(self, extension_id=None, body="", request_headers:Dict={}):
        """Create a new draft for an extension section within the specified organization.
        :param extension_id : Extension ID : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id

        # Parameter validation
        schema = ThemeValidator.createExtensionSectionDraft()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DraftExtensionSectionRequest
        schema = DraftExtensionSectionRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/extension-section/{extension_id}/draft", """{"required":[{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string","example":"661cc798e51d7b8ea1f75f25"}},{"name":"extension_id","in":"path","description":"Extension ID","required":true,"schema":{"type":"string","example":"64b3dc661a1b16dea7fadc23"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string","example":"661cc798e51d7b8ea1f75f25"}},{"name":"extension_id","in":"path","description":"Extension ID","required":true,"schema":{"type":"string","example":"64b3dc661a1b16dea7fadc23"}}]}""", serverType="partner", extension_id=extension_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/extension-section/{extension_id}/draft", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DraftExtensionSectionResponse
            schema = DraftExtensionSectionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createExtensionSectionDraft")
                print(e)

        return response
    
    async def publishExtensionSections(self, extension_id=None, body="", request_headers:Dict={}):
        """Publish a draft extension section within the specified organization.
        :param extension_id : Extension ID : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id

        # Parameter validation
        schema = ThemeValidator.publishExtensionSections()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PublishExtensionSectionRequest
        schema = PublishExtensionSectionRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/extension-section/{extension_id}/publish", """{"required":[{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string","example":"661cc798e51d7b8ea1f75f25"}},{"name":"extension_id","in":"path","description":"Extension ID","required":true,"schema":{"type":"string","example":"64b3dc661a1b16dea7fadc23"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string","example":"661cc798e51d7b8ea1f75f25"}},{"name":"extension_id","in":"path","description":"Extension ID","required":true,"schema":{"type":"string","example":"64b3dc661a1b16dea7fadc23"}}]}""", serverType="partner", extension_id=extension_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/extension-section/{extension_id}/publish", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PublishExtensionSectionResponse
            schema = PublishExtensionSectionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for publishExtensionSections")
                print(e)

        return response
    
    async def applyExtensionPreview(self, extension_section_id=None, body="", request_headers:Dict={}):
        """Use this API to start a local session for previewing the extension section binding.
        :param extension_section_id : Extension Section ID : type string
        """
        payload = {}
        
        if extension_section_id is not None:
            payload["extension_section_id"] = extension_section_id

        # Parameter validation
        schema = ThemeValidator.applyExtensionPreview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ExtensionPreviewRequest
        schema = ExtensionPreviewRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/extension-section/{extension_section_id}/preview", """{"required":[{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string","example":"5f8d04c12345f8b1234d5678"}},{"name":"extension_section_id","in":"path","description":"Extension Section ID","required":true,"schema":{"type":"string","example":"60b8d7e54f4d2e7b55c4d013"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string","example":"5f8d04c12345f8b1234d5678"}},{"name":"extension_section_id","in":"path","description":"Extension Section ID","required":true,"schema":{"type":"string","example":"60b8d7e54f4d2e7b55c4d013"}}]}""", serverType="partner", extension_section_id=extension_section_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/extension-section/{extension_section_id}/preview", extension_section_id=extension_section_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ExtensionPreviewResponse
            schema = ExtensionPreviewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for applyExtensionPreview")
                print(e)

        return response
    
    async def removeExtensionPreview(self, extension_section_id=None, body="", request_headers:Dict={}):
        """Use this API to close a local session for previewing the extension section binding
        :param extension_section_id : Extension Section ID : type string
        """
        payload = {}
        
        if extension_section_id is not None:
            payload["extension_section_id"] = extension_section_id

        # Parameter validation
        schema = ThemeValidator.removeExtensionPreview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ExtensionPreviewRequest
        schema = ExtensionPreviewRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/extension-section/{extension_section_id}/preview", """{"required":[{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string","example":"5f8d04c12345f8b1234d5678"}},{"name":"extension_section_id","in":"path","description":"Extension Section ID","required":true,"schema":{"type":"string","example":"60b8d7e54f4d2e7b55c4d013"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string","example":"5f8d04c12345f8b1234d5678"}},{"name":"extension_section_id","in":"path","description":"Extension Section ID","required":true,"schema":{"type":"string","example":"60b8d7e54f4d2e7b55c4d013"}}]}""", serverType="partner", extension_section_id=extension_section_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/extension-section/{extension_section_id}/preview", extension_section_id=extension_section_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ExtensionPreviewResponse
            schema = ExtensionPreviewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeExtensionPreview")
                print(e)

        return response
    
    async def getThemeRejectionReasons(self, theme_id=None, request_headers:Dict={}):
        """Retrieve reasons for the rejection of themes within partner server organizations.
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id

        # Parameter validation
        schema = ThemeValidator.getThemeRejectionReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_id}/reasons", """{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string","example":"6492e223f50a821de260a481"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string","example":"6492e223f50a821de260a481"}}]}""", serverType="partner", theme_id=theme_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_id}/reasons", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemeRejectionReasons
            schema = ThemeRejectionReasons()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getThemeRejectionReasons")
                print(e)

        return response
    
    async def getThemeVersions(self, theme_slug=None, page_size=None, page_no=None, request_headers:Dict={}):
        """Retrieve a list of versions available for a theme within partner server organizations.
        :param theme_slug : The slug of the theme. : type string
        :param page_size : The number of items to return per page. : type integer
        :param page_no : The page number to return. : type integer
        """
        payload = {}
        
        if theme_slug is not None:
            payload["theme_slug"] = theme_slug
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no

        # Parameter validation
        schema = ThemeValidator.getThemeVersions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_slug}/versions", """{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization.","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_slug","in":"path","description":"The slug of the theme.","required":true,"schema":{"type":"string","example":"manrge"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to return per page.","required":false,"schema":{"type":"integer","example":10}},{"name":"page_no","in":"query","description":"The page number to return.","required":false,"schema":{"type":"integer","example":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to return per page.","required":false,"schema":{"type":"integer","example":10}},{"name":"page_no","in":"query","description":"The page number to return.","required":false,"schema":{"type":"integer","example":1}}],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization.","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_slug","in":"path","description":"The slug of the theme.","required":true,"schema":{"type":"string","example":"manrge"}}]}""", serverType="partner", theme_slug=theme_slug, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(page_size=page_size, page_no=page_no)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/theme/{theme_slug}/versions", theme_slug=theme_slug, page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceThemeSchema
            schema = MarketplaceThemeSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getThemeVersions")
                print(e)

        return response
    
    async def createTheme(self, company_id=None, application_id=None, body="", request_headers:Dict={}):
        """Themes improve the look and appearance of a website. Use this API to create a theme.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id

        # Parameter validation
        schema = ThemeValidator.createTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateNewTheme
        schema = CreateNewTheme()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", serverType="partner", company_id=company_id, application_id=application_id, )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/theme/v1.0/organization/{self._conf.organizationId}/company/{company_id}/application/{application_id}", company_id=company_id, application_id=application_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createTheme")
                print(e)

        return response
    