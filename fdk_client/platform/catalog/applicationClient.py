"""Catalog Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import CatalogValidator

class Catalog:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def getCatalogInsights(self, brand=None, request_headers:Dict={}):
        """Retrieve the count of catalog related data like products, brands, departments and categories that have been made live as per configuration of the application.
        :param brand : Brand slug : type string
        """
        payload = {}
        
        if brand is not None:
            payload["brand"] = brand

        # Parameter validation
        schema = CatalogValidator.getCatalogInsights()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/analytics/insights", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Brand slug","in":"query","name":"brand","required":false,"schema":{"type":"string"}}],"query":[{"description":"Brand slug","in":"query","name":"brand","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", brand=brand)
        query_string = await create_query_string(brand=brand)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/analytics/insights", brand=brand), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CatalogInsightResponse
            schema = CatalogInsightResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCatalogInsights")
                print(e)

        return response
    
    async def getApplicationBrandListing(self, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Retrieve brand listings related to the application. A brand is the name under which a product is being sold
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name.Use this parameter to search brands by brand name. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationBrandListingSchema
            schema = ApplicationBrandListingSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationBrandListing")
                print(e)

        return response
    
    async def updateAppBrand(self, brand_uid=None, body="", request_headers:Dict={}):
        """Modify data associated to a item custom meta.
        :param brand_uid : brand id for which the custom_json is associated. : type integer
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand/{brand_uid}", """{"required":[{"description":"Id of the company associated to brand custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"brand id for which the custom_json is associated.","in":"path","name":"brand_uid","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to brand custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"brand id for which the custom_json is associated.","in":"path","name":"brand_uid","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", brand_uid=brand_uid)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand/{brand_uid}", brand_uid=brand_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppBrand")
                print(e)

        return response
    
    async def getApplicationBrands(self, department=None, page_no=None, page_size=None, q=None, brand_id=None, request_headers:Dict={}):
        """List all the brands. A brand is the name under which a product is being sold.
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name.Use this parameter to search brands by brand name. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brands", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","in":"query","name":"department","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Helps to sort the brands list on the basis of uid list.","in":"query","name":"brand_id","required":false,"schema":{"type":"array","items":{"type":"integer"}}}],"query":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","in":"query","name":"department","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Helps to sort the brands list on the basis of uid list.","in":"query","name":"brand_id","required":false,"schema":{"type":"array","items":{"type":"integer"}}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id)
        query_string = await create_query_string(department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brands", department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BrandListingResponse
            schema = BrandListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationBrands")
                print(e)

        return response
    
    async def getCategories(self, department=None, request_headers:Dict={}):
        """Retrieve a list of categories. Optionally pass filter the brands by the department.
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API : type string
        """
        payload = {}
        
        if department is not None:
            payload["department"] = department

        # Parameter validation
        schema = CatalogValidator.getCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","in":"query","name":"department","required":false,"schema":{"type":"string"}}],"query":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","in":"query","name":"department","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", department=department)
        query_string = await create_query_string(department=department)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/categories", department=department), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CategoryListingResponse
            schema = CategoryListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCategories")
                print(e)

        return response
    
    async def getApplicationCategoryListing(self, department_id=None, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Retrieve category listings related to the application. A brand is the name under which a product is being sold.
        :param department_id : A `department_id` is a unique identifier for a particular department. : type integer
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name.Use this parameter to search brands by brand name. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"A `department_id` is a unique identifier for a particular department.","in":"query","name":"department_id","required":false,"schema":{"type":"integer"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"A `department_id` is a unique identifier for a particular department.","in":"query","name":"department_id","required":false,"schema":{"type":"integer"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", department_id=department_id, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(department_id=department_id, page_no=page_no, page_size=page_size, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category", department_id=department_id, page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationCategoryListingSchema
            schema = ApplicationCategoryListingSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationCategoryListing")
                print(e)

        return response
    
    async def updateAppCategory(self, category_uid=None, body="", request_headers:Dict={}):
        """Modify category data related to the application. Helps to update data associated to a item custom meta.
        :param category_uid : category id for which the custom_json is associated. : type integer
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category/{category_uid}", """{"required":[{"description":"Id of the company associated to category custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"category id for which the custom_json is associated.","in":"path","name":"category_uid","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to category custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"category id for which the custom_json is associated.","in":"path","name":"category_uid","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", category_uid=category_uid)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category/{category_uid}", category_uid=category_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCategory")
                print(e)

        return response
    
    async def createCollection(self, body="", request_headers:Dict={}):
        """Create a collection to the catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCollection()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateCollection
        schema = CreateCollection()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CollectionCreateResponse
            schema = CollectionCreateResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCollection")
                print(e)

        return response
    
    async def getAllCollections(self, q=None, schedule_status=None, type=None, tag=None, is_active=None, page_no=None, page_size=None, request_headers:Dict={}):
        """A Collection allows you to organize your products into hierarchical groups.
        :param q : Get collection list filtered by q string, : type string
        :param schedule_status : Get collection list filtered by scheduled status, : type string
        :param type : type of the collections : type string
        :param tag : Each response will contain next_id param, which should be sent back to make pagination work. : type array
        :param is_active : get collections filtered by active status. : type boolean
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Get collection list filtered by q string,","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Get collection list filtered by scheduled status,","in":"query","name":"schedule_status","required":false,"schema":{"enum":["live","upcoming","expired"],"type":"string"}},{"description":"type of the collections","in":"query","name":"type","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"tag","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"get collections filtered by active status.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"query":[{"description":"Get collection list filtered by q string,","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Get collection list filtered by scheduled status,","in":"query","name":"schedule_status","required":false,"schema":{"enum":["live","upcoming","expired"],"type":"string"}},{"description":"type of the collections","in":"query","name":"type","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"tag","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"get collections filtered by active status.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", q=q, schedule_status=schedule_status, type=type, tag=tag, is_active=is_active, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(q=q, schedule_status=schedule_status, type=type, tag=tag, is_active=is_active, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections", q=q, schedule_status=schedule_status, type=type, tag=tag, is_active=is_active, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionListingResponse
            schema = GetCollectionListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllCollections")
                print(e)

        return response
    
    async def getApplicationFilterValues(self, filter_key=None, c=None, collection_id=None, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Get query filters keys to configure a collection
        :param filter_key : A `filter_key` is a filter key for a for which all the available filter values will returned. channel. : type string
        :param c : The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts** : type string
        :param collection_id : A `collection_id` is a unique identifier for a particular collection. channel. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param q : Get Values filtered by q string : type string
        """
        payload = {}
        
        if filter_key is not None:
            payload["filter_key"] = filter_key
        if c is not None:
            payload["c"] = c
        if collection_id is not None:
            payload["collection_id"] = collection_id
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = CatalogValidator.getApplicationFilterValues()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/filter-options/{filter_key}/values", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `filter_key` is a filter key for a for which all the available filter values will returned. channel.","in":"path","name":"filter_key","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","in":"query","name":"c","required":false,"schema":{"type":"string"}},{"description":"A `collection_id` is a unique identifier for a particular collection. channel.","in":"query","name":"collection_id","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"Get Values filtered by q string","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","in":"query","name":"c","required":false,"schema":{"type":"string"}},{"description":"A `collection_id` is a unique identifier for a particular collection. channel.","in":"query","name":"collection_id","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"Get Values filtered by q string","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `filter_key` is a filter key for a for which all the available filter values will returned. channel.","in":"path","name":"filter_key","required":true,"schema":{"type":"string"}}]}""", serverType="platform", filter_key=filter_key, c=c, collection_id=collection_id, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(c=c, collection_id=collection_id, page_no=page_no, page_size=page_size, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/filter-options/{filter_key}/values", filter_key=filter_key, c=c, collection_id=collection_id, page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetQueryFiltersValuesResponse
            schema = GetQueryFiltersValuesResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationFilterValues")
                print(e)

        return response
    
    async def getApplicationFilterKeys(self, c=None, request_headers:Dict={}):
        """Get query filters keys to configure a collection
        :param c : The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts** : type string
        """
        payload = {}
        
        if c is not None:
            payload["c"] = c

        # Parameter validation
        schema = CatalogValidator.getApplicationFilterKeys()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/filter-options/keys", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","in":"query","name":"c","required":false,"schema":{"type":"string"}}],"query":[{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","in":"query","name":"c","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", c=c)
        query_string = await create_query_string(c=c)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/filter-options/keys", c=c), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetQueryFiltersKeysResponse
            schema = GetQueryFiltersKeysResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationFilterKeys")
                print(e)

        return response
    
    async def getQueryFilters(self, request_headers:Dict={}):
        """Retrieve query filters to configure a collection
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getQueryFilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetQueryFiltersResponse
            schema = GetQueryFiltersResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getQueryFilters")
                print(e)

        return response
    
    async def getCollectionItems(self, id=None, sort_on=None, page_size=None, page_no=None, is_pinned=None, q=None, is_excluded=None, request_headers:Dict={}):
        """Get items from a collection specified by its `id`.
        :param id : A `id` is a unique identifier of a collection. : type string
        :param sort_on : Each response will contain sort_on param, which should be sent back to make pagination work. : type string
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param page_no : Identifies the specific page of results being requested. : type integer
        :param is_pinned : Number of items that are pinned and have priority in each page. Default is 12. : type boolean
        :param q : Get multiple products filtered by q string : type string
        :param is_excluded : Number of items that are excluded from collections in each page. Default is 12. : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if sort_on is not None:
            payload["sort_on"] = sort_on
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no
        if is_pinned is not None:
            payload["is_pinned"] = is_pinned
        if q is not None:
            payload["q"] = q
        if is_excluded is not None:
            payload["is_excluded"] = is_excluded

        # Parameter validation
        schema = CatalogValidator.getCollectionItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Each response will contain sort_on param, which should be sent back to make pagination work.","in":"query","name":"sort_on","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Identifies the specific page of results being requested.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items that are pinned and have priority in each page. Default is 12.","in":"query","name":"is_pinned","required":false,"schema":{"type":"boolean"}},{"description":"Get multiple products filtered by q string","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Number of items that are excluded from collections in each page. Default is 12.","in":"query","name":"is_excluded","required":false,"schema":{"type":"boolean"}}],"query":[{"description":"Each response will contain sort_on param, which should be sent back to make pagination work.","in":"query","name":"sort_on","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Identifies the specific page of results being requested.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items that are pinned and have priority in each page. Default is 12.","in":"query","name":"is_pinned","required":false,"schema":{"type":"boolean"}},{"description":"Get multiple products filtered by q string","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Number of items that are excluded from collections in each page. Default is 12.","in":"query","name":"is_excluded","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id, sort_on=sort_on, page_size=page_size, page_no=page_no, is_pinned=is_pinned, q=q, is_excluded=is_excluded)
        query_string = await create_query_string(sort_on=sort_on, page_size=page_size, page_no=page_no, is_pinned=is_pinned, q=q, is_excluded=is_excluded)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items", id=id, sort_on=sort_on, page_size=page_size, page_no=page_no, is_pinned=is_pinned, q=q, is_excluded=is_excluded), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionItemsResponseSchema
            schema = GetCollectionItemsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCollectionItems")
                print(e)

        return response
    
    async def clearCollectionItemsPriority(self, id=None, request_headers:Dict={}):
        """Clear priorities set for collection items.
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.clearCollectionItemsPriority()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CommonResponseSchemaCollection
            schema = CommonResponseSchemaCollection()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for clearCollectionItemsPriority")
                print(e)

        return response
    
    async def addCollectionItems(self, id=None, body="", request_headers:Dict={}):
        """Adds items to a collection specified by its `id`. See `CollectionItemRequest` for the list of attributes needed to add items to an collection.
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.addCollectionItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CollectionItemUpdateSchema
        schema = CollectionItemUpdateSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CommonResponseSchemaCollection
            schema = CommonResponseSchemaCollection()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addCollectionItems")
                print(e)

        return response
    
    async def getCollectionDetail(self, slug=None, request_headers:Dict={}):
        """Get the details of a collection by its slug.
        :param slug : A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getCollectionDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{slug}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionDetailResponse
            schema = GetCollectionDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCollectionDetail")
                print(e)

        return response
    
    async def updateCollection(self, id=None, body="", request_headers:Dict={}):
        """Update a collection by it's id. On successful request, returns the updated collection
        :param id : A `id` is a unique identifier of a collection. : type string
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateCollection
            schema = UpdateCollection()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCollection")
                print(e)

        return response
    
    async def deleteCollection(self, id=None, request_headers:Dict={}):
        """Delete a collection by it's id. Returns an object that tells whether the collection was deleted successfully
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.deleteCollection()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CommonResponseSchemaCollection
            schema = CommonResponseSchemaCollection()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCollection")
                print(e)

        return response
    
    async def getApplicationDepartmentListing(self, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Retrieve department listings related to the application. Departments are a way to categorise similar products. A product can lie in multiple departments.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search department by name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search department by name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationDepartmentListingResponse
            schema = ApplicationDepartmentListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationDepartmentListing")
                print(e)

        return response
    
    async def updateAppDepartment(self, department_uid=None, body="", request_headers:Dict={}):
        """Modify department data related to the application.
        :param department_uid : department id for which the custom_json is associated. : type integer
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department/{department_uid}", """{"required":[{"description":"Id of the company associated to department custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"department id for which the custom_json is associated.","in":"path","name":"department_uid","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to department custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"department id for which the custom_json is associated.","in":"path","name":"department_uid","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", department_uid=department_uid)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department/{department_uid}", department_uid=department_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppDepartment")
                print(e)

        return response
    
    async def getConfigurationsFilterMetadata(self, filter=None, request_headers:Dict={}):
        """configured details for catalog.
        :param filter : Filter whose values needs to be fetched. : type string
        """
        payload = {}
        
        if filter is not None:
            payload["filter"] = filter

        # Parameter validation
        schema = CatalogValidator.getConfigurationsFilterMetadata()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata/{filter}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Filter whose values needs to be fetched.","in":"path","name":"filter","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Filter whose values needs to be fetched.","in":"path","name":"filter","required":true,"schema":{"type":"string"}}]}""", serverType="platform", filter=filter)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata/{filter}", filter=filter), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FilterResponse
            schema = FilterResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getConfigurationsFilterMetadata")
                print(e)

        return response
    
    async def getDepartments(self, request_headers:Dict={}):
        """Retrieve a list of departments. Departments are a way to categorise similar products. A product can lie in multiple departments.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getDepartments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/departments", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/departments", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DepartmentResponse
            schema = DepartmentResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDepartments")
                print(e)

        return response
    
    async def getAppInventory(self, item_ids=None, store_ids=None, brand_ids=None, seller_identifiers=None, timestamp=None, page_size=None, page_id=None, qty_gt=None, qty_lt=None, qty_type=None, from_date=None, to_date=None, request_headers:Dict={}):
        """Retrieve inventory data related to the application. Retrieve the available Inventory of the products. Use this API to get the Inventory status of products with the filters of timestamp, store_ids, brand_ids, item_id, Items, Pagination
        :param item_ids : The Item Id of the product. : type array
        :param store_ids : The Store Id of products to fetch inventory. : type array
        :param brand_ids : The Brand Id of products to fetch inventory. : type array
        :param seller_identifiers : Unique seller_identifier of the product. : type array
        :param timestamp : Timestamp in UTC format (2020-07-23T10:27:50Z) : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        :param page_id : Page ID to retrieve next set of results. : type string
        :param qty_gt : This field allows you to filter for inventories that have quantity greater than to the specified value based on qty_type filter. : type integer
        :param qty_lt : This field allows you to filter for inventories that have a quantity less than to the specified value based on qty_type filter. : type integer
        :param qty_type : This field provides flexibility in selecting filter for inventory quantity counts and date queries. For example, you might use this field to specify "total" or "sellable" quantity. : type string
        :param from_date : Inventory updated on filter to get inventories greater then or equal to provided date based on qty_type value. : type string
        :param to_date : Inventory updated on filter to get inventories less then or equal to provided date based on qty_type value. : type string
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
        if qty_gt is not None:
            payload["qty_gt"] = qty_gt
        if qty_lt is not None:
            payload["qty_lt"] = qty_lt
        if qty_type is not None:
            payload["qty_type"] = qty_type
        if from_date is not None:
            payload["from_date"] = from_date
        if to_date is not None:
            payload["to_date"] = to_date

        # Parameter validation
        schema = CatalogValidator.getAppInventory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/inventory", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The Item Id of the product.","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Store Id of products to fetch inventory.","in":"query","name":"store_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Brand Id of products to fetch inventory.","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Unique seller_identifier of the product.","in":"query","name":"seller_identifiers","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Timestamp in UTC format (2020-07-23T10:27:50Z)","in":"query","name":"timestamp","required":false,"schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Page ID to retrieve next set of results.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"This field allows you to filter for inventories that have quantity greater than to the specified value based on qty_type filter.","in":"query","name":"qty_gt","required":false,"schema":{"type":"integer"}},{"description":"This field allows you to filter for inventories that have a quantity less than to the specified value based on qty_type filter.","in":"query","name":"qty_lt","required":false,"schema":{"type":"integer"}},{"description":"This field provides flexibility in selecting filter for inventory quantity counts and date queries. For example, you might use this field to specify \"total\" or \"sellable\" quantity.","in":"query","name":"qty_type","required":false,"schema":{"enum":["total","sellable"],"type":"string"}},{"description":"Inventory updated on filter to get inventories greater then or equal to provided date based on qty_type value.","in":"query","name":"from_date","required":false,"schema":{"format":"date-time","type":"string"}},{"description":"Inventory updated on filter to get inventories less then or equal to provided date based on qty_type value.","in":"query","name":"to_date","required":false,"schema":{"format":"date-time","type":"string"}}],"query":[{"description":"The Item Id of the product.","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Store Id of products to fetch inventory.","in":"query","name":"store_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Brand Id of products to fetch inventory.","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Unique seller_identifier of the product.","in":"query","name":"seller_identifiers","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Timestamp in UTC format (2020-07-23T10:27:50Z)","in":"query","name":"timestamp","required":false,"schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Page ID to retrieve next set of results.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"This field allows you to filter for inventories that have quantity greater than to the specified value based on qty_type filter.","in":"query","name":"qty_gt","required":false,"schema":{"type":"integer"}},{"description":"This field allows you to filter for inventories that have a quantity less than to the specified value based on qty_type filter.","in":"query","name":"qty_lt","required":false,"schema":{"type":"integer"}},{"description":"This field provides flexibility in selecting filter for inventory quantity counts and date queries. For example, you might use this field to specify \"total\" or \"sellable\" quantity.","in":"query","name":"qty_type","required":false,"schema":{"enum":["total","sellable"],"type":"string"}},{"description":"Inventory updated on filter to get inventories greater then or equal to provided date based on qty_type value.","in":"query","name":"from_date","required":false,"schema":{"format":"date-time","type":"string"}},{"description":"Inventory updated on filter to get inventories less then or equal to provided date based on qty_type value.","in":"query","name":"to_date","required":false,"schema":{"format":"date-time","type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_ids=item_ids, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, timestamp=timestamp, page_size=page_size, page_id=page_id, qty_gt=qty_gt, qty_lt=qty_lt, qty_type=qty_type, from_date=from_date, to_date=to_date)
        query_string = await create_query_string(item_ids=item_ids, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, timestamp=timestamp, page_size=page_size, page_id=page_id, qty_gt=qty_gt, qty_lt=qty_lt, qty_type=qty_type, from_date=from_date, to_date=to_date)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/inventory", item_ids=item_ids, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, timestamp=timestamp, page_size=page_size, page_id=page_id, qty_gt=qty_gt, qty_lt=qty_lt, qty_type=qty_type, from_date=from_date, to_date=to_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryStockResponse
            schema = InventoryStockResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppInventory")
                print(e)

        return response
    
    async def getAppLocations(self, store_type=None, uid=None, q=None, stage=None, page_no=None, page_size=None, tags=None, store_types=None, company_uids=None, request_headers:Dict={}):
        """Retrieve locations specific to the application. View all the locations asscoiated to a application.
        :param store_type : Helps to sort the location list on the basis of location type. : type string
        :param uid : Helps to sort the location list on the basis of uid list. : type array
        :param q : Query that is to be searched. : type string
        :param stage : to filter companies on basis of verified or unverified companies. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 20. : type integer
        :param tags : Get locations filtered by tags. : type array
        :param store_types : Get locations filtered by store types. : type array
        :param company_uids : Filter stores by company IDs available in the application. : type array
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
        if tags is not None:
            payload["tags"] = tags
        if store_types is not None:
            payload["store_types"] = store_types
        if company_uids is not None:
            payload["company_uids"] = company_uids

        # Parameter validation
        schema = CatalogValidator.getAppLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/locations", """{"required":[{"description":"Id of the company whose locations are to fetched","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Id of the application whose locations are to fetched","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Helps to sort the location list on the basis of location type.","in":"query","name":"store_type","required":false,"schema":{"type":"string"}},{"description":"Helps to sort the location list on the basis of uid list.","in":"query","name":"uid","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Query that is to be searched.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"to filter companies on basis of verified or unverified companies.","in":"query","name":"stage","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 20.","in":"query","name":"page_size","required":false,"schema":{"default":20,"type":"integer"}},{"description":"Get locations filtered by tags.","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get locations filtered by store types.","in":"query","name":"store_types","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Filter stores by company IDs available in the application.","in":"query","name":"company_uids","required":false,"schema":{"type":"array","items":{"type":"integer"}}}],"query":[{"description":"Helps to sort the location list on the basis of location type.","in":"query","name":"store_type","required":false,"schema":{"type":"string"}},{"description":"Helps to sort the location list on the basis of uid list.","in":"query","name":"uid","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Query that is to be searched.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"to filter companies on basis of verified or unverified companies.","in":"query","name":"stage","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 20.","in":"query","name":"page_size","required":false,"schema":{"default":20,"type":"integer"}},{"description":"Get locations filtered by tags.","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get locations filtered by store types.","in":"query","name":"store_types","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Filter stores by company IDs available in the application.","in":"query","name":"company_uids","required":false,"schema":{"type":"array","items":{"type":"integer"}}}],"headers":[],"path":[{"description":"Id of the company whose locations are to fetched","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Id of the application whose locations are to fetched","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size, tags=tags, store_types=store_types, company_uids=company_uids)
        query_string = await create_query_string(store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size, tags=tags, store_types=store_types, company_uids=company_uids)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/locations", store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size, tags=tags, store_types=store_types, company_uids=company_uids), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LocationListSerializer
            schema = LocationListSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppLocations")
                print(e)

        return response
    
    async def getConfigurations(self, request_headers:Dict={}):
        """Retrieve a configured details for catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAppCatalogConfiguration
            schema = GetAppCatalogConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getConfigurations")
                print(e)

        return response
    
    async def createConfigurationProductListing(self, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAppCatalogConfiguration
            schema = GetAppCatalogConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createConfigurationProductListing")
                print(e)

        return response
    
    async def getCatalogConfiguration(self, request_headers:Dict={}):
        """Retrieve configuration meta details for the catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getCatalogConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCatalogConfigurationMetaData
            schema = GetCatalogConfigurationMetaData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCatalogConfiguration")
                print(e)

        return response
    
    async def getConfigurationByType(self, type=None, request_headers:Dict={}):
        """Retrieve configuration details based on a specific type in the catalog.
        :param type : type can be brands, categories etc. : type string
        """
        payload = {}
        
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = CatalogValidator.getConfigurationByType()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}]}""", serverType="platform", type=type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}", type=type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAppCatalogEntityConfiguration
            schema = GetAppCatalogEntityConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getConfigurationByType")
                print(e)

        return response
    
    async def createConfigurationByType(self, type=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}]}""", serverType="platform", type=type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAppCatalogConfiguration
            schema = GetAppCatalogConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createConfigurationByType")
                print(e)

        return response
    
    async def getAppProduct(self, item_id=None, request_headers:Dict={}):
        """Products are the core resource of an application. If successful, returns a Company Application Product resource in the response body depending upon filter sent.
        :param item_id : product id for a particular product. : type integer
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id

        # Parameter validation
        schema = CatalogValidator.getAppProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"product id for a particular product.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"product id for a particular product.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", item_id=item_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}", item_id=item_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OwnerAppItemResponse
            schema = OwnerAppItemResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppProduct")
                print(e)

        return response
    
    async def updateAppProduct(self, item_id=None, body="", request_headers:Dict={}):
        """Allows to update data associated to a item custom meta.
        :param item_id : product id for which the custom_meta is associated. : type integer
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}", """{"required":[{"description":"Id of the company associated to custom meta.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"application id for which the custom_meta is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"product id for which the custom_meta is associated.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to custom meta.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"application id for which the custom_meta is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"product id for which the custom_meta is associated.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", item_id=item_id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}", item_id=item_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppProduct")
                print(e)

        return response
    
    async def getAppicationProducts(self, q=None, f=None, c=None, filters=None, is_dependent=None, sort_on=None, page_id=None, page_size=None, page_no=None, page_type=None, item_ids=None, request_headers:Dict={}):
        """Retrieve products associated with the application. List all the products associated with a brand, collection or category in a requested sort order.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The search query. This can be a partial or complete name of a either a product, brand or category","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","in":"query","name":"f","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","in":"query","name":"c","required":false,"schema":{"type":"string"}},{"description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","in":"query","name":"filters","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"This query parameter is used to get the dependent products in the listing.","in":"query","name":"is_dependent","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","in":"query","name":"sort_on","required":false,"schema":{"enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"],"type":"string"}},{"description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"If page_type is number then pass it to fetch page items. Default is 1.","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"For pagination type should be cursor or number. Default is cursor.","in":"query","name":"page_type","required":false,"schema":{"default":"cursor","type":"string"}},{"description":"Item Ids of product","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"string"},"type":"array"}}],"query":[{"description":"The search query. This can be a partial or complete name of a either a product, brand or category","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","in":"query","name":"f","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","in":"query","name":"c","required":false,"schema":{"type":"string"}},{"description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","in":"query","name":"filters","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"This query parameter is used to get the dependent products in the listing.","in":"query","name":"is_dependent","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","in":"query","name":"sort_on","required":false,"schema":{"enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"],"type":"string"}},{"description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"If page_type is number then pass it to fetch page items. Default is 1.","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"For pagination type should be cursor or number. Default is cursor.","in":"query","name":"page_type","required":false,"schema":{"default":"cursor","type":"string"}},{"description":"Item Ids of product","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"string"},"type":"array"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", q=q, f=f, c=c, filters=filters, is_dependent=is_dependent, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids)
        query_string = await create_query_string(q=q, f=f, c=c, filters=filters, is_dependent=is_dependent, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products", q=q, f=f, c=c, filters=filters, is_dependent=is_dependent, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationProductListingResponse
            schema = ApplicationProductListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppicationProducts")
                print(e)

        return response
    
    async def getDiscountedInventoryBySizeIdentifier(self, item_id=None, size_identifier=None, page_no=None, page_size=None, location_ids=None, request_headers:Dict={}):
        """Allows to retrieve Inventory data for particular company grouped by size and store.
        :param item_id : Item code of the product of which size is to be get. : type integer
        :param size_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type integer
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
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
        if location_ids is not None:
            payload["location_ids"] = location_ids

        # Parameter validation
        schema = CatalogValidator.getDiscountedInventoryBySizeIdentifier()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{item_id}/inventory/{size_identifier}", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Uniquer Application ID.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"path","name":"size_identifier","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search by store ids.","in":"query","name":"location_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search by store ids.","in":"query","name":"location_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Uniquer Application ID.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"path","name":"size_identifier","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, location_ids=location_ids)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, location_ids=location_ids)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{item_id}/inventory/{size_identifier}", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, location_ids=location_ids), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventorySellerIdentifierResponsePaginated
            schema = InventorySellerIdentifierResponsePaginated()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDiscountedInventoryBySizeIdentifier")
                print(e)

        return response
    
    async def getProductDetailBySlug(self, slug=None, request_headers:Dict={}):
        """Retrieve detailed product information using a product slug. Products are the core resource of an application. Products can be associated by categories, collections, brands and more.
        :param slug : The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/** : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getProductDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{slug}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/**","in":"path","name":"slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/**","in":"path","name":"slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductDetail
            schema = ProductDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductDetailBySlug")
                print(e)

        return response
    
    async def getAppProducts(self, brand_ids=None, category_ids=None, department_ids=None, tags=None, item_ids=None, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Retrieve products specific to the application. Products are the core resource of an application. Products can be associated by categories, collections, brands and more.
        :param brand_ids : Get multiple products filtered by Brand Ids : type array
        :param category_ids : Get multiple products filtered by Category Ids : type array
        :param department_ids : Get multiple products filtered by Department Ids : type array
        :param tags : Get multiple products filtered by tags : type array
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Get multiple products filtered by Brand Ids","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Category Ids","in":"query","name":"category_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Department Ids","in":"query","name":"department_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by tags","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get multiple products filtered by Item Ids","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"Search with Item Code, Name, Slug or Identifier.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"Get multiple products filtered by Brand Ids","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Category Ids","in":"query","name":"category_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Department Ids","in":"query","name":"department_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by tags","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get multiple products filtered by Item Ids","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"Search with Item Code, Name, Slug or Identifier.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, item_ids=item_ids, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, item_ids=item_ids, page_no=page_no, page_size=page_size, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, item_ids=item_ids, page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RawProductListingResponse
            schema = RawProductListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppProducts")
                print(e)

        return response
    
    async def getAppReturnConfiguration(self, request_headers:Dict={}):
        """Get Product Return configuration set at an application level
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAppReturnConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppReturnConfigResponse
            schema = AppReturnConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppReturnConfiguration")
                print(e)

        return response
    
    async def createAppReturnConfiguration(self, body="", request_headers:Dict={}):
        """Create Return configuration level set for an application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createAppReturnConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUpdateAppReturnConfig
        schema = CreateUpdateAppReturnConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppReturnConfiguration")
                print(e)

        return response
    
    async def updateAppReturnConfiguration(self, body="", request_headers:Dict={}):
        """Update Return configuration level set for an application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateAppReturnConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUpdateAppReturnConfig
        schema = CreateUpdateAppReturnConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppReturnConfiguration")
                print(e)

        return response
    
    async def deleteAppCategoryReturnConfiguration(self, body="", request_headers:Dict={}):
        """Delete Category level Application Return Configuration setttings
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.deleteAppCategoryReturnConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DeleteAppCategoryReturnConfig
        schema = DeleteAppCategoryReturnConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse
            schema = SuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAppCategoryReturnConfiguration")
                print(e)

        return response
    
    async def getAppCategoryReturnConfig(self, q=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Get all category level configuration level set for an application.
        :param q : Get return configurations for categories by matching the search string with category names. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getAppCategoryReturnConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sales channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Get return configurations for categories by matching the search string with category names.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"query":[{"description":"Get return configurations for categories by matching the search string with category names.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sales channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", q=q, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(q=q, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", q=q, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BaseAppCategoryReturnConfigResponse
            schema = BaseAppCategoryReturnConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCategoryReturnConfig")
                print(e)

        return response
    
    async def createAppCategoryReturnConfiguration(self, body="", request_headers:Dict={}):
        """Create Category level Application Return Configuration setttings
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createAppCategoryReturnConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BaseAppCategoryReturnConfig
        schema = BaseAppCategoryReturnConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppCategoryReturnConfiguration")
                print(e)

        return response
    
    async def updateAppCategoryReturnConfiguration(self, body="", request_headers:Dict={}):
        """Update Category level Application Return Configuration setttings
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateAppCategoryReturnConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BaseAppCategoryReturnConfig
        schema = BaseAppCategoryReturnConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse
            schema = SuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCategoryReturnConfiguration")
                print(e)

        return response
    
    async def createCustomAutocompleteRule(self, body="", request_headers:Dict={}):
        """Generate and add custom autocomplete rules to the catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCustomAutocompleteRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateAutocompleteKeyword
        schema = CreateAutocompleteKeyword()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAutocompleteWordsResponse
            schema = CreateAutocompleteWordsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomAutocompleteRule")
                print(e)

        return response
    
    async def getAutocompleteConfig(self, page_no=None, page_size=None, q=None, is_active=None, request_headers:Dict={}):
        """Custom Autocomplete Keyword allows you to map conditions with keywords to give you the ultimate results
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with words name.Use this parameter to search keywords by words. : type string
        :param is_active : Can query for keywords based on whether they are active or inactive. : type boolean
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if is_active is not None:
            payload["is_active"] = is_active

        # Parameter validation
        schema = CatalogValidator.getAutocompleteConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with words name.Use this parameter to search keywords by words.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Can query for keywords based on whether they are active or inactive.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with words name.Use this parameter to search keywords by words.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Can query for keywords based on whether they are active or inactive.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q, is_active=is_active)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, is_active=is_active)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete", page_no=page_no, page_size=page_size, q=q, is_active=is_active), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAutocompleteWordsResponse
            schema = GetAutocompleteWordsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAutocompleteConfig")
                print(e)

        return response
    
    async def getAutocompleteKeywordDetail(self, id=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific autocomplete keyword.
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getAutocompleteKeywordDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAutocompleteWordsData
            schema = GetAutocompleteWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAutocompleteKeywordDetail")
                print(e)

        return response
    
    async def updateAutocompleteKeyword(self, id=None, body="", request_headers:Dict={}):
        """Update a mapping by it's id. On successful request, returns the updated Keyword mapping
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.updateAutocompleteKeyword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateAutocompleteKeyword
        schema = CreateAutocompleteKeyword()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAutocompleteWordsData
            schema = GetAutocompleteWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAutocompleteKeyword")
                print(e)

        return response
    
    async def deleteAutocompleteKeyword(self, id=None, request_headers:Dict={}):
        """Delete a keywords by it's id. Returns an object that tells whether the keywords was deleted successfully
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.deleteAutocompleteKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteResponse
            schema = DeleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAutocompleteKeyword")
                print(e)

        return response
    
    async def createSearchRerank(self, body="", request_headers:Dict={}):
        """This view allows you to create search rerank attributes for an application
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createSearchRerank()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchRerankRequest
        schema = CreateSearchRerankRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateSearchRerankResponse
            schema = CreateSearchRerankResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSearchRerank")
                print(e)

        return response
    
    async def getSearchRerank(self, request_headers:Dict={}):
        """This view allows you to create search rerank attributes for an application
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getSearchRerank()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchRerankResponse
            schema = GetSearchRerankResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSearchRerank")
                print(e)

        return response
    
    async def getSearchRerankDetail(self, id=None, request_headers:Dict={}):
        """This view allows you to retrieve search rerank attribute detail for an application
        :param id : An `id` is the identifier for a particular search rerank configuration. channel. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getSearchRerankDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sales channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"An `id` is the identifier for a particular search rerank configuration. channel.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sales channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"An `id` is the identifier for a particular search rerank configuration. channel.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchRerankDetailResponse
            schema = GetSearchRerankDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSearchRerankDetail")
                print(e)

        return response
    
    async def updateSearchRerankConfiguration(self, id=None, body="", request_headers:Dict={}):
        """This view allows you to update search rerank attribute for an application
        :param id : An `id` is the identifier for a particular search rerank configuration. channel. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.updateSearchRerankConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateSearchRerankRequest
        schema = UpdateSearchRerankRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"An `id` is the identifier for a particular search rerank configuration. channel.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"An `id` is the identifier for a particular search rerank configuration. channel.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateSearchRerankResponse
            schema = UpdateSearchRerankResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSearchRerankConfiguration")
                print(e)

        return response
    
    async def deleteSearchRerankConfiguration(self, id=None, request_headers:Dict={}):
        """This view allows you to delete search rerank configuration for an application
        :param id : An `id` is the identifier for a particular search rerank configuration. channel. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.deleteSearchRerankConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"An `id` is the identifier for a particular search rerank configuration. channel.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"An `id` is the identifier for a particular search rerank configuration. channel.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/rerank/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteSearchRerankConfigurationResponse
            schema = DeleteSearchRerankConfigurationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSearchRerankConfiguration")
                print(e)

        return response
    
    async def createSearchConfiguration(self, body="", request_headers:Dict={}):
        """Create search configuration for the catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createSearchConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchConfigurationRequest
        schema = CreateSearchConfigurationRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateSearchConfigurationResponse
            schema = CreateSearchConfigurationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSearchConfiguration")
                print(e)

        return response
    
    async def getSearchConfiguration(self, request_headers:Dict={}):
        """Get search configuration in the catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getSearchConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchConfigurationResponse
            schema = GetSearchConfigurationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSearchConfiguration")
                print(e)

        return response
    
    async def updateSearchConfiguration(self, body="", request_headers:Dict={}):
        """This view allows you to modify searchable attributes for an application
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateSearchConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateSearchConfigurationRequest
        schema = UpdateSearchConfigurationRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateSearchConfigurationResponse
            schema = UpdateSearchConfigurationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSearchConfiguration")
                print(e)

        return response
    
    async def deleteSearchConfiguration(self, request_headers:Dict={}):
        """Delete search configuration in the catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.deleteSearchConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteSearchConfigurationResponse
            schema = DeleteSearchConfigurationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSearchConfiguration")
                print(e)

        return response
    
    async def createCustomKeyword(self, body="", request_headers:Dict={}):
        """Create a Custom Search Keywords. 
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCustomKeyword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchKeyword
        schema = CreateSearchKeyword()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsData
            schema = GetSearchWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomKeyword")
                print(e)

        return response
    
    async def getAllSearchKeyword(self, page_no=None, page_size=None, q=None, is_active=None, request_headers:Dict={}):
        """Custom Search Keyword allows you to map conditions with keywords to give you the ultimate results
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with words name.Use this parameter to search keywords by words. : type string
        :param is_active : Can query for keywords based on whether they are active or inactive. : type boolean
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if is_active is not None:
            payload["is_active"] = is_active

        # Parameter validation
        schema = CatalogValidator.getAllSearchKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with words name.Use this parameter to search keywords by words.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Can query for keywords based on whether they are active or inactive.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with words name.Use this parameter to search keywords by words.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Can query for keywords based on whether they are active or inactive.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q, is_active=is_active)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, is_active=is_active)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword", page_no=page_no, page_size=page_size, q=q, is_active=is_active), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsResponse
            schema = GetSearchWordsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllSearchKeyword")
                print(e)

        return response
    
    async def getSearchKeywords(self, id=None, request_headers:Dict={}):
        """Retrieve a list of search keywords from the catalog.
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsData
            schema = GetSearchWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSearchKeywords")
                print(e)

        return response
    
    async def updateSearchKeywords(self, id=None, body="", request_headers:Dict={}):
        """Update Search Keyword by its id. On successful request, returns the updated collection
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsData
            schema = GetSearchWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSearchKeywords")
                print(e)

        return response
    
    async def deleteSearchKeywords(self, id=None, request_headers:Dict={}):
        """Delete a keywords by it's id. Returns an object that tells whether the keywords was deleted successfully
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.deleteSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteResponse
            schema = DeleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSearchKeywords")
                print(e)

        return response
    
    async def updateAppLocation(self, store_uid=None, body="", request_headers:Dict={}):
        """Modify location data related to the application. Helps to update data associated to a item custom meta
        :param store_uid : store id for which the custom_json is associated. : type integer
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/{store_uid}", """{"required":[{"description":"Id of the company associated to location custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"store id for which the custom_json is associated.","in":"path","name":"store_uid","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to location custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"store id for which the custom_json is associated.","in":"path","name":"store_uid","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", store_uid=store_uid)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/{store_uid}", store_uid=store_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse1
            schema = SuccessResponse1()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppLocation")
                print(e)

        return response
    
    async def updateAllowSingle(self, body="", request_headers:Dict={}):
        """Modify allow single flag for filters of the application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateAllowSingle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AllowSingleRequest
        schema = AllowSingleRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/filter/allow_single", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/filter/allow_single", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigSuccessResponse
            schema = ConfigSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAllowSingle")
                print(e)

        return response
    
    async def updateDefaultSort(self, body="", request_headers:Dict={}):
        """Modify the default sort key configuration for the application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateDefaultSort()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DefaultKeyRequest
        schema = DefaultKeyRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/sort/default_key", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/sort/default_key", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigSuccessResponse
            schema = ConfigSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateDefaultSort")
                print(e)

        return response
    
    async def createListingConfiguration(self, config_type=None, body="", request_headers:Dict={}):
        """Add configuration for catalog listing.
        :param config_type : A `config_type` is a unique identifier for a particular listing configuration type. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type

        # Parameter validation
        schema = CatalogValidator.createListingConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppConfigurationsFilter
        schema = AppConfigurationsFilter()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}}]}""", serverType="platform", config_type=config_type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}", config_type=config_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppConfigurationsFilterResponse
            schema = AppConfigurationsFilterResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createListingConfiguration")
                print(e)

        return response
    
    async def getListingConfigurations(self, config_type=None, page_no=None, page_size=None, search=None, uids=None, request_headers:Dict={}):
        """Retrieve the details of the application configured configurations of listing config types.
        :param config_type : A `config_type` is an identifier that defines a specific type of configuration. : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param search : Get configuration list filtered by `search` string. : type string
        :param uids : Only for categories config type, Get configuration list filtered by `uids`. : type array
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
        if uids is not None:
            payload["uids"] = uids

        # Parameter validation
        schema = CatalogValidator.getListingConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"Only for categories config type, Get configuration list filtered by `uids`.","in":"query","name":"uids","required":false,"schema":{"type":"array","items":{"type":"integer"}}}],"query":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"Only for categories config type, Get configuration list filtered by `uids`.","in":"query","name":"uids","required":false,"schema":{"type":"array","items":{"type":"integer"}}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}}]}""", serverType="platform", config_type=config_type, page_no=page_no, page_size=page_size, search=search, uids=uids)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, search=search, uids=uids)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}", config_type=config_type, page_no=page_no, page_size=page_size, search=search, uids=uids), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetListingConfigResponse
            schema = GetListingConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getListingConfigurations")
                print(e)

        return response
    
    async def createGroupConfiguration(self, config_type=None, body="", request_headers:Dict={}):
        """Create configuration for group configuration types.
        :param config_type : A `config_type` is a unique identifier for a particular group configuration type. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type

        # Parameter validation
        schema = CatalogValidator.createGroupConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppConfigurationCreateDetail
        schema = AppConfigurationCreateDetail()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}]}""", serverType="platform", config_type=config_type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", config_type=config_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppConfigurationDetail
            schema = AppConfigurationDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createGroupConfiguration")
                print(e)

        return response
    
    async def getGroupConfigurations(self, config_type=None, page_no=None, page_size=None, search=None, template_slug=None, request_headers:Dict={}):
        """Retrieve the details of the application configured configurations of group config types.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}]}""", serverType="platform", config_type=config_type, page_no=page_no, page_size=page_size, search=search, template_slug=template_slug)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, search=search, template_slug=template_slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", config_type=config_type, page_no=page_no, page_size=page_size, search=search, template_slug=template_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetConfigResponse
            schema = GetConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGroupConfigurations")
                print(e)

        return response
    
    async def updateGroupConfiguration(self, config_type=None, group_slug=None, body="", request_headers:Dict={}):
        """Modify the group configurations for the application.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", config_type=config_type, group_slug=group_slug)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", config_type=config_type, group_slug=group_slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppConfigurationDetail
            schema = AppConfigurationDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateGroupConfiguration")
                print(e)

        return response
    
    async def deleteGroupConfiguration(self, config_type=None, group_slug=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", config_type=config_type, group_slug=group_slug)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", config_type=config_type, group_slug=group_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def updateListingConfiguration(self, config_type=None, config_id=None, body="", request_headers:Dict={}):
        """Modify the details and settings of an existing listing configuration.
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
        from .models import AppConfigurationsFilterResponse
        schema = AppConfigurationsFilterResponse()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", config_type=config_type, config_id=config_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}", config_type=config_type, config_id=config_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppConfigurationsFilterResponse
            schema = AppConfigurationsFilterResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateListingConfiguration")
                print(e)

        return response
    
    async def deleteListingConfiguration(self, config_type=None, config_id=None, request_headers:Dict={}):
        """Remove a specific listing configuration from the catalog.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", config_type=config_type, config_id=config_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}", config_type=config_type, config_id=config_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigSuccessResponse
            schema = ConfigSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteListingConfiguration")
                print(e)

        return response
    
    async def getConfigurationMetadata(self, config_type=None, template_slug=None, request_headers:Dict={}):
        """Retrieve the configuraion metadata details for catalog.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/metadata", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","details_groups","comparisons_groups","variant","similar","brands","categories","seller_groups"],"type":"string"}}],"optional":[{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}}],"query":[{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","details_groups","comparisons_groups","variant","similar","brands","categories","seller_groups"],"type":"string"}}]}""", serverType="platform", config_type=config_type, template_slug=template_slug)
        query_string = await create_query_string(template_slug=template_slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/metadata", config_type=config_type, template_slug=template_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetConfigMetadataResponse
            schema = GetConfigMetadataResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getConfigurationMetadata")
                print(e)

        return response
    
    async def createAutocompleteSettings(self, body="", request_headers:Dict={}):
        """This API allows to create autocomplete settings for an application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createAutocompleteSettings()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AutocompleteRequestSchema
        schema = AutocompleteRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/settings", """{"required":[{"name":"application_id","description":"The company id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"string"}},{"name":"company_id","description":"The application id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"application_id","description":"The company id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"string"}},{"name":"company_id","description":"The application id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/settings", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AutocompleteUpsertResponseSchema
            schema = AutocompleteUpsertResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAutocompleteSettings")
                print(e)

        return response
    
    async def getAutocompleteSettings(self, request_headers:Dict={}):
        """This API allows to get autocomplete settings config for an application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAutocompleteSettings()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/settings", """{"required":[{"description":"The company id for which the autocomplete settings is being referenced","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"The application id for which the autocomplete settings is being referenced","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The company id for which the autocomplete settings is being referenced","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"The application id for which the autocomplete settings is being referenced","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/settings", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AutocompleteResponseSchema
            schema = AutocompleteResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAutocompleteSettings")
                print(e)

        return response
    
    async def updateAutocompleteSettings(self, id=None, body="", request_headers:Dict={}):
        """This API allows to update autocomplete settings for an application.
        :param id : An `id` is a unique identifier for a particular autocomplete settings config. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.updateAutocompleteSettings()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AutocompleteRequestSchema
        schema = AutocompleteRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/settings/{id}", """{"required":[{"name":"application_id","description":"The company id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"string"}},{"name":"company_id","description":"The application id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"integer"}},{"name":"id","description":"An `id` is a unique identifier for a particular autocomplete settings config.","in":"path","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"application_id","description":"The company id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"string"}},{"name":"company_id","description":"The application id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"integer"}},{"name":"id","description":"An `id` is a unique identifier for a particular autocomplete settings config.","in":"path","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/settings/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AutocompleteUpsertResponseSchema
            schema = AutocompleteUpsertResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAutocompleteSettings")
                print(e)

        return response
    
    async def getAutocompletePreview(self, q=None, category_suggestion=None, brand_suggestion=None, collection_suggestion=None, product_suggestion=None, query_suggestion=None, request_headers:Dict={}):
        """This API allows to get autocomplete suggestions as per config.
        :param q : Get suggestions related to `q` string. : type string
        :param category_suggestion : For getting related category suggestions. : type integer
        :param brand_suggestion : For getting related brand suggestions. : type integer
        :param collection_suggestion : For getting collection suggestions. : type integer
        :param product_suggestion : For getting product suggestions. : type integer
        :param query_suggestion : For getting query suggestions. : type integer
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q
        if category_suggestion is not None:
            payload["category_suggestion"] = category_suggestion
        if brand_suggestion is not None:
            payload["brand_suggestion"] = brand_suggestion
        if collection_suggestion is not None:
            payload["collection_suggestion"] = collection_suggestion
        if product_suggestion is not None:
            payload["product_suggestion"] = product_suggestion
        if query_suggestion is not None:
            payload["query_suggestion"] = query_suggestion

        # Parameter validation
        schema = CatalogValidator.getAutocompletePreview()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/preview", """{"required":[{"name":"application_id","description":"The company id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"string"}},{"name":"company_id","description":"The application id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"q","in":"query","description":"Get suggestions related to `q` string.","schema":{"type":"string"},"required":false},{"name":"category_suggestion","description":"For getting related category suggestions.","in":"query","required":false,"schema":{"type":"integer"}},{"name":"brand_suggestion","description":"For getting related brand suggestions.","in":"query","required":false,"schema":{"type":"integer"}},{"name":"collection_suggestion","description":"For getting collection suggestions.","in":"query","required":false,"schema":{"type":"integer"}},{"name":"product_suggestion","description":"For getting product suggestions.","in":"query","required":false,"schema":{"type":"integer"}},{"name":"query_suggestion","description":"For getting query suggestions.","in":"query","required":false,"schema":{"type":"integer"}}],"query":[{"name":"q","in":"query","description":"Get suggestions related to `q` string.","schema":{"type":"string"},"required":false},{"name":"category_suggestion","description":"For getting related category suggestions.","in":"query","required":false,"schema":{"type":"integer"}},{"name":"brand_suggestion","description":"For getting related brand suggestions.","in":"query","required":false,"schema":{"type":"integer"}},{"name":"collection_suggestion","description":"For getting collection suggestions.","in":"query","required":false,"schema":{"type":"integer"}},{"name":"product_suggestion","description":"For getting product suggestions.","in":"query","required":false,"schema":{"type":"integer"}},{"name":"query_suggestion","description":"For getting query suggestions.","in":"query","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"application_id","description":"The company id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"string"}},{"name":"company_id","description":"The application id for which the autocomplete settings is being referenced","in":"path","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", q=q, category_suggestion=category_suggestion, brand_suggestion=brand_suggestion, collection_suggestion=collection_suggestion, product_suggestion=product_suggestion, query_suggestion=query_suggestion)
        query_string = await create_query_string(q=q, category_suggestion=category_suggestion, brand_suggestion=brand_suggestion, collection_suggestion=collection_suggestion, product_suggestion=product_suggestion, query_suggestion=query_suggestion)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/preview", q=q, category_suggestion=category_suggestion, brand_suggestion=brand_suggestion, collection_suggestion=collection_suggestion, product_suggestion=product_suggestion, query_suggestion=query_suggestion), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AutocompletePreviewResponseSchema
            schema = AutocompletePreviewResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAutocompletePreview")
                print(e)

        return response
    
    async def createMerchandisingRulePinAction(self, merchandising_rule_id=None, body="", request_headers:Dict={}):
        """This allows you to create pin action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.createMerchandisingRulePinAction()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PinRequest
        schema = PinRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/pin", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/pin", merchandising_rule_id=merchandising_rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createMerchandisingRulePinAction")
                print(e)

        return response
    
    async def updateMerchandisingRulePinAction(self, merchandising_rule_id=None, body="", request_headers:Dict={}):
        """This allows you to update pin action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.updateMerchandisingRulePinAction()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PinRequest
        schema = PinRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/pin", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/pin", merchandising_rule_id=merchandising_rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateMerchandisingRulePinAction")
                print(e)

        return response
    
    async def getMerchandisingRulePinAction(self, merchandising_rule_id=None, request_headers:Dict={}):
        """This allows you to get details of pin action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.getMerchandisingRulePinAction()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/pin", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/pin", merchandising_rule_id=merchandising_rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PinResponse
            schema = PinResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchandisingRulePinAction")
                print(e)

        return response
    
    async def createMerchandisingRuleHideAction(self, merchandising_rule_id=None, body="", request_headers:Dict={}):
        """This allows you to create hide action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.createMerchandisingRuleHideAction()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import HideRequest
        schema = HideRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/hide", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/hide", merchandising_rule_id=merchandising_rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createMerchandisingRuleHideAction")
                print(e)

        return response
    
    async def updateMerchandisingRuleHideAction(self, merchandising_rule_id=None, body="", request_headers:Dict={}):
        """This allows you to update hide action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.updateMerchandisingRuleHideAction()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import HideRequest
        schema = HideRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/hide", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/hide", merchandising_rule_id=merchandising_rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateMerchandisingRuleHideAction")
                print(e)

        return response
    
    async def getMerchandisingRuleHideAction(self, merchandising_rule_id=None, request_headers:Dict={}):
        """This allows you to get details of hide action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.getMerchandisingRuleHideAction()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/hide", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/hide", merchandising_rule_id=merchandising_rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import HideResponse
            schema = HideResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchandisingRuleHideAction")
                print(e)

        return response
    
    async def createMerchandisingRuleBoostAction(self, merchandising_rule_id=None, body="", request_headers:Dict={}):
        """This allows you to create Boost action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.createMerchandisingRuleBoostAction()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostMerchandisingRuleBoostAction
        schema = PostMerchandisingRuleBoostAction()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/boost", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/boost", merchandising_rule_id=merchandising_rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createMerchandisingRuleBoostAction")
                print(e)

        return response
    
    async def updateMerchandisingRuleBoostAction(self, merchandising_rule_id=None, body="", request_headers:Dict={}):
        """This allows you to update Boost action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.updateMerchandisingRuleBoostAction()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostMerchandisingRuleBoostAction
        schema = PostMerchandisingRuleBoostAction()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/boost", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/boost", merchandising_rule_id=merchandising_rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateMerchandisingRuleBoostAction")
                print(e)

        return response
    
    async def getMerchandisingRuleBoostAction(self, merchandising_rule_id=None, request_headers:Dict={}):
        """This allows you to get details of Boost action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.getMerchandisingRuleBoostAction()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/boost", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/boost", merchandising_rule_id=merchandising_rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetMerchandisingRuleBoostAction
            schema = GetMerchandisingRuleBoostAction()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchandisingRuleBoostAction")
                print(e)

        return response
    
    async def createMerchandisingRuleBuryAction(self, merchandising_rule_id=None, body="", request_headers:Dict={}):
        """This allows you to create Bury action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.createMerchandisingRuleBuryAction()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostMerchandisingRuleBoostAction
        schema = PostMerchandisingRuleBoostAction()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/bury", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/bury", merchandising_rule_id=merchandising_rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createMerchandisingRuleBuryAction")
                print(e)

        return response
    
    async def updateMerchandisingRuleBuryAction(self, merchandising_rule_id=None, body="", request_headers:Dict={}):
        """This allows you to update Bury action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.updateMerchandisingRuleBuryAction()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostMerchandisingRuleBoostAction
        schema = PostMerchandisingRuleBoostAction()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/bury", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/bury", merchandising_rule_id=merchandising_rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateMerchandisingRuleBuryAction")
                print(e)

        return response
    
    async def getMerchandisingRuleBuryAction(self, merchandising_rule_id=None, request_headers:Dict={}):
        """This allows you to get details of Bury action of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.getMerchandisingRuleBuryAction()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/bury", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/bury", merchandising_rule_id=merchandising_rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetMerchandisingRuleBuryAction
            schema = GetMerchandisingRuleBuryAction()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchandisingRuleBuryAction")
                print(e)

        return response
    
    async def createMerchandisingRuleQuery(self, body="", request_headers:Dict={}):
        """This allows you to Create a merchandising rule's query.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createMerchandisingRuleQuery()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MerchandisingRuleQueryPost
        schema = MerchandisingRuleQueryPost()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/query", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/query", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MerchandiseQueryResponse
            schema = MerchandiseQueryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createMerchandisingRuleQuery")
                print(e)

        return response
    
    async def getMerchandisingQuery(self, merchandising_rule_id=None, request_headers:Dict={}):
        """This allows you to get details of a merchandising rule's query.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.getMerchandisingQuery()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/query", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/query", merchandising_rule_id=merchandising_rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SearchResponseSchema
            schema = SearchResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchandisingQuery")
                print(e)

        return response
    
    async def updateMerchandisingRuleQuery(self, merchandising_rule_id=None, body="", request_headers:Dict={}):
        """This allows you to Update a merchandising rule's query.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.updateMerchandisingRuleQuery()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MerchandisingRuleQueryPost
        schema = MerchandisingRuleQueryPost()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/query", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/query", merchandising_rule_id=merchandising_rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateMerchandisingRuleQuery")
                print(e)

        return response
    
    async def saveMerchandisingRules(self, merchandising_rule_id=None, body="", request_headers:Dict={}):
        """This allows you to Save a merchandising rule's preview state.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.saveMerchandisingRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MerchandisingRuleSave
        schema = MerchandisingRuleSave()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}", merchandising_rule_id=merchandising_rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for saveMerchandisingRules")
                print(e)

        return response
    
    async def deleteMerchandisingRule(self, merchandising_rule_id=None, request_headers:Dict={}):
        """This allows you to Update a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.deleteMerchandisingRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}", merchandising_rule_id=merchandising_rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteMerchandisingRule")
                print(e)

        return response
    
    async def getMerchandisingRules(self, page_id=None, page_size=None, request_headers:Dict={}):
        """This allows you to get details of all merchandising rule's details.
        :param page_id : Each response will contain next_id param, which should be sent back to make pagination work. : type string
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if page_id is not None:
            payload["page_id"] = page_id
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getMerchandisingRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_id","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"page_id","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="platform", page_id=page_id, page_size=page_size)
        query_string = await create_query_string(page_id=page_id, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules", page_id=page_id, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MerchandisingRulesList
            schema = MerchandisingRulesList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchandisingRules")
                print(e)

        return response
    
    async def deleteMerchandisingRulesPreview(self, merchandising_rule_id=None, request_headers:Dict={}):
        """This allows you to Update a merchandising rule's preview.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id

        # Parameter validation
        schema = CatalogValidator.deleteMerchandisingRulesPreview()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/preview", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/preview", merchandising_rule_id=merchandising_rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseMerchandising
            schema = SuccessResponseMerchandising()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteMerchandisingRulesPreview")
                print(e)

        return response
    
    async def getLivePreview(self, merchandising_rule_id=None, search_keyword=None, request_headers:Dict={}):
        """This allows you to get live preview of a merchandising rule.
        :param merchandising_rule_id : A `merchandising_rule_id` is a unique identifier for a particular merchandising rule. : type string
        :param search_keyword : A sample query that can be used to get a live preview of the merchandising rule. : type string
        """
        payload = {}
        
        if merchandising_rule_id is not None:
            payload["merchandising_rule_id"] = merchandising_rule_id
        if search_keyword is not None:
            payload["search_keyword"] = search_keyword

        # Parameter validation
        schema = CatalogValidator.getLivePreview()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/preview", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"search_keyword","description":"A sample query that can be used to get a live preview of the merchandising rule.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"search_keyword","description":"A sample query that can be used to get a live preview of the merchandising rule.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"merchandising_rule_id","description":"A `merchandising_rule_id` is a unique identifier for a particular merchandising rule.","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchandising_rule_id=merchandising_rule_id, search_keyword=search_keyword)
        query_string = await create_query_string(search_keyword=search_keyword)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchandise/rules/{merchandising_rule_id}/preview", merchandising_rule_id=merchandising_rule_id, search_keyword=search_keyword), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductListingResponse
            schema = ProductListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLivePreview")
                print(e)

        return response
    
    async def createAppPriceFactory(self, body="", request_headers:Dict={}):
        """This API allows to create price factory.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createAppPriceFactory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateAppPriceFactoryRequestSchema
        schema = CreateAppPriceFactoryRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAppPriceFactoryResponse
            schema = CreateAppPriceFactoryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppPriceFactory")
                print(e)

        return response
    
    async def getAppPriceFactories(self, is_active=None, factory_type_id=None, code=None, page_no=None, page_size=None, request_headers:Dict={}):
        """This API allows to get price factories.
        :param is_active : gets price factory filtered by active status. : type boolean
        :param factory_type_id : gets price factory filtered by factory_type_id. : type string
        :param code : gets price factory filtered by pricezone code. : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if is_active is not None:
            payload["is_active"] = is_active
        if factory_type_id is not None:
            payload["factory_type_id"] = factory_type_id
        if code is not None:
            payload["code"] = code
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getAppPriceFactories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true}],"optional":[{"description":"gets price factory filtered by active status.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"gets price factory filtered by factory_type_id.","in":"query","name":"factory_type_id","required":false,"schema":{"type":"string"}},{"description":"gets price factory filtered by pricezone code.","in":"query","name":"code","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"query":[{"description":"gets price factory filtered by active status.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"gets price factory filtered by factory_type_id.","in":"query","name":"factory_type_id","required":false,"schema":{"type":"string"}},{"description":"gets price factory filtered by pricezone code.","in":"query","name":"code","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true}]}""", serverType="platform", is_active=is_active, factory_type_id=factory_type_id, code=code, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(is_active=is_active, factory_type_id=factory_type_id, code=code, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory", is_active=is_active, factory_type_id=factory_type_id, code=code, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAppPriceFactoryResponse
            schema = GetAppPriceFactoryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppPriceFactories")
                print(e)

        return response
    
    async def getAppPriceFactory(self, id=None, request_headers:Dict={}):
        """This API allows to get price factory.
        :param id : An `id` is a unique identifier for a particular price factory. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getAppPriceFactory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppPriceFactory
            schema = AppPriceFactory()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppPriceFactory")
                print(e)

        return response
    
    async def editAppPriceFactory(self, id=None, body="", request_headers:Dict={}):
        """This API allows to update price factory.
        :param id : An `id` is a unique identifier for a particular price factory. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.editAppPriceFactory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditAppPriceFactoryRequestSchema
        schema = EditAppPriceFactoryRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppPriceFactory
            schema = AppPriceFactory()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editAppPriceFactory")
                print(e)

        return response
    
    async def addProductsInPriceFactoryByZoneId(self, id=None, body="", request_headers:Dict={}):
        """This API allows to add products in price factory.
        :param id : An `id` is a unique identifier for a particular price factory. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.addProductsInPriceFactoryByZoneId()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreatePriceFactoryProductRequest
        schema = CreatePriceFactoryProductRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/products", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/products", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreatePriceFactoryProductResponse
            schema = CreatePriceFactoryProductResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addProductsInPriceFactoryByZoneId")
                print(e)

        return response
    
    async def getProductsInPriceFactoryByZoneId(self, id=None, zone_id=None, item_id=None, q=None, page_no=None, page_size=None, request_headers:Dict={}):
        """This API allows to get products in price factory.
        :param id : An `id` is a unique identifier for a particular price factory. : type string
        :param zone_id : An `zone_id` is a unique identifier for a particular price factory zone. : type string
        :param item_id : gets price factory filtered by item_id. : type number
        :param q : gets price factory filtered by search query. : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if zone_id is not None:
            payload["zone_id"] = zone_id
        if item_id is not None:
            payload["item_id"] = item_id
        if q is not None:
            payload["q"] = q
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getProductsInPriceFactoryByZoneId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/products", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true},{"description":"An `zone_id` is a unique identifier for a particular price factory zone.","in":"query","name":"zone_id","schema":{"type":"string"},"required":true}],"optional":[{"description":"gets price factory filtered by item_id.","in":"query","name":"item_id","required":false,"schema":{"type":"number"}},{"description":"gets price factory filtered by search query.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"query":[{"description":"An `zone_id` is a unique identifier for a particular price factory zone.","in":"query","name":"zone_id","schema":{"type":"string"},"required":true},{"description":"gets price factory filtered by item_id.","in":"query","name":"item_id","required":false,"schema":{"type":"number"}},{"description":"gets price factory filtered by search query.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}]}""", serverType="platform", id=id, zone_id=zone_id, item_id=item_id, q=q, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(zone_id=zone_id, item_id=item_id, q=q, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/products", id=id, zone_id=zone_id, item_id=item_id, q=q, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAppPriceFactoryProductsResponse
            schema = CreateAppPriceFactoryProductsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductsInPriceFactoryByZoneId")
                print(e)

        return response
    
    async def createProductPriceFactoryBulkJob(self, id=None, body="", request_headers:Dict={}):
        """This API allows to create bulk job for adding products in price factory.
        :param id : An `id` is a unique identifier for a particular price factory. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.createProductPriceFactoryBulkJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateAppPriceFactoryProductBulkJobRequest
        schema = CreateAppPriceFactoryProductBulkJobRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/bulk", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/bulk", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAppPriceFactoryProductBulkJobResponse
            schema = CreateAppPriceFactoryProductBulkJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createProductPriceFactoryBulkJob")
                print(e)

        return response
    
    async def pollProductPriceFactoryBulkJob(self, id=None, job_id=None, request_headers:Dict={}):
        """This API allows to poll bulk job for adding products in price factory.
        :param id : An `id` is a unique identifier for a particular price factory. : type string
        :param job_id : A `job_id` is a unique identifier for a particular bulk job. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if job_id is not None:
            payload["job_id"] = job_id

        # Parameter validation
        schema = CatalogValidator.pollProductPriceFactoryBulkJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/poll/{job_id}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true},{"description":"A `job_id` is a unique identifier for a particular bulk job.","in":"path","name":"job_id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true},{"description":"A `job_id` is a unique identifier for a particular bulk job.","in":"path","name":"job_id","schema":{"type":"string"},"required":true}]}""", serverType="platform", id=id, job_id=job_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/poll/{job_id}", id=id, job_id=job_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAppPriceFactoryProductBulkJobPollResponse
            schema = CreateAppPriceFactoryProductBulkJobPollResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for pollProductPriceFactoryBulkJob")
                print(e)

        return response
    
    async def validateProductPriceFactoryBulkJob(self, id=None, job_id=None, body="", request_headers:Dict={}):
        """This API allows to validate bulk job for adding products in price factory.
        :param id : An `id` is a unique identifier for a particular price factory. : type string
        :param job_id : A `job_id` is a unique identifier for a particular bulk job. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if job_id is not None:
            payload["job_id"] = job_id

        # Parameter validation
        schema = CatalogValidator.validateProductPriceFactoryBulkJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateAppPriceFactoryProductBulkJobRequest
        schema = CreateAppPriceFactoryProductBulkJobRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/bulk/{job_id}/validate", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true},{"description":"A `job_id` is a unique identifier for a particular bulk job.","in":"path","name":"job_id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true},{"description":"A `job_id` is a unique identifier for a particular bulk job.","in":"path","name":"job_id","schema":{"type":"string"},"required":true}]}""", serverType="platform", id=id, job_id=job_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/bulk/{job_id}/validate", id=id, job_id=job_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAppPriceFactoryProductBulkJobValidateResponse
            schema = CreateAppPriceFactoryProductBulkJobValidateResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateProductPriceFactoryBulkJob")
                print(e)

        return response
    
    async def processProductPriceFactoryBulkJob(self, id=None, job_id=None, body="", request_headers:Dict={}):
        """This API allows to process bulk job for adding products in price factory.
        :param id : An `id` is a unique identifier for a particular price factory. : type string
        :param job_id : A `job_id` is a unique identifier for a particular bulk job. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if job_id is not None:
            payload["job_id"] = job_id

        # Parameter validation
        schema = CatalogValidator.processProductPriceFactoryBulkJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateAppPriceFactoryProductBulkJobRequest
        schema = CreateAppPriceFactoryProductBulkJobRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/bulk/{job_id}/process", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true},{"description":"A `job_id` is a unique identifier for a particular bulk job.","in":"path","name":"job_id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true},{"description":"A `job_id` is a unique identifier for a particular bulk job.","in":"path","name":"job_id","schema":{"type":"string"},"required":true}]}""", serverType="platform", id=id, job_id=job_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/bulk/{job_id}/process", id=id, job_id=job_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAppPriceFactoryProductBulkJobResponse
            schema = CreateAppPriceFactoryProductBulkJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for processProductPriceFactoryBulkJob")
                print(e)

        return response
    
    async def exportProductsInPriceFactory(self, id=None, body="", request_headers:Dict={}):
        """This API allows to export products in price factory.
        :param id : An `id` is a unique identifier for a particular price factory. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.exportProductsInPriceFactory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateAppPriceFactoryProductExportJobRequest
        schema = CreateAppPriceFactoryProductExportJobRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/export", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/export", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAppPriceFactoryProductExportJobResponse
            schema = CreateAppPriceFactoryProductExportJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for exportProductsInPriceFactory")
                print(e)

        return response
    
    async def pollPriceFactoryJobs(self, id=None, request_headers:Dict={}):
        """This API allows to poll job for adding products in price factory.
        :param id : An `id` is a unique identifier for a particular price factory. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.pollPriceFactoryJobs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/poll", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true},{"description":"An `id` is a unique identifier for a particular price factory.","in":"path","name":"id","schema":{"type":"string"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/owner-application/{self.applicationId}/price-factory/{id}/poll", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAppPriceFactoryProductExportJobPollResponse
            schema = CreateAppPriceFactoryProductExportJobPollResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for pollPriceFactoryJobs")
                print(e)

        return response
    
    async def getAppProductPrices(self, item_ids=None, factory_type_ids=None, page_no=None, page_size=None, request_headers:Dict={}):
        """This API allows to get product prices.
        :param item_ids : List of item ids to get product prices filtered by items. : type array
        :param factory_type_ids : List of factory type ids to get product prices filtered by factory type id. : type array
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if item_ids is not None:
            payload["item_ids"] = item_ids
        if factory_type_ids is not None:
            payload["factory_type_ids"] = factory_type_ids
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getAppProductPrices()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-prices", """{"required":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true}],"optional":[{"description":"List of item ids to get product prices filtered by items.","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"List of factory type ids to get product prices filtered by factory type id.","in":"query","name":"factory_type_ids","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","required":false,"schema":{"type":"integer","default":12}}],"query":[{"description":"List of item ids to get product prices filtered by items.","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"List of factory type ids to get product prices filtered by factory type id.","in":"query","name":"factory_type_ids","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","required":false,"schema":{"type":"integer","default":12}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular company.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","schema":{"type":"string"},"required":true}]}""", serverType="platform", item_ids=item_ids, factory_type_ids=factory_type_ids, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(item_ids=item_ids, factory_type_ids=factory_type_ids, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-prices", item_ids=item_ids, factory_type_ids=factory_type_ids, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductPrices
            schema = ProductPrices()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppProductPrices")
                print(e)

        return response
    
    async def getSynonyms(self, id=None, name=None, type=None, request_headers:Dict={}):
        """This view allows you to list down the available synonyms for an application
        :param id : Mongo id of the particular synonym : type string
        :param name : Synonym name : type string
        :param type : Synonym type - oneway/twoway : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if name is not None:
            payload["name"] = name
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = CatalogValidator.getSynonyms()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/synonyms", """{"required":[{"description":"The company id for which the synonym is being referenced","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"The application id for which the synonym is being referenced","in":"path","name":"application_id","schema":{"type":"string"},"required":true}],"optional":[{"description":"Mongo id of the particular synonym","in":"query","name":"id","required":false,"schema":{"type":"string"}},{"description":"Synonym name","in":"query","name":"name","required":false,"schema":{"type":"string"}},{"description":"Synonym type - oneway/twoway","in":"query","name":"type","required":false,"schema":{"type":"string"}}],"query":[{"description":"Mongo id of the particular synonym","in":"query","name":"id","required":false,"schema":{"type":"string"}},{"description":"Synonym name","in":"query","name":"name","required":false,"schema":{"type":"string"}},{"description":"Synonym type - oneway/twoway","in":"query","name":"type","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"The company id for which the synonym is being referenced","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"The application id for which the synonym is being referenced","in":"path","name":"application_id","schema":{"type":"string"},"required":true}]}""", serverType="platform", id=id, name=name, type=type)
        query_string = await create_query_string(id=id, name=name, type=type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/synonyms", id=id, name=name, type=type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SynonymListResponseSchema
            schema = SynonymListResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSynonyms")
                print(e)

        return response
    
    async def createSynonyms(self, body="", request_headers:Dict={}):
        """This view allows you to create search synonyms for an application
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createSynonyms()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SynonymCreateRequestSchema
        schema = SynonymCreateRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/synonyms", """{"required":[{"description":"The company id for which the synonym is being referenced","in":"path","name":"application_id","required":true,"schema":{"type":"integer"}},{"description":"The application id for which the synonym is being referenced","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The company id for which the synonym is being referenced","in":"path","name":"application_id","required":true,"schema":{"type":"integer"}},{"description":"The application id for which the synonym is being referenced","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/synonyms", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SynonymCreateResponseSchema
            schema = SynonymCreateResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSynonyms")
                print(e)

        return response
    
    async def updateSynonyms(self, id=None, body="", request_headers:Dict={}):
        """This view allows you to modify synonym attributes for a particular application
        :param id : An `id` is a unique identifier for a particular synonym channel. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.updateSynonyms()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SynonymCreateRequestSchema
        schema = SynonymCreateRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/synonym/{id}", """{"required":[{"name":"company_id","description":"The company id for which the synonym is being referenced","in":"path","required":true,"schema":{"type":"string"}},{"name":"application_id","description":"The application id for which the synonym is being referenced channel.","in":"path","required":true,"schema":{"type":"string"}},{"name":"id","description":"An `id` is a unique identifier for a particular synonym channel.","in":"path","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","description":"The company id for which the synonym is being referenced","in":"path","required":true,"schema":{"type":"string"}},{"name":"application_id","description":"The application id for which the synonym is being referenced channel.","in":"path","required":true,"schema":{"type":"string"}},{"name":"id","description":"An `id` is a unique identifier for a particular synonym channel.","in":"path","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/synonym/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SynonymUpdateResponseSchema
            schema = SynonymUpdateResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSynonyms")
                print(e)

        return response
    
    async def deleteSynonym(self, id=None, request_headers:Dict={}):
        """This view allows you to delete synonym for an application
        :param id : A `id` is a unique identifier of a synonym that is to be deleted. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.deleteSynonym()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/synonym", """{"required":[{"description":"The company id for which the synonym is being referenced account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"The application id for which the synonym is being referenced channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a synonym that is to be deleted.","in":"query","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"description":"A `id` is a unique identifier of a synonym that is to be deleted.","in":"query","name":"id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"The company id for which the synonym is being referenced account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"The application id for which the synonym is being referenced channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string(id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/synonym", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SynonymDeleteResponseSchema
            schema = SynonymDeleteResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSynonym")
                print(e)

        return response
    
    async def exportSynonyms(self, request_headers:Dict={}):
        """This API allows you to start a job creates a csv file containing all the synonyms for that application
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.exportSynonyms()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/bulk/export", """{"required":[{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/bulk/export", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SynonymExportResponseSchema
            schema = SynonymExportResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for exportSynonyms")
                print(e)

        return response
    
    async def sampleBulkSynonymsFile(self, type=None, request_headers:Dict={}):
        """This api return you the sample file for bulk synonyms upload
        :param type : Type of the file : type string
        """
        payload = {}
        
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = CatalogValidator.sampleBulkSynonymsFile()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/bulk/sample", """{"required":[{"description":"Type of the file","in":"query","name":"type","required":true,"schema":{"type":"string"}},{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[{"description":"Type of the file","in":"query","name":"type","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", type=type, )
        query_string = await create_query_string(type=type, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/bulk/sample", type=type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def uploadSynonyms(self, body="", request_headers:Dict={}):
        """This API allows you to upload a list of one-way/two-way synonyms
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.uploadSynonyms()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SynonymUploadRequestSchema
        schema = SynonymUploadRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/bulk", """{"required":[{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/bulk", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SynonymUploadResponseSchema
            schema = SynonymUploadResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for uploadSynonyms")
                print(e)

        return response
    
    async def validateBulkSynonyms(self, body="", request_headers:Dict={}):
        """This view allows you to validate the file uploaded for synonyms
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.validateBulkSynonyms()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SynonymBulkValidateRequestSchema
        schema = SynonymBulkValidateRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/bulk/validate", """{"required":[{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/bulk/validate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SynonymBulkValidateResponseSchema
            schema = SynonymBulkValidateResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateBulkSynonyms")
                print(e)

        return response
    
    async def processBulkSynonyms(self, body="", request_headers:Dict={}):
        """This view allows you to process a list of one-way/two-way synonyms
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.processBulkSynonyms()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SynonymBulkProcessRequestSchema
        schema = SynonymBulkProcessRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/bulk/process", """{"required":[{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/bulk/process", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SynonymBulkProcessResponseSchema
            schema = SynonymBulkProcessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for processBulkSynonyms")
                print(e)

        return response
    
    async def pollBulkSynonyms(self, id=None, request_headers:Dict={}):
        """This view allows you to poll for the status of the respective bulk upload job
        :param id : Id of the bulk job that needs to be polled. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.pollBulkSynonyms()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/poll/{id}", """{"required":[{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Id of the bulk job that needs to be polled.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The application id where custom search configuration is set","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Id of the bulk job that needs to be polled.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/poll/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SynonymBulkPollResponseSchema
            schema = SynonymBulkPollResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for pollBulkSynonyms")
                print(e)

        return response
    
    async def getAppPriceById(self, item_id=None, store_ids=None, factory_type_ids=None, seller_id=None, request_headers:Dict={}):
        """Retrieve the discounted price of a specific product for a given application. This endpoint allows filtering by stores, factory types, and sellers
        :param item_id : Unique identifier of the product : type integer
        :param store_ids : An array of unique identifiers representing the store locations from which the product pricing should be fetched. If not provided, pricing for all applicable store locations will be returned. : type array
        :param factory_type_ids : An array of unique factory type identifiers that specify that pricing from which factory type should be retrieved. This parameter allows filtering the price based on factory types. : type array
        :param seller_id : The company uid for which we want to fetch discounted pricing for a product : type integer
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        if store_ids is not None:
            payload["store_ids"] = store_ids
        if factory_type_ids is not None:
            payload["factory_type_ids"] = factory_type_ids
        if seller_id is not None:
            payload["seller_id"] = seller_id

        # Parameter validation
        schema = CatalogValidator.getAppPriceById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/item/{item_id}/price", """{"required":[{"description":"An `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"item_id","description":"Unique identifier of the product","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"store_ids","description":"An array of unique identifiers representing the store locations from which the product pricing should be fetched. If not provided, pricing for all applicable store locations will be returned.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"factory_type_ids","description":"An array of unique factory type identifiers that specify that pricing from which factory type should be retrieved. This parameter allows filtering the price based on factory types.","schema":{"type":"array","items":{"type":"string"}}},{"in":"query","name":"seller_id","description":"The company uid for which we want to fetch discounted pricing for a product","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"store_ids","description":"An array of unique identifiers representing the store locations from which the product pricing should be fetched. If not provided, pricing for all applicable store locations will be returned.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"factory_type_ids","description":"An array of unique factory type identifiers that specify that pricing from which factory type should be retrieved. This parameter allows filtering the price based on factory types.","schema":{"type":"array","items":{"type":"string"}}},{"in":"query","name":"seller_id","description":"The company uid for which we want to fetch discounted pricing for a product","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"description":"An `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"item_id","description":"Unique identifier of the product","schema":{"type":"integer"},"required":true}]}""", serverType="platform", item_id=item_id, store_ids=store_ids, factory_type_ids=factory_type_ids, seller_id=seller_id)
        query_string = await create_query_string(store_ids=store_ids, factory_type_ids=factory_type_ids, seller_id=seller_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/item/{item_id}/price", item_id=item_id, store_ids=store_ids, factory_type_ids=factory_type_ids, seller_id=seller_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppPriceByIdResponse
            schema = AppPriceByIdResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppPriceById")
                print(e)

        return response
    