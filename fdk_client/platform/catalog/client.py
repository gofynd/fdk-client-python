

""" Catalog Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import CatalogValidator

class Catalog:
    def __init__(self, config):
        self._conf = config
    
    async def createProductBundle(self, body=""):
        """Create Product Bundle. See `ProductBundleRequest` for the request body parameter need to create a product bundle. On successful request, returns in `ProductBundleRequest` with id
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createProductBundle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductBundleRequest
        schema = ProductBundleRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProductBundle(self, q=None, slug=None):
        """Get all product bundles for a particular company
        :param q : A search string that is searched with product bundle name. : type string
        :param slug : slugs of bundles to be retrieved. : type array
        """
        payload = {}
        
        if q:
            payload["q"] = q
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.getProductBundle()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"q","description":"A search string that is searched with product bundle name.","schema":{"type":"string"},"required":false},{"in":"query","name":"slug","description":"slugs of bundles to be retrieved.","schema":{"type":"array","items":{"type":"string"}},"required":false}],"query":[{"in":"query","name":"q","description":"A search string that is searched with product bundle name.","schema":{"type":"string"},"required":false},{"in":"query","name":"slug","description":"slugs of bundles to be retrieved.","schema":{"type":"array","items":{"type":"string"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", q=q, slug=slug)
        query_string = await create_query_string(q=q, slug=slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", q=q, slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateProductBundle(self, id=None, body=""):
        """Update a Product Bundle by its id. On successful request, returns the updated product bundle
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateProductBundle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductBundleUpdateRequest
        schema = ProductBundleUpdateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProductBundleDetail(self, id=None):
        """Get a particular Bundle details by its `id`. If successful, returns a Product bundle resource in the response body specified in `GetProductBundleResponse`
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getProductBundleDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createSizeGuide(self, body=""):
        """This API allows to create a size guide associated to a brand.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createSizeGuide()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateSizeGuide
        schema = ValidateSizeGuide()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the size guide is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the size guide is to be created.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSizeGuides(self, active=None, q=None, tag=None, page_no=None, page_size=None):
        """This API allows to view all the size guides associated to the seller.
        :param active : filter size guide on basis of active, in-active : type boolean
        :param q : Query that is to be searched. : type string
        :param tag : to filter size guide on basis of tag. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if active:
            payload["active"] = active
        
        if q:
            payload["q"] = q
        
        if tag:
            payload["tag"] = tag
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getSizeGuides()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", """{"required":[{"in":"path","name":"company_id","description":"Id of the company for which the size guides are to be fetched.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"active","description":"filter size guide on basis of active, in-active","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"tag","description":"to filter size guide on basis of tag.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"query":[{"in":"query","name":"active","description":"filter size guide on basis of active, in-active","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"tag","description":"to filter size guide on basis of tag.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company for which the size guides are to be fetched.","schema":{"type":"string"},"required":true}]}""", active=active, q=q, tag=tag, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(active=active, q=q, tag=tag, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", active=active, q=q, tag=tag, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateSizeGuide(self, id=None, body=""):
        """This API allows to edit a size guide.
        :param id : Mongo id of the size guide to be edited : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateSizeGuide()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateSizeGuide
        schema = ValidateSizeGuide()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Mongo id of the size guide to be edited","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Mongo id of the size guide to be edited","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSizeGuide(self, id=None):
        """This API helps to get data associated to a size guide.
        :param id : Id of the size guide to be viewed. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getSizeGuide()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to size guide.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Id of the size guide to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to size guide.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Id of the size guide to be viewed.","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSellerInsights(self, seller_app_id=None):
        """Analytics data of catalog and inventory that are being cross-selled.
        :param seller_app_id : Id of the seller application which is serving the invetory/catalog of the company : type string
        """
        payload = {}
        
        if seller_app_id:
            payload["seller_app_id"] = seller_app_id
        

        # Parameter validation
        schema = CatalogValidator.getSellerInsights()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/cross-selling/{seller_app_id}/analytics/insights/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"seller_app_id","description":"Id of the seller application which is serving the invetory/catalog of the company","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"seller_app_id","description":"Id of the seller application which is serving the invetory/catalog of the company","schema":{"type":"string"},"required":true}]}""", seller_app_id=seller_app_id)
        query_string = await create_query_string(seller_app_id=seller_app_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/cross-selling/{seller_app_id}/analytics/insights/", seller_app_id=seller_app_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createMarketplaceOptin(self, marketplace=None, body=""):
        """Use this API to create/update opt-in information for given platform. If successful, returns data in the response body as specified in `OptInPostResponseSchema`
        :param marketplace : The marketplace for which the detail needs to be retrieved. : type string
        """
        payload = {}
        
        if marketplace:
            payload["marketplace"] = marketplace
        

        # Parameter validation
        schema = CatalogValidator.createMarketplaceOptin()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OptInPostRequest
        schema = OptInPostRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/{marketplace}/optin/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true},{"in":"path","name":"marketplace","description":"The marketplace for which the detail needs to be retrieved.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true},{"in":"path","name":"marketplace","description":"The marketplace for which the detail needs to be retrieved.","schema":{"type":"string"},"required":true}]}""", marketplace=marketplace)
        query_string = await create_query_string(marketplace=marketplace)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/{marketplace}/optin/", marketplace=marketplace), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getMarketplaceOptinDetail(self, ):
        """Use this API to fetch opt-in information for all the platforms. If successful, returns a logs in the response body as specified in `GetOptInPlatformSchema`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getMarketplaceOptinDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/", """{"required":[{"in":"path","name":"company_id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCompanyDetail(self, ):
        """Get the details of the company associated with the given company_id passed.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getCompanyDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-details/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-details/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCompanyBrandDetail(self, is_active=None, q=None, page_no=None, page_size=None, marketplace=None):
        """Get the details of the Brands associated with the given company_id passed.
        :param is_active : The is_active status for the optin id. : type boolean
        :param q : The search value to filter the list. : type boolean
        :param page_no : The number of page for the company id. : type integer
        :param page_size : Number of records that can be seen on the page for the company id. : type integer
        :param marketplace : The marketplace platform associated with the company id. : type string
        """
        payload = {}
        
        if is_active:
            payload["is_active"] = is_active
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if marketplace:
            payload["marketplace"] = marketplace
        

        # Parameter validation
        schema = CatalogValidator.getCompanyBrandDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-brand-details/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"is_active","description":"The is_active status for the optin id.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"The search value to filter the list.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"marketplace","description":"The marketplace platform associated with the company id.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"is_active","description":"The is_active status for the optin id.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"The search value to filter the list.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"marketplace","description":"The marketplace platform associated with the company id.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}]}""", is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace)
        query_string = await create_query_string(is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-brand-details/", is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCompanyMetrics(self, ):
        """Get the Company metrics associated with the company ID passed.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getCompanyMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-metrics/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-metrics/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getStoreDetail(self, q=None, page_no=None, page_size=None):
        """Get the details of the store associated with the company ID passed.
        :param q : The search related the store for the company id. : type string
        :param page_no : The number of page for the company id. : type integer
        :param page_size : Number of records that can be seen on the page for the company id. : type integer
        """
        payload = {}
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getStoreDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/location-details/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"q","description":"The search related the store for the company id.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"q","description":"The search related the store for the company id.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}]}""", q=q, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(q=q, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/location-details/", q=q, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getGenderAttribute(self, attribute_slug=None):
        """This API allows to view the gender attribute details.
        :param attribute_slug : slug of the attribute for which you want to view the genders : type string
        """
        payload = {}
        
        if attribute_slug:
            payload["attribute_slug"] = attribute_slug
        

        # Parameter validation
        schema = CatalogValidator.getGenderAttribute()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/{attribute_slug}", """{"required":[{"in":"path","name":"company_id","description":"company for which you want to view the genders","schema":{"type":"integer"},"required":true},{"in":"path","name":"attribute_slug","description":"slug of the attribute for which you want to view the genders","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company for which you want to view the genders","schema":{"type":"integer"},"required":true},{"in":"path","name":"attribute_slug","description":"slug of the attribute for which you want to view the genders","schema":{"type":"string"},"required":true}]}""", attribute_slug=attribute_slug)
        query_string = await create_query_string(attribute_slug=attribute_slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/{attribute_slug}", attribute_slug=attribute_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def listProductTemplateCategories(self, departments=None, item_type=None):
        """Allows you to list all product categories values for the departments specified
        :param departments : A `department` is name of a departments whose category needs to be listed. Can specify multiple departments. : type string
        :param item_type : An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc. : type string
        """
        payload = {}
        
        if departments:
            payload["departments"] = departments
        
        if item_type:
            payload["item_type"] = item_type
        

        # Parameter validation
        schema = CatalogValidator.listProductTemplateCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/categories/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"departments","description":"A `department` is name of a departments whose category needs to be listed. Can specify multiple departments.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"departments","description":"A `department` is name of a departments whose category needs to be listed. Can specify multiple departments.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc.","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", departments=departments, item_type=item_type)
        query_string = await create_query_string(departments=departments, item_type=item_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/categories/", departments=departments, item_type=item_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createDepartments(self, body=""):
        """Create departments using the API.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createDepartments()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DepartmentCreateUpdate
        schema = DepartmentCreateUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def listDepartmentsData(self, page_no=None, item_type=None, page_size=None, name=None, search=None, is_active=None):
        """Allows you to list all departments, also can search using name and filter active and incative departments, and item type.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param item_type : A `item_type` is a type of product eg. set, standard, digital : type string
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param name : Can search departments by passing name. : type string
        :param search : Can search departments by passing name of the department in search parameter. : type string
        :param is_active : Can query for departments based on whether they are active or inactive. : type boolean
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if item_type:
            payload["item_type"] = item_type
        
        if page_size:
            payload["page_size"] = page_size
        
        if name:
            payload["name"] = name
        
        if search:
            payload["search"] = search
        
        if is_active:
            payload["is_active"] = is_active
        

        # Parameter validation
        schema = CatalogValidator.listDepartmentsData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"item_type","description":"A `item_type` is a type of product eg. set, standard, digital","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer"},"required":false},{"in":"query","name":"name","description":"Can search departments by passing name.","schema":{"type":"string"},"required":false},{"in":"query","name":"search","description":"Can search departments by passing name of the department in search parameter.","schema":{"type":"string"},"required":false},{"in":"query","name":"is_active","description":"Can query for departments based on whether they are active or inactive.","schema":{"type":"boolean"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"item_type","description":"A `item_type` is a type of product eg. set, standard, digital","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer"},"required":false},{"in":"query","name":"name","description":"Can search departments by passing name.","schema":{"type":"string"},"required":false},{"in":"query","name":"search","description":"Can search departments by passing name of the department in search parameter.","schema":{"type":"string"},"required":false},{"in":"query","name":"is_active","description":"Can query for departments based on whether they are active or inactive.","schema":{"type":"boolean"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", page_no=page_no, item_type=item_type, page_size=page_size, name=name, search=search, is_active=is_active)
        query_string = await create_query_string(page_no=page_no, item_type=item_type, page_size=page_size, name=name, search=search, is_active=is_active)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/", page_no=page_no, item_type=item_type, page_size=page_size, name=name, search=search, is_active=is_active), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateDepartment(self, uid=None, body=""):
        """Update the department by their uid using this API.
        :param uid : A `uid` is a unique identifier of a department. : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.updateDepartment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DepartmentCreateUpdate
        schema = DepartmentCreateUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/{uid}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"A `uid` is a unique identifier of a department.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"A `uid` is a unique identifier of a department.","schema":{"type":"string"},"required":true}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/{uid}/", uid=uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getDepartmentData(self, uid=None):
        """Allows you to get department data, by uid.
        :param uid : A `uid` is a unique identifier of a department. : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.getDepartmentData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/{uid}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"A `uid` is a unique identifier of a department.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"A `uid` is a unique identifier of a department.","schema":{"type":"string"},"required":true}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/{uid}/", uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def listProductTemplate(self, department=None):
        """Allows you to list all product templates, also can filter by department
        :param department : A `department` is the name of a particular department. : type string
        """
        payload = {}
        
        if department:
            payload["department"] = department
        

        # Parameter validation
        schema = CatalogValidator.listProductTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"department","description":"A `department` is the name of a particular department.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"department","description":"A `department` is the name of a particular department.","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", department=department)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/", department=department), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def validateProductTemplate(self, slug=None):
        """Allows you to list all product templates validation values for all the fields present in the database
        :param slug : A `slug` is a unique identifier for a particular template. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.validateProductTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/validation/schema/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a unique identifier for a particular template.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a unique identifier for a particular template.","schema":{"type":"string"},"required":true}]}""", slug=slug)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/validation/schema/", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def downloadProductTemplateViews(self, slug=None):
        """Allows you to download product template data
        :param slug : A `slug` is a unique identifier for a particular template. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.downloadProductTemplateViews()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/download/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a unique identifier for a particular template.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a unique identifier for a particular template.","schema":{"type":"string"},"required":true}]}""", slug=slug)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/download/", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def downloadInventoryTemplateView(self, item_type=None):
        """Allows you to download product template data
        :param item_type : An `item_type` defines the type of item. : type string
        """
        payload = {}
        
        if item_type:
            payload["item_type"] = item_type
        

        # Parameter validation
        schema = CatalogValidator.downloadInventoryTemplateView()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/download/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` defines the type of item.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"item_type","description":"An `item_type` defines the type of item.","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", item_type=item_type)
        query_string = await create_query_string(item_type=item_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/download/", item_type=item_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def validateProductTemplateSchema(self, item_type=None):
        """Allows you to list all product templates validation values for all the fields present in the database
        :param item_type : An `item_type` defines the type of item. The default value is standard. : type string
        """
        payload = {}
        
        if item_type:
            payload["item_type"] = item_type
        

        # Parameter validation
        schema = CatalogValidator.validateProductTemplateSchema()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/validation/schema/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` defines the type of item. The default value is standard.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"item_type","description":"An `item_type` defines the type of item. The default value is standard.","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", item_type=item_type)
        query_string = await create_query_string(item_type=item_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/validation/schema/", item_type=item_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def listHSNCodes(self, ):
        """Allows you to list all hsn Codes
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.listHSNCodes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/hsn/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/hsn/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def listProductTemplateExportDetails(self, ):
        """Can view details including trigger data, task id , etc.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.listProductTemplateExportDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/downloads/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/downloads/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createProductExportJob(self, body=""):
        """This API helps to create a Inventory export job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createProductExportJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductTemplateDownloadsExport
        schema = ProductTemplateDownloadsExport()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def listAllProductTemplateExportDetails(self, status=None, from_date=None, to_date=None, q=None):
        """Can view details including trigger data, task id , etc.
        :param status : This is a parameter used to find all the jobs with the specified status. : type string
        :param from_date : This is a parameter used to find the job from the date specified to the current date. : type string
        :param to_date : This is a parameter used to find the job from the from_date specified to the to_date. : type string
        :param q : It is a query parameter to search the export job with the task ID. : type string
        """
        payload = {}
        
        if status:
            payload["status"] = status
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.listAllProductTemplateExportDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"status","description":"This is a parameter used to find all the jobs with the specified status.","schema":{"type":"string"},"required":false},{"in":"query","name":"from_date","description":"This is a parameter used to find the job from the date specified to the current date.","schema":{"type":"string","format":"date"},"required":false},{"in":"query","name":"to_date","description":"This is a parameter used to find the job from the from_date specified to the to_date.","schema":{"type":"string","format":"date"},"required":false},{"in":"query","name":"q","description":"It is a query parameter to search the export job with the task ID.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"status","description":"This is a parameter used to find all the jobs with the specified status.","schema":{"type":"string"},"required":false},{"in":"query","name":"from_date","description":"This is a parameter used to find the job from the date specified to the current date.","schema":{"type":"string","format":"date"},"required":false},{"in":"query","name":"to_date","description":"This is a parameter used to find the job from the from_date specified to the to_date.","schema":{"type":"string","format":"date"},"required":false},{"in":"query","name":"q","description":"It is a query parameter to search the export job with the task ID.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", status=status, from_date=from_date, to_date=to_date, q=q)
        query_string = await create_query_string(status=status, from_date=from_date, to_date=to_date, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/", status=status, from_date=from_date, to_date=to_date, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateProductExportJob(self, job_id=None, body=""):
        """This API helps to update a Product export job.
        :param job_id : A `job_id` is a unique identifier for a particular job. : type string
        """
        payload = {}
        
        if job_id:
            payload["job_id"] = job_id
        

        # Parameter validation
        schema = CatalogValidator.updateProductExportJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductPartialExportRequest
        schema = ProductPartialExportRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/{job_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"job_id","description":"A `job_id` is a unique identifier for a particular job.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"job_id","description":"A `job_id` is a unique identifier for a particular job.","schema":{"type":"string"},"required":true}]}""", job_id=job_id)
        query_string = await create_query_string(job_id=job_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/{job_id}", job_id=job_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProductTemplateExportDetail(self, job_id=None):
        """Can view details including export data, task id , etc for a job.
        :param job_id : A `job_id` is a unique identifier for a particular job. : type string
        """
        payload = {}
        
        if job_id:
            payload["job_id"] = job_id
        

        # Parameter validation
        schema = CatalogValidator.getProductTemplateExportDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/{job_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"job_id","description":"A `job_id` is a unique identifier for a particular job.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"job_id","description":"A `job_id` is a unique identifier for a particular job.","schema":{"type":"string"},"required":true}]}""", job_id=job_id)
        query_string = await create_query_string(job_id=job_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/{job_id}", job_id=job_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def listTemplateBrandTypeValues(self, filter=None, template_tag=None, item_type=None):
        """The filter type query parameter defines what type of data to return. The type of query returns the valid values for the same
        :param filter : A `filter` is the unique identifier of the type of value required. : type string
        :param template_tag : A `template_tag` is the identifier of the type of template required. : type string
        :param item_type : A `item_type` is the identifier of the type of template required. : type string
        """
        payload = {}
        
        if filter:
            payload["filter"] = filter
        
        if template_tag:
            payload["template_tag"] = template_tag
        
        if item_type:
            payload["item_type"] = item_type
        

        # Parameter validation
        schema = CatalogValidator.listTemplateBrandTypeValues()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/downloads/configuration/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"filter","description":"A `filter` is the unique identifier of the type of value required.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"template_tag","description":"A `template_tag` is the identifier of the type of template required.","schema":{"type":"string"},"required":false},{"in":"query","name":"item_type","description":"A `item_type` is the identifier of the type of template required.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"filter","description":"A `filter` is the unique identifier of the type of value required.","schema":{"type":"string"},"required":true},{"in":"query","name":"template_tag","description":"A `template_tag` is the identifier of the type of template required.","schema":{"type":"string"},"required":false},{"in":"query","name":"item_type","description":"A `item_type` is the identifier of the type of template required.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", filter=filter, template_tag=template_tag, item_type=item_type)
        query_string = await create_query_string(filter=filter, template_tag=template_tag, item_type=item_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/downloads/configuration/", filter=filter, template_tag=template_tag, item_type=item_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createCategories(self, body=""):
        """This API lets user create product categories
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCategories()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CategoryRequestBody
        schema = CategoryRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def listCategories(self, level=None, department=None, q=None, page_no=None, page_size=None):
        """This API gets meta associated to product categories.
        :param level : Get category for multiple levels : type string
        :param department : Get category for multiple departments filtered : type string
        :param q : Get multiple categories filtered by search string : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if level:
            payload["level"] = level
        
        if department:
            payload["department"] = department
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.listCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"level","description":"Get category for multiple levels","schema":{"type":"string"},"required":false,"example":1},{"in":"query","name":"department","description":"Get category for multiple departments filtered","schema":{"type":"string"},"required":false,"example":10},{"in":"query","name":"q","description":"Get multiple categories filtered by search string","schema":{"type":"string"},"required":false,"example":"test-item"},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"level","description":"Get category for multiple levels","schema":{"type":"string"},"required":false,"example":1},{"in":"query","name":"department","description":"Get category for multiple departments filtered","schema":{"type":"string"},"required":false,"example":10},{"in":"query","name":"q","description":"Get multiple categories filtered by search string","schema":{"type":"string"},"required":false,"example":"test-item"},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", level=level, department=department, q=q, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(level=level, department=department, q=q, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/", level=level, department=department, q=q, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateCategory(self, uid=None, body=""):
        """Update a product category using this apu
        :param uid : Category unique id : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.updateCategory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CategoryRequestBody
        schema = CategoryRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/{uid}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"Category unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"Category unique id","schema":{"type":"string"},"required":true}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/{uid}/", uid=uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getCategoryData(self, uid=None):
        """This API gets meta associated to product categories.
        :param uid : Category unique id : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.getCategoryData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/{uid}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"Category unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"Category unique id","schema":{"type":"string"},"required":true}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/{uid}/", uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createProduct(self, body=""):
        """This API allows to create product.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductCreateUpdateSchemaV2
        schema = ProductCreateUpdateSchemaV2()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProducts(self, brand_ids=None, category_ids=None, item_ids=None, department_ids=None, item_code=None, q=None, tags=None, page_no=None, page_size=None):
        """This API gets meta associated to products.
        :param brand_ids : Get multiple products filtered by Brand Ids : type array
        :param category_ids : Get multiple products filtered by Category Ids : type array
        :param item_ids : Get multiple products filtered by Item Ids : type array
        :param department_ids : Get multiple products filtered by Department Ids : type array
        :param item_code : Get multiple products filtered by Item Code : type array
        :param q : Get multiple products filtered by q string : type string
        :param tags : Get multiple products filtered by tags : type array
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if brand_ids:
            payload["brand_ids"] = brand_ids
        
        if category_ids:
            payload["category_ids"] = category_ids
        
        if item_ids:
            payload["item_ids"] = item_ids
        
        if department_ids:
            payload["department_ids"] = department_ids
        
        if item_code:
            payload["item_code"] = item_code
        
        if q:
            payload["q"] = q
        
        if tags:
            payload["tags"] = tags
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/", """{"required":[{"in":"path","name":"company_id","description":"Get list of products filtered by company Id","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_ids","description":"Get multiple products filtered by Item Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_code","description":"Get multiple products filtered by Item Code","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"q","description":"Get multiple products filtered by q string","schema":{"type":"string"},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"query":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_ids","description":"Get multiple products filtered by Item Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_code","description":"Get multiple products filtered by Item Code","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"q","description":"Get multiple products filtered by q string","schema":{"type":"string"},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Get list of products filtered by company Id","schema":{"type":"integer"},"required":true}]}""", brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, q=q, tags=tags, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, q=q, tags=tags, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/", brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, q=q, tags=tags, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getVariantsOfProducts(self, item_id=None, variant_type=None, page_no=None, page_size=None):
        """This API gets meta associated to products.
        :param item_id : Get list of variants of item Id : type integer
        :param variant_type : Get multiple products filtered by variant type : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if variant_type:
            payload["variant_type"] = variant_type
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getVariantsOfProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/variants/{variant_type}", """{"required":[{"in":"path","name":"company_id","description":"Get list of products filtered by company Id","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Get list of variants of item Id","schema":{"type":"integer"},"required":true},{"in":"path","name":"variant_type","description":"Get multiple products filtered by variant type","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Get list of products filtered by company Id","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Get list of variants of item Id","schema":{"type":"integer"},"required":true},{"in":"path","name":"variant_type","description":"Get multiple products filtered by variant type","schema":{"type":"string"},"required":true}]}""", item_id=item_id, variant_type=variant_type, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(item_id=item_id, variant_type=variant_type, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/variants/{variant_type}", item_id=item_id, variant_type=variant_type, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getProductAttributes(self, category=None, filter=None):
        """This API allows to list all the attributes by their l3_categories.
        :param category : It is the name of the l3 cateogry : type string
        :param filter : If true, returns filtered values, else returns all the attributes : type boolean
        """
        payload = {}
        
        if category:
            payload["category"] = category
        
        if filter:
            payload["filter"] = filter
        

        # Parameter validation
        schema = CatalogValidator.getProductAttributes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/", """{"required":[{"in":"path","name":"company_id","description":"company for which you want to view the genders","schema":{"type":"integer"},"required":true},{"in":"query","name":"category","description":"It is the name of the l3 cateogry","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"filter","description":"If true, returns filtered values, else returns all the attributes","schema":{"type":"boolean"},"required":false}],"query":[{"in":"query","name":"category","description":"It is the name of the l3 cateogry","schema":{"type":"string"},"required":true},{"in":"query","name":"filter","description":"If true, returns filtered values, else returns all the attributes","schema":{"type":"boolean"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"company for which you want to view the genders","schema":{"type":"integer"},"required":true}]}""", category=category, filter=filter)
        query_string = await create_query_string(category=category, filter=filter)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/", category=category, filter=filter), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def editProduct(self, item_id=None, body=""):
        """This API allows to edit product.
        :param item_id : Id of the product to be updated. : type integer
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        

        # Parameter validation
        schema = CatalogValidator.editProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductCreateUpdateSchemaV2
        schema = ProductCreateUpdateSchemaV2()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}]}""", item_id=item_id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", item_id=item_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteProduct(self, item_id=None):
        """This API allows to delete product.
        :param item_id : Id of the product to be updated. : type integer
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        

        # Parameter validation
        schema = CatalogValidator.deleteProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated to product that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the company associated to product that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}]}""", item_id=item_id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", item_id=item_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getProduct(self, item_id=None, brand_uid=None, item_code=None):
        """This API helps to get data associated to a particular product.
        :param item_id : Item Id of the product. : type integer
        :param brand_uid : Brand Id of the product. : type integer
        :param item_code : Item code of the product. : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if brand_uid:
            payload["brand_uid"] = brand_uid
        
        if item_code:
            payload["item_code"] = item_code
        

        # Parameter validation
        schema = CatalogValidator.getProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the product.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"brand_uid","description":"Brand Id of the product.","schema":{"type":"integer"},"required":false},{"in":"query","name":"item_code","description":"Item code of the product.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"brand_uid","description":"Brand Id of the product.","schema":{"type":"integer"},"required":false},{"in":"query","name":"item_code","description":"Item code of the product.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the product.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product.","schema":{"type":"integer"},"required":true}]}""", item_id=item_id, brand_uid=brand_uid, item_code=item_code)
        query_string = await create_query_string(item_id=item_id, brand_uid=brand_uid, item_code=item_code)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", item_id=item_id, brand_uid=brand_uid, item_code=item_code), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def allSizes(self, item_id=None):
        """This API allows to get  All Sizes for a given Product.
        :param item_id : Id of the product to be updated. : type integer
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        

        # Parameter validation
        schema = CatalogValidator.allSizes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/all_sizes", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}]}""", item_id=item_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/all_sizes", item_id=item_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getProductValidation(self, ):
        """This API validates product data.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getProductValidation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/validation/", """{"required":[{"in":"path","name":"company_id","description":"Validates data against given company","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Validates data against given company","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/validation/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getProductSize(self, item_code=None, item_id=None, brand_uid=None, uid=None):
        """This API helps to get data associated to a particular product size.
        :param item_code : Item code of the product size. : type string
        :param item_id : Item Id of the product size. : type integer
        :param brand_uid : Brand Id of the product size. : type integer
        :param uid : Id of the product size. : type integer
        """
        payload = {}
        
        if item_code:
            payload["item_code"] = item_code
        
        if item_id:
            payload["item_id"] = item_id
        
        if brand_uid:
            payload["brand_uid"] = brand_uid
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.getProductSize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the product size.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product size.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"item_code","description":"Item code of the product size.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_uid","description":"Brand Id of the product size.","schema":{"type":"integer"},"required":false},{"in":"query","name":"uid","description":"Id of the product size.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"item_code","description":"Item code of the product size.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_uid","description":"Brand Id of the product size.","schema":{"type":"integer"},"required":false},{"in":"query","name":"uid","description":"Id of the product size.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the product size.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product size.","schema":{"type":"integer"},"required":true}]}""", item_code=item_code, item_id=item_id, brand_uid=brand_uid, uid=uid)
        query_string = await create_query_string(item_code=item_code, item_id=item_id, brand_uid=brand_uid, uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/", item_code=item_code, item_id=item_id, brand_uid=brand_uid, uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createBulkProductUploadJob(self, body=""):
        """This API helps to create a bulk products upload job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createBulkProductUploadJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkJob
        schema = BulkJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProductBulkUploadHistory(self, search=None, page_no=None, page_size=None):
        """This API helps to get bulk product upload jobs data.
        :param search : Search string to filter the results by batch id : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if search:
            payload["search"] = search
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getProductBulkUploadHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", """{"required":[{"in":"path","name":"company_id","description":"Company Id of of which Product Bulk Upload History to be obtained.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"search","description":"Search string to filter the results by batch id","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"search","description":"Search string to filter the results by batch id","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of of which Product Bulk Upload History to be obtained.","schema":{"type":"integer"},"required":true}]}""", search=search, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(search=search, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", search=search, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def uploadBulkProducts(self, department=None, product_type=None, body=""):
        """This API helps to create a bulk products upload job.
        :param department : Department of the product to be uploaded. : type string
        :param product_type : Product type of the product to be uploaded i.e. set, standard , digital. : type string
        """
        payload = {}
        
        if department:
            payload["department"] = department
        
        if product_type:
            payload["product_type"] = product_type
        

        # Parameter validation
        schema = CatalogValidator.uploadBulkProducts()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkJob
        schema = BulkJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/bulk", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"query","name":"department","description":"Department of the product to be uploaded.","schema":{"type":"string"},"required":true},{"in":"query","name":"product_type","description":"Product type of the product to be uploaded i.e. set, standard , digital.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"department","description":"Department of the product to be uploaded.","schema":{"type":"string"},"required":true},{"in":"query","name":"product_type","description":"Product type of the product to be uploaded i.e. set, standard , digital.","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}]}""", department=department, product_type=product_type)
        query_string = await create_query_string(department=department, product_type=product_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/bulk", department=department, product_type=product_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def createProductsInBulk(self, batch_id=None, body=""):
        """This API helps to create products in bulk push to kafka for approval/creation.
        :param batch_id : Batch Id in which assets to be uploaded. : type string
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.createProductsInBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkProductRequest
        schema = BulkProductRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id in which assets to be uploaded.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id in which assets to be uploaded.","schema":{"type":"string"},"required":true}]}""", batch_id=batch_id)
        query_string = await create_query_string(batch_id=batch_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", batch_id=batch_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteProductBulkJob(self, batch_id=None):
        """This API allows to delete bulk product job associated with company.
        :param batch_id : Batch Id of the bulk product job to be deleted. : type integer
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.deleteProductBulkJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated to size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk product job to be deleted.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the company associated to size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk product job to be deleted.","schema":{"type":"integer"},"required":true}]}""", batch_id=batch_id)
        query_string = await create_query_string(batch_id=batch_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getProductTags(self, ):
        """This API helps to get tags data associated to a particular company.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getProductTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/tags", """{"required":[{"in":"path","name":"company_id","description":"Company Id for which tags to be fetched.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id for which tags to be fetched.","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/tags", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createProductAssetsInBulk(self, body=""):
        """This API helps to create a bulk asset upload job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createProductAssetsInBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductBulkAssets
        schema = ProductBulkAssets()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProductAssetsInBulk(self, page_no=None, page_size=None):
        """This API helps to get bulk asset jobs data associated to a particular company.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getProductAssetsInBulk()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the product size.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the product size.","schema":{"type":"integer"},"required":true}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def deleteSize(self, item_id=None, size=None):
        """This API allows to delete size associated with product.
        :param item_id : Item Id of the product associated with size to be deleted. : type integer
        :param size : size to be deleted. : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if size:
            payload["size"] = size
        

        # Parameter validation
        schema = CatalogValidator.deleteSize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated to size that is to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product associated with size to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"size","description":"size to be deleted.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the company associated to size that is to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product associated with size to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"size","description":"size to be deleted.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, size=size)
        query_string = await create_query_string(item_id=item_id, size=size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", item_id=item_id, size=size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def addInventory(self, item_id=None, size=None, body=""):
        """This API allows add Inventory for particular size and store.
        :param item_id : Item code of the product of which size is to be get. : type integer
        :param size : Size in which inventory is to be added. : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if size:
            payload["size"] = size
        

        # Parameter validation
        schema = CatalogValidator.addInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryRequest
        schema = InventoryRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"integer"},"required":true},{"in":"path","name":"size","description":"Size in which inventory is to be added.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"integer"},"required":true},{"in":"path","name":"size","description":"Size in which inventory is to be added.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, size=size)
        query_string = await create_query_string(item_id=item_id, size=size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", item_id=item_id, size=size), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getInventoryBySize(self, item_id=None, size=None, page_no=None, page_size=None, q=None, sellable=None):
        """This API allows get Inventory data for particular company grouped by size and store.
        :param item_id : Item code of the product of which size is to be get. : type string
        :param size : Size of which inventory is to get. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search with help of store code. : type string
        :param sellable : Filter on whether product is in stock or not. : type boolean
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if size:
            payload["size"] = size
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if sellable:
            payload["sellable"] = sellable
        

        # Parameter validation
        schema = CatalogValidator.getInventoryBySize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"Size of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"sellable","description":"Filter on whether product is in stock or not.","schema":{"type":"boolean","default":false},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"sellable","description":"Filter on whether product is in stock or not.","schema":{"type":"boolean","default":false},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"Size of which inventory is to get.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable)
        query_string = await create_query_string(item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getInventoryBySizeIdentifier(self, item_id=None, size_identifier=None, page_no=None, page_size=None, q=None, location_ids=None):
        """This API allows get Inventory data for particular company grouped by size and store.
        :param item_id : Item code of the product of which size is to be get. : type string
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
        schema = CatalogValidator.getInventoryBySizeIdentifier()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/inventory/{size_identifier}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":true},{"in":"path","name":"size_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"location_ids","description":"Search by store ids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"location_ids","description":"Search by store ids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":true},{"in":"path","name":"size_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/inventory/{size_identifier}", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getInventories(self, item_id=None, size=None, page_no=None, page_size=None, q=None, sellable=None, store_ids=None, size_identifier=None):
        """This API allows get Inventories data for particular company.
        :param item_id : Item code of the product of which size is to be get. : type string
        :param size : Size of which inventory is to get. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search with help of store code. : type string
        :param sellable : Filter on whether product is in stock or not. : type boolean
        :param store_ids : The Store Id of products to fetch inventory. : type array
        :param size_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if size:
            payload["size"] = size
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if sellable:
            payload["sellable"] = sellable
        
        if store_ids:
            payload["store_ids"] = store_ids
        
        if size_identifier:
            payload["size_identifier"] = size_identifier
        

        # Parameter validation
        schema = CatalogValidator.getInventories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventories", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":false},{"in":"query","name":"size","description":"Size of which inventory is to get.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"sellable","description":"Filter on whether product is in stock or not.","schema":{"type":"boolean","default":false},"required":false},{"in":"query","name":"store_ids","description":"The Store Id of products to fetch inventory.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"size_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":false},{"in":"query","name":"size","description":"Size of which inventory is to get.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"sellable","description":"Filter on whether product is in stock or not.","schema":{"type":"boolean","default":false},"required":false},{"in":"query","name":"store_ids","description":"The Store Id of products to fetch inventory.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"size_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable, store_ids=store_ids, size_identifier=size_identifier)
        query_string = await create_query_string(item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable, store_ids=store_ids, size_identifier=size_identifier)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventories", item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable, store_ids=store_ids, size_identifier=size_identifier), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def deleteInventory(self, size=None, item_id=None, location_id=None):
        """This API allows to delete inventory of a particular product for particular company.
        :param size : size that is to be deleted. : type string
        :param item_id : Id of the product associated with Inventory to be deleted. : type integer
        :param location_id : Location ID of store of which inventory is to be deleted. : type number
        """
        payload = {}
        
        if size:
            payload["size"] = size
        
        if item_id:
            payload["item_id"] = item_id
        
        if location_id:
            payload["location_id"] = location_id
        

        # Parameter validation
        schema = CatalogValidator.deleteInventory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}/location/{location_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated with Inventory that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product associated with Inventory to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"location_id","description":"Location ID of store of which inventory is to be deleted.","schema":{"type":"number"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the company associated with Inventory that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product associated with Inventory to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"location_id","description":"Location ID of store of which inventory is to be deleted.","schema":{"type":"number"},"required":true}]}""", size=size, item_id=item_id, location_id=location_id)
        query_string = await create_query_string(size=size, item_id=item_id, location_id=location_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}/location/{location_id}/", size=size, item_id=item_id, location_id=location_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createBulkInventoryJob(self, body=""):
        """This API helps to create a bulk Inventory upload job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createBulkInventoryJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkJob
        schema = BulkJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which Inventory to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which Inventory to be uploaded.","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getInventoryBulkUploadHistory(self, page_no=None, page_size=None):
        """This API helps to get bulk Inventory upload jobs data.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getInventoryBulkUploadHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of of which Inventory Bulk Upload History to be obtained.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of of which Inventory Bulk Upload History to be obtained.","schema":{"type":"integer"},"required":true}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createBulkInventory(self, batch_id=None, body=""):
        """This API helps to create products in bulk push to kafka for approval/creation.
        :param batch_id : Batch Id of the bulk create job. : type string
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.createBulkInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryBulkRequest
        schema = InventoryBulkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which Inventory is to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk create job.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which Inventory is to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk create job.","schema":{"type":"string"},"required":true}]}""", batch_id=batch_id)
        query_string = await create_query_string(batch_id=batch_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", batch_id=batch_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteBulkInventoryJob(self, batch_id=None):
        """This API allows to delete bulk Inventory job associated with company.
        :param batch_id : Batch Id of the bulk delete job. : type string
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.deleteBulkInventoryJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company of which bulk Inventory job is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk delete job.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the company of which bulk Inventory job is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk delete job.","schema":{"type":"string"},"required":true}]}""", batch_id=batch_id)
        query_string = await create_query_string(batch_id=batch_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createInventoryExportJob(self, body=""):
        """This API helps to create a Inventory export job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createInventoryExportJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryExportRequest
        schema = InventoryExportRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getInventoryExport(self, ):
        """This API helps to get Inventory export history.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getInventoryExport()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createInventoryExport(self, body=""):
        """This API helps to create a Inventory export job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createInventoryExport()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryCreateRequest
        schema = InventoryCreateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def listInventoryExport(self, status=None, from_date=None, to_date=None, q=None):
        """This API helps you the get the history of inventory jobs depending on the filtered criteria.
        :param status : Status of the export job. : type string
        :param from_date : Inventory export history filtered according to from_date. : type string
        :param to_date : Inventory export history filtered according to from_date. : type string
        :param q : Inventory export history filtered according to task ID. : type string
        """
        payload = {}
        
        if status:
            payload["status"] = status
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.listInventoryExport()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/", """{"required":[{"in":"path","name":"company_id","description":"It is the unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"status","description":"Status of the export job.","schema":{"type":"string"},"required":false},{"in":"query","name":"from_date","description":"Inventory export history filtered according to from_date.","schema":{"type":"string"},"required":false},{"in":"query","name":"to_date","description":"Inventory export history filtered according to from_date.","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Inventory export history filtered according to task ID.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"status","description":"Status of the export job.","schema":{"type":"string"},"required":false},{"in":"query","name":"from_date","description":"Inventory export history filtered according to from_date.","schema":{"type":"string"},"required":false},{"in":"query","name":"to_date","description":"Inventory export history filtered according to from_date.","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Inventory export history filtered according to task ID.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"It is the unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", status=status, from_date=from_date, to_date=to_date, q=q)
        query_string = await create_query_string(status=status, from_date=from_date, to_date=to_date, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/", status=status, from_date=from_date, to_date=to_date, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateInventoryExportJob(self, job_id=None, body=""):
        """This API helps to update the status and the notification email of the running export jobs.
        :param job_id : Job Id in which assets to be uploaded. : type string
        """
        payload = {}
        
        if job_id:
            payload["job_id"] = job_id
        

        # Parameter validation
        schema = CatalogValidator.updateInventoryExportJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryPartialExportRequest
        schema = InventoryPartialExportRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/{job_id}", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"job_id","description":"Job Id in which assets to be uploaded.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"job_id","description":"Job Id in which assets to be uploaded.","schema":{"type":"string"},"required":true}]}""", job_id=job_id)
        query_string = await create_query_string(job_id=job_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/{job_id}", job_id=job_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getInventoryExportJobDetail(self, job_id=None):
        """This API gives you the details information of an invnetory export job by their job id.
        :param job_id : This is the id of the job. : type string
        """
        payload = {}
        
        if job_id:
            payload["job_id"] = job_id
        

        # Parameter validation
        schema = CatalogValidator.getInventoryExportJobDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/{job_id}", """{"required":[{"in":"path","name":"company_id","description":"This is the uid of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"job_id","description":"This is the id of the job.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"This is the uid of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"job_id","description":"This is the id of the job.","schema":{"type":"string"},"required":true}]}""", job_id=job_id)
        query_string = await create_query_string(job_id=job_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/{job_id}", job_id=job_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def exportInventoryConfig(self, filter_type=None):
        """This API allows get List of different filters like brand, store, and type for inventory export.
        :param filter_type : filter type from any one of ['brand', 'store', 'type'] : type string
        """
        payload = {}
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = CatalogValidator.exportInventoryConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/configuration/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"filter_type","description":"filter type from any one of ['brand', 'store', 'type']","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"filter_type","description":"filter type from any one of ['brand', 'store', 'type']","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}]}""", filter_type=filter_type)
        query_string = await create_query_string(filter_type=filter_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/configuration/", filter_type=filter_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateRealtimeInventory(self, item_id=None, seller_identifier=None, body=""):
        """This API allows add Inventory for particular size and store.
        :param item_id : Item code of the product of which size is to be get. : type integer
        :param seller_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if seller_identifier:
            payload["seller_identifier"] = seller_identifier
        

        # Parameter validation
        schema = CatalogValidator.updateRealtimeInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryRequestSchemaV2
        schema = InventoryRequestSchemaV2()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"integer"},"required":true},{"in":"path","name":"seller_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"integer"},"required":true},{"in":"path","name":"seller_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, seller_identifier=seller_identifier)
        query_string = await create_query_string(item_id=item_id, seller_identifier=seller_identifier)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}/", item_id=item_id, seller_identifier=seller_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteRealtimeInventory(self, item_id=None, seller_identifier=None, body=""):
        """This API allows add Inventory for particular size and store.
        :param item_id : Item code of the product of which size is to be get. : type integer
        :param seller_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if seller_identifier:
            payload["seller_identifier"] = seller_identifier
        

        # Parameter validation
        schema = CatalogValidator.deleteRealtimeInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryRequestSchemaV2
        schema = InventoryRequestSchemaV2()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"integer"},"required":true},{"in":"path","name":"seller_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"integer"},"required":true},{"in":"path","name":"seller_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, seller_identifier=seller_identifier)
        query_string = await create_query_string(item_id=item_id, seller_identifier=seller_identifier)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}/", item_id=item_id, seller_identifier=seller_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateInventories(self, body=""):
        """This API allows add Inventory for particular size and store.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateInventories()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryRequestSchemaV2
        schema = InventoryRequestSchemaV2()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateHsnCode(self, id=None, body=""):
        """Update Hsn Code.
        :param id : Unique id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateHsnCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import HsnUpsert
        schema = HsnUpsert()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Unique id","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getHsnCode(self, id=None):
        """Fetch Hsn Code.
        :param id : Unique id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getHsnCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Unique id","schema":{"type":"string"},"required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def bulkHsnCode(self, body=""):
        """Bulk Create or Update Hsn Code.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.bulkHsnCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkHsnUpsert
        schema = BulkHsnUpsert()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/bulk/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/bulk/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAllProductHsnCodes(self, page_no=None, page_size=None, q=None, type=None):
        """Hsn Code List.
        :param page_no : page no : type integer
        :param page_size : page size : type integer
        :param q : search using hsn code, description, reporting_hsn : type string
        :param type : search using type : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if type:
            payload["type"] = type
        

        # Parameter validation
        schema = CatalogValidator.getAllProductHsnCodes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/", """{"required":[{"in":"path","name":"company_id","description":"Company Id for which HSN codes needs to be fetched","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"page no","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"search using hsn code, description, reporting_hsn","schema":{"type":"string"},"required":false},{"in":"query","name":"type","description":"search using type","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"page no","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"search using hsn code, description, reporting_hsn","schema":{"type":"string"},"required":false},{"in":"query","name":"type","description":"search using type","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id for which HSN codes needs to be fetched","schema":{"type":"integer"},"required":true}]}""", page_no=page_no, page_size=page_size, q=q, type=type, )
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, type=type, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/", page_no=page_no, page_size=page_size, q=q, type=type, ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSingleProductHSNCode(self, reporting_hsn=None):
        """Hsn Code List.
        :param reporting_hsn : reporting_hsn : type string
        """
        payload = {}
        
        if reporting_hsn:
            payload["reporting_hsn"] = reporting_hsn
        

        # Parameter validation
        schema = CatalogValidator.getSingleProductHSNCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/{reporting_hsn}", """{"required":[{"in":"path","name":"reporting_hsn","description":"reporting_hsn","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"Company Id for which HSN codes needs to be fetched","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"reporting_hsn","description":"reporting_hsn","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"Company Id for which HSN codes needs to be fetched","schema":{"type":"integer"},"required":true}]}""", reporting_hsn=reporting_hsn, )
        query_string = await create_query_string(reporting_hsn=reporting_hsn, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/{reporting_hsn}", reporting_hsn=reporting_hsn, ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOptimalLocations(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getOptimalLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AssignStore
        schema = AssignStore()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/location/reassign/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/location/reassign/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

