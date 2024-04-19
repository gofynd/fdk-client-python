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
        """Catalog Insights api returns the count of catalog related data like products, brands, departments and categories that have been made live as per configuration of the app.
        :param brand : Brand slug : type string
        """
        payload = {}
        
        if brand is not None:
            payload["brand"] = brand

        # Parameter validation
        schema = CatalogValidator.getCatalogInsights()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/analytics/insights/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Brand slug","in":"query","name":"brand","required":false,"schema":{"type":"string"}}],"query":[{"description":"Brand slug","in":"query","name":"brand","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", brand=brand)
        query_string = await create_query_string(brand=brand)

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
    
    async def getApplicationBrandListing(self, page_no=None, page_size=None, q=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by  brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by  brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)

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
    
    async def updateAppBrand(self, brand_uid=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brand/{brand_uid}", """{"required":[{"description":"Id of the company associated to brand custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"brand id for which the custom_json is associated.","in":"path","name":"brand_uid","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to brand custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"brand id for which the custom_json is associated.","in":"path","name":"brand_uid","required":true,"schema":{"type":"string"}}]}""", brand_uid=brand_uid)
        query_string = await create_query_string(brand_uid=brand_uid)

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
    
    async def getApplicationBrands(self, department=None, page_no=None, page_size=None, q=None, brand_id=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brands", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","in":"query","name":"department","required":false,"schema":{"enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"],"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by  brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Helps to sort the brands list on the basis of uid list.","in":"query","name":"brand_id","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"query":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","in":"query","name":"department","required":false,"schema":{"enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"],"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by  brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Helps to sort the brands list on the basis of uid list.","in":"query","name":"brand_id","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id)
        query_string = await create_query_string(department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id)

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
    
    async def getCategories(self, department=None, request_headers:Dict={}):
        """List all the categories. You can optionally pass filter the brands by the department. If successful, returns a paginated list of brands specified in `CategoryListingResponse`
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API : type string
        """
        payload = {}
        
        if department is not None:
            payload["department"] = department

        # Parameter validation
        schema = CatalogValidator.getCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","in":"query","name":"department","required":false,"schema":{"enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"],"type":"string"}}],"query":[{"description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","in":"query","name":"department","required":false,"schema":{"enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"],"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", department=department)
        query_string = await create_query_string(department=department)

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
    
    async def getApplicationCategoryListing(self, department_id=None, page_no=None, page_size=None, q=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"A `department_id` is a unique identifier for a particular department.","in":"query","name":"department_id","required":false,"schema":{"type":"integer"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by  brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"A `department_id` is a unique identifier for a particular department.","in":"query","name":"department_id","required":false,"schema":{"type":"integer"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search brands by  brand name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", department_id=department_id, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(department_id=department_id, page_no=page_no, page_size=page_size, q=q)

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
    
    async def updateAppCategory(self, category_uid=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/category/{category_uid}", """{"required":[{"description":"Id of the company associated to category custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"category id for which the custom_json is associated.","in":"path","name":"category_uid","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to category custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"category id for which the custom_json is associated.","in":"path","name":"category_uid","required":true,"schema":{"type":"string"}}]}""", category_uid=category_uid)
        query_string = await create_query_string(category_uid=category_uid)

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
    
    async def getAllCollections(self, q=None, schedule_status=None, type=None, tags=None, is_active=None, page_no=None, page_size=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Get collection list filtered by q string,","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Get collection list filtered by scheduled status,","in":"query","name":"schedule_status","required":false,"schema":{"enum":["live","upcoming","expired"],"type":"string"}},{"description":"type of the collections","in":"query","name":"type","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"get collections filtered by active status.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"query":[{"description":"Get collection list filtered by q string,","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Get collection list filtered by scheduled status,","in":"query","name":"schedule_status","required":false,"schema":{"enum":["live","upcoming","expired"],"type":"string"}},{"description":"type of the collections","in":"query","name":"type","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"get collections filtered by active status.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", q=q, schedule_status=schedule_status, type=type, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionListingResponse
            schema = GetCollectionListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllCollections")
                print(e)

        return response
    
    async def createCollection(self, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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
    
    async def getQueryFilters(self, request_headers:Dict={}):
        """Get query filters to configure a collection
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getQueryFilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionQueryOptionResponse
            schema = GetCollectionQueryOptionResponse()
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateCollection
            schema = UpdateCollection()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCollection")
                print(e)

        return response
    
    async def getCollectionItems(self, id=None, sort_on=None, page_id=None, page_size=None, request_headers:Dict={}):
        """Get items from a collection specified by its `id`.
        :param id : A `id` is a unique identifier of a collection. : type string
        :param sort_on : Each response will contain sort_on param, which should be sent back to make pagination work. : type string
        :param page_id : Each response will contain next_id param, which should be sent back to make pagination work. : type string
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
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

        # Parameter validation
        schema = CatalogValidator.getCollectionItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Each response will contain sort_on param, which should be sent back to make pagination work.","in":"query","name":"sort_on","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"query":[{"description":"Each response will contain sort_on param, which should be sent back to make pagination work.","in":"query","name":"sort_on","required":false,"schema":{"type":"string"}},{"description":"Each response will contain next_id param, which should be sent back to make pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id, sort_on=sort_on, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(id=id, sort_on=sort_on, page_id=page_id, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", id=id, sort_on=sort_on, page_id=page_id, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionItemsResponse
            schema = GetCollectionItemsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCollectionItems")
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
        from .models import CollectionItemUpdate
        schema = CollectionItemUpdate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier of a collection.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)

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
    
    async def getCollectionDetail(self, slug=None, request_headers:Dict={}):
        """Get the details of a collection by its `slug`. If successful, returns a Collection resource in the response body specified in `CollectionDetailResponse`
        :param slug : A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getCollectionDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{slug}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}]}""", slug=slug)
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
    
    async def getApplicationDepartmentListing(self, page_no=None, page_size=None, q=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search department by name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search query with brand name.Use this parameter to search department by name.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)

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
    
    async def updateAppDepartment(self, department_uid=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/department/{department_uid}", """{"required":[{"description":"Id of the company associated to department custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"department id for which the custom_json is associated.","in":"path","name":"department_uid","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to department custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"department id for which the custom_json is associated.","in":"path","name":"department_uid","required":true,"schema":{"type":"string"}}]}""", department_uid=department_uid)
        query_string = await create_query_string(department_uid=department_uid)

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
    
    async def getDepartments(self, request_headers:Dict={}):
        """Departments are a way to categorise similar products. A product can lie in multiple departments. For example, a skirt can below to the 'Women's Fashion' Department while a handbag can lie in 'Women's Accessories' Department. Use this API to list all the departments. If successful, returns the list of departments specified in `DepartmentResponse`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getDepartments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/departments", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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
    
    async def getAppInventory(self, item_ids=None, store_ids=None, brand_ids=None, seller_identifiers=None, timestamp=None, page_size=None, page_id=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/inventory/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The Item Id of the product.","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Store Id of products to fetch inventory.","in":"query","name":"store_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Brand Id of products to fetch inventory.","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Unique seller_identifier of the product.","in":"query","name":"seller_identifiers","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Timestamp in UTC format (2020-07-23T10:27:50Z)","in":"query","name":"timestamp","required":false,"schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Page ID to retrieve next set of results.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}}],"query":[{"description":"The Item Id of the product.","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Store Id of products to fetch inventory.","in":"query","name":"store_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Brand Id of products to fetch inventory.","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Unique seller_identifier of the product.","in":"query","name":"seller_identifiers","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Timestamp in UTC format (2020-07-23T10:27:50Z)","in":"query","name":"timestamp","required":false,"schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Page ID to retrieve next set of results.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", item_ids=item_ids, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, timestamp=timestamp, page_size=page_size, page_id=page_id)
        query_string = await create_query_string(item_ids=item_ids, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, timestamp=timestamp, page_size=page_size, page_id=page_id)

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
    
    async def getAppLocations(self, store_type=None, uid=None, q=None, stage=None, page_no=None, page_size=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/locations", """{"required":[{"description":"Id of the company whose locations are to fetched","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the application whose locations are to fetched","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Helps to sort the location list on the basis of location type.","in":"query","name":"store_type","required":false,"schema":{"type":"string"}},{"description":"Helps to sort the location list on the basis of uid list.","in":"query","name":"uid","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Query that is to be searched.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"to filter companies on basis of verified or unverified companies.","in":"query","name":"stage","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 20.","in":"query","name":"page_size","required":false,"schema":{"default":20,"type":"integer"}}],"query":[{"description":"Helps to sort the location list on the basis of location type.","in":"query","name":"store_type","required":false,"schema":{"type":"string"}},{"description":"Helps to sort the location list on the basis of uid list.","in":"query","name":"uid","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Query that is to be searched.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"to filter companies on basis of verified or unverified companies.","in":"query","name":"stage","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 20.","in":"query","name":"page_size","required":false,"schema":{"default":20,"type":"integer"}}],"headers":[],"path":[{"description":"Id of the company whose locations are to fetched","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the application whose locations are to fetched","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size)

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
    
    async def getConfigurations(self, request_headers:Dict={}):
        """configured details for catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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
    
    async def getCatalogConfiguration(self, request_headers:Dict={}):
        """configuration meta  details for catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getCatalogConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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
    
    async def getConfigurationByType(self, type=None, request_headers:Dict={}):
        """configured details for catalog.
        :param type : type can be brands, categories etc. : type string
        """
        payload = {}
        
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = CatalogValidator.getConfigurationByType()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}]}""", type=type)
        query_string = await create_query_string(type=type)

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"type can be brands, categories etc.","in":"path","name":"type","required":true,"schema":{"type":"string"}}]}""", type=type)
        query_string = await create_query_string(type=type)

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
    
    async def getAppProduct(self, item_id=None, request_headers:Dict={}):
        """Products are the core resource of an application. If successful, returns a Company Application Product resource in the response body depending upon filter sent.
        :param item_id : product id for a particular product. : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id

        # Parameter validation
        schema = CatalogValidator.getAppProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"product id for a particular product.","in":"path","name":"item_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"product id for a particular product.","in":"path","name":"item_id","required":true,"schema":{"type":"string"}}]}""", item_id=item_id)
        query_string = await create_query_string(item_id=item_id)

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
    
    async def updateAppProduct(self, item_id=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", """{"required":[{"description":"Id of the company associated to custom meta.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id for which the custom_meta is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"product id for which the custom_meta is associated.","in":"path","name":"item_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to custom meta.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id for which the custom_meta is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"product id for which the custom_meta is associated.","in":"path","name":"item_id","required":true,"schema":{"type":"string"}}]}""", item_id=item_id)
        query_string = await create_query_string(item_id=item_id)

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
    
    async def getAppicationProducts(self, q=None, f=None, c=None, filters=None, is_dependent=None, sort_on=None, page_id=None, page_size=None, page_no=None, page_type=None, item_ids=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The search query. This can be a partial or complete name of a either a product, brand or category","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","in":"query","name":"f","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","in":"query","name":"c","required":false,"schema":{"type":"string"}},{"description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","in":"query","name":"filters","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"This query parameter is used to get the dependent products in the listing.","in":"query","name":"is_dependent","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","in":"query","name":"sort_on","required":false,"schema":{"enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"],"type":"string"}},{"description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"If page_type is number then pass it to fetch page items. Default is 1.","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"For pagination type should be cursor or number. Default is cursor.","in":"query","name":"page_type","required":false,"schema":{"default":"cursor","type":"string"}},{"description":"Item Ids of product","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"query":[{"description":"The search query. This can be a partial or complete name of a either a product, brand or category","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","in":"query","name":"f","required":false,"schema":{"type":"string"}},{"description":"The search filter parameters for collection items. All the parameter filtered from filter parameters will be passed in **c** parameter in this format. **?c=brand:in:voi-jeans|and:::category:nin:t-shirts|shirts**","in":"query","name":"c","required":false,"schema":{"type":"string"}},{"description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","in":"query","name":"filters","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"This query parameter is used to get the dependent products in the listing.","in":"query","name":"is_dependent","required":false,"schema":{"default":true,"type":"boolean"}},{"description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","in":"query","name":"sort_on","required":false,"schema":{"enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"],"type":"string"}},{"description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"If page_type is number then pass it to fetch page items. Default is 1.","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"For pagination type should be cursor or number. Default is cursor.","in":"query","name":"page_type","required":false,"schema":{"default":"cursor","type":"string"}},{"description":"Item Ids of product","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", q=q, f=f, c=c, filters=filters, is_dependent=is_dependent, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids)
        query_string = await create_query_string(q=q, f=f, c=c, filters=filters, is_dependent=is_dependent, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids)

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
    
    async def getDiscountedInventoryBySizeIdentifier(self, item_id=None, size_identifier=None, page_no=None, page_size=None, q=None, location_ids=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{item_id}/inventory/{size_identifier}", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Uniquer Application ID.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"path","name":"size_identifier","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search with help of store code.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Search by store ids.","in":"query","name":"location_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search with help of store code.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Search by store ids.","in":"query","name":"location_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Uniquer Application ID.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"path","name":"size_identifier","required":true,"schema":{"type":"string"}}]}""", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
        query_string = await create_query_string(item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)

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
    
    async def getProductDetailBySlug(self, slug=None, request_headers:Dict={}):
        """Products are the core resource of an application. Products can be associated by categories, collections, brands and more. This API retrieves the product specified by the given **slug**. If successful, returns a Product resource in the response body specified in `ProductDetail`
        :param slug : The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/** : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getProductDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{slug}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/**","in":"path","name":"slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/**","in":"path","name":"slug","required":true,"schema":{"type":"string"}}]}""", slug=slug)
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
    
    async def getAppProducts(self, brand_ids=None, category_ids=None, department_ids=None, tags=None, item_ids=None, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Products are the core resource of an application. Products can be associated by categories, collections, brands and more. If successful, returns a Product resource in the response body specified in `ApplicationProductListingResponseDatabasePowered`
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Get multiple products filtered by Brand Ids","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Category Ids","in":"query","name":"category_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Department Ids","in":"query","name":"department_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by tags","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get multiple products filtered by Item Ids","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"Search with Item Code, Name, Slug or Identifier.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"query":[{"description":"Get multiple products filtered by Brand Ids","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Category Ids","in":"query","name":"category_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Department Ids","in":"query","name":"department_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by tags","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get multiple products filtered by Item Ids","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"Search with Item Code, Name, Slug or Identifier.","in":"query","name":"q","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, item_ids=item_ids, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, item_ids=item_ids, page_no=page_no, page_size=page_size, q=q)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products/", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, item_ids=item_ids, page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse
            schema = SuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAppCategoryReturnConfiguration")
                print(e)

        return response
    
    async def getAppCategoryReturnConfig(self, request_headers:Dict={}):
        """Get all category level configuration level set for an application.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAppCategoryReturnConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/return-config/categories", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse
            schema = SuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCategoryReturnConfiguration")
                print(e)

        return response
    
    async def getAutocompleteConfig(self, request_headers:Dict={}):
        """Custom Autocomplete Keyword allows you to map conditions with keywords to give you the ultimate results
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAutocompleteConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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
    
    async def createCustomAutocompleteRule(self, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAutocompleteWordsResponse
            schema = CreateAutocompleteWordsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomAutocompleteRule")
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)

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
    
    async def getAutocompleteKeywordDetail(self, id=None, request_headers:Dict={}):
        """Get the details of a words by its `id`. If successful, returns a keywords resource in the response body specified in `GetAutocompleteWordsResponseSchema`
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getAutocompleteKeywordDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAutocompleteWordsResponse
            schema = GetAutocompleteWordsResponse()
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAutocompleteWordsResponse
            schema = GetAutocompleteWordsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAutocompleteKeyword")
                print(e)

        return response
    
    async def deleteSearchConfiguration(self, request_headers:Dict={}):
        """This view allows you to reset search config for an application
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.deleteSearchConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteSearchConfigurationResponse
            schema = DeleteSearchConfigurationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSearchConfiguration")
                print(e)

        return response
    
    async def getSearchConfiguration(self, request_headers:Dict={}):
        """This view allows you to add/modify searchable attributes for an application
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getSearchConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchConfigurationResponse
            schema = GetSearchConfigurationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSearchConfiguration")
                print(e)

        return response
    
    async def createSearchConfiguration(self, body="", request_headers:Dict={}):
        """This view allows you to modify searchable attributes for an application
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createSearchConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSearchConfigurationRequest
        schema = CreateSearchConfigurationRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateSearchConfigurationResponse
            schema = CreateSearchConfigurationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSearchConfiguration")
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/configuration/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateSearchConfigurationResponse
            schema = UpdateSearchConfigurationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSearchConfiguration")
                print(e)

        return response
    
    async def getAllSearchKeyword(self, request_headers:Dict={}):
        """Custom Search Keyword allows you to map conditions with keywords to give you the ultimate results
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAllSearchKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsResponse
            schema = GetSearchWordsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllSearchKeyword")
                print(e)

        return response
    
    async def createCustomKeyword(self, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)

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
    
    async def getSearchKeywords(self, id=None, request_headers:Dict={}):
        """Get the details of a words by its `id`. If successful, returns a Collection resource in the response body specified in `GetSearchWordsDetailResponseSchema`
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSearchWordsDetailResponse
            schema = GetSearchWordsDetailResponse()
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)

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
    
    async def updateAppLocation(self, store_uid=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store/{store_uid}", """{"required":[{"description":"Id of the company associated to location custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"store id for which the custom_json is associated.","in":"path","name":"store_uid","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to location custom json.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id for which the custom_json is associated.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"store id for which the custom_json is associated.","in":"path","name":"store_uid","required":true,"schema":{"type":"string"}}]}""", store_uid=store_uid)
        query_string = await create_query_string(store_uid=store_uid)

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
    
    async def updateAllowSingle(self, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/filter/allow_single", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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
    
    async def updateDefaultSort(self, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/sort/default_key", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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
    
    async def getListingConfigurations(self, config_type=None, page_no=None, page_size=None, search=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}}]}""", config_type=config_type, page_no=page_no, page_size=page_size, search=search)
        query_string = await create_query_string(config_type=config_type, page_no=page_no, page_size=page_size, search=search)

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
    
    async def createListingConfiguration(self, config_type=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}}]}""", config_type=config_type)
        query_string = await create_query_string(config_type=config_type)

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
    
    async def getGroupConfigurations(self, config_type=None, page_no=None, page_size=None, search=None, template_slug=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Get configuration list filtered by `search` string.","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}]}""", config_type=config_type, page_no=page_no, page_size=page_size, search=search, template_slug=template_slug)
        query_string = await create_query_string(config_type=config_type, page_no=page_no, page_size=page_size, search=search, template_slug=template_slug)

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
    
    async def createGroupConfiguration(self, config_type=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}}]}""", config_type=config_type)
        query_string = await create_query_string(config_type=config_type)

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}]}""", config_type=config_type, group_slug=group_slug)
        query_string = await create_query_string(config_type=config_type, group_slug=group_slug)

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
    
    async def updateGroupConfiguration(self, config_type=None, group_slug=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/groups/{group_slug}", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular group configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["comparisons_groups","details_groups","seller_groups"],"type":"string"}},{"description":"A `group_slug` is a unique identifier of a particular configuration.","in":"path","name":"group_slug","required":true,"schema":{"type":"string"}}]}""", config_type=config_type, group_slug=group_slug)
        query_string = await create_query_string(config_type=config_type, group_slug=group_slug)

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
    
    async def deleteListingConfiguration(self, config_type=None, config_id=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}]}""", config_type=config_type, config_id=config_id)
        query_string = await create_query_string(config_type=config_type, config_id=config_id)

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
    
    async def updateListingConfiguration(self, config_type=None, config_id=None, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/item/{config_id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is a unique identifier for a particular listing configuration type.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","brands","categories","variant","similar"],"type":"string"}},{"description":"A `config_id` is a unique identifier of a particular configuration.","in":"path","name":"config_id","required":true,"schema":{"type":"string"}}]}""", config_type=config_type, config_id=config_id)
        query_string = await create_query_string(config_type=config_type, config_id=config_id)

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
    
    async def getConfigurationMetadata(self, config_type=None, template_slug=None, request_headers:Dict={}):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{config_type}/metadata/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","details_groups","comparisons_groups","variant","similar","brands","categories","seller_groups"],"type":"string"}}],"optional":[{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}}],"query":[{"description":"Get configuration list filtered by `template_slug` string. This is for the details and comparision groups.","in":"query","name":"template_slug","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `application_id` is a unique identifier for a particular sale channel.","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"A `config_type` is an identifier that defines a specific type of configuration.","in":"path","name":"config_type","required":true,"schema":{"enum":["filter","sort","details_groups","comparisons_groups","variant","similar","brands","categories","seller_groups"],"type":"string"}}]}""", config_type=config_type, template_slug=template_slug)
        query_string = await create_query_string(config_type=config_type, template_slug=template_slug)

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
    