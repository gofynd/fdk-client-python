

"""Catalog Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import CatalogValidator

class Catalog:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getSearchKeywords(self, id=None):
        """Get the details of a words by its `id`. If successful, returns a Collection resource in the response body specified in `GetSearchWordsDetailResponseSchema`
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateSearchKeywords(self, id=None, body=""):
        """Update Search Keyword by its id. On successful request, returns the updated collection
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateSearchKeywords()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchKeyword
        schema = CreateSearchKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteSearchKeywords(self, id=None):
        """Delete a keywords by it's id. Returns an object that tells whether the keywords was deleted successfully
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createCustomKeyword(self, body=""):
        """Create a Custom Search Keywords. See `CreateSearchKeywordSchema` for the list of attributes needed to create a mapping and /collections/query-options for the available options to create a rule. On successful request, returns a paginated list of collections specified in `CreateSearchKeywordSchema`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCustomKeyword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchKeyword
        schema = CreateSearchKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAllSearchKeyword(self, ):
        """Custom Search Keyword allows you to map conditions with keywords to give you the ultimate results
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAllSearchKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getAutocompleteKeywordDetail(self, id=None):
        """Get the details of a words by its `id`. If successful, returns a keywords resource in the response body specified in `GetAutocompleteWordsResponseSchema`
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getAutocompleteKeywordDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateAutocompleteKeyword(self, id=None, body=""):
        """Update a mapping by it's id. On successful request, returns the updated Keyword mapping
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateAutocompleteKeyword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateAutocompleteKeyword
        schema = CreateAutocompleteKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteAutocompleteKeyword(self, id=None):
        """Delete a keywords by it's id. Returns an object that tells whether the keywords was deleted successfully
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteAutocompleteKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createCustomAutocompleteRule(self, body=""):
        """Create a Custom Autocomplete Keywords. See `CreateAutocompleteKeywordSchema` for the list of attributes needed to create a mapping and /collections/query-options for the available options to create a rule. On successful request, returns a paginated list of collections specified in `CreateAutocompleteKeywordSchema`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCustomAutocompleteRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateAutocompleteKeyword
        schema = CreateAutocompleteKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAutocompleteConfig(self, ):
        """Custom Autocomplete Keyword allows you to map conditions with keywords to give you the ultimate results
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAutocompleteConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateAppProduct(self, item_id=None, body=""):
        """This API helps to update data associated to a item custom meta.
        :param item_id : product id for which the custom_meta is associated. : type string
        """
        payload = {}
        
        if item_id:
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
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", item_id=item_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAppProduct(self, item_id=None, slice_attr=None):
        """Products are the core resource of an application. If successful, returns a Company Application Product resource in the response body depending upon filter sent.
        :param item_id : product id for a particular product. : type string
        :param slice_attr : Get product's data sliced by attribute : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if slice_attr:
            payload["slice_attr"] = slice_attr
        

        # Parameter validation
        schema = CatalogValidator.getAppProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"product id for a particular product.","schema":{"type":"string"},"required":true},{"in":"query","name":"slice_attr","description":"Get product's data sliced by attribute","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"slice_attr","description":"Get product's data sliced by attribute","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"product id for a particular product.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, slice_attr=slice_attr)
        query_string = await create_query_string(item_id=item_id, slice_attr=slice_attr)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", item_id=item_id, slice_attr=slice_attr), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getConfigurationMetadata(self, config_type=None, template_slug=None):
        """Get the configuraion metadata details for catalog.
        :param config_type : A `config_type` is an identifier that defines a specific type of configuration. : type string
        :param template_slug : Get configuration list filtered by `template_slug` string. This is for the details and comparision groups. : type string
        """
        payload = {}
        
        if config_type:
            payload["config_type"] = config_type
        
        if template_slug:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/metadata/", config_type=config_type, template_slug=template_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createGroupConfiguration(self, config_type=None, body=""):
        """Create configuration for Group config types.
        :param config_type : A `config_type` is a unique identifier for a particular group configuration type. : type string
        """
        payload = {}
        
        if config_type:
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", config_type=config_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getGroupConfigurations(self, config_type=None, page_no=None, page_size=None, search=None, template_slug=None):
        """Get the details of the application configured configurations of group config types.
        :param config_type : A `config_type` is an identifier that defines a specific type of configuration. : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param search : Get configuration list filtered by `search` string. : type string
        :param template_slug : Get configuration list filtered by `template_slug` string. This is for the details and comparision groups. : type string
        """
        payload = {}
        
        if config_type:
            payload["config_type"] = config_type
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if search:
            payload["search"] = search
        
        if template_slug:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", config_type=config_type, page_no=page_no, page_size=page_size, search=search, template_slug=template_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateGroupConfiguration(self, config_type=None, group_slug=None, body=""):
        """Update the group configurations for the application.
        :param config_type : A `config_type` is a unique identifier for a particular group configuration type. : type string
        :param group_slug : A `group_slug` is a unique identifier of a particular configuration. : type string
        """
        payload = {}
        
        if config_type:
            payload["config_type"] = config_type
        
        if group_slug:
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", config_type=config_type, group_slug=group_slug), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteGroupConfiguration(self, config_type=None, group_slug=None):
        """Delete configuration of the product config type of the application.
        :param config_type : A `config_type` is a unique identifier for a particular group configuration type. : type string
        :param group_slug : A `group_slug` is a unique identifier of a particular configuration. : type string
        """
        payload = {}
        
        if config_type:
            payload["config_type"] = config_type
        
        if group_slug:
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", config_type=config_type, group_slug=group_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createListingConfiguration(self, config_type=None, body=""):
        """Add configuration for listing.
        :param config_type : A `config_type` is a unique identifier for a particular listing configuration type. : type string
        """
        payload = {}
        
        if config_type:
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", config_type=config_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getListingConfigurations(self, config_type=None, page_no=None, page_size=None, search=None):
        """Get the details of the application configured configurations of listing config types.
        :param config_type : A `config_type` is an identifier that defines a specific type of configuration. : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param search : Get configuration list filtered by `search` string. : type string
        """
        payload = {}
        
        if config_type:
            payload["config_type"] = config_type
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if search:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", config_type=config_type, page_no=page_no, page_size=page_size, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateListingConfiguration(self, config_type=None, config_id=None, body=""):
        """Update configuration for listing.
        :param config_type : A `config_type` is a unique identifier for a particular listing configuration type. : type string
        :param config_id : A `config_id` is a unique identifier of a particular configuration. : type string
        """
        payload = {}
        
        if config_type:
            payload["config_type"] = config_type
        
        if config_id:
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", config_type=config_type, config_id=config_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteListingConfiguration(self, config_type=None, config_id=None):
        """Delete configuration for listing.
        :param config_type : A `config_type` is a unique identifier for a particular listing configuration type. : type string
        :param config_id : A `config_id` is a unique identifier of a particular configuration. : type string
        """
        payload = {}
        
        if config_type:
            payload["config_type"] = config_type
        
        if config_id:
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", config_type=config_type, config_id=config_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/filter/allow_single", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/sort/default_key", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createConfigurationByType(self, type=None, body=""):
        """Add configuration for categories & brands.
        :param type : type can be brands, categories etc. : type string
        """
        payload = {}
        
        if type:
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getConfigurationByType(self, type=None):
        """configured details for catalog.
        :param type : type can be brands, categories etc. : type string
        """
        payload = {}
        
        if type:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", type=type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getQueryFilters(self, ):
        """Get query filters to configure a collection
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getQueryFilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createCollection(self, body=""):
        """Create a collection. See `CreateCollectionRequestSchema` for the list of attributes needed to create a collection and collections/query-options for the available options to create a collection. On successful request, returns a paginated list of collections specified in `CollectionCreateResponse`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCollection()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateCollection
        schema = CreateCollection()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAllCollections(self, q=None, schedule_status=None, type=None, tags=None, is_active=None, page_no=None, page_size=None):
        """A Collection allows you to organize your products into hierarchical groups. For example, a dress might be in the category _Clothing_, the individual product might also be in the collection _Summer_. On successful request, returns all the collections as specified in `CollectionListingSchema`
        :param q : Get collection list filtered by q string, : type string
        :param schedule_status : Get collection list filtered by scheduled status, : type string
        :param type : type of the collections : type string
        :param tags : Each response will contain next_id param, which should be sent back to make pagination work. : type array
        :param is_active : get collections filtered by active status. : type boolean
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if q:
            payload["q"] = q
        
        if schedule_status:
            payload["schedule_status"] = schedule_status
        
        if type:
            payload["type"] = type
        
        if tags:
            payload["tags"] = tags
        
        if is_active:
            payload["is_active"] = is_active
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getAllCollections()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"q","description":"Get collection list filtered by q string,","schema":{"type":"string"},"required":false},{"in":"query","name":"schedule_status","description":"Get collection list filtered by scheduled status,","schema":{"type":"string","enum":["live","upcoming","expired"]},"required":false},{"in":"query","name":"type","description":"type of the collections","schema":{"type":"string"},"required":false},{"in":"query","name":"tags","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"is_active","description":"get collections filtered by active status.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"q","description":"Get collection list filtered by q string,","schema":{"type":"string"},"required":false},{"in":"query","name":"schedule_status","description":"Get collection list filtered by scheduled status,","schema":{"type":"string","enum":["live","upcoming","expired"]},"required":false},{"in":"query","name":"type","description":"type of the collections","schema":{"type":"string"},"required":false},{"in":"query","name":"tags","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"is_active","description":"get collections filtered by active status.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCollectionDetail(self, slug=None):
        """Get the details of a collection by its `slug`. If successful, returns a Collection resource in the response body specified in `CollectionDetailResponse`
        :param slug : A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.getCollectionDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{slug}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","schema":{"type":"string"},"required":true}]}""", slug=slug)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{slug}/", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateCollection(self, id=None, body=""):
        """Update a collection by it's id. On successful request, returns the updated collection
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateCollection()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCollection
        schema = UpdateCollection()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteCollection(self, id=None):
        """Delete a collection by it's id. Returns an object that tells whether the collection was deleted successfully
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteCollection()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def addCollectionItems(self, id=None, body=""):
        """Adds items to a collection specified by its `id`. See `CollectionItemRequest` for the list of attributes needed to add items to an collection.
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.addCollectionItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CollectionItemRequest
        schema = CollectionItemRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getCollectionItems(self, id=None, sort_on=None, page_id=None, page_size=None):
        """Get items from a collection specified by its `id`.
        :param id : A `id` is a unique identifier of a collection. : type string
        :param sort_on : Each response will contain sort_on param, which should be sent back to make pagination work. : type string
        :param page_id : Each response will contain next_id param, which should be sent back to make pagination work. : type string
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if sort_on:
            payload["sort_on"] = sort_on
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getCollectionItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"sort_on","description":"Each response will contain sort_on param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_id","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"sort_on","description":"Each response will contain sort_on param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_id","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}]}""", id=id, sort_on=sort_on, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(id=id, sort_on=sort_on, page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", id=id, sort_on=sort_on, page_id=page_id, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCatalogInsights(self, brand=None):
        """Catalog Insights api returns the count of catalog related data like products, brands, departments and categories that have been made live as per configuration of the app.
        :param brand : Brand slug : type string
        """
        payload = {}
        
        if brand:
            payload["brand"] = brand
        

        # Parameter validation
        schema = CatalogValidator.getCatalogInsights()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/analytics/insights/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"brand","description":"Brand slug","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"brand","description":"Brand slug","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", brand=brand)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/analytics/insights/", brand=brand), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
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
        
        if item_id:
            payload["item_id"] = item_id
        
        if size_identifier:
            payload["size_identifier"] = size_identifier
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if location_ids:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{item_id}/inventory/{size_identifier}", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getApplicationBrands(self, department=None, page_no=None, page_size=None, q=None, brand_id=None):
        """A brand is the name under which a product is being sold. Use this API to list all the brands. You can pass optionally filter the brands by the department. If successful, returns a paginated list of brands specified in `BrandListingResponse`
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name.Use this parameter to search brands by  brand name. : type string
        :param brand_id : Helps to sort the brands list on the basis of uid list. : type array
        """
        payload = {}
        
        if department:
            payload["department"] = department
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if brand_id:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brands", department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/departments", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCategories(self, department=None):
        """List all the categories. You can optionally pass filter the brands by the department. If successful, returns a paginated list of brands specified in `CategoryListingResponse`
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API : type string
        """
        payload = {}
        
        if department:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/categories", department=department), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
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
        
        if q:
            payload["q"] = q
        
        if f:
            payload["f"] = f
        
        if c:
            payload["c"] = c
        
        if filters:
            payload["filters"] = filters
        
        if is_dependent:
            payload["is_dependent"] = is_dependent
        
        if sort_on:
            payload["sort_on"] = sort_on
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_type:
            payload["page_type"] = page_type
        
        if item_ids:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products", q=q, f=f, c=c, filters=filters, is_dependent=is_dependent, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getProductDetailBySlug(self, slug=None):
        """Products are the core resource of an application. Products can be associated by categories, collections, brands and more. This API retrieves the product specified by the given **slug**. If successful, returns a Product resource in the response body specified in `ProductDetail`
        :param slug : The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/** : type string
        """
        payload = {}
        
        if slug:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getAppProducts(self, brand_ids=None, category_ids=None, department_ids=None, tags=None, page_no=None, page_size=None, q=None):
        """Products are the core resource of an application. Products can be associated by categories, collections, brands and more. If successful, returns a Product resource in the response body specified in `ApplicationProductListingResponseDatabasePowered`
        :param brand_ids : Get multiple products filtered by Brand Ids : type array
        :param category_ids : Get multiple products filtered by Category Ids : type array
        :param department_ids : Get multiple products filtered by Department Ids : type array
        :param tags : Get multiple products filtered by tags : type array
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param q : Search with Item Code, Name, Slug or Identifier. : type string
        """
        payload = {}
        
        if brand_ids:
            payload["brand_ids"] = brand_ids
        
        if category_ids:
            payload["category_ids"] = category_ids
        
        if department_ids:
            payload["department_ids"] = department_ids
        
        if tags:
            payload["tags"] = tags
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getAppProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false},{"in":"query","name":"q","description":"Search with Item Code, Name, Slug or Identifier.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false},{"in":"query","name":"q","description":"Search with Item Code, Name, Slug or Identifier.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, page_no=page_no, page_size=page_size, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products/", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
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
        
        if item_ids:
            payload["item_ids"] = item_ids
        
        if store_ids:
            payload["store_ids"] = store_ids
        
        if brand_ids:
            payload["brand_ids"] = brand_ids
        
        if seller_identifiers:
            payload["seller_identifiers"] = seller_identifiers
        
        if timestamp:
            payload["timestamp"] = timestamp
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_id:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/inventory/", item_ids=item_ids, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, timestamp=timestamp, page_size=page_size, page_id=page_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
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
        
        if store_type:
            payload["store_type"] = store_type
        
        if uid:
            payload["uid"] = uid
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/locations", store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getApplicationBrandListing(self, page_no=None, page_size=None, q=None):
        """A brand is the name under which a product is being sold. Use this API to list all the brands. You can pass optionally filter the brands by the department. If successful, returns a paginated list of brands specified in `BrandListingResponse`
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name.Use this parameter to search brands by  brand name. : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateAppBrand(self, brand_uid=None, body=""):
        """This API helps to update data associated to a item custom meta.
        :param brand_uid : brand id for which the custom_json is associated. : type string
        """
        payload = {}
        
        if brand_uid:
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
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand/{brand_uid}", brand_uid=brand_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getApplicationCategoryListing(self, page_no=None, page_size=None, q=None):
        """A brand is the name under which a product is being sold. Use this API to list all the brands. You can pass optionally filter the brands by the department. If successful, returns a paginated list of brands specified in `BrandListingResponse`
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name.Use this parameter to search brands by  brand name. : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getApplicationCategoryListing()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search brands by  brand name.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search brands by  brand name.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", page_no=page_no, page_size=page_size, q=q)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateAppCategory(self, category_uid=None, body=""):
        """This API helps to update data associated to a item custom meta.
        :param category_uid : category id for which the custom_json is associated. : type string
        """
        payload = {}
        
        if category_uid:
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
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category/{category_uid}", category_uid=category_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateAppLocation(self, store_uid=None, body=""):
        """This API helps to update data associated to a item custom meta.
        :param store_uid : store id for which the custom_json is associated. : type string
        """
        payload = {}
        
        if store_uid:
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
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/{store_uid}", store_uid=store_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

