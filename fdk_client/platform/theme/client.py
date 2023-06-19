

"""Theme Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import ThemeValidator

class Theme:
    def __init__(self, config):
        self._conf = config

    
    async def getCompanyLevelThemes(self, ):
        """Retrieve a list of themes available for a specific company.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getCompanyLevelThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/themes", """{"required":[{"name":"company_id","in":"path","description":"The ID of the company to retrieve the themes associated with it.","required":true,"schema":{"type":"integer","example":17426}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"The ID of the company to retrieve the themes associated with it.","required":true,"schema":{"type":"integer","example":17426}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/themes", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        return response
    
    async def addMarketplaceThemeToCompany(self, body=""):
        """Add a marketplace theme to a company by providing the theme ID and company ID.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.addMarketplaceThemeToCompany()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ThemeReq
        schema = ThemeReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}", """{"required":[{"name":"company_id","in":"path","description":"The ID of the company to apply the theme to.","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"The ID of the company to apply the theme to.","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemeSchema
            schema = ThemeSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addMarketplaceThemeToCompany")
                print(e)

        

        return response
    
    async def deleteCompanyTheme(self, theme_id=None):
        """Delete a specific theme for a company by providing the company ID and theme ID.
        :param theme_id : The ID of the theme. : type string
        """
        payload = {}
        
        if theme_id is not None:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.deleteCompanyTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v2.0/company/{self._conf.companyId}/{theme_id}", """{"required":[{"in":"path","name":"company_id","schema":{"type":"integer"},"required":true,"description":"The ID of the company."},{"in":"path","name":"theme_id","schema":{"type":"string"},"required":true,"description":"The ID of the theme."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","schema":{"type":"integer"},"required":true,"description":"The ID of the company."},{"in":"path","name":"theme_id","schema":{"type":"string"},"required":true,"description":"The ID of the theme."}]}""", theme_id=theme_id)
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
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/theme/v2.0/company/{self._conf.companyId}/{theme_id}", theme_id=theme_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ThemeSchema
            schema = ThemeSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCompanyTheme")
                print(e)

        

        return response
    

