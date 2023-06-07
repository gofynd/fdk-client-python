

"""Catalog Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import CatalogValidator

class Catalog:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId

    
    async def updateSearchKeywords(self, id=None, body=""):
        """Thist API allows you to update the search keyword configuration by their ID.
        :param id : A `id` is a unique identifier for a specific keyword search configuration. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateSearchKeywords()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchKeyword
        schema = CreateSearchKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsData
            schema = GetSearchWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSearchKeywords")
                print(e)

        

        return response
    
    async def deleteSearchKeywords(self, id=None):
        """This API allows you to delete a custom keyword mapping by their ID within an application. Returns an object that tells whether the keywords was deleted successfully
        :param id : A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteResponse
            schema = DeleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSearchKeywords")
                print(e)

        

        return response
    
    async def getSearchKeywords(self, id=None):
        """The API allows you to get the details of a words by its `id`. If successful, returns a Collection resource in the response body specified in `GetSearchWordsDetailResponseSchema`
        :param id : A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsData
            schema = GetSearchWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSearchKeywords")
                print(e)

        

        return response
    
    async def getAllSearchKeyword(self, is_active=None, q=None):
        """Custom Search Keyword allows you to map conditions with keywords to give you the ultimate results. This API allows you to list all the custom keyword search configured for the application.
        :param is_active : Filter the custom keyword listing by their active status. : type boolean
        :param q : It is to search by keywords. : type string
        """
        payload = {}
        
        if is_active is not None:
            payload["is_active"] = is_active
        
        if q is not None:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getAllSearchKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}],"optional":[{"in":"query","name":"is_active","description":"Filter the custom keyword listing by their active status.","schema":{"type":"boolean"},"required":false,"example":false},{"in":"query","name":"q","description":"It is to search by keywords.","schema":{"type":"string"},"example":"mobile phones","required":false}],"query":[{"in":"query","name":"is_active","description":"Filter the custom keyword listing by their active status.","schema":{"type":"boolean"},"required":false,"example":false},{"in":"query","name":"q","description":"It is to search by keywords.","schema":{"type":"string"},"example":"mobile phones","required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}]}""", is_active=is_active, q=q)
        query_string = await create_query_string(is_active=is_active, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", is_active=is_active, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsResponse
            schema = GetSearchWordsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllSearchKeyword")
                print(e)

        

        return response
    
    async def createCustomKeyword(self, body=""):
        """Custom Search Keyword allows you to map conditions with keywords to give you the ultimate results. This API allows you to add a rule for the custom keyword to a search behaviour for an application. See `CreateSearchKeywordSchema` for the list of attributes needed to create a mapping and /collections/query-options for the available options to create a rule. On successful request, returns a paginated list of collections specified in `CreateSearchKeywordSchema`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCustomKeyword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchKeyword
        schema = CreateSearchKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsData
            schema = GetSearchWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomKeyword")
                print(e)

        

        return response
    
    async def updateAutocompleteKeyword(self, id=None, body=""):
        """Autocomplete keywords configuration help you to extend and customize the behaviour of autocomplete search results in Fynd Platform. This API allows you to update a mapping by it's `id`.
        :param id : A `id` is a unique identifier for a specific autocomplete keyword map. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateAutocompleteKeyword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetAutocompleteWordsData
        schema = GetAutocompleteWordsData()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific autocomplete keyword map. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific autocomplete keyword map. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateAutocompleteWordData
            schema = UpdateAutocompleteWordData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAutocompleteKeyword")
                print(e)

        

        return response
    
    async def deleteAutocompleteKeyword(self, id=None):
        """Autocomplete keywords configuration help you to extend and customize the behaviour of autocomplete search results in Fynd Platform. This API allows you to delete a keywords by it's `id`.
        :param id : A `id` is a unique identifier for a specific autocomplete keyword map. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteAutocompleteKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific autocomplete keyword map. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific autocomplete keyword map. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteResponse
            schema = DeleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAutocompleteKeyword")
                print(e)

        

        return response
    
    async def getAutocompleteKeywordDetail(self, id=None):
        """Autocomplete keywords configuration help you to extend and customize the behaviour of autocomplete search results in Fynd Platform. This API allows you to get the details of a words by its `id`.
        :param id : A `id` is a unique identifier for a specific autocomplete keyword map. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getAutocompleteKeywordDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific autocomplete keyword map. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific autocomplete keyword map. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAutocompleteWordsData
            schema = GetAutocompleteWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAutocompleteKeywordDetail")
                print(e)

        

        return response
    
    async def getAutocompleteConfig(self, ):
        """The custom autocomplete keyword allows you to map conditions with keywords to give you the autocomplete results. This API allows you to list all the autocomplete keyword configured for an application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAutocompleteConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAutocompleteWordsResponse
            schema = GetAutocompleteWordsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAutocompleteConfig")
                print(e)

        

        return response
    
    async def createCustomAutocompleteRule(self, body=""):
        """Autocomplete keywords configuration help you to extend and customize the behaviour of autocomplete search results in Fynd Platform. This API allows to create the auto-complete configuration for the application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCustomAutocompleteRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateAutocompleteKeyword
        schema = CreateAutocompleteKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAutocompleteWordsData
            schema = GetAutocompleteWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomAutocompleteRule")
                print(e)

        

        return response
    
    async def listSearchRerankConfig(self, is_active=None, q=None):
        """Search Reranking allows you rank and boost the search of the keywords and products in the product listing. This API allows you to list all the search re-ranking configured for the application.
        :param is_active : Filter the custom keyword listing by their active status. : type boolean
        :param q : It is to search by keywords. : type string
        """
        payload = {}
        
        if is_active is not None:
            payload["is_active"] = is_active
        
        if q is not None:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.listSearchRerankConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}],"optional":[{"in":"query","name":"is_active","description":"Filter the custom keyword listing by their active status.","schema":{"type":"boolean"},"required":false,"example":false},{"in":"query","name":"q","description":"It is to search by keywords.","schema":{"type":"string"},"example":"mobile phone","required":false}],"query":[{"in":"query","name":"is_active","description":"Filter the custom keyword listing by their active status.","schema":{"type":"boolean"},"required":false,"example":false},{"in":"query","name":"q","description":"It is to search by keywords.","schema":{"type":"string"},"example":"mobile phone","required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}]}""", is_active=is_active, q=q)
        query_string = await create_query_string(is_active=is_active, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/", is_active=is_active, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SearchRerankListing
            schema = SearchRerankListing()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for listSearchRerankConfig")
                print(e)

        

        return response
    
    async def createSearchRerankingConfig(self, body=""):
        """Search Reranking allows you rank and boost the search of the keywords and products in the product listing. Create a Custom Search Reranking rule. This API allows you to create a custom search re rank rule to re-rank the search in the listing of an application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createSearchRerankingConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchReranking
        schema = CreateSearchReranking()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SearchRerankingModel
            schema = SearchRerankingModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSearchRerankingConfig")
                print(e)

        

        return response
    
    async def updateSearchRerankConfig(self, id=None, body=""):
        """Search Reranking allows you rank and boost the search of the keywords and products in the product listing. This API allows you to update the search re-ranking configured for the application.
        :param id : A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateSearchRerankConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchReranking
        schema = CreateSearchReranking()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SearchRerankingModel
            schema = SearchRerankingModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSearchRerankConfig")
                print(e)

        

        return response
    
    async def deleteSearchRerankConfig(self, id=None):
        """Search Reranking allows you rank and boost the search of the keywords and products in the product listing. This API allows you to delete a search re-ranking configured for the application.
        :param id : A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteSearchRerankConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteRerankResponse
            schema = DeleteRerankResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSearchRerankConfig")
                print(e)

        

        return response
    
    async def getSearchRerankingConfig(self, id=None):
        """Search Reranking allows you rank and boost the search of the keywords and products in the product listing. This API allows you to get the data of a search re-ranking configured for the application by their ID.
        :param id : A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getSearchRerankingConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1,"example":1},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24,"example":"000000000000000000000001"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a specific keyword search configuration. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string","example":"602fa1e9a596ce349563f6b9"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SearchRerankingModel
            schema = SearchRerankingModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSearchRerankingConfig")
                print(e)

        

        return response
    
    async def getAppProduct(self, item_id=None):
        """Products are the core resource of an application. If successful, returns a Company Application Product resource in the response body depending upon filter sent.
        :param item_id : product id for a particular product. : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        

        # Parameter validation
        schema = CatalogValidator.getAppProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"product id for a particular product.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"product id for a particular product.","schema":{"type":"string"},"required":true}]}""", item_id=item_id)
        query_string = await create_query_string(item_id=item_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", item_id=item_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import OwnerAppItemResponse
            schema = OwnerAppItemResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppProduct")
                print(e)

        

        return response
    
    async def updateAppProduct(self, item_id=None, body=""):
        """This API helps to update data associated to a item custom meta.
        :param item_id : product id for which the custom_meta is associated. : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        

        # Parameter validation
        schema = CatalogValidator.updateAppProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationItemMeta
        schema = ApplicationItemMeta()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to custom meta.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_meta is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"product id for which the custom_meta is associated.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to custom meta.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_meta is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"product id for which the custom_meta is associated.","schema":{"type":"string"},"required":true}]}""", item_id=item_id)
        query_string = await create_query_string(item_id=item_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", item_id=item_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppProduct")
                print(e)

        

        return response
    
    async def getConfigurationMetadata(self, config_type=None, template_slug=None):
        """Get the configuraion metadata details for catalog.
        :param config_type : A `config_type` is an identifier that defines a specific type of configuration. : type string
        :param template_slug : Get configuration list filtered by `template_slug` string. This is for the details and comparision groups. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        
        if template_slug is not None:
            payload["template_slug"] = template_slug
        

        # Parameter validation
        schema = CatalogValidator.getConfigurationMetadata()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/metadata/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is an identifier that defines a specific type of configuration.","schema":{"type":"string","enum":["filter","sort","details_groups","comparisons_groups","variant","similar","brands","categories","seller_groups"]},"required":true}],"optional":[{"in":"query","name":"template_slug","description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"template_slug","description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is an identifier that defines a specific type of configuration.","schema":{"type":"string","enum":["filter","sort","details_groups","comparisons_groups","variant","similar","brands","categories","seller_groups"]},"required":true}]}""", config_type=config_type, template_slug=template_slug)
        query_string = await create_query_string(config_type=config_type, template_slug=template_slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/metadata/", config_type=config_type, template_slug=template_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetConfigMetadataResponse
            schema = GetConfigMetadataResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getConfigurationMetadata")
                print(e)

        

        return response
    
    async def getGroupConfigurations(self, config_type=None, page_no=None, page_size=None, search=None, template_slug=None):
        """Get the details of the application configured configurations of group config types.
        :param config_type : A `config_type` is an identifier that defines a specific type of configuration. : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param search : Get configuration list filtered by `search` string. : type string
        :param template_slug : Get configuration list filtered by `template_slug` string. This is for the details and comparision groups. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if search is not None:
            payload["search"] = search
        
        if template_slug is not None:
            payload["template_slug"] = template_slug
        

        # Parameter validation
        schema = CatalogValidator.getGroupConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is an identifier that defines a specific type of configuration.","schema":{"type":"string","enum":["comparisons_groups","details_groups","seller_groups"]},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false},{"in":"query","name":"search","description":"Get configuration list filtered by `search` string.","schema":{"type":"string"},"required":false},{"in":"query","name":"template_slug","description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false},{"in":"query","name":"search","description":"Get configuration list filtered by `search` string.","schema":{"type":"string"},"required":false},{"in":"query","name":"template_slug","description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is an identifier that defines a specific type of configuration.","schema":{"type":"string","enum":["comparisons_groups","details_groups","seller_groups"]},"required":true}]}""", config_type=config_type, page_no=page_no, page_size=page_size, search=search, template_slug=template_slug)
        query_string = await create_query_string(config_type=config_type, page_no=page_no, page_size=page_size, search=search, template_slug=template_slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", config_type=config_type, page_no=page_no, page_size=page_size, search=search, template_slug=template_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetConfigResponse
            schema = GetConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGroupConfigurations")
                print(e)

        

        return response
    
    async def createGroupConfiguration(self, config_type=None, body=""):
        """Create configuration for Group config types.
        :param config_type : A `config_type` is a unique identifier for a particular group configuration type. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        

        # Parameter validation
        schema = CatalogValidator.createGroupConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppConfigurationDetail
        schema = AppConfigurationDetail()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular group configuration type.","schema":{"type":"string","enum":["comparisons_groups","details_groups","seller_groups"]},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular group configuration type.","schema":{"type":"string","enum":["comparisons_groups","details_groups","seller_groups"]},"required":true}]}""", config_type=config_type)
        query_string = await create_query_string(config_type=config_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", config_type=config_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AppConfigurationDetail
            schema = AppConfigurationDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createGroupConfiguration")
                print(e)

        

        return response
    
    async def updateGroupConfiguration(self, config_type=None, group_slug=None, body=""):
        """Update the group configurations for the application.
        :param config_type : A `config_type` is a unique identifier for a particular group configuration type. : type string
        :param group_slug : A `group_slug` is a unique identifier of a particular configuration. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        
        if group_slug is not None:
            payload["group_slug"] = group_slug
        

        # Parameter validation
        schema = CatalogValidator.updateGroupConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppConfigurationDetail
        schema = AppConfigurationDetail()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular group configuration type.","schema":{"type":"string","enum":["comparisons_groups","details_groups","seller_groups"]},"required":true},{"in":"path","name":"group_slug","description":"A `group_slug` is a unique identifier of a particular configuration.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular group configuration type.","schema":{"type":"string","enum":["comparisons_groups","details_groups","seller_groups"]},"required":true},{"in":"path","name":"group_slug","description":"A `group_slug` is a unique identifier of a particular configuration.","schema":{"type":"string"},"required":true}]}""", config_type=config_type, group_slug=group_slug)
        query_string = await create_query_string(config_type=config_type, group_slug=group_slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", config_type=config_type, group_slug=group_slug), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AppConfigurationDetail
            schema = AppConfigurationDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateGroupConfiguration")
                print(e)

        

        return response
    
    async def deleteGroupConfiguration(self, config_type=None, group_slug=None):
        """Delete configuration of the product config type of the application.
        :param config_type : A `config_type` is a unique identifier for a particular group configuration type. : type string
        :param group_slug : A `group_slug` is a unique identifier of a particular configuration. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        
        if group_slug is not None:
            payload["group_slug"] = group_slug
        

        # Parameter validation
        schema = CatalogValidator.deleteGroupConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular group configuration type.","schema":{"type":"string","enum":["comparisons_groups","details_groups","seller_groups"]},"required":true},{"in":"path","name":"group_slug","description":"A `group_slug` is a unique identifier of a particular configuration.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular group configuration type.","schema":{"type":"string","enum":["comparisons_groups","details_groups","seller_groups"]},"required":true},{"in":"path","name":"group_slug","description":"A `group_slug` is a unique identifier of a particular configuration.","schema":{"type":"string"},"required":true}]}""", config_type=config_type, group_slug=group_slug)
        query_string = await create_query_string(config_type=config_type, group_slug=group_slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", config_type=config_type, group_slug=group_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigSuccessResponse
            schema = ConfigSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteGroupConfiguration")
                print(e)

        

        return response
    
    async def getListingConfigurations(self, config_type=None, page_no=None, page_size=None, search=None):
        """Get the details of the application configured configurations of listing config types.
        :param config_type : A `config_type` is an identifier that defines a specific type of configuration. : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param search : Get configuration list filtered by `search` string. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if search is not None:
            payload["search"] = search
        

        # Parameter validation
        schema = CatalogValidator.getListingConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is an identifier that defines a specific type of configuration.","schema":{"type":"string","enum":["filter","sort","brands","categories","variant","similar"]},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false},{"in":"query","name":"search","description":"Get configuration list filtered by `search` string.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false},{"in":"query","name":"search","description":"Get configuration list filtered by `search` string.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is an identifier that defines a specific type of configuration.","schema":{"type":"string","enum":["filter","sort","brands","categories","variant","similar"]},"required":true}]}""", config_type=config_type, page_no=page_no, page_size=page_size, search=search)
        query_string = await create_query_string(config_type=config_type, page_no=page_no, page_size=page_size, search=search)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", config_type=config_type, page_no=page_no, page_size=page_size, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetConfigResponse
            schema = GetConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getListingConfigurations")
                print(e)

        

        return response
    
    async def createListingConfiguration(self, config_type=None, body=""):
        """Add configuration for listing.
        :param config_type : A `config_type` is a unique identifier for a particular listing configuration type. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        

        # Parameter validation
        schema = CatalogValidator.createListingConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppConfigurationsSort
        schema = AppConfigurationsSort()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular listing configuration type.","schema":{"type":"string","enum":["filter","sort","brands","categories","variant","similar"]},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular listing configuration type.","schema":{"type":"string","enum":["filter","sort","brands","categories","variant","similar"]},"required":true}]}""", config_type=config_type)
        query_string = await create_query_string(config_type=config_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", config_type=config_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AppConfigurationsSort
            schema = AppConfigurationsSort()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createListingConfiguration")
                print(e)

        

        return response
    
    async def updateListingConfiguration(self, config_type=None, config_id=None, body=""):
        """Update configuration for listing.
        :param config_type : A `config_type` is a unique identifier for a particular listing configuration type. : type string
        :param config_id : A `config_id` is a unique identifier of a particular configuration. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        
        if config_id is not None:
            payload["config_id"] = config_id
        

        # Parameter validation
        schema = CatalogValidator.updateListingConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppConfigurationsSort
        schema = AppConfigurationsSort()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular listing configuration type.","schema":{"type":"string","enum":["filter","sort","brands","categories","variant","similar"]},"required":true},{"in":"path","name":"config_id","description":"A `config_id` is a unique identifier of a particular configuration.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular listing configuration type.","schema":{"type":"string","enum":["filter","sort","brands","categories","variant","similar"]},"required":true},{"in":"path","name":"config_id","description":"A `config_id` is a unique identifier of a particular configuration.","schema":{"type":"string"},"required":true}]}""", config_type=config_type, config_id=config_id)
        query_string = await create_query_string(config_type=config_type, config_id=config_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", config_type=config_type, config_id=config_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AppConfigurationsSort
            schema = AppConfigurationsSort()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateListingConfiguration")
                print(e)

        

        return response
    
    async def deleteListingConfiguration(self, config_type=None, config_id=None):
        """Delete configuration for listing.
        :param config_type : A `config_type` is a unique identifier for a particular listing configuration type. : type string
        :param config_id : A `config_id` is a unique identifier of a particular configuration. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        
        if config_id is not None:
            payload["config_id"] = config_id
        

        # Parameter validation
        schema = CatalogValidator.deleteListingConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular listing configuration type.","schema":{"type":"string","enum":["filter","sort","brands","categories","variant","similar"]},"required":true},{"in":"path","name":"config_id","description":"A `config_id` is a unique identifier of a particular configuration.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"config_type","description":"A `config_type` is a unique identifier for a particular listing configuration type.","schema":{"type":"string","enum":["filter","sort","brands","categories","variant","similar"]},"required":true},{"in":"path","name":"config_id","description":"A `config_id` is a unique identifier of a particular configuration.","schema":{"type":"string"},"required":true}]}""", config_type=config_type, config_id=config_id)
        query_string = await create_query_string(config_type=config_type, config_id=config_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", config_type=config_type, config_id=config_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigSuccessResponse
            schema = ConfigSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteListingConfiguration")
                print(e)

        

        return response
    
    async def updateAllowSingle(self, body=""):
        """Update allow single flag for filters of the application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateAllowSingle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AllowSingleRequest
        schema = AllowSingleRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/filter/allow_single", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/filter/allow_single", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigSuccessResponse
            schema = ConfigSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAllowSingle")
                print(e)

        

        return response
    
    async def updateDefaultSort(self, body=""):
        """Update the default sort key configuration for the application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateDefaultSort()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DefaultKeyRequest
        schema = DefaultKeyRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/sort/default_key", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/sort/default_key", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigSuccessResponse
            schema = ConfigSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateDefaultSort")
                print(e)

        

        return response
    
    async def getCatalogConfiguration(self, ):
        """configuration meta  details for catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getCatalogConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCatalogConfigurationMetaData
            schema = GetCatalogConfigurationMetaData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCatalogConfiguration")
                print(e)

        

        return response
    
    async def getConfigurations(self, ):
        """configured details for catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAppCatalogConfiguration
            schema = GetAppCatalogConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getConfigurations")
                print(e)

        

        return response
    
    async def createConfigurationProductListing(self, body=""):
        """Add configuration for products & listing.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createConfigurationProductListing()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppConfiguration
        schema = AppConfiguration()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAppCatalogConfiguration
            schema = GetAppCatalogConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createConfigurationProductListing")
                print(e)

        

        return response
    
    async def getConfigurationByType(self, type=None):
        """configured details for catalog.
        :param type : type can be brands, categories etc. : type string
        """
        payload = {}
        
        if type is not None:
            payload["type"] = type
        

        # Parameter validation
        schema = CatalogValidator.getConfigurationByType()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"type","description":"type can be brands, categories etc.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"type","description":"type can be brands, categories etc.","schema":{"type":"string"},"required":true}]}""", type=type)
        query_string = await create_query_string(type=type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", type=type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAppCatalogEntityConfiguration
            schema = GetAppCatalogEntityConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getConfigurationByType")
                print(e)

        

        return response
    
    async def createConfigurationByType(self, type=None, body=""):
        """Add configuration for categories & brands.
        :param type : type can be brands, categories etc. : type string
        """
        payload = {}
        
        if type is not None:
            payload["type"] = type
        

        # Parameter validation
        schema = CatalogValidator.createConfigurationByType()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppConfiguration
        schema = AppConfiguration()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"type","description":"type can be brands, categories etc.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"type","description":"type can be brands, categories etc.","schema":{"type":"string"},"required":true}]}""", type=type)
        query_string = await create_query_string(type=type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAppCatalogConfiguration
            schema = GetAppCatalogConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createConfigurationByType")
                print(e)

        

        return response
    
    async def getQueryFilters(self, f=None, sort_on=None):
        """A Collection allows you to organize your products into hierarchical groups. This API retrieves the query filters that can be used to configure a collection for a specific seller account and sale channel.
        :param f : Filter the products in the collection using key-value pairs. : type string
        :param sort_on : Attribute key on which the products should be sorted. : type string
        """
        payload = {}
        
        if f is not None:
            payload["f"] = f
        
        if sort_on is not None:
            payload["sort_on"] = sort_on
        

        # Parameter validation
        schema = CatalogValidator.getQueryFilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true}],"optional":[{"in":"query","name":"f","description":"Filter the products in the collection using key-value pairs.","schema":{"type":"string"},"examples":{"Multivalued Filter":{"summary":"Multivalued filter","value":"gender:Women||Unisex"},"Range Filter":{"summary":"Range filter","value":"min_price_effective:[99,INR TO 32910,INR]"}},"required":false},{"in":"query","name":"sort_on","description":"Attribute key on which the products should be sorted.","schema":{"type":"string"},"required":false,"example":"popular"}],"query":[{"in":"query","name":"f","description":"Filter the products in the collection using key-value pairs.","schema":{"type":"string"},"examples":{"Multivalued Filter":{"summary":"Multivalued filter","value":"gender:Women||Unisex"},"Range Filter":{"summary":"Range filter","value":"min_price_effective:[99,INR TO 32910,INR]"}},"required":false},{"in":"query","name":"sort_on","description":"Attribute key on which the products should be sorted.","schema":{"type":"string"},"required":false,"example":"popular"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true}]}""", f=f, sort_on=sort_on)
        query_string = await create_query_string(f=f, sort_on=sort_on)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options/", f=f, sort_on=sort_on), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionQueryOptionResponse
            schema = GetCollectionQueryOptionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getQueryFilters")
                print(e)

        

        return response
    
    async def getAllCollections(self, q=None, schedule_status=None, type=None, tag=None, is_active=None, page_no=None, page_size=None):
        """A Collection allows you to organize your products into hierarchical groups. For example, a dress might be in the category _Clothing_, the individual product might also be in the collection _Summer_. On successful request, returns all the collections as specified in `CollectionListingSchema`
        :param q : The query string for searching collections. : type string
        :param schedule_status : Filter collections by their schedule status. : type string
        :param type : It is the type of collection. : type string
        :param tag : Filter the collections by a tag. : type array
        :param is_active : Filter collections by active status. : type boolean
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q
        
        if schedule_status is not None:
            payload["schedule_status"] = schedule_status
        
        if type is not None:
            payload["type"] = type
        
        if tag is not None:
            payload["tag"] = tag
        
        if is_active is not None:
            payload["is_active"] = is_active
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getAllCollections()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true}],"optional":[{"in":"query","name":"q","description":"The query string for searching collections.","schema":{"type":"string"},"example":"flat 10","required":false},{"in":"query","name":"schedule_status","description":"Filter collections by their schedule status.","schema":{"type":"string","enum":["live","upcoming","expired"]},"example":"live","required":false},{"in":"query","name":"type","description":"It is the type of collection.","schema":{"type":"string","enum":["query","items"]},"examples":{"Get all handpick collection":{"summary":"Get all handpick collections.","value":"items"},"Get all basic collection":{"summary":"Get all basic collections.","value":"query"}},"required":false},{"in":"query","name":"tag","description":"Filter the collections by a tag.","schema":{"type":"array","items":{"type":"string"},"example":"flat_10"},"required":false},{"in":"query","name":"is_active","description":"Filter collections by active status.","schema":{"type":"boolean"},"required":false,"example":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","minimum":1},"example":1,"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer","default":12},"example":10,"required":false}],"query":[{"in":"query","name":"q","description":"The query string for searching collections.","schema":{"type":"string"},"example":"flat 10","required":false},{"in":"query","name":"schedule_status","description":"Filter collections by their schedule status.","schema":{"type":"string","enum":["live","upcoming","expired"]},"example":"live","required":false},{"in":"query","name":"type","description":"It is the type of collection.","schema":{"type":"string","enum":["query","items"]},"examples":{"Get all handpick collection":{"summary":"Get all handpick collections.","value":"items"},"Get all basic collection":{"summary":"Get all basic collections.","value":"query"}},"required":false},{"in":"query","name":"tag","description":"Filter the collections by a tag.","schema":{"type":"array","items":{"type":"string"},"example":"flat_10"},"required":false},{"in":"query","name":"is_active","description":"Filter collections by active status.","schema":{"type":"boolean"},"required":false,"example":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","minimum":1},"example":1,"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer","default":12},"example":10,"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true}]}""", q=q, schedule_status=schedule_status, type=type, tag=tag, is_active=is_active, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(q=q, schedule_status=schedule_status, type=type, tag=tag, is_active=is_active, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", q=q, schedule_status=schedule_status, type=type, tag=tag, is_active=is_active, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionListingResponse
            schema = GetCollectionListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllCollections")
                print(e)

        

        return response
    
    async def createCollection(self, body=""):
        """A Collection allows you to organize your products into hierarchical groups. This API helps you in creating the collection.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCollection()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateCollection
        schema = CreateCollection()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CollectionCreateResponse
            schema = CollectionCreateResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCollection")
                print(e)

        

        return response
    
    async def getCollectionDetail(self, slug=None):
        """This API retrieves the detail of the collection in an application.
        :param slug : A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.getCollectionDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{slug}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true},{"in":"path","name":"slug","description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","schema":{"type":"string"},"example":"flat_10_fynd_summer_sale","required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true},{"in":"path","name":"slug","description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","schema":{"type":"string"},"example":"flat_10_fynd_summer_sale","required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{slug}/", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CollectionDetailResponse
            schema = CollectionDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCollectionDetail")
                print(e)

        

        return response
    
    async def updateCollection(self, id=None, body=""):
        """This API enables you to update a collection by specifying its unique identifier (`ID`). By utilizing this endpoint, you can easily modify and refine the attributes, settings, and contents of a specific collection, ensuring it remains relevant and aligned with your business goals.
        :param id : An `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateCollection()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCollection
        schema = UpdateCollection()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true},{"in":"path","name":"id","description":"An `id` is a unique identifier of a collection.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"63b277d1a3d0fe0891479741","required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true},{"in":"path","name":"id","description":"An `id` is a unique identifier of a collection.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"63b277d1a3d0fe0891479741","required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CollectionUpdateResponse
            schema = CollectionUpdateResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCollection")
                print(e)

        

        return response
    
    async def deleteCollection(self, id=None):
        """This API allows you to delete the collection of an application.
        :param id : An `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteCollection()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true},{"in":"path","name":"id","description":"An `id` is a unique identifier of a collection.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"63b277d1a3d0fe0891479741","required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true},{"in":"path","name":"id","description":"An `id` is a unique identifier of a collection.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"63b277d1a3d0fe0891479741","required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteResponse
            schema = DeleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCollection")
                print(e)

        

        return response
    
    async def getCollectionItems(self, id=None, f=None, sort_on=None, page_id=None, page_size=None, x_currency_code=None):
        """A Collection API allows you to organize your products into hierarchical groups. This API provides a list of items and filters that can be applied to the items within a collection. It enables you to retrieve specific items based on various filter criteria.The API allows you to fetch information about items in the collection, including their attributes, categories, media URLs, pricing details, and more. Additionally, you can apply filters such as size and color to narrow down the search results and find the desired items. By utilizing this API, you can efficiently manage and display collections of products, making it easier for users to navigate and explore your e-commerce platform. It offers flexibility in organizing and presenting products, enhancing the overall user experience.
        :param id : An `id` is a unique identifier of a collection. : type string
        :param f : Filter the products in the collection using key-value pairs. : type string
        :param sort_on : It is the attribute's value on which the products will be sorted for a collection. : type string
        :param page_id : It is the currency id of the page in the pagniation. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param x-currency-code : The currency code used for pricing and monetary transactions. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        
        if f is not None:
            payload["f"] = f
        
        if sort_on is not None:
            payload["sort_on"] = sort_on
        
        if page_id is not None:
            payload["page_id"] = page_id
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if x_currency_code is not None:
            payload["x_currency_code"] = x_currency_code
        

        # Parameter validation
        schema = CatalogValidator.getCollectionItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true},{"in":"path","name":"id","description":"An `id` is a unique identifier of a collection.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"63b277d1a3d0fe0891479741","required":true}],"optional":[{"in":"query","name":"f","description":"Filter the products in the collection using key-value pairs.","schema":{"type":"string"},"examples":{"Multivalued Filter":{"summary":"Multivalued filter","value":"gender:Women||Unisex"},"Range Filter":{"summary":"Range filter","value":"min_price_effective:[99,INR TO 32910,INR]"}},"required":false},{"in":"query","name":"sort_on","description":"It is the attribute's value on which the products will be sorted for a collection.","schema":{"type":"string"},"example":"popular","required":false},{"in":"query","name":"page_id","description":"It is the currency id of the page in the pagniation.","schema":{"type":"integer","minimum":1},"example":2,"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"example":10,"required":false},{"in":"header","name":"x-currency-code","description":"The currency code used for pricing and monetary transactions.","schema":{"type":"string","minLength":3,"maxLength":3,"default":"INR"},"example":"USD","required":false}],"query":[{"in":"query","name":"f","description":"Filter the products in the collection using key-value pairs.","schema":{"type":"string"},"examples":{"Multivalued Filter":{"summary":"Multivalued filter","value":"gender:Women||Unisex"},"Range Filter":{"summary":"Range filter","value":"min_price_effective:[99,INR TO 32910,INR]"}},"required":false},{"in":"query","name":"sort_on","description":"It is the attribute's value on which the products will be sorted for a collection.","schema":{"type":"string"},"example":"popular","required":false},{"in":"query","name":"page_id","description":"It is the currency id of the page in the pagniation.","schema":{"type":"integer","minimum":1},"example":2,"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"example":10,"required":false}],"headers":[{"in":"header","name":"x-currency-code","description":"The currency code used for pricing and monetary transactions.","schema":{"type":"string","minLength":3,"maxLength":3,"default":"INR"},"example":"USD","required":false}],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true},{"in":"path","name":"id","description":"An `id` is a unique identifier of a collection.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"63b277d1a3d0fe0891479741","required":true}]}""", id=id, f=f, sort_on=sort_on, page_id=page_id, page_size=page_size, x_currency_code=x_currency_code)
        query_string = await create_query_string(id=id, f=f, sort_on=sort_on, page_id=page_id, page_size=page_size, x_currency_code=x_currency_code)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", id=id, f=f, sort_on=sort_on, page_id=page_id, page_size=page_size, x_currency_code=x_currency_code), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionItemsResponse
            schema = GetCollectionItemsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCollectionItems")
                print(e)

        

        return response
    
    async def addCollectionItems(self, id=None, body=""):
        """Adds items to a collection specified by its `id`. This API allows you to add items to a specific collection identified by its unique `id`. By utilizing this endpoint, you can expand and enhance the product offerings within a collection, providing users with a wider range of options and choices.
        :param id : An `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.addCollectionItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CollectionItemUpdate
        schema = CollectionItemUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true},{"in":"path","name":"id","description":"An `id` is a unique identifier of a collection.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"63b277d1a3d0fe0891479741","required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true},{"in":"path","name":"id","description":"An `id` is a unique identifier of a collection.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"63b277d1a3d0fe0891479741","required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdatedResponse
            schema = UpdatedResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addCollectionItems")
                print(e)

        

        return response
    
    async def getCatalogInsights(self, brand=None):
        """The Catalog Insights API provides information about the count of catalog-related data, including products, brands, departments, and categories that have been made available based on the configuration of the application. This API allows you to retrieve statistical insights and metrics regarding the catalog, helping you gain valuable information about the live data in your catalog.
        :param brand : The slug of the brand. : type string
        """
        payload = {}
        
        if brand is not None:
            payload["brand"] = brand
        

        # Parameter validation
        schema = CatalogValidator.getCatalogInsights()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/analytics/insights/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true}],"optional":[{"in":"query","name":"brand","description":"The slug of the brand.","schema":{"type":"string"},"example":"fynd","required":false}],"query":[{"in":"query","name":"brand","description":"The slug of the brand.","schema":{"type":"string"},"example":"fynd","required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a numeric ID allotted to a business account on Fynd Platform.","schema":{"type":"integer","minimum":1},"example":1,"required":true},{"in":"path","name":"application_id","description":"A `application_id` is alphanumeric ID allotted to a sales channel application created within a business account.","schema":{"type":"string","minLength":24,"maxLength":24},"example":"000000000000000000000001","required":true}]}""", brand=brand)
        query_string = await create_query_string(brand=brand)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/analytics/insights/", brand=brand), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CatalogInsightResponse
            schema = CatalogInsightResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCatalogInsights")
                print(e)

        

        return response
    
    async def getDiscountedInventoryBySizeIdentifier(self, item_id=None, size_identifier=None, page_no=None, page_size=None, q=None, location_ids=None):
        """This API allows get Inventory data for particular company grouped by size and store.
        :param item_id : Item code of the product of which size is to be get. : type integer
        :param size_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search with help of store code. : type string
        :param location_ids : Search by store ids. : type array
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        
        if size_identifier is not None:
            payload["size_identifier"] = size_identifier
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if q is not None:
            payload["q"] = q
        
        if location_ids is not None:
            payload["location_ids"] = location_ids
        

        # Parameter validation
        schema = CatalogValidator.getDiscountedInventoryBySizeIdentifier()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{item_id}/inventory/{size_identifier}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Uniquer Application ID.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"integer"},"required":true},{"in":"path","name":"size_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"location_ids","description":"Search by store ids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"location_ids","description":"Search by store ids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Uniquer Application ID.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"integer"},"required":true},{"in":"path","name":"size_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
        query_string = await create_query_string(item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{item_id}/inventory/{size_identifier}", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import InventorySellerIdentifierResponsePaginated
            schema = InventorySellerIdentifierResponsePaginated()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDiscountedInventoryBySizeIdentifier")
                print(e)

        

        return response
    
    async def getApplicationBrands(self, department=None, page_no=None, page_size=None, q=None, brand_id=None):
        """A brand is the name under which a product is being sold. Use this API to list all the brands. You can pass optionally filter the brands by the department. If successful, returns a paginated list of brands specified in `BrandListingResponse`
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name.Use this parameter to search brands by  brand name. : type string
        :param brand_id : Helps to sort the brands list on the basis of uid list. : type array
        """
        payload = {}
        
        if department is not None:
            payload["department"] = department
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if q is not None:
            payload["q"] = q
        
        if brand_id is not None:
            payload["brand_id"] = brand_id
        

        # Parameter validation
        schema = CatalogValidator.getApplicationBrands()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brands", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search brands by  brand name.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_id","description":"Helps to sort the brands list on the basis of uid list.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"query":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search brands by  brand name.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_id","description":"Helps to sort the brands list on the basis of uid list.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id)
        query_string = await create_query_string(department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brands", department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import BrandListingResponse
            schema = BrandListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationBrands")
                print(e)

        

        return response
    
    async def getDepartments(self, ):
        """Departments are a way to categorise similar products. A product can lie in multiple departments. For example, a skirt can below to the 'Women's Fashion' Department while a handbag can lie in 'Women's Accessories' Department. Use this API to list all the departments. If successful, returns the list of departments specified in `DepartmentResponse`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getDepartments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/departments", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/departments", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DepartmentResponse
            schema = DepartmentResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDepartments")
                print(e)

        

        return response
    
    async def getCategories(self, department=None):
        """List all the categories. You can optionally pass filter the brands by the department. If successful, returns a paginated list of brands specified in `CategoryListingResponse`
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API : type string
        """
        payload = {}
        
        if department is not None:
            payload["department"] = department
        

        # Parameter validation
        schema = CatalogValidator.getCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/categories", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false}],"query":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", department=department)
        query_string = await create_query_string(department=department)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/categories", department=department), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CategoryListingResponse
            schema = CategoryListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCategories")
                print(e)

        

        return response
    
    async def getAppicationProducts(self, q=None, f=None, c=None, filters=None, is_dependent=None, sort_on=None, page_id=None, page_size=None, page_no=None, page_type=None, item_ids=None):
        """List all the products associated with a brand, collection or category in a requested sort order. The API additionally supports arbitrary search queries that may refer the name of any product, brand, category or collection. If successful, returns a paginated list of products specified in `ApplicationProductListingResponse`
        :param q : The search query. This can be a partial or complete name of a either a product, brand or category : type string
        :param f : The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts** : type string
        :param c : The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts** : type string
        :param filters : Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters : type boolean
        :param is_dependent : This query parameter is used to get the dependent products in the listing. : type boolean
        :param sort_on : The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below. : type string
        :param page_id : Each response will contain **page_id** param, which should be sent back to make pagination work. : type string
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param page_no : If page_type is number then pass it to fetch page items. Default is 1. : type integer
        :param page_type : For pagination type should be cursor or number. Default is cursor. : type string
        :param item_ids : Item Ids of product : type array
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q
        
        if f is not None:
            payload["f"] = f
        
        if c is not None:
            payload["c"] = c
        
        if filters is not None:
            payload["filters"] = filters
        
        if is_dependent is not None:
            payload["is_dependent"] = is_dependent
        
        if sort_on is not None:
            payload["sort_on"] = sort_on
        
        if page_id is not None:
            payload["page_id"] = page_id
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_type is not None:
            payload["page_type"] = page_type
        
        if item_ids is not None:
            payload["item_ids"] = item_ids
        

        # Parameter validation
        schema = CatalogValidator.getAppicationProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"q","description":"The search query. This can be a partial or complete name of a either a product, brand or category","schema":{"type":"string"},"required":false},{"in":"query","name":"f","description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","schema":{"type":"string"},"required":false},{"in":"query","name":"c","description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","schema":{"type":"string"},"required":false},{"in":"query","name":"filters","description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"is_dependent","description":"This query parameter is used to get the dependent products in the listing.","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"If page_type is number then pass it to fetch page items. Default is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"For pagination type should be cursor or number. Default is cursor.","schema":{"type":"string","default":"cursor"},"required":false},{"in":"query","name":"item_ids","description":"Item Ids of product","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"query":[{"in":"query","name":"q","description":"The search query. This can be a partial or complete name of a either a product, brand or category","schema":{"type":"string"},"required":false},{"in":"query","name":"f","description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","schema":{"type":"string"},"required":false},{"in":"query","name":"c","description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","schema":{"type":"string"},"required":false},{"in":"query","name":"filters","description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"is_dependent","description":"This query parameter is used to get the dependent products in the listing.","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"If page_type is number then pass it to fetch page items. Default is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"For pagination type should be cursor or number. Default is cursor.","schema":{"type":"string","default":"cursor"},"required":false},{"in":"query","name":"item_ids","description":"Item Ids of product","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", q=q, f=f, c=c, filters=filters, is_dependent=is_dependent, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids)
        query_string = await create_query_string(q=q, f=f, c=c, filters=filters, is_dependent=is_dependent, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products", q=q, f=f, c=c, filters=filters, is_dependent=is_dependent, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationProductListingResponse
            schema = ApplicationProductListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppicationProducts")
                print(e)

        

        return response
    
    async def getProductDetailBySlug(self, slug=None):
        """Products are the core resource of an application. Products can be associated by categories, collections, brands and more. This API retrieves the product specified by the given **slug**. If successful, returns a Product resource in the response body specified in `ProductDetail`
        :param slug : The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/** : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.getProductDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{slug}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/**","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/**","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductDetail
            schema = ProductDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductDetailBySlug")
                print(e)

        

        return response
    
    async def getAppProducts(self, brand_ids=None, category_ids=None, department_ids=None, tags=None, is_dependent=None, item_ids=None, page_no=None, page_size=None, q=None):
        """Products are the core resource of an application. Products can be associated by categories, collections, brands and more. If successful, returns a Product resource in the response body specified in `ApplicationProductListingResponseDatabasePowered`
        :param brand_ids : Get multiple products filtered by Brand Ids : type array
        :param category_ids : Get multiple products filtered by Category Ids : type array
        :param department_ids : Get multiple products filtered by Department Ids : type array
        :param tags : Get multiple products filtered by tags : type array
        :param is_dependent : This query parameter is used to get the dependent products in the listing. : type boolean
        :param item_ids : Get multiple products filtered by Item Ids : type array
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param q : Search with Item Code, Name, Slug or Identifier. : type string
        """
        payload = {}
        
        if brand_ids is not None:
            payload["brand_ids"] = brand_ids
        
        if category_ids is not None:
            payload["category_ids"] = category_ids
        
        if department_ids is not None:
            payload["department_ids"] = department_ids
        
        if tags is not None:
            payload["tags"] = tags
        
        if is_dependent is not None:
            payload["is_dependent"] = is_dependent
        
        if item_ids is not None:
            payload["item_ids"] = item_ids
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if q is not None:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getAppProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"is_dependent","description":"This query parameter is used to get the dependent products in the listing.","schema":{"type":"boolean","default":true}},{"in":"query","name":"item_ids","description":"Get multiple products filtered by Item Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false},{"in":"query","name":"q","description":"Search with Item Code, Name, Slug or Identifier.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"is_dependent","description":"This query parameter is used to get the dependent products in the listing.","schema":{"type":"boolean","default":true}},{"in":"query","name":"item_ids","description":"Get multiple products filtered by Item Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false},{"in":"query","name":"q","description":"Search with Item Code, Name, Slug or Identifier.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, is_dependent=is_dependent, item_ids=item_ids, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, is_dependent=is_dependent, item_ids=item_ids, page_no=page_no, page_size=page_size, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products/", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, is_dependent=is_dependent, item_ids=item_ids, page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductListingResponse
            schema = ProductListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppProducts")
                print(e)

        

        return response
    
    async def getAppInventory(self, item_ids=None, store_ids=None, brand_ids=None, seller_identifiers=None, timestamp=None, page_size=None, page_id=None):
        """Retrieve the available Inventory of the products. Use this API to get the Inventory status of products with the filters of timestamp, store_ids, brand_ids, item_id - Items - Pagination
        :param item_ids : The Item Id of the product. : type array
        :param store_ids : The Store Id of products to fetch inventory. : type array
        :param brand_ids : The Brand Id of products to fetch inventory. : type array
        :param seller_identifiers : Unique seller_identifier of the product. : type array
        :param timestamp : Timestamp in UTC format (2020-07-23T10:27:50Z) : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        :param page_id : Page ID to retrieve next set of results. : type string
        """
        payload = {}
        
        if item_ids is not None:
            payload["item_ids"] = item_ids
        
        if store_ids is not None:
            payload["store_ids"] = store_ids
        
        if brand_ids is not None:
            payload["brand_ids"] = brand_ids
        
        if seller_identifiers is not None:
            payload["seller_identifiers"] = seller_identifiers
        
        if timestamp is not None:
            payload["timestamp"] = timestamp
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if page_id is not None:
            payload["page_id"] = page_id
        

        # Parameter validation
        schema = CatalogValidator.getAppInventory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/inventory/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"item_ids","description":"The Item Id of the product.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"store_ids","description":"The Store Id of products to fetch inventory.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"brand_ids","description":"The Brand Id of products to fetch inventory.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"seller_identifiers","description":"Unique seller_identifier of the product.","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"timestamp","description":"Timestamp in UTC format (2020-07-23T10:27:50Z)","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"item_ids","description":"The Item Id of the product.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"store_ids","description":"The Store Id of products to fetch inventory.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"brand_ids","description":"The Brand Id of products to fetch inventory.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"seller_identifiers","description":"Unique seller_identifier of the product.","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"timestamp","description":"Timestamp in UTC format (2020-07-23T10:27:50Z)","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", item_ids=item_ids, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, timestamp=timestamp, page_size=page_size, page_id=page_id)
        query_string = await create_query_string(item_ids=item_ids, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, timestamp=timestamp, page_size=page_size, page_id=page_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/inventory/", item_ids=item_ids, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, timestamp=timestamp, page_size=page_size, page_id=page_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryStockResponse
            schema = InventoryStockResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppInventory")
                print(e)

        

        return response
    
    async def getAppLocations(self, store_type=None, uid=None, q=None, stage=None, page_no=None, page_size=None):
        """This API allows to view all the locations asscoiated to a application.
        :param store_type : Helps to sort the location list on the basis of location type. : type string
        :param uid : Helps to sort the location list on the basis of uid list. : type array
        :param q : Query that is to be searched. : type string
        :param stage : to filter companies on basis of verified or unverified companies. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 20. : type integer
        """
        payload = {}
        
        if store_type is not None:
            payload["store_type"] = store_type
        
        if uid is not None:
            payload["uid"] = uid
        
        if q is not None:
            payload["q"] = q
        
        if stage is not None:
            payload["stage"] = stage
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getAppLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/locations", """{"required":[{"in":"path","name":"company_id","description":"Id of the company whose locations are to fetched","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"Id of the application whose locations are to fetched","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"store_type","description":"Helps to sort the location list on the basis of location type.","schema":{"type":"string"},"required":false},{"in":"query","name":"uid","description":"Helps to sort the location list on the basis of uid list.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified companies.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 20.","schema":{"type":"integer","default":20},"required":false}],"query":[{"in":"query","name":"store_type","description":"Helps to sort the location list on the basis of location type.","schema":{"type":"string"},"required":false},{"in":"query","name":"uid","description":"Helps to sort the location list on the basis of uid list.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified companies.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 20.","schema":{"type":"integer","default":20},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company whose locations are to fetched","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"Id of the application whose locations are to fetched","schema":{"type":"string"},"required":true}]}""", store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/locations", store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import LocationListSerializer
            schema = LocationListSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppLocations")
                print(e)

        

        return response
    
    async def getApplicationBrandListing(self, page_no=None, page_size=None, q=None):
        """A brand is the name under which a product is being sold. Use this API to list all the brands. You can pass optionally filter the brands by the department. If successful, returns a paginated list of brands specified in `BrandListingResponse`
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name.Use this parameter to search brands by  brand name. : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if q is not None:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getApplicationBrandListing()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search brands by  brand name.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search brands by  brand name.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import BrandListingResponse
            schema = BrandListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationBrandListing")
                print(e)

        

        return response
    
    async def updateAppBrand(self, brand_uid=None, body=""):
        """This API helps to update data associated to a item custom meta.
        :param brand_uid : brand id for which the custom_json is associated. : type string
        """
        payload = {}
        
        if brand_uid is not None:
            payload["brand_uid"] = brand_uid
        

        # Parameter validation
        schema = CatalogValidator.updateAppBrand()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationBrandJson
        schema = ApplicationBrandJson()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand/{brand_uid}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to brand custom json.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_json is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_uid","description":"brand id for which the custom_json is associated.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to brand custom json.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_json is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_uid","description":"brand id for which the custom_json is associated.","schema":{"type":"string"},"required":true}]}""", brand_uid=brand_uid)
        query_string = await create_query_string(brand_uid=brand_uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand/{brand_uid}", brand_uid=brand_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppBrand")
                print(e)

        

        return response
    
    async def getApplicationCategoryListing(self, department_id=None, page_no=None, page_size=None, q=None):
        """A brand is the name under which a product is being sold. Use this API to list all the brands. You can pass optionally filter the brands by the department. If successful, returns a paginated list of brands specified in `BrandListingResponse`
        :param department_id : A `department_id` is a unique identifier for a particular department. : type integer
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name.Use this parameter to search brands by  brand name. : type string
        """
        payload = {}
        
        if department_id is not None:
            payload["department_id"] = department_id
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if q is not None:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getApplicationCategoryListing()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"department_id","description":"A `department_id` is a unique identifier for a particular department.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search brands by  brand name.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"department_id","description":"A `department_id` is a unique identifier for a particular department.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search brands by  brand name.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", department_id=department_id, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(department_id=department_id, page_no=page_no, page_size=page_size, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category", department_id=department_id, page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import BrandListingResponse
            schema = BrandListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationCategoryListing")
                print(e)

        

        return response
    
    async def updateAppCategory(self, category_uid=None, body=""):
        """This API helps to update data associated to a item custom meta.
        :param category_uid : category id for which the custom_json is associated. : type string
        """
        payload = {}
        
        if category_uid is not None:
            payload["category_uid"] = category_uid
        

        # Parameter validation
        schema = CatalogValidator.updateAppCategory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationCategoryJson
        schema = ApplicationCategoryJson()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category/{category_uid}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to category custom json.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_json is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"category_uid","description":"category id for which the custom_json is associated.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to category custom json.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_json is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"category_uid","description":"category id for which the custom_json is associated.","schema":{"type":"string"},"required":true}]}""", category_uid=category_uid)
        query_string = await create_query_string(category_uid=category_uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category/{category_uid}", category_uid=category_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCategory")
                print(e)

        

        return response
    
    async def getApplicationDepartmentListing(self, page_no=None, page_size=None, q=None):
        """Departments are a way to categorise similar products. A product can lie in multiple departments. For example, a skirt can below to the 'Women's Fashion' Department while a handbag can lie in 'Women's Accessories' Department. Use this API to list all the application departments. If successful, returns the list of departments specified in `ApplicationDepartmentListingResponse`
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name.Use this parameter to search department by name. : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if q is not None:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getApplicationDepartmentListing()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search department by name.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search department by name.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationDepartmentListingResponse
            schema = ApplicationDepartmentListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationDepartmentListing")
                print(e)

        

        return response
    
    async def updateAppDepartment(self, department_uid=None, body=""):
        """This API helps to update data associated to a item custom meta.
        :param department_uid : department id for which the custom_json is associated. : type string
        """
        payload = {}
        
        if department_uid is not None:
            payload["department_uid"] = department_uid
        

        # Parameter validation
        schema = CatalogValidator.updateAppDepartment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationDepartmentJson
        schema = ApplicationDepartmentJson()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department/{department_uid}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to department custom json.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_json is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"department_uid","description":"department id for which the custom_json is associated.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to department custom json.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_json is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"department_uid","description":"department id for which the custom_json is associated.","schema":{"type":"string"},"required":true}]}""", department_uid=department_uid)
        query_string = await create_query_string(department_uid=department_uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department/{department_uid}", department_uid=department_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppDepartment")
                print(e)

        

        return response
    
    async def updateAppLocation(self, store_uid=None, body=""):
        """This API helps to update data associated to a item custom meta.
        :param store_uid : store id for which the custom_json is associated. : type string
        """
        payload = {}
        
        if store_uid is not None:
            payload["store_uid"] = store_uid
        

        # Parameter validation
        schema = CatalogValidator.updateAppLocation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationStoreJson
        schema = ApplicationStoreJson()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/{store_uid}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to location custom json.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_json is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"store_uid","description":"store id for which the custom_json is associated.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to location custom json.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_json is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"store_uid","description":"store id for which the custom_json is associated.","schema":{"type":"string"},"required":true}]}""", store_uid=store_uid)
        query_string = await create_query_string(store_uid=store_uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/{store_uid}", store_uid=store_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppLocation")
                print(e)

        

        return response
    

