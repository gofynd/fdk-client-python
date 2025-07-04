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
        """Retrieve the count of catalog related data like products, brands, departments and categories that have been made live as per configuration of the sales channel.
        :param brand : Brand slug that is to be searched. : type string
        """
        payload = {}
        
        if brand is not None:
            payload["brand"] = brand

        # Parameter validation
        schema = CatalogValidator.getCatalogInsights()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/analytics/insights/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Brand slug that is to be searched.","in":"query","name":"brand","required":false,"schema":{"type":"string"}}],"query":[{"description":"Brand slug that is to be searched.","in":"query","name":"brand","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", brand=brand)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/analytics/insights/", brand=brand), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CatalogInsightResponseSchema
            schema = CatalogInsightResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCatalogInsights")
                print(e)

        return response
    
    async def getApplicationBrandListing(self, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Retrieve brand listings related to the sales channel. A brand is the name under which a product is being sold
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name. Use this parameter to search brands by  brand name. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name. Use this parameter to search brands by  brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name. Use this parameter to search brands by  brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q)
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
        """Modify data associated to the brand for that particular sales channel.
        :param brand_uid : A `brand id` is a unique identifier for a particular brand. : type integer
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand/{brand_uid}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `brand id` is a unique identifier for a particular brand.","in":"path","name":"brand_uid","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `brand id` is a unique identifier for a particular brand.","in":"path","name":"brand_uid","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", brand_uid=brand_uid)
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
            from .models import SuccessResponseObject
            schema = SuccessResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppBrand")
                print(e)

        return response
    
    async def getApplicationBrands(self, department=None, page_no=None, page_size=None, q=None, brand_id=None, request_headers:Dict={}):
        """List all the brands.
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the "v1.0/departments/" API : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name. Use this parameter to search brands by  brand name. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brands", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the \"v1.0/departments/\" API","in":"query","name":"department","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name. Use this parameter to search brands by  brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Helps to sort the brands list on the basis of uid list.","in":"query","name":"brand_id","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"query":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the \"v1.0/departments/\" API","in":"query","name":"department","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name. Use this parameter to search brands by  brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Helps to sort the brands list on the basis of uid list.","in":"query","name":"brand_id","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id)
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
            from .models import BrandListingResponseSchema
            schema = BrandListingResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationBrands")
                print(e)

        return response
    
    async def getCategories(self, department=None, request_headers:Dict={}):
        """Retrieve a list of categories associated to company and sales channel. user can filter on departments.
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the "v1.0/departments/" API : type string
        """
        payload = {}
        
        if department is not None:
            payload["department"] = department

        # Parameter validation
        schema = CatalogValidator.getCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the \"v1.0/departments/\" API","in":"query","name":"department","required":false,"schema":{"type":"string"}}],"query":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the \"v1.0/departments/\" API","in":"query","name":"department","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", department=department)
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
            from .models import CategoryListingResponseSchema
            schema = CategoryListingResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCategories")
                print(e)

        return response
    
    async def getApplicationCategoryListing(self, department_id=None, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Retrieve category listings related to the sales channel , with the ability to filter results based on department ,category names etc.
        :param department_id : A `department_id` is a unique identifier for a particular department. : type integer
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : A search query string. Use this parameter to filter results based on a keyword or specific value. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"A `department_id` is a unique identifier for a particular department.","in":"query","name":"department_id","required":false,"schema":{"type":"integer"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"A search query string. Use this parameter to filter results based on a keyword or specific value.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"A `department_id` is a unique identifier for a particular department.","in":"query","name":"department_id","required":false,"schema":{"type":"integer"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"A search query string. Use this parameter to filter results based on a keyword or specific value.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", department_id=department_id, page_no=page_no, page_size=page_size, q=q)
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
        """Modify category data related to the sales channel .
        :param category_uid : A `category id` is a unique identifier for a particular category. : type string
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category/{category_uid}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `category id` is a unique identifier for a particular category.","in":"path","name":"category_uid","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `category id` is a unique identifier for a particular category.","in":"path","name":"category_uid","required":true,"schema":{"type":"string"}}]}""", serverType="platform", category_uid=category_uid)
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
            from .models import SuccessResponseObject
            schema = SuccessResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCategory")
                print(e)

        return response
    
    async def getAllCollections(self, q=None, schedule_status=None, type=None, tags=None, is_active=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve all collections based on criteria such as collection name, schedule status, and active status.
        :param q : Get collection list filtered by q string, : type string
        :param schedule_status : Get collection list filtered by scheduled status, : type string
        :param type : Type of the collections : type string
        :param tags : Each response will contain next_id param, which should be sent back to make pagination work. : type array
        :param is_active : Get collections filtered by active status. : type boolean
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
        if tags is not None:
            payload["tags"] = tags
        if is_active is not None:
            payload["is_active"] = is_active
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getAllCollections()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Get collection list filtered by q string,","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Get collection list filtered by scheduled status,","in":"query","name":"schedule_status","required":false,"schema":{"enum":["live","upcoming","expired"],"type":"string"}},{"description":"Type of the collections","in":"query","name":"type","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get collections filtered by active status.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"query":[{"description":"Get collection list filtered by q string,","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Get collection list filtered by scheduled status,","in":"query","name":"schedule_status","required":false,"schema":{"enum":["live","upcoming","expired"],"type":"string"}},{"description":"Type of the collections","in":"query","name":"type","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get collections filtered by active status.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionListingResponseSchema
            schema = GetCollectionListingResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllCollections")
                print(e)

        return response
    
    async def createCollection(self, q=None, schedule_status=None, type=None, tags=None, is_active=None, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Create a collection for a sales channel linked to a company.
        :param q : Get collection list filtered by q string, : type string
        :param schedule_status : Get collection list filtered by scheduled status, : type string
        :param type : Type of the collections : type string
        :param tags : Each response will contain next_id param, which should be sent back to make pagination work. : type array
        :param is_active : Get collections filtered by active status. : type boolean
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
        if tags is not None:
            payload["tags"] = tags
        if is_active is not None:
            payload["is_active"] = is_active
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.createCollection()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateCollection
        schema = CreateCollection()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Get collection list filtered by q string,","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Get collection list filtered by scheduled status,","in":"query","name":"schedule_status","required":false,"schema":{"enum":["live","upcoming","expired"],"type":"string"}},{"description":"Type of the collections","in":"query","name":"type","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get collections filtered by active status.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"query":[{"description":"Get collection list filtered by q string,","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Get collection list filtered by scheduled status,","in":"query","name":"schedule_status","required":false,"schema":{"enum":["live","upcoming","expired"],"type":"string"}},{"description":"Type of the collections","in":"query","name":"type","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get collections filtered by active status.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CollectionCreateResponseSchema
            schema = CollectionCreateResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCollection")
                print(e)

        return response
    
    async def getApplicationFilterValues(self, filter_key=None, c=None, collection_id=None, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """This API is designed to retrieve the filter values for all available options within the selected filter, such as "red" for color.

        :param filter_key : A `filter_key` is a filter key which returns all the available filter values. : type string
        :param c : The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in "c" parameter in this format. "?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts" : type string
        :param collection_id : A `collection_id` is a unique identifier for a particular collection. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param q : The `q` parameter allows you to search and filter specific data within the filter options. It acts as a query keyword that can refine the results by matching relevant filter values, such as a category name or any other applicable filter criteria. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/filter-options/{filter_key}/values", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `filter_key` is a filter key which returns all the available filter values.","in":"path","name":"filter_key","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in \"c\" parameter in this format. \"?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts\"","in":"query","name":"c","required":false,"schema":{"type":"string"}},{"description":"A `collection_id` is a unique identifier for a particular collection.","in":"query","name":"collection_id","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"The `q` parameter allows you to search and filter specific data within the filter options. It acts as a query keyword that can refine the results by matching relevant filter values, such as a category name or any other applicable filter criteria.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in \"c\" parameter in this format. \"?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts\"","in":"query","name":"c","required":false,"schema":{"type":"string"}},{"description":"A `collection_id` is a unique identifier for a particular collection.","in":"query","name":"collection_id","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"The `q` parameter allows you to search and filter specific data within the filter options. It acts as a query keyword that can refine the results by matching relevant filter values, such as a category name or any other applicable filter criteria.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `filter_key` is a filter key which returns all the available filter values.","in":"path","name":"filter_key","required":true,"schema":{"type":"string"}}]}""", serverType="platform", filter_key=filter_key, c=c, collection_id=collection_id, page_no=page_no, page_size=page_size, q=q)
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
            from .models import GetQueryFiltersValuesResponseSchema
            schema = GetQueryFiltersValuesResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationFilterValues")
                print(e)

        return response
    
    async def getApplicationFilterKeys(self, c=None, request_headers:Dict={}):
        """Retrieve the details of all applicable product filters, such as Color, Brand, and Category, indicating the criteria keys where filters can be applied.
        :param c : The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in "c" parameter in this format. "?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts" : type string
        """
        payload = {}
        
        if c is not None:
            payload["c"] = c

        # Parameter validation
        schema = CatalogValidator.getApplicationFilterKeys()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/filter-options/keys", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in \"c\" parameter in this format. \"?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts\"","in":"query","name":"c","required":false,"schema":{"type":"string"}}],"query":[{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in \"c\" parameter in this format. \"?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts\"","in":"query","name":"c","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", c=c)
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
            from .models import GetQueryFiltersKeysResponseSchema
            schema = GetQueryFiltersKeysResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationFilterKeys")
                print(e)

        return response
    
    async def getQueryFilters(self, request_headers:Dict={}):
        """Retrieve query filters to configure a collection for a company and a sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getQueryFilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetQueryFiltersResponseSchema
            schema = GetQueryFiltersResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getQueryFilters")
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CommonResponseSchemaCollection
            schema = CommonResponseSchemaCollection()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCollection")
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateCollection
            schema = UpdateCollection()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCollection")
                print(e)

        return response
    
    async def getCollectionItems(self, id=None, sort_on=None, page_id=None, page_size=None, page_no=None, request_headers:Dict={}):
        """Get items from a collection specified by its id.
        :param id : A `id` is a unique identifier of a collection. : type string
        :param sort_on : Each response will contain sort_on param, which should be sent back to make pagination work. : type string
        :param page_id : Each response will contain next_id param, which should be sent back to make pagination work. : type string
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param page_no : Identifies the specific page of results being requested. : type integer
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if sort_on is not None:
            payload["sort_on"] = sort_on
        if page_id is not None:
            payload["page_id"] = page_id
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no

        # Parameter validation
        schema = CatalogValidator.getCollectionItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Each response will contain sort_on param, which should be sent back to make pagination work.","in":"query","name":"sort_on","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Identifies the specific page of results being requested.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}}],"query":[{"description":"Each response will contain sort_on param, which should be sent back to make pagination work.","in":"query","name":"sort_on","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Identifies the specific page of results being requested.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", id=id, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionItemsResponseSchema
            schema = GetCollectionItemsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCollectionItems")
                print(e)

        return response
    
    async def addCollectionItems(self, id=None, body="", request_headers:Dict={}):
        """Adds items to a collection specified by its id
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{slug}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{slug}/", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionDetailResponseSchema
            schema = GetCollectionDetailResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCollectionDetail")
                print(e)

        return response
    
    async def getApplicationDepartmentListing(self, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Retrieve department listings related to the sales channel. Departments are used to categorize similar products, and you can filter the results based on department names
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : A search query string. Use this parameter to filter results based on a keyword or specific value. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"A search query string. Use this parameter to filter results based on a keyword or specific value.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"A search query string. Use this parameter to filter results based on a keyword or specific value.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q)
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
            from .models import ApplicationDepartmentListingResponseSchema
            schema = ApplicationDepartmentListingResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationDepartmentListing")
                print(e)

        return response
    
    async def updateAppDepartment(self, department_uid=None, body="", request_headers:Dict={}):
        """Modify department data associated to the sales channel.
        :param department_uid : A `department id` is a unique identifier for a particular department. : type integer
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department/{department_uid}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `department id` is a unique identifier for a particular department.","in":"path","name":"department_uid","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `department id` is a unique identifier for a particular department.","in":"path","name":"department_uid","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", department_uid=department_uid)
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
            from .models import SuccessResponseObject
            schema = SuccessResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppDepartment")
                print(e)

        return response
    
    async def getDepartments(self, request_headers:Dict={}):
        """Retrieve a list of departments associated with a comapny and sales channel.
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
            from .models import DepartmentResponseSchema
            schema = DepartmentResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDepartments")
                print(e)

        return response
    
    async def getAppInventory(self, item_ids=None, store_ids=None, brand_ids=None, seller_identifiers=None, timestamp=None, page_size=None, page_id=None, qty_gt=None, qty_lt=None, qty_type=None, from_date=None, to_date=None, request_headers:Dict={}):
        """Retrieve inventory data related to the sales channel. this can be used  to get the Inventory status of products.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/inventory/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The Item Id of the product.","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Store Id of products to fetch inventory.","in":"query","name":"store_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Brand Id of products to fetch inventory.","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Unique seller_identifier of the product.","in":"query","name":"seller_identifiers","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Timestamp in UTC format (2020-07-23T10:27:50Z)","in":"query","name":"timestamp","required":false,"schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Page ID to retrieve next set of results.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"This field allows you to filter for inventories that have quantity greater than to the specified value based on qty_type filter.","in":"query","name":"qty_gt","required":false,"schema":{"type":"integer"}},{"description":"This field allows you to filter for inventories that have a quantity less than to the specified value based on qty_type filter.","in":"query","name":"qty_lt","required":false,"schema":{"type":"integer"}},{"description":"This field provides flexibility in selecting filter for inventory quantity counts and date queries. For example, you might use this field to specify \"total\" or \"sellable\" quantity.","in":"query","name":"qty_type","required":false,"schema":{"enum":["total","sellable"],"type":"string"}},{"description":"Inventory updated on filter to get inventories greater then or equal to provided date based on qty_type value.","in":"query","name":"from_date","required":false,"schema":{"format":"date-time","type":"string"}},{"description":"Inventory updated on filter to get inventories less then or equal to provided date based on qty_type value.","in":"query","name":"to_date","required":false,"schema":{"format":"date-time","type":"string"}}],"query":[{"description":"The Item Id of the product.","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Store Id of products to fetch inventory.","in":"query","name":"store_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Brand Id of products to fetch inventory.","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Unique seller_identifier of the product.","in":"query","name":"seller_identifiers","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Timestamp in UTC format (2020-07-23T10:27:50Z)","in":"query","name":"timestamp","required":false,"schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Page ID to retrieve next set of results.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"This field allows you to filter for inventories that have quantity greater than to the specified value based on qty_type filter.","in":"query","name":"qty_gt","required":false,"schema":{"type":"integer"}},{"description":"This field allows you to filter for inventories that have a quantity less than to the specified value based on qty_type filter.","in":"query","name":"qty_lt","required":false,"schema":{"type":"integer"}},{"description":"This field provides flexibility in selecting filter for inventory quantity counts and date queries. For example, you might use this field to specify \"total\" or \"sellable\" quantity.","in":"query","name":"qty_type","required":false,"schema":{"enum":["total","sellable"],"type":"string"}},{"description":"Inventory updated on filter to get inventories greater then or equal to provided date based on qty_type value.","in":"query","name":"from_date","required":false,"schema":{"format":"date-time","type":"string"}},{"description":"Inventory updated on filter to get inventories less then or equal to provided date based on qty_type value.","in":"query","name":"to_date","required":false,"schema":{"format":"date-time","type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_ids=item_ids, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, timestamp=timestamp, page_size=page_size, page_id=page_id, qty_gt=qty_gt, qty_lt=qty_lt, qty_type=qty_type, from_date=from_date, to_date=to_date)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/inventory/", item_ids=item_ids, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, timestamp=timestamp, page_size=page_size, page_id=page_id, qty_gt=qty_gt, qty_lt=qty_lt, qty_type=qty_type, from_date=from_date, to_date=to_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryStockResponseSchema
            schema = InventoryStockResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppInventory")
                print(e)

        return response
    
    async def getAppLocations(self, store_type=None, uid=None, q=None, stage=None, page_no=None, page_size=None, tags=None, store_types=None, request_headers:Dict={}):
        """Retrieve all stores associated with a sales channel, with support for searching by store name and filtering by store type and status.
        :param store_type : Helps to sort the location list on the basis of location type. : type string
        :param uid : Helps to sort the location list on the basis of uid list. : type array
        :param q : Query that is to be searched. : type string
        :param stage : to filter companies on basis of verified or unverified companies. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 20. : type integer
        :param tags : Get locations filtered by tags. : type array
        :param store_types : Get locations filtered by store types. : type array
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

        # Parameter validation
        schema = CatalogValidator.getAppLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/locations", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Helps to sort the location list on the basis of location type.","in":"query","name":"store_type","required":false,"schema":{"type":"string","enum":["high_street","warehouse","mall"]}},{"description":"Helps to sort the location list on the basis of uid list.","in":"query","name":"uid","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Query that is to be searched.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"to filter companies on basis of verified or unverified companies.","in":"query","name":"stage","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 20.","in":"query","name":"page_size","required":false,"schema":{"default":20,"type":"integer"}},{"description":"Get locations filtered by tags.","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get locations filtered by store types.","in":"query","name":"store_types","required":false,"schema":{"items":{"type":"string"},"type":"array"}}],"query":[{"description":"Helps to sort the location list on the basis of location type.","in":"query","name":"store_type","required":false,"schema":{"type":"string","enum":["high_street","warehouse","mall"]}},{"description":"Helps to sort the location list on the basis of uid list.","in":"query","name":"uid","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Query that is to be searched.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"to filter companies on basis of verified or unverified companies.","in":"query","name":"stage","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 20.","in":"query","name":"page_size","required":false,"schema":{"default":20,"type":"integer"}},{"description":"Get locations filtered by tags.","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get locations filtered by store types.","in":"query","name":"store_types","required":false,"schema":{"items":{"type":"string"},"type":"array"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size, tags=tags, store_types=store_types)
        query_string = await create_query_string(store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size, tags=tags, store_types=store_types)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/locations", store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size, tags=tags, store_types=store_types), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LocationListSchema
            schema = LocationListSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppLocations")
                print(e)

        return response
    
    async def getConfigurations(self, request_headers:Dict={}):
        """Retrieve a detailed configurations for product catalog specific to a company and an sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Add configuration for products & listing specific to a company and an sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createConfigurationProductListing()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppConfiguration
        schema = AppConfiguration()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        """Retrieve configuration meta data for the catalog specific to a company and an sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getCatalogConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCatalogConfigurationMetaData
            schema = GetCatalogConfigurationMetaData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCatalogConfiguration")
                print(e)

        return response
    
    async def getConfigurationByType(self, type=None, include_inactive=None, request_headers:Dict={}):
        """Retrieve configuration details based on a specific type in the catalog for a company and an sales channel.
        :param type : type can be brands, categories etc. : type string
        :param include_inactive : Pass the `include_inactive` parameter to retrieve inactive brand or category details. This flag enables fetching all brands or categories,including those that are inactive. : type boolean
        """
        payload = {}
        
        if type is not None:
            payload["type"] = type
        if include_inactive is not None:
            payload["include_inactive"] = include_inactive

        # Parameter validation
        schema = CatalogValidator.getConfigurationByType()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Pass the `include_inactive` parameter to retrieve inactive brand or category details. This flag enables fetching all brands or categories,including those that are inactive.","in":"query","name":"include_inactive","required":false,"schema":{"default":false,"type":"boolean"}}],"query":[{"description":"Pass the `include_inactive` parameter to retrieve inactive brand or category details. This flag enables fetching all brands or categories,including those that are inactive.","in":"query","name":"include_inactive","required":false,"schema":{"default":false,"type":"boolean"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}]}""", serverType="platform", type=type, include_inactive=include_inactive)
        query_string = await create_query_string(include_inactive=include_inactive)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", type=type, include_inactive=include_inactive), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Add configuration details based on a specific type in the catalog for a company and an sales channel.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}]}""", serverType="platform", type=type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        """Retrieve sales channel product details by its item_id and depending upon filters sent in request.
        :param item_id : product id for a particular product. : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id

        # Parameter validation
        schema = CatalogValidator.getAppProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"product id for a particular product.","in":"path","name":"item_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"product id for a particular product.","in":"path","name":"item_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_id=item_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", item_id=item_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OwnerAppItemResponseSchema
            schema = OwnerAppItemResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppProduct")
                print(e)

        return response
    
    async def updateAppProduct(self, item_id=None, body="", request_headers:Dict={}):
        """Allows to update data associated to a item by its item_id for a sales channel.
        :param item_id : A `item_id` is a unique identifier for a particular item. : type integer
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `item_id` is a unique identifier for a particular item.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `item_id` is a unique identifier for a particular item.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", item_id=item_id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", item_id=item_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseObject
            schema = SuccessResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppProduct")
                print(e)

        return response
    
    async def getApplicationProducts(self, q=None, f=None, c=None, filters=None, is_dependent=None, sort_on=None, page_id=None, page_size=None, page_no=None, page_type=None, item_ids=None, request_headers:Dict={}):
        """Retrieve products associated with the sales channel. List all the products associated with a brand, collection or category in a requested sort order.
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
        schema = CatalogValidator.getApplicationProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The search query. This can be a partial or complete name of a either a product, brand or category","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","in":"query","name":"f","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","in":"query","name":"c","required":false,"schema":{"type":"string"}},{"description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","in":"query","name":"filters","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"This query parameter is used to get the dependent products in the listing.","in":"query","name":"is_dependent","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","in":"query","name":"sort_on","required":false,"schema":{"enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"],"type":"string"}},{"description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"If page_type is number then pass it to fetch page items. Default is 1.","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"For pagination type should be cursor or number. Default is cursor.","in":"query","name":"page_type","required":false,"schema":{"default":"cursor","type":"string","enum":["cursor","number"]}},{"description":"Item Ids of product","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"string"},"type":"array"}}],"query":[{"description":"The search query. This can be a partial or complete name of a either a product, brand or category","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","in":"query","name":"f","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","in":"query","name":"c","required":false,"schema":{"type":"string"}},{"description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","in":"query","name":"filters","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"This query parameter is used to get the dependent products in the listing.","in":"query","name":"is_dependent","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","in":"query","name":"sort_on","required":false,"schema":{"enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"],"type":"string"}},{"description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"If page_type is number then pass it to fetch page items. Default is 1.","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"For pagination type should be cursor or number. Default is cursor.","in":"query","name":"page_type","required":false,"schema":{"default":"cursor","type":"string","enum":["cursor","number"]}},{"description":"Item Ids of product","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"string"},"type":"array"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", q=q, f=f, c=c, filters=filters, is_dependent=is_dependent, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids)
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
            from .models import ApplicationProductListingResponseSchema
            schema = ApplicationProductListingResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationProducts")
                print(e)

        return response
    
    async def getDiscountedInventoryBySizeIdentifier(self, item_id=None, size_identifier=None, page_no=None, page_size=None, location_ids=None, request_headers:Dict={}):
        """Allows to retrieve Inventory data for particular company grouped by size and store.
        :param item_id : A `item_id` is a unique identifier for a specific product. : type integer
        :param size_identifier : Size Identifier (Seller Identifier or Primary Identifier). : type integer
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{item_id}/inventory/{size_identifier}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `item_id` is a unique identifier for a specific product.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier).","in":"path","name":"size_identifier","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search by store ids.","in":"query","name":"location_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search by store ids.","in":"query","name":"location_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `item_id` is a unique identifier for a specific product.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier).","in":"path","name":"size_identifier","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, location_ids=location_ids)
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
            from .models import ApplicationInventorySellerIdentifierResponsePaginated
            schema = ApplicationInventorySellerIdentifierResponsePaginated()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDiscountedInventoryBySizeIdentifier")
                print(e)

        return response
    
    async def getProductDetailBySlug(self, slug=None, request_headers:Dict={}):
        """Retrieve detailed product information using a product slug. 
        :param slug : The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like "v1.0/products/" : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getProductDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{slug}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like \"v1.0/products/\"","in":"path","name":"slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like \"v1.0/products/\"","in":"path","name":"slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug)
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
        """Retrieve products specific to the sales channel, with filtering options available for brand, category, department, tags, item IDs, product name, and pagination support
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Get multiple products filtered by Brand Ids","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Category Ids","in":"query","name":"category_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Department Ids","in":"query","name":"department_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by tags","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get multiple products filtered by Item Ids","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"Search with Item Code, Name, Slug or Identifier.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"Get multiple products filtered by Brand Ids","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Category Ids","in":"query","name":"category_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Department Ids","in":"query","name":"department_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by tags","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get multiple products filtered by Item Ids","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"Search with Item Code, Name, Slug or Identifier.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, item_ids=item_ids, page_no=page_no, page_size=page_size, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products/", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, item_ids=item_ids, page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RawProductListingResponseSchema
            schema = RawProductListingResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppProducts")
                print(e)

        return response
    
    async def getAppReturnConfiguration(self, request_headers:Dict={}):
        """Get Product Return configuration set at an sales channel level
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAppReturnConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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
            from .models import AppReturnConfigResponseSchema
            schema = AppReturnConfigResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppReturnConfiguration")
                print(e)

        return response
    
    async def createAppReturnConfiguration(self, body="", request_headers:Dict={}):
        """This allows you to configure all return-related settings, such as is_returnable and return window etc. for sales channel level
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createAppReturnConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUpdateAppReturnConfig
        schema = CreateUpdateAppReturnConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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
            from .models import SuccessResponseObject
            schema = SuccessResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppReturnConfiguration")
                print(e)

        return response
    
    async def updateAppReturnConfiguration(self, body="", request_headers:Dict={}):
        """Update Return configuration level set for an sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateAppReturnConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUpdateAppReturnConfig
        schema = CreateUpdateAppReturnConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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
            from .models import SuccessResponseObject
            schema = SuccessResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppReturnConfiguration")
                print(e)

        return response
    
    async def deleteAppCategoryReturnConfiguration(self, body="", request_headers:Dict={}):
        """Delete Category level sales channel Return Configuration setttings
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.deleteAppCategoryReturnConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DeleteAppCategoryReturnConfig
        schema = DeleteAppCategoryReturnConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAppCategoryReturnConfiguration")
                print(e)

        return response
    
    async def getAppCategoryReturnConfig(self, q=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Get all category level configuration level set for an sales channel.
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
            from .models import BaseAppCategoryReturnConfigResponseSchema
            schema = BaseAppCategoryReturnConfigResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCategoryReturnConfig")
                print(e)

        return response
    
    async def createAppCategoryReturnConfiguration(self, body="", request_headers:Dict={}):
        """Create Category level sales channel Return Configuration setttings
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createAppCategoryReturnConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BaseAppCategoryReturnConfig
        schema = BaseAppCategoryReturnConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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
            from .models import SuccessResponseObject
            schema = SuccessResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppCategoryReturnConfiguration")
                print(e)

        return response
    
    async def updateAppCategoryReturnConfiguration(self, body="", request_headers:Dict={}):
        """Update Category level sales channel Return Configuration setttings
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateAppCategoryReturnConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BaseAppCategoryReturnConfig
        schema = BaseAppCategoryReturnConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCategoryReturnConfiguration")
                print(e)

        return response
    
    async def getAutocompleteConfig(self, request_headers:Dict={}):
        """Get custom autocomplete keyword configuration for a specific sales channel which allows you to map any endpoint with these keywords to give you the ultimate suggestion results.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAutocompleteConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAutocompleteWordsResponseSchema
            schema = GetAutocompleteWordsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAutocompleteConfig")
                print(e)

        return response
    
    async def createCustomAutocompleteRule(self, body="", request_headers:Dict={}):
        """Create custom autocomplete keyword configurations for a specific sales channel to map any endpoint with these keywords.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCustomAutocompleteRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateAutocompleteKeyword
        schema = CreateAutocompleteKeyword()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAutocompleteWordsResponseSchema
            schema = CreateAutocompleteWordsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomAutocompleteRule")
                print(e)

        return response
    
    async def deleteAutocompleteKeyword(self, id=None, request_headers:Dict={}):
        """Delete custom autocomplete keyword configurations for a specific sales channel by its id.
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.deleteAutocompleteKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteResponseSchema
            schema = DeleteResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAutocompleteKeyword")
                print(e)

        return response
    
    async def getAutocompleteKeywordDetail(self, id=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific autocomplete keyword for a specific sales channel by its id.
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getAutocompleteKeywordDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAutocompleteWordsResponseSchema
            schema = GetAutocompleteWordsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAutocompleteKeywordDetail")
                print(e)

        return response
    
    async def updateAutocompleteKeyword(self, id=None, body="", request_headers:Dict={}):
        """Update a specific autocomplete keyword configuration by its id for a specific sales channel.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAutocompleteWordsResponseSchema
            schema = GetAutocompleteWordsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAutocompleteKeyword")
                print(e)

        return response
    
    async def deleteSearchConfiguration(self, request_headers:Dict={}):
        """Delete Search Configuration for a specific sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.deleteSearchConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteSearchConfigurationResponseSchema
            schema = DeleteSearchConfigurationResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSearchConfiguration")
                print(e)

        return response
    
    async def getSearchConfiguration(self, request_headers:Dict={}):
        """Get search configuration for a specific company and sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getSearchConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchConfigurationResponseSchema
            schema = GetSearchConfigurationResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSearchConfiguration")
                print(e)

        return response
    
    async def createSearchConfiguration(self, body="", request_headers:Dict={}):
        """Create search configuration for the catalog for a specific company and sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createSearchConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchConfigurationRequestSchema
        schema = CreateSearchConfigurationRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateSearchConfigurationResponseSchema
            schema = CreateSearchConfigurationResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSearchConfiguration")
                print(e)

        return response
    
    async def updateSearchConfiguration(self, body="", request_headers:Dict={}):
        """Allows you to modify searchable attributes for an sales channel. searchable attributes are the fields on which the products are searched.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateSearchConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateSearchConfigurationRequestSchema
        schema = UpdateSearchConfigurationRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateSearchConfigurationResponseSchema
            schema = UpdateSearchConfigurationResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSearchConfiguration")
                print(e)

        return response
    
    async def getAllSearchKeyword(self, request_headers:Dict={}):
        """Get all custom search keywords for a specific company and sales channel allows you to map certain conditions with the keywords to give you ultimate results.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAllSearchKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsResponseSchema
            schema = GetSearchWordsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllSearchKeyword")
                print(e)

        return response
    
    async def createCustomKeyword(self, body="", request_headers:Dict={}):
        """Create a Custom Search Keywords for a specific company and sales channel allows you to map certail conditions with the keywords to give you ultimate results.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCustomKeyword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchKeyword
        schema = CreateSearchKeyword()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsData
            schema = GetSearchWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomKeyword")
                print(e)

        return response
    
    async def deleteSearchKeywords(self, id=None, request_headers:Dict={}):
        """Delete a search keywords by its id for a specific company and sales channel.
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.deleteSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteResponseSchema
            schema = DeleteResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSearchKeywords")
                print(e)

        return response
    
    async def getSearchKeywords(self, id=None, request_headers:Dict={}):
        """Retrieve a list of a specific list of keywords by its id for a specific company and sales channel.
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsDetailResponseSchema
            schema = GetSearchWordsDetailResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSearchKeywords")
                print(e)

        return response
    
    async def updateSearchKeywords(self, id=None, body="", request_headers:Dict={}):
        """Update a specific search keyword by its id for a specific company and sales channel.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsData
            schema = GetSearchWordsData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSearchKeywords")
                print(e)

        return response
    
    async def updateAppLocation(self, store_uid=None, body="", request_headers:Dict={}):
        """Modify location data related to the sales channel.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/{store_uid}", """{"required":[{"description":"Id of the company associated to location custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"store id for which the custom_json is associated.","in":"path","name":"store_uid","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to location custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"store id for which the custom_json is associated.","in":"path","name":"store_uid","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", store_uid=store_uid)
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
            from .models import SuccessResponseObject
            schema = SuccessResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppLocation")
                print(e)

        return response
    
    async def updateAllowSingle(self, body="", request_headers:Dict={}):
        """Modify allow single flag for filters of the sales channel for a company and an sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateAllowSingle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AllowSingleRequestSchema
        schema = AllowSingleRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/filter/allow_single", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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
            from .models import ConfigSuccessResponseSchema
            schema = ConfigSuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAllowSingle")
                print(e)

        return response
    
    async def updateDefaultSort(self, body="", request_headers:Dict={}):
        """Modify the default sort key configuration for a company and an sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateDefaultSort()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DefaultKeyRequestSchema
        schema = DefaultKeyRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/sort/default_key", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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
            from .models import ConfigSuccessResponseSchema
            schema = ConfigSuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateDefaultSort")
                print(e)

        return response
    
    async def getListingConfigurations(self, config_type=None, page_no=None, page_size=None, search=None, request_headers:Dict={}):
        """Retrieve product listing configurations based on specific config_type for a company and an sales channel.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}}]}""", serverType="platform", config_type=config_type, page_no=page_no, page_size=page_size, search=search)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, search=search)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", config_type=config_type, page_no=page_no, page_size=page_size, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetConfigResponseSchema
            schema = GetConfigResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getListingConfigurations")
                print(e)

        return response
    
    async def createListingConfiguration(self, config_type=None, body="", request_headers:Dict={}):
        """Add configuration for product catalog listing specific to a company and an sales channel.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}}]}""", serverType="platform", config_type=config_type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", config_type=config_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppConfigurationsSort
            schema = AppConfigurationsSort()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createListingConfiguration")
                print(e)

        return response
    
    async def getGroupConfigurations(self, config_type=None, page_no=None, page_size=None, search=None, template_slug=None, request_headers:Dict={}):
        """Retrieve the details of product group configurations based on config types for a company and an sales channel.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}]}""", serverType="platform", config_type=config_type, page_no=page_no, page_size=page_size, search=search, template_slug=template_slug)
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
            from .models import GetConfigResponseSchema
            schema = GetConfigResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGroupConfigurations")
                print(e)

        return response
    
    async def createGroupConfiguration(self, config_type=None, body="", request_headers:Dict={}):
        """Create group configuration for a specific config_type for a company and an sales channel.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}]}""", serverType="platform", config_type=config_type)
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
    
    async def deleteGroupConfiguration(self, config_type=None, group_slug=None, request_headers:Dict={}):
        """Delete group configurations by its slug for a specific config_type for a company and an sales channel.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", config_type=config_type, group_slug=group_slug)
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

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigSuccessResponseSchema
            schema = ConfigSuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteGroupConfiguration")
                print(e)

        return response
    
    async def updateGroupConfiguration(self, config_type=None, group_slug=None, body="", request_headers:Dict={}):
        """Modify group configurations by its slug for specific config_type for a company and an sales channel.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", config_type=config_type, group_slug=group_slug)
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
    
    async def deleteListingConfiguration(self, config_type=None, config_id=None, request_headers:Dict={}):
        """Remove a specific product listing configuration by its config_id for a specific config_type for a company and an sales channel.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", config_type=config_type, config_id=config_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", config_type=config_type, config_id=config_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigSuccessResponseSchema
            schema = ConfigSuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteListingConfiguration")
                print(e)

        return response
    
    async def updateListingConfiguration(self, config_type=None, config_id=None, body="", request_headers:Dict={}):
        """Modify a specific product listing configuration by its config_id for a specific config_type for a company and an sales channel.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", config_type=config_type, config_id=config_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", config_type=config_type, config_id=config_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppConfigurationsSort
            schema = AppConfigurationsSort()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateListingConfiguration")
                print(e)

        return response
    
    async def getConfigurationMetadata(self, config_type=None, template_slug=None, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Retrieve the configuraion metadata details for specific config_type for a company and an sales channel.
        :param config_type : A `config_type` is an identifier that defines a specific type of configuration. : type string
        :param template_slug : Get configuration list filtered by `template_slug` string. This is for the details and comparision groups. : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. : type integer
        :param q : Get configuration list filtered by `q` string. : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        if template_slug is not None:
            payload["template_slug"] = template_slug
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = CatalogValidator.getConfigurationMetadata()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/metadata/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","details_groups","comparisons_groups","variant","similar","brands","categories","seller_groups"],"type":"string"}}],"optional":[{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer"},"required":false},{"in":"query","name":"q","description":"Get configuration list filtered by `q` string.","schema":{"type":"string"},"required":false}],"query":[{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer"},"required":false},{"in":"query","name":"q","description":"Get configuration list filtered by `q` string.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","details_groups","comparisons_groups","variant","similar","brands","categories","seller_groups"],"type":"string"}}]}""", serverType="platform", config_type=config_type, template_slug=template_slug, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(template_slug=template_slug, page_no=page_no, page_size=page_size, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/metadata/", config_type=config_type, template_slug=template_slug, page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetConfigMetadataResponseSchema
            schema = GetConfigMetadataResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getConfigurationMetadata")
                print(e)

        return response
    