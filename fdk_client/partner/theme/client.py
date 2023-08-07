

"""Theme Partner Client"""

from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import ThemeValidator

class Theme:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getAllPages": "/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/page",
            "createPage": "/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/page",
            "updateMultiplePages": "/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/page",
            "getPage": "/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}",
            "updatePage": "/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}",
            "deletePage": "/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}",
            "getApplicationThemes": "/service/partner/theme/v2.0/organization/{organization_id}/company/{company_id}/application/{application_id}/themes",
            "getThemeById": "/service/partner/theme/v2.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}",
            "updateTheme": "/service/partner/theme/v2.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}",
            "deleteTheme": "/service/partner/theme/v2.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}",
            "getOrganizationThemes": "/service/partner/theme/v1.0/organization/{organization_id}/themes",
            "getOrganizationThemeDetails": "/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_id}",
            "updateDraftTheme": "/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_id}",
            "submitOrganizationTheme": "/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_id}",
            "deleteOrganizationTheme": "/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_id}",
            "getLatestVersionOfThemeBySlug": "/service/partner/theme/v1.0/organization/{organization_id}/{slug_name}/latest",
            "createNewThemeInOrganization": "/service/partner/theme/v1.0/organization/{organization_id}/theme",
            "getThemeRejectionReasons": "/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_id}/reasons",
            "getThemeVersions": "/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_slug}/versions"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getAllPages(self, company_id=None, application_id=None, theme_id=None, organization_id=None, body=""):
        """Use this API to retrieve all the available pages of a theme by its ID.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme to be retrieved : type string
        :param organization_id : Organization ID : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        
        if application_id is not None:
            payload["application_id"] = application_id
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        # Parameter validation
        schema = ThemeValidator.getAllPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAllPages"], proccessed_params="""{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAllPages"]).netloc, "get", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/page", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AllAvailablePageSchema
            schema = AllAvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllPages")
                print(e)

        

        return response
    
    async def createPage(self, company_id=None, application_id=None, theme_id=None, organization_id=None, body=""):
        """Use this API to create a page for a theme by its ID.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme : type string
        :param organization_id : Organization ID : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        
        if application_id is not None:
            payload["application_id"] = application_id
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        # Parameter validation
        schema = ThemeValidator.createPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AvailablePageSchema
        schema = AvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createPage"], proccessed_params="""{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["createPage"]).netloc, "post", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/page", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPage")
                print(e)

        

        return response
    
    async def updateMultiplePages(self, company_id=None, application_id=None, theme_id=None, organization_id=None, body=""):
        """Use this API to update multiple pages of a theme by its ID.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme to be retrieved : type string
        :param organization_id : Organization ID : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        
        if application_id is not None:
            payload["application_id"] = application_id
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        # Parameter validation
        schema = ThemeValidator.updateMultiplePages()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AllAvailablePageSchema
        schema = AllAvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateMultiplePages"], proccessed_params="""{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateMultiplePages"]).netloc, "put", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/page", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AllAvailablePageSchema
            schema = AllAvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateMultiplePages")
                print(e)

        

        return response
    
    async def getPage(self, company_id=None, application_id=None, theme_id=None, page_value=None, organization_id=None, body=""):
        """Use this API to retrieve a page of a theme.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme to be retrieved : type string
        :param page_value : Value of the page to be retrieved : type string
        :param organization_id : Organization ID : type string
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
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        # Parameter validation
        schema = ThemeValidator.getPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPage"], proccessed_params="""{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, organization_id=organization_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, organization_id=organization_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPage"]).netloc, "get", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, organization_id=organization_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPage")
                print(e)

        

        return response
    
    async def updatePage(self, company_id=None, application_id=None, theme_id=None, page_value=None, organization_id=None, body=""):
        """Use this API to update a page for a theme by its ID.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        :param organization_id : Organization ID : type string
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
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        # Parameter validation
        schema = ThemeValidator.updatePage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AvailablePageSchema
        schema = AvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updatePage"], proccessed_params="""{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, organization_id=organization_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, organization_id=organization_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updatePage"]).netloc, "put", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, organization_id=organization_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePage")
                print(e)

        

        return response
    
    async def deletePage(self, company_id=None, application_id=None, theme_id=None, page_value=None, organization_id=None, body=""):
        """Use this API to delete a page for a theme by its ID and page_value.
        :param company_id : Company ID : type integer
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        :param organization_id : Organization ID : type string
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
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        # Parameter validation
        schema = ThemeValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deletePage"], proccessed_params="""{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"integer","example":19243}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, organization_id=organization_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, organization_id=organization_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deletePage"]).netloc, "delete", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value, organization_id=organization_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AvailablePageSchema
            schema = AvailablePageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deletePage")
                print(e)

        

        return response
    
    async def getApplicationThemes(self, company_id=None, application_id=None, organization_id=None, body=""):
        """Use this API to get list of theme
        :param company_id : The ID of the company : type integer
        :param application_id : The ID of the application : type string
        :param organization_id : Organization ID : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        
        if application_id is not None:
            payload["application_id"] = application_id
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        # Parameter validation
        schema = ThemeValidator.getApplicationThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getApplicationThemes"], proccessed_params="""{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer"},"examples":{"example1":{"summary":"Example 1 - Company ID","value":19243},"example2":{"summary":"Example 2 - Company ID","value":98765}}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string"},"examples":{"example1":{"summary":"Example 1 - Application ID","value":"6487ea376e1442284917c44e"},"example2":{"summary":"Example 2 - Application ID","value":"7487ea376e1442284917c44e"}}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer"},"examples":{"example1":{"summary":"Example 1 - Company ID","value":19243},"example2":{"summary":"Example 2 - Company ID","value":98765}}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string"},"examples":{"example1":{"summary":"Example 1 - Application ID","value":"6487ea376e1442284917c44e"},"example2":{"summary":"Example 2 - Application ID","value":"7487ea376e1442284917c44e"}}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", company_id=company_id, application_id=application_id, organization_id=organization_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, organization_id=organization_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getApplicationThemes"]).netloc, "get", await create_url_without_domain("/service/partner/theme/v2.0/organization/{organization_id}/company/{company_id}/application/{application_id}/themes", company_id=company_id, application_id=application_id, organization_id=organization_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        return response
    
    async def getThemeById(self, company_id=None, application_id=None, theme_id=None, organization_id=None, body=""):
        """Use this API to get theme details
        :param company_id : The ID of the company : type integer
        :param application_id : The ID of the application : type string
        :param theme_id : The ID of the theme : type string
        :param organization_id : Organization ID : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        
        if application_id is not None:
            payload["application_id"] = application_id
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        # Parameter validation
        schema = ThemeValidator.getThemeById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getThemeById"], proccessed_params="""{"required":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"64be4423bc7b28003211322e"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"The ID of the company","schema":{"type":"integer","example":19243}},{"in":"path","name":"application_id","required":true,"description":"The ID of the application","schema":{"type":"string","example":"6487ea376e1442284917c44e"}},{"in":"path","name":"theme_id","required":true,"description":"The ID of the theme","schema":{"type":"string","example":"64be4423bc7b28003211322e"}},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getThemeById"]).netloc, "get", await create_url_without_domain("/service/partner/theme/v2.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getThemeById")
                print(e)

        

        return response
    
    async def updateTheme(self, company_id=None, application_id=None, theme_id=None, organization_id=None, body=""):
        """Update theme for a specific company and application
        :param company_id : The ID of the company. : type integer
        :param application_id : The ID of the application. : type string
        :param theme_id : The ID of the theme. : type string
        :param organization_id : Organization ID : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        
        if application_id is not None:
            payload["application_id"] = application_id
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        # Parameter validation
        schema = ThemeValidator.updateTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateThemeRequestBody
        schema = UpdateThemeRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateTheme"], proccessed_params="""{"required":[{"in":"path","name":"company_id","schema":{"type":"integer","example":19243},"required":true,"description":"The ID of the company."},{"in":"path","name":"application_id","schema":{"type":"string","example":"6487ea376e1442284917c44e"},"required":true,"description":"The ID of the application."},{"in":"path","name":"theme_id","schema":{"type":"string","example":"64be4423bc7b28003211322e"},"required":true,"description":"The ID of the theme."},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","schema":{"type":"integer","example":19243},"required":true,"description":"The ID of the company."},{"in":"path","name":"application_id","schema":{"type":"string","example":"6487ea376e1442284917c44e"},"required":true,"description":"The ID of the application."},{"in":"path","name":"theme_id","schema":{"type":"string","example":"64be4423bc7b28003211322e"},"required":true,"description":"The ID of the theme."},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateTheme"]).netloc, "put", await create_url_without_domain("/service/partner/theme/v2.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateTheme")
                print(e)

        

        return response
    
    async def deleteTheme(self, company_id=None, application_id=None, theme_id=None, organization_id=None, body=""):
        """This endpoint is used to delete a theme from the specified company and application.
        :param company_id : The ID of the company. : type integer
        :param application_id : The ID of the application. : type string
        :param theme_id : The ID of the theme to be deleted. : type string
        :param organization_id : Organization ID : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        
        if application_id is not None:
            payload["application_id"] = application_id
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        # Parameter validation
        schema = ThemeValidator.deleteTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteTheme"], proccessed_params="""{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"name":"theme_id","in":"path","required":true,"schema":{"type":"string","example":"64be4423bc7b28003211322e"},"description":"The ID of the theme to be deleted."},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","example":19243},"description":"The ID of the company."},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","example":"6487ea376e1442284917c44e"},"description":"The ID of the application."},{"name":"theme_id","in":"path","required":true,"schema":{"type":"string","example":"64be4423bc7b28003211322e"},"description":"The ID of the theme to be deleted."},{"name":"organization_id","in":"path","description":"Organization ID","required":true,"schema":{"type":"string"}}]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deleteTheme"]).netloc, "delete", await create_url_without_domain("/service/partner/theme/v2.0/organization/{organization_id}/company/{company_id}/application/{application_id}/{theme_id}", company_id=company_id, application_id=application_id, theme_id=theme_id, organization_id=organization_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemesSchema
            schema = ThemesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteTheme")
                print(e)

        

        return response
    
    async def getOrganizationThemes(self, organization_id=None, status=None, page_size=None, page_no=None, body=""):
        """Get organization's themes
        :param organization_id : Id of your organization : type string
        :param status : The status of the theme : type string
        :param page_size : Number of themes per page : type integer
        :param page_no : Page number to retrieve : type integer
        """
        payload = {}
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        if status is not None:
            payload["status"] = status
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        # Parameter validation
        schema = ThemeValidator.getOrganizationThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrganizationThemes"], proccessed_params="""{"required":[{"name":"organization_id","in":"path","description":"Id of your organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"}],"optional":[{"name":"status","in":"query","description":"The status of the theme","required":false,"schema":{"type":"string","enum":["published","submitted","in-review","rejected"]},"example":"published"},{"name":"page_size","in":"query","description":"Number of themes per page","required":false,"schema":{"type":"integer","example":6}},{"name":"page_no","in":"query","description":"Page number to retrieve","required":false,"schema":{"type":"integer","example":2}}],"query":[{"name":"status","in":"query","description":"The status of the theme","required":false,"schema":{"type":"string","enum":["published","submitted","in-review","rejected"]},"example":"published"},{"name":"page_size","in":"query","description":"Number of themes per page","required":false,"schema":{"type":"integer","example":6}},{"name":"page_no","in":"query","description":"Page number to retrieve","required":false,"schema":{"type":"integer","example":2}}],"headers":[],"path":[{"name":"organization_id","in":"path","description":"Id of your organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"}]}""", organization_id=organization_id, status=status, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(organization_id=organization_id, status=status, page_size=page_size, page_no=page_no)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrganizationThemes"]).netloc, "get", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/themes", organization_id=organization_id, status=status, page_size=page_size, page_no=page_no), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceThemeSchema
            schema = MarketplaceThemeSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrganizationThemes")
                print(e)

        

        return response
    
    async def getOrganizationThemeDetails(self, organization_id=None, theme_id=None, body=""):
        """Fetches the theme details for a specific organization and theme ID
        :param organization_id : The ID of the organization : type string
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        # Parameter validation
        schema = ThemeValidator.getOrganizationThemeDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrganizationThemeDetails"], proccessed_params="""{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}]}""", organization_id=organization_id, theme_id=theme_id)
        query_string = await create_query_string(organization_id=organization_id, theme_id=theme_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrganizationThemeDetails"]).netloc, "get", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_id}", organization_id=organization_id, theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceTheme
            schema = MarketplaceTheme()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrganizationThemeDetails")
                print(e)

        

        return response
    
    async def updateDraftTheme(self, organization_id=None, theme_id=None, body=""):
        """Update theme draft/submitted
        :param organization_id : The ID of the organization : type string
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        # Parameter validation
        schema = ThemeValidator.updateDraftTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MarketplaceTheme
        schema = MarketplaceTheme()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateDraftTheme"], proccessed_params="""{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}]}""", organization_id=organization_id, theme_id=theme_id)
        query_string = await create_query_string(organization_id=organization_id, theme_id=theme_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateDraftTheme"]).netloc, "patch", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_id}", organization_id=organization_id, theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceTheme
            schema = MarketplaceTheme()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateDraftTheme")
                print(e)

        

        return response
    
    async def submitOrganizationTheme(self, organization_id=None, theme_id=None, body=""):
        """Use this api to Submit a theme
        :param organization_id : The ID of the organization : type string
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        # Parameter validation
        schema = ThemeValidator.submitOrganizationTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MarketplaceTheme
        schema = MarketplaceTheme()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["submitOrganizationTheme"], proccessed_params="""{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string"},"example":"60d1de982ee3683a0a6322c3"},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string"},"example":"64913008bb9d3364f4cba968"}]}""", organization_id=organization_id, theme_id=theme_id)
        query_string = await create_query_string(organization_id=organization_id, theme_id=theme_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["submitOrganizationTheme"]).netloc, "put", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_id}", organization_id=organization_id, theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceTheme
            schema = MarketplaceTheme()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for submitOrganizationTheme")
                print(e)

        

        return response
    
    async def deleteOrganizationTheme(self, organization_id=None, theme_id=None, body=""):
        """This endpoint allows you to delete a theme by providing the organization and theme IDs.
        :param organization_id : The ID of the organization : type string
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        # Parameter validation
        schema = ThemeValidator.deleteOrganizationTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteOrganizationTheme"], proccessed_params="""{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string","example":"64934032f50a825d1360a4b5"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string","example":"64934032f50a825d1360a4b5"}}]}""", organization_id=organization_id, theme_id=theme_id)
        query_string = await create_query_string(organization_id=organization_id, theme_id=theme_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deleteOrganizationTheme"]).netloc, "delete", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_id}", organization_id=organization_id, theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceTheme
            schema = MarketplaceTheme()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteOrganizationTheme")
                print(e)

        

        return response
    
    async def getLatestVersionOfThemeBySlug(self, organization_id=None, slug_name=None, body=""):
        """Use this api to get latest version of specified theme
        :param organization_id : The ID of the organization : type string
        :param slug_name : Slug of theme : type string
        """
        payload = {}
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        if slug_name is not None:
            payload["slug_name"] = slug_name
        
        # Parameter validation
        schema = ThemeValidator.getLatestVersionOfThemeBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLatestVersionOfThemeBySlug"], proccessed_params="""{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"slug_name","in":"path","description":"Slug of theme","required":true,"schema":{"type":"string","example":"emerge"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"slug_name","in":"path","description":"Slug of theme","required":true,"schema":{"type":"string","example":"emerge"}}]}""", organization_id=organization_id, slug_name=slug_name)
        query_string = await create_query_string(organization_id=organization_id, slug_name=slug_name)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLatestVersionOfThemeBySlug"]).netloc, "get", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/{slug_name}/latest", organization_id=organization_id, slug_name=slug_name), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        return response
    
    async def createNewThemeInOrganization(self, organization_id=None, slug=None, body=""):
        """Use this api to create a new theme for the organization
        :param organization_id : The ID of the organization : type string
        :param slug : The slug of the theme. : type string
        """
        payload = {}
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        if slug is not None:
            payload["slug"] = slug
        
        # Parameter validation
        schema = ThemeValidator.createNewThemeInOrganization()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MarketplaceTheme
        schema = MarketplaceTheme()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createNewThemeInOrganization"], proccessed_params="""{"required":[{"in":"path","name":"organization_id","required":true,"schema":{"type":"string"},"description":"The ID of the organization"}],"optional":[{"name":"slug","in":"query","required":false,"schema":{"type":"string"},"description":"The slug of the theme."}],"query":[{"name":"slug","in":"query","required":false,"schema":{"type":"string"},"description":"The slug of the theme."}],"headers":[],"path":[{"in":"path","name":"organization_id","required":true,"schema":{"type":"string"},"description":"The ID of the organization"}]}""", organization_id=organization_id, slug=slug)
        query_string = await create_query_string(organization_id=organization_id, slug=slug)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["createNewThemeInOrganization"]).netloc, "post", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/theme", organization_id=organization_id, slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceTheme
            schema = MarketplaceTheme()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createNewThemeInOrganization")
                print(e)

        

        return response
    
    async def getThemeRejectionReasons(self, organization_id=None, theme_id=None, body=""):
        """Use this api to get theme rejection reasons
        :param organization_id : The ID of the organization : type string
        :param theme_id : The ID of the theme : type string
        """
        payload = {}
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        
        # Parameter validation
        schema = ThemeValidator.getThemeRejectionReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getThemeRejectionReasons"], proccessed_params="""{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string","example":"6492e223f50a821de260a481"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_id","in":"path","description":"The ID of the theme","required":true,"schema":{"type":"string","example":"6492e223f50a821de260a481"}}]}""", organization_id=organization_id, theme_id=theme_id)
        query_string = await create_query_string(organization_id=organization_id, theme_id=theme_id)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getThemeRejectionReasons"]).netloc, "get", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_id}/reasons", organization_id=organization_id, theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemeRejectionReasons
            schema = ThemeRejectionReasons()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getThemeRejectionReasons")
                print(e)

        

        return response
    
    async def getThemeVersions(self, organization_id=None, theme_slug=None, page_size=None, page_no=None, body=""):
        """Retrieve a list of theme versions for a specific theme in an organization.
        :param organization_id : The ID of the organization. : type string
        :param theme_slug : The slug of the theme. : type string
        :param page_size : The number of items to return per page. : type integer
        :param page_no : The page number to return. : type integer
        """
        payload = {}
        
        if organization_id is not None:
            payload["organization_id"] = organization_id
        
        if theme_slug is not None:
            payload["theme_slug"] = theme_slug
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        # Parameter validation
        schema = ThemeValidator.getThemeVersions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getThemeVersions"], proccessed_params="""{"required":[{"name":"organization_id","in":"path","description":"The ID of the organization.","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_slug","in":"path","description":"The slug of the theme.","required":true,"schema":{"type":"string","example":"manrge"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to return per page.","required":false,"schema":{"type":"integer","example":10}},{"name":"page_no","in":"query","description":"The page number to return.","required":false,"schema":{"type":"integer","example":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to return per page.","required":false,"schema":{"type":"integer","example":10}},{"name":"page_no","in":"query","description":"The page number to return.","required":false,"schema":{"type":"integer","example":1}}],"headers":[],"path":[{"name":"organization_id","in":"path","description":"The ID of the organization.","required":true,"schema":{"type":"string","example":"60d1de982ee3683a0a6322c3"}},{"name":"theme_slug","in":"path","description":"The slug of the theme.","required":true,"schema":{"type":"string","example":"manrge"}}]}""", organization_id=organization_id, theme_slug=theme_slug, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(organization_id=organization_id, theme_slug=theme_slug, page_size=page_size, page_no=page_no)
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getThemeVersions"]).netloc, "get", await create_url_without_domain("/service/partner/theme/v1.0/organization/{organization_id}/theme/{theme_slug}/versions", organization_id=organization_id, theme_slug=theme_slug, page_size=page_size, page_no=page_no), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import MarketplaceThemeSchema
            schema = MarketplaceThemeSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getThemeVersions")
                print(e)

        

        return response
    

