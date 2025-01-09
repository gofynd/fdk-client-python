"""Catalog Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import CatalogValidator

class Catalog:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def listCategories(self, level=None, department=None, q=None, page_no=None, page_size=None, uids=None, slug=None, request_headers:Dict={}):
        """Retrieve a list of categories data associated to a specific company and queries passed in the request.
        :param level : Get category for multiple levels : type string
        :param department : Get category for multiple departments filtered : type integer
        :param q : Get multiple categories filtered by search string : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param uids : Get multiple categories filtered by category uids. : type array
        :param slug : Get category by slug : type string
        """
        payload = {}
        
        if level is not None:
            payload["level"] = level
        if department is not None:
            payload["department"] = department
        if q is not None:
            payload["q"] = q
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if uids is not None:
            payload["uids"] = uids
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.listCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"Get category for multiple levels","in":"query","name":"level","required":false,"schema":{"type":"string"}},{"description":"Get category for multiple departments filtered","in":"query","name":"department","required":false,"schema":{"type":"integer"}},{"description":"Get multiple categories filtered by search string","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Get multiple categories filtered by category uids.","in":"query","name":"uids","schema":{"type":"array","items":{"type":"integer"},"maxItems":100},"required":false},{"in":"query","name":"slug","description":"Get category by slug","schema":{"type":"string"},"required":false}],"query":[{"description":"Get category for multiple levels","in":"query","name":"level","required":false,"schema":{"type":"string"}},{"description":"Get category for multiple departments filtered","in":"query","name":"department","required":false,"schema":{"type":"integer"}},{"description":"Get multiple categories filtered by search string","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Get multiple categories filtered by category uids.","in":"query","name":"uids","schema":{"type":"array","items":{"type":"integer"},"maxItems":100},"required":false},{"in":"query","name":"slug","description":"Get category by slug","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", level=level, department=department, q=q, page_no=page_no, page_size=page_size, uids=uids, slug=slug)
        query_string = await create_query_string(level=level, department=department, q=q, page_no=page_no, page_size=page_size, uids=uids, slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/", level=level, department=department, q=q, page_no=page_no, page_size=page_size, uids=uids, slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CategoryResponseSchema
            schema = CategoryResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for listCategories")
                print(e)

        return response
    
    async def getCategoryData(self, uid=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific category by its uid for a specific company.
        :param uid : Category unique id : type string
        """
        payload = {}
        
        if uid is not None:
            payload["uid"] = uid

        # Parameter validation
        schema = CatalogValidator.getCategoryData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/{uid}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Category unique id","in":"path","name":"uid","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Category unique id","in":"path","name":"uid","required":true,"schema":{"type":"string"}}]}""", serverType="platform", uid=uid)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/{uid}/", uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SingleCategoryResponseSchema
            schema = SingleCategoryResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCategoryData")
                print(e)

        return response
    
    async def getSellerInsights(self, seller_app_id=None, request_headers:Dict={}):
        """Retrieve the count of catalog related data for sellers.
        :param seller_app_id : Id of the seller application which is serving the invetory/catalog of the company : type string
        """
        payload = {}
        
        if seller_app_id is not None:
            payload["seller_app_id"] = seller_app_id

        # Parameter validation
        schema = CatalogValidator.getSellerInsights()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/cross-selling/{seller_app_id}/analytics/insights/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the seller application which is serving the invetory/catalog of the company","in":"path","name":"seller_app_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the seller application which is serving the invetory/catalog of the company","in":"path","name":"seller_app_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", seller_app_id=seller_app_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/cross-selling/{seller_app_id}/analytics/insights/", seller_app_id=seller_app_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CrossSellingResponseSchema
            schema = CrossSellingResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSellerInsights")
                print(e)

        return response
    
    async def listDepartmentsData(self, page_no=None, item_type=None, page_size=None, name=None, search=None, is_active=None, slug=None, request_headers:Dict={}):
        """Allows you to list all departments data for a specific company.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param item_type : A `item_type` is a type of product eg. set, standard, digital : type string
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param name : Can search departments by passing name. : type string
        :param search : Can search departments by passing name of the department in search parameter. : type string
        :param is_active : Can query for departments based on whether they are active or inactive. : type boolean
        :param slug : Can filter by slug : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if item_type is not None:
            payload["item_type"] = item_type
        if page_size is not None:
            payload["page_size"] = page_size
        if name is not None:
            payload["name"] = name
        if search is not None:
            payload["search"] = search
        if is_active is not None:
            payload["is_active"] = is_active
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.listDepartmentsData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"A `item_type` is a type of product eg. set, standard, digital","in":"query","name":"item_type","required":false,"schema":{"type":"string","enum":["standard","set","digital"]}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Can search departments by passing name.","in":"query","name":"name","required":false,"schema":{"type":"string"}},{"description":"Can search departments by passing name of the department in search parameter.","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"Can query for departments based on whether they are active or inactive.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"slug","description":"Can filter by slug","schema":{"type":"string"},"required":false}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"A `item_type` is a type of product eg. set, standard, digital","in":"query","name":"item_type","required":false,"schema":{"type":"string","enum":["standard","set","digital"]}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"Can search departments by passing name.","in":"query","name":"name","required":false,"schema":{"type":"string"}},{"description":"Can search departments by passing name of the department in search parameter.","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"Can query for departments based on whether they are active or inactive.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"slug","description":"Can filter by slug","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, item_type=item_type, page_size=page_size, name=name, search=search, is_active=is_active, slug=slug)
        query_string = await create_query_string(page_no=page_no, item_type=item_type, page_size=page_size, name=name, search=search, is_active=is_active, slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/", page_no=page_no, item_type=item_type, page_size=page_size, name=name, search=search, is_active=is_active, slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DepartmentsResponseSchema
            schema = DepartmentsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for listDepartmentsData")
                print(e)

        return response
    
    async def getDepartmentData(self, uid=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific department for a specific company by uid.
        :param uid : A `uid` is a unique identifier of a department. : type string
        """
        payload = {}
        
        if uid is not None:
            payload["uid"] = uid

        # Parameter validation
        schema = CatalogValidator.getDepartmentData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/{uid}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `uid` is a unique identifier of a department.","in":"path","name":"uid","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `uid` is a unique identifier of a department.","in":"path","name":"uid","required":true,"schema":{"type":"string"}}]}""", serverType="platform", uid=uid)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/{uid}/", uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DepartmentsResponseSchema
            schema = DepartmentsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDepartmentData")
                print(e)

        return response
    
    async def listTemplateBrandTypeValues(self, filter=None, template_tag=None, item_type=None, request_headers:Dict={}):
        """Retrieve values related to template brand types for a specific company. The filter type query parameter defines what type of data to return. 
        :param filter : A `filter` is the unique identifier of the type of value required. : type string
        :param template_tag : A `template_tag` is the identifier of the type of template required. : type string
        :param item_type : A `item_type` is the identifier of the type of template required. : type string
        """
        payload = {}
        
        if filter is not None:
            payload["filter"] = filter
        if template_tag is not None:
            payload["template_tag"] = template_tag
        if item_type is not None:
            payload["item_type"] = item_type

        # Parameter validation
        schema = CatalogValidator.listTemplateBrandTypeValues()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/downloads/configuration/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `filter` is the unique identifier of the type of value required.","in":"query","name":"filter","required":true,"schema":{"type":"string"}}],"optional":[{"description":"A `template_tag` is the identifier of the type of template required.","in":"query","name":"template_tag","required":false,"schema":{"type":"string"}},{"description":"A `item_type` is the identifier of the type of template required.","in":"query","name":"item_type","required":false,"schema":{"type":"string","enum":["set","standard","composite","digital"]}}],"query":[{"description":"A `filter` is the unique identifier of the type of value required.","in":"query","name":"filter","required":true,"schema":{"type":"string"}},{"description":"A `template_tag` is the identifier of the type of template required.","in":"query","name":"template_tag","required":false,"schema":{"type":"string"}},{"description":"A `item_type` is the identifier of the type of template required.","in":"query","name":"item_type","required":false,"schema":{"type":"string","enum":["set","standard","composite","digital"]}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", filter=filter, template_tag=template_tag, item_type=item_type)
        query_string = await create_query_string(filter=filter, template_tag=template_tag, item_type=item_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/downloads/configuration/", filter=filter, template_tag=template_tag, item_type=item_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductConfigurationDownloads
            schema = ProductConfigurationDownloads()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for listTemplateBrandTypeValues")
                print(e)

        return response
    
    async def bulkHsnCode(self, body="", request_headers:Dict={}):
        """Execute bulk updates for HSN codes across multiple products.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.bulkHsnCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkHsnUpsert
        schema = BulkHsnUpsert()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/bulk/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/bulk/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkHsnResponseSchema
            schema = BulkHsnResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkHsnCode")
                print(e)

        return response
    
    async def getHsnCode(self, id=None, request_headers:Dict={}):
        """Retrieve the HSN code for a product.
        :param id : Unique id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getHsnCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Unique id","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Unique id","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import HsnCode
            schema = HsnCode()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getHsnCode")
                print(e)

        return response
    
    async def updateHsnCode(self, id=None, body="", request_headers:Dict={}):
        """Modify the HSN code associated with a product.
        :param id : Unique id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.updateHsnCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import HsnUpsert
        schema = HsnUpsert()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Unique id","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Unique id","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import HsnCode
            schema = HsnCode()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateHsnCode")
                print(e)

        return response
    
    async def getInventories(self, item_id=None, size=None, page_no=None, page_size=None, page_id=None, page_type=None, q=None, sellable=None, store_ids=None, brand_ids=None, seller_identifiers=None, qty_gt=None, qty_lt=None, qty_type=None, from_date=None, to_date=None, size_identifier=None, request_headers:Dict={}):
        """Allows to get Inventories data for particular company. 
        :param item_id : Item code of the product of which size is to be get. : type string
        :param size : Size of which inventory is to get. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param page_id : Alphanumeric Page ID to retrieve next set of results. : type string
        :param page_type : Available pagination types are cursor or number. : type string
        :param q : Search with help of store code. : type string
        :param sellable : Filter on whether product is in stock or not. : type boolean
        :param store_ids : The Store Id of products to fetch inventory. : type array
        :param brand_ids : The Brand Id of products to fetch inventory. : type array
        :param seller_identifiers : The Seller Identifier or Primary Identifier of the inventory. : type array
        :param qty_gt : This field allows you to filter for inventories that have quantity greater than to the specified value based on qty_type filter. : type integer
        :param qty_lt : This field allows you to filter for inventories that have a quantity less than to the specified value based on qty_type filter. : type integer
        :param qty_type : This field provides flexibility in selecting filter for inventory quantity counts and date queries. For example, you might use this field to specify "total" or "sellable" quantity. : type string
        :param from_date : Inventory updated on filter to get inventories greater then or equal to provided date based on qty_type value. : type string
        :param to_date : Inventory updated on filter to get inventories less then or equal to provided date based on qty_type value. : type string
        :param size_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        if size is not None:
            payload["size"] = size
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if page_id is not None:
            payload["page_id"] = page_id
        if page_type is not None:
            payload["page_type"] = page_type
        if q is not None:
            payload["q"] = q
        if sellable is not None:
            payload["sellable"] = sellable
        if store_ids is not None:
            payload["store_ids"] = store_ids
        if brand_ids is not None:
            payload["brand_ids"] = brand_ids
        if seller_identifiers is not None:
            payload["seller_identifiers"] = seller_identifiers
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
        if size_identifier is not None:
            payload["size_identifier"] = size_identifier

        # Parameter validation
        schema = CatalogValidator.getInventories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventories", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Item code of the product of which size is to be get.","in":"query","name":"item_id","required":false,"schema":{"type":"string"}},{"description":"Size of which inventory is to get.","in":"query","name":"size","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Alphanumeric Page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"},"required":false},{"description":"Available pagination types are cursor or number.","in":"query","name":"page_type","schema":{"type":"string","default":"number","enum":["cursor","number"]},"required":false},{"description":"Search with help of store code.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Filter on whether product is in stock or not.","in":"query","name":"sellable","required":false,"schema":{"default":false,"type":"boolean"}},{"description":"The Store Id of products to fetch inventory.","in":"query","name":"store_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Brand Id of products to fetch inventory.","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Seller Identifier or Primary Identifier of the inventory.","in":"query","name":"seller_identifiers","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"This field allows you to filter for inventories that have quantity greater than to the specified value based on qty_type filter.","in":"query","name":"qty_gt","required":false,"schema":{"type":"integer"}},{"description":"This field allows you to filter for inventories that have a quantity less than to the specified value based on qty_type filter.","in":"query","name":"qty_lt","required":false,"schema":{"type":"integer"}},{"description":"This field provides flexibility in selecting filter for inventory quantity counts and date queries. For example, you might use this field to specify \"total\" or \"sellable\" quantity.","in":"query","name":"qty_type","required":false,"schema":{"enum":["total","sellable"],"type":"string"}},{"description":"Inventory updated on filter to get inventories greater then or equal to provided date based on qty_type value.","in":"query","name":"from_date","required":false,"schema":{"format":"date-time","type":"string"}},{"description":"Inventory updated on filter to get inventories less then or equal to provided date based on qty_type value.","in":"query","name":"to_date","required":false,"schema":{"format":"date-time","type":"string"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"query","name":"size_identifier","required":false,"schema":{"type":"string"}}],"query":[{"description":"Item code of the product of which size is to be get.","in":"query","name":"item_id","required":false,"schema":{"type":"string"}},{"description":"Size of which inventory is to get.","in":"query","name":"size","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Alphanumeric Page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"},"required":false},{"description":"Available pagination types are cursor or number.","in":"query","name":"page_type","schema":{"type":"string","default":"number","enum":["cursor","number"]},"required":false},{"description":"Search with help of store code.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Filter on whether product is in stock or not.","in":"query","name":"sellable","required":false,"schema":{"default":false,"type":"boolean"}},{"description":"The Store Id of products to fetch inventory.","in":"query","name":"store_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Brand Id of products to fetch inventory.","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"The Seller Identifier or Primary Identifier of the inventory.","in":"query","name":"seller_identifiers","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"This field allows you to filter for inventories that have quantity greater than to the specified value based on qty_type filter.","in":"query","name":"qty_gt","required":false,"schema":{"type":"integer"}},{"description":"This field allows you to filter for inventories that have a quantity less than to the specified value based on qty_type filter.","in":"query","name":"qty_lt","required":false,"schema":{"type":"integer"}},{"description":"This field provides flexibility in selecting filter for inventory quantity counts and date queries. For example, you might use this field to specify \"total\" or \"sellable\" quantity.","in":"query","name":"qty_type","required":false,"schema":{"enum":["total","sellable"],"type":"string"}},{"description":"Inventory updated on filter to get inventories greater then or equal to provided date based on qty_type value.","in":"query","name":"from_date","required":false,"schema":{"format":"date-time","type":"string"}},{"description":"Inventory updated on filter to get inventories less then or equal to provided date based on qty_type value.","in":"query","name":"to_date","required":false,"schema":{"format":"date-time","type":"string"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"query","name":"size_identifier","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_id=item_id, size=size, page_no=page_no, page_size=page_size, page_id=page_id, page_type=page_type, q=q, sellable=sellable, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, qty_gt=qty_gt, qty_lt=qty_lt, qty_type=qty_type, from_date=from_date, to_date=to_date, size_identifier=size_identifier)
        query_string = await create_query_string(item_id=item_id, size=size, page_no=page_no, page_size=page_size, page_id=page_id, page_type=page_type, q=q, sellable=sellable, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, qty_gt=qty_gt, qty_lt=qty_lt, qty_type=qty_type, from_date=from_date, to_date=to_date, size_identifier=size_identifier)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventories", item_id=item_id, size=size, page_no=page_no, page_size=page_size, page_id=page_id, page_type=page_type, q=q, sellable=sellable, store_ids=store_ids, brand_ids=brand_ids, seller_identifiers=seller_identifiers, qty_gt=qty_gt, qty_lt=qty_lt, qty_type=qty_type, from_date=from_date, to_date=to_date, size_identifier=size_identifier), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetInventoriesResponseSchema
            schema = GetInventoriesResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInventories")
                print(e)

        return response
    
    async def getInventoryBulkUploadHistory(self, page_no=None, page_size=None, search=None, request_headers:Dict={}):
        """Helps to get bulk Inventory upload jobs status.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param search : Search string to filter the results by batch id : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if search is not None:
            payload["search"] = search

        # Parameter validation
        schema = CatalogValidator.getInventoryBulkUploadHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", """{"required":[{"description":"Company Id of of which Inventory Bulk Upload History to be obtained.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search string to filter the results by batch id","in":"query","name":"search","required":false,"schema":{"type":"string"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search string to filter the results by batch id","in":"query","name":"search","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"Company Id of of which Inventory Bulk Upload History to be obtained.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, search=search)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", page_no=page_no, page_size=page_size, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkInventoryGet
            schema = BulkInventoryGet()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInventoryBulkUploadHistory")
                print(e)

        return response
    
    async def createBulkInventoryJob(self, body="", request_headers:Dict={}):
        """Helps to create a bulk Inventory upload job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createBulkInventoryJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkJob
        schema = BulkJob()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", """{"required":[{"description":"Company Id in which Inventory to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id in which Inventory to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkResponseSchema
            schema = BulkResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createBulkInventoryJob")
                print(e)

        return response
    
    async def deleteBulkInventoryJob(self, batch_id=None, request_headers:Dict={}):
        """Allows to delete bulk Inventory job associated with company.
        :param batch_id : Batch Id of the bulk delete job. : type string
        """
        payload = {}
        
        if batch_id is not None:
            payload["batch_id"] = batch_id

        # Parameter validation
        schema = CatalogValidator.deleteBulkInventoryJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", """{"required":[{"description":"Company Id of the company of which bulk Inventory job is to be deleted.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Batch Id of the bulk delete job.","in":"path","name":"batch_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id of the company of which bulk Inventory job is to be deleted.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Batch Id of the bulk delete job.","in":"path","name":"batch_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", batch_id=batch_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteBulkInventoryJob")
                print(e)

        return response
    
    async def createBulkInventory(self, batch_id=None, body="", request_headers:Dict={}):
        """Helps to create products in bulk push to kafka for approval/creation.
        :param batch_id : Batch Id of the bulk create job. : type string
        """
        payload = {}
        
        if batch_id is not None:
            payload["batch_id"] = batch_id

        # Parameter validation
        schema = CatalogValidator.createBulkInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryBulkRequestSchema
        schema = InventoryBulkRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", """{"required":[{"description":"Company Id in which Inventory is to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Batch Id of the bulk create job.","in":"path","name":"batch_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id in which Inventory is to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Batch Id of the bulk create job.","in":"path","name":"batch_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", batch_id=batch_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", batch_id=batch_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createBulkInventory")
                print(e)

        return response
    
    async def getInventoryExport(self, request_headers:Dict={}):
        """Retrieves inventory for all products for that particular company
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getInventoryExport()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", """{"required":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryExportJob
            schema = InventoryExportJob()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInventoryExport")
                print(e)

        return response
    
    async def createInventoryExportJob(self, body="", request_headers:Dict={}):
        """Helps to create a Inventory export job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createInventoryExportJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryExportRequestSchema
        schema = InventoryExportRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", """{"required":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryExportResponseSchema
            schema = InventoryExportResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createInventoryExportJob")
                print(e)

        return response
    
    async def exportInventoryConfig(self, filter_type=None, request_headers:Dict={}):
        """Retrieve List of different filters like brand, store, and type for inventory export.
        :param filter_type : filter type from any one of ['brand', 'store', 'type'] : type string
        """
        payload = {}
        
        if filter_type is not None:
            payload["filter_type"] = filter_type

        # Parameter validation
        schema = CatalogValidator.exportInventoryConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/configuration/", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"filter type from any one of ['brand', 'store', 'type']","in":"query","name":"filter_type","required":false,"schema":{"type":"string","enum":["brand","store","type"]}}],"query":[{"description":"filter type from any one of ['brand', 'store', 'type']","in":"query","name":"filter_type","required":false,"schema":{"type":"string","enum":["brand","store","type"]}}],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", filter_type=filter_type)
        query_string = await create_query_string(filter_type=filter_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/configuration/", filter_type=filter_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryConfig
            schema = InventoryConfig()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for exportInventoryConfig")
                print(e)

        return response
    
    async def downloadInventoryTemplateView(self, item_type=None, request_headers:Dict={}):
        """Allows you to download inventory product template data for a specific company in formats like csv and excel.
        :param item_type : An `item_type` defines the type of item. : type string
        """
        payload = {}
        
        if item_type is not None:
            payload["item_type"] = item_type

        # Parameter validation
        schema = CatalogValidator.downloadInventoryTemplateView()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/download/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"An `item_type` defines the type of item.","in":"query","name":"item_type","required":true,"schema":{"type":"string","enum":["set","standard","composite","digital"]}}],"optional":[],"query":[{"description":"An `item_type` defines the type of item.","in":"query","name":"item_type","required":true,"schema":{"type":"string","enum":["set","standard","composite","digital"]}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_type=item_type)
        query_string = await create_query_string(item_type=item_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/download/", item_type=item_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def validateProductTemplateSchema(self, item_type=None, request_headers:Dict={}):
        """Allows you to list all product templates validation values for all the fields present in the database for a specific company.
        :param item_type : An `item_type` defines the type of item. The default value is standard. : type string
        """
        payload = {}
        
        if item_type is not None:
            payload["item_type"] = item_type

        # Parameter validation
        schema = CatalogValidator.validateProductTemplateSchema()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/validation/schema/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"An `item_type` defines the type of item. The default value is standard.","in":"query","name":"item_type","required":true,"schema":{"type":"string","enum":["set","standard","composite","digital"]}}],"optional":[],"query":[{"description":"An `item_type` defines the type of item. The default value is standard.","in":"query","name":"item_type","required":true,"schema":{"type":"string","enum":["set","standard","composite","digital"]}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_type=item_type)
        query_string = await create_query_string(item_type=item_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/validation/schema/", item_type=item_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryValidationResponseSchema
            schema = InventoryValidationResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateProductTemplateSchema")
                print(e)

        return response
    
    async def getOptimalLocations(self, body="", request_headers:Dict={}):
        """This API returns the optimal locations where inventory is available for the given articles.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getOptimalLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AssignStore
        schema = AssignStore()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/location/reassign/", """{"required":[{"description":"Id of the company inside which the location is to be created.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company inside which the location is to be created.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/location/reassign/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreAssignResponseSchema
            schema = StoreAssignResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOptimalLocations")
                print(e)

        return response
    
    async def getMarketplaceOptinDetail(self, request_headers:Dict={}):
        """Allows to fetch opt-in information for a company.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getMarketplaceOptinDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetOptInPlatform
            schema = GetOptInPlatform()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMarketplaceOptinDetail")
                print(e)

        return response
    
    async def getCompanyBrandDetail(self, is_active=None, q=None, page_no=None, page_size=None, marketplace=None, request_headers:Dict={}):
        """Get the details of the Brands associated with the given company_id passed which has opt-in.
        :param is_active : The is_active status for the optin id. : type boolean
        :param q : The search value to filter the list. : type string
        :param page_no : The number of page for the company id. : type integer
        :param page_size : Number of records that can be seen on the page for the company id. : type integer
        :param marketplace : The marketplace platform associated with the company id. : type string
        """
        payload = {}
        
        if is_active is not None:
            payload["is_active"] = is_active
        if q is not None:
            payload["q"] = q
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if marketplace is not None:
            payload["marketplace"] = marketplace

        # Parameter validation
        schema = CatalogValidator.getCompanyBrandDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-brand-details/", """{"required":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"The is_active status for the optin id.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"The search value to filter the list.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The number of page for the company id.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of records that can be seen on the page for the company id.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"The marketplace platform associated with the company id.","in":"query","name":"marketplace","required":false,"schema":{"type":"string"}}],"query":[{"description":"The is_active status for the optin id.","in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"description":"The search value to filter the list.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The number of page for the company id.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of records that can be seen on the page for the company id.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"description":"The marketplace platform associated with the company id.","in":"query","name":"marketplace","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace)
        query_string = await create_query_string(is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-brand-details/", is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OptinCompanyBrandDetailsView
            schema = OptinCompanyBrandDetailsView()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCompanyBrandDetail")
                print(e)

        return response
    
    async def getCompanyDetail(self, request_headers:Dict={}):
        """Get the details of the company associated with the given company_id passed which has opt-in.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getCompanyDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-details/", """{"required":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-details/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OptinCompanyDetail
            schema = OptinCompanyDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCompanyDetail")
                print(e)

        return response
    
    async def getCompanyMetrics(self, request_headers:Dict={}):
        """Allows viewing company metrics, including brand and store status, as well as the number of verified and unverified products, company documents, and store documents.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getCompanyMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-metrics/", """{"required":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-metrics/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OptinCompanyMetrics
            schema = OptinCompanyMetrics()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCompanyMetrics")
                print(e)

        return response
    
    async def getStoreDetail(self, q=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve the details of the selling location (store) associated with a specific company passed.
        :param q : The search related the store for the company id. : type string
        :param page_no : The number of page for the company id. : type integer
        :param page_size : Number of records that can be seen on the page for the company id. : type integer
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getStoreDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/location-details/", """{"required":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"The search related the store for the company id.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The number of page for the company id.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of records that can be seen on the page for the company id.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"query":[{"description":"The search related the store for the company id.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The number of page for the company id.","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of records that can be seen on the page for the company id.","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", q=q, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/location-details/", q=q, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OptinStoreDetails
            schema = OptinStoreDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStoreDetail")
                print(e)

        return response
    
    async def getProductAttributes(self, category=None, filter=None, request_headers:Dict={}):
        """Retrieve attributes attached to products based on their L3 category.
        :param category : It is the name of the l3 cateogry : type string
        :param filter : If true, returns filtered values, else returns all the attributes : type boolean
        """
        payload = {}
        
        if category is not None:
            payload["category"] = category
        if filter is not None:
            payload["filter"] = filter

        # Parameter validation
        schema = CatalogValidator.getProductAttributes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/", """{"required":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"It is the name of the l3 cateogry","in":"query","name":"category","required":true,"schema":{"type":"string"}}],"optional":[{"description":"If true, returns filtered values, else returns all the attributes","in":"query","name":"filter","required":false,"schema":{"type":"boolean"}}],"query":[{"description":"It is the name of the l3 cateogry","in":"query","name":"category","required":true,"schema":{"type":"string"}},{"description":"If true, returns filtered values, else returns all the attributes","in":"query","name":"filter","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", category=category, filter=filter)
        query_string = await create_query_string(category=category, filter=filter)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/", category=category, filter=filter), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductAttributesResponseSchema
            schema = ProductAttributesResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductAttributes")
                print(e)

        return response
    
    async def getAttribute(self, attribute_slug=None, request_headers:Dict={}):
        """Retrieve the attribute detail for catalog listings by attribute slug passed for a specific company.
        :param attribute_slug : Slug of the attribute for which you want to view the details : type string
        """
        payload = {}
        
        if attribute_slug is not None:
            payload["attribute_slug"] = attribute_slug

        # Parameter validation
        schema = CatalogValidator.getAttribute()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/{attribute_slug}", """{"required":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Slug of the attribute for which you want to view the details","in":"path","name":"attribute_slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Slug of the attribute for which you want to view the details","in":"path","name":"attribute_slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", attribute_slug=attribute_slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/{attribute_slug}", attribute_slug=attribute_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AttributeDetail
            schema = AttributeDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAttribute")
                print(e)

        return response
    
    async def getProductBundle(self, q=None, slug=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve a list of product bundles available in the catalog associated to a specific company.
        :param q : A search string that is searched with product bundle name. : type string
        :param slug : slugs of bundles to be retrieved. : type array
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q
        if slug is not None:
            payload["slug"] = slug
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getProductBundle()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"A search string that is searched with product bundle name.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"slugs of bundles to be retrieved.","in":"query","name":"slug","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"query":[{"description":"A search string that is searched with product bundle name.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"slugs of bundles to be retrieved.","in":"query","name":"slug","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", q=q, slug=slug, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(q=q, slug=slug, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", q=q, slug=slug, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetProductBundleListingResponseSchema
            schema = GetProductBundleListingResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductBundle")
                print(e)

        return response
    
    async def createProductBundle(self, body="", request_headers:Dict={}):
        """Create product bundle in the catalog associated to a specific company
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createProductBundle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductBundleRequestSchema
        schema = ProductBundleRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetProductBundleCreateResponseSchema
            schema = GetProductBundleCreateResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createProductBundle")
                print(e)

        return response
    
    async def getProductBundleDetail(self, id=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific product bundle associated to a specific company.
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getProductBundleDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetProductBundleResponseSchema
            schema = GetProductBundleResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductBundleDetail")
                print(e)

        return response
    
    async def updateProductBundle(self, id=None, body="", request_headers:Dict={}):
        """Modify the details of an existing product bundle in the catalog associated to a specific company.
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.updateProductBundle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductBundleUpdateRequestSchema
        schema = ProductBundleUpdateRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetProductBundleCreateResponseSchema
            schema = GetProductBundleCreateResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateProductBundle")
                print(e)

        return response
    
    async def getProductAssetsInBulk(self, page_no=None, page_size=None, request_headers:Dict={}):
        """Helps to retrieve bulk asset jobs data associated to a particular company.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getProductAssetsInBulk()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", """{"required":[{"description":"Company Id of the product size.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"headers":[],"path":[{"description":"Company Id of the product size.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkAssetResponseSchema
            schema = BulkAssetResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductAssetsInBulk")
                print(e)

        return response
    
    async def createProductAssetsInBulk(self, body="", request_headers:Dict={}):
        """Helps to create a bulk asset upload job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createProductAssetsInBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductBulkAssets
        schema = ProductBulkAssets()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", """{"required":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createProductAssetsInBulk")
                print(e)

        return response
    
    async def getProductBulkUploadHistory(self, search=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Helps to get bulk product upload jobs data.
        :param search : Search string to filter the results by batch id : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if search is not None:
            payload["search"] = search
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getProductBulkUploadHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", """{"required":[{"description":"Company Id of of which Product Bulk Upload History to be obtained.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"Search string to filter the results by batch id","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"query":[{"description":"Search string to filter the results by batch id","in":"query","name":"search","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"headers":[],"path":[{"description":"Company Id of of which Product Bulk Upload History to be obtained.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", search=search, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(search=search, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", search=search, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductBulkRequestList
            schema = ProductBulkRequestList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductBulkUploadHistory")
                print(e)

        return response
    
    async def createBulkProductUploadJob(self, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", """{"required":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkResponseSchema
            schema = BulkResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createBulkProductUploadJob")
                print(e)

        return response
    
    async def deleteProductBulkJob(self, batch_id=None, request_headers:Dict={}):
        """Allows to delete bulk product job associated with company.
        :param batch_id : Batch Id of the bulk product job to be deleted. : type integer
        """
        payload = {}
        
        if batch_id is not None:
            payload["batch_id"] = batch_id

        # Parameter validation
        schema = CatalogValidator.deleteProductBulkJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", """{"required":[{"description":"Company Id of the company associated to size that is to be deleted.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Batch Id of the bulk product job to be deleted.","in":"path","name":"batch_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id of the company associated to size that is to be deleted.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Batch Id of the bulk product job to be deleted.","in":"path","name":"batch_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", batch_id=batch_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteProductBulkJob")
                print(e)

        return response
    
    async def createProductsInBulk(self, batch_id=None, body="", request_headers:Dict={}):
        """Helps to create products in bulk push to kafka for approval/creation.
        :param batch_id : Batch Id in which assets to be uploaded. : type string
        """
        payload = {}
        
        if batch_id is not None:
            payload["batch_id"] = batch_id

        # Parameter validation
        schema = CatalogValidator.createProductsInBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkProductRequestSchema
        schema = BulkProductRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", """{"required":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Batch Id in which assets to be uploaded.","in":"path","name":"batch_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Batch Id in which assets to be uploaded.","in":"path","name":"batch_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", batch_id=batch_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", batch_id=batch_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createProductsInBulk")
                print(e)

        return response
    
    async def listProductTemplateExportDetails(self, request_headers:Dict={}):
        """Retrieve export details related to product templates for a specific company. Can view details including trigger data, task id , etc.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.listProductTemplateExportDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/downloads/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/downloads/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductDownloadsResponseSchema
            schema = ProductDownloadsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for listProductTemplateExportDetails")
                print(e)

        return response
    
    async def listHSNCodes(self, request_headers:Dict={}):
        """Retrieve a list of Harmonized System Nomenclature (HSN) codes for a company.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.listHSNCodes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/hsn/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/hsn/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import HSNCodesResponseSchema
            schema = HSNCodesResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for listHSNCodes")
                print(e)

        return response
    
    async def getProductTags(self, request_headers:Dict={}):
        """Retrieve tags data associated to a particular company.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getProductTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/tags", """{"required":[{"description":"Company Id for which tags to be fetched.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id for which tags to be fetched.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/tags", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductTagsViewResponseSchema
            schema = ProductTagsViewResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductTags")
                print(e)

        return response
    
    async def listProductTemplate(self, department=None, request_headers:Dict={}):
        """Allows you to list all product templates for a specific company. also can filter by department.
        :param department : A `department` is the name of a particular department. : type string
        """
        payload = {}
        
        if department is not None:
            payload["department"] = department

        # Parameter validation
        schema = CatalogValidator.listProductTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `department` is the name of a particular department.","in":"query","name":"department","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"description":"A `department` is the name of a particular department.","in":"query","name":"department","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", department=department)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/", department=department), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TemplatesResponseSchema
            schema = TemplatesResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for listProductTemplate")
                print(e)

        return response
    
    async def listProductTemplateCategories(self, departments=None, item_type=None, request_headers:Dict={}):
        """Allows you to list all product template categories values for the departments specified for a specific company.
        :param departments : A `department` is name of a departments whose category needs to be listed. Can specify multiple departments. : type string
        :param item_type : An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc. : type string
        """
        payload = {}
        
        if departments is not None:
            payload["departments"] = departments
        if item_type is not None:
            payload["item_type"] = item_type

        # Parameter validation
        schema = CatalogValidator.listProductTemplateCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/categories/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"A `department` is name of a departments whose category needs to be listed. Can specify multiple departments.","in":"query","name":"departments","required":true,"schema":{"type":"string"}},{"description":"An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc.","in":"query","name":"item_type","required":true,"schema":{"type":"string","enum":["set","standard","digital"]}}],"optional":[],"query":[{"description":"A `department` is name of a departments whose category needs to be listed. Can specify multiple departments.","in":"query","name":"departments","required":true,"schema":{"type":"string"}},{"description":"An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc.","in":"query","name":"item_type","required":true,"schema":{"type":"string","enum":["set","standard","digital"]}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", departments=departments, item_type=item_type)
        query_string = await create_query_string(departments=departments, item_type=item_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/categories/", departments=departments, item_type=item_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProdcutTemplateCategoriesResponseSchema
            schema = ProdcutTemplateCategoriesResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for listProductTemplateCategories")
                print(e)

        return response
    
    async def downloadProductTemplateViews(self, slug=None, item_type=None, type=None, request_headers:Dict={}):
        """Allows you to download product template data by its slug for a specific company.
        :param slug : A `slug` is a unique identifier for a particular template. : type string
        :param item_type : An `item_type` defines the type of item. The default value is standard. : type string
        :param type : Format type of the sample file. The default value is excel. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if item_type is not None:
            payload["item_type"] = item_type
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = CatalogValidator.downloadProductTemplateViews()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/download/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `slug` is a unique identifier for a particular template.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}],"optional":[{"description":"An `item_type` defines the type of item. The default value is standard.","in":"query","name":"item_type","schema":{"type":"string","enum":["set","standard","composite","digital"]}},{"description":"Format type of the sample file. The default value is excel.","in":"query","name":"type","schema":{"type":"string"}}],"query":[{"description":"An `item_type` defines the type of item. The default value is standard.","in":"query","name":"item_type","schema":{"type":"string","enum":["set","standard","composite","digital"]}},{"description":"Format type of the sample file. The default value is excel.","in":"query","name":"type","schema":{"type":"string"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `slug` is a unique identifier for a particular template.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug, item_type=item_type, type=type)
        query_string = await create_query_string(item_type=item_type, type=type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/download/", slug=slug, item_type=item_type, type=type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def validateProductTemplate(self, slug=None, item_type=None, bulk=None, request_headers:Dict={}):
        """Allows you to list all product templates validation values by its slug for all the fields present in the database for a specific company.
        :param slug : A `slug` is a unique identifier for a particular template. : type string
        :param item_type : An `item_type` defines the type of item. The default value is standard. : type string
        :param bulk : This specification determines the schema type to be retrieved. When set to true, it will return the schema for bulk data; when set to false, it will provide the schema for a single product. The default value is false. : type boolean
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if item_type is not None:
            payload["item_type"] = item_type
        if bulk is not None:
            payload["bulk"] = bulk

        # Parameter validation
        schema = CatalogValidator.validateProductTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/validation/schema/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `slug` is a unique identifier for a particular template.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}],"optional":[{"description":"An `item_type` defines the type of item. The default value is standard.","in":"query","name":"item_type","schema":{"type":"string","enum":["set","standard","composite","digital"]}},{"description":"This specification determines the schema type to be retrieved. When set to true, it will return the schema for bulk data; when set to false, it will provide the schema for a single product. The default value is false.","in":"query","name":"bulk","schema":{"type":"boolean"}}],"query":[{"description":"An `item_type` defines the type of item. The default value is standard.","in":"query","name":"item_type","schema":{"type":"string","enum":["set","standard","composite","digital"]}},{"description":"This specification determines the schema type to be retrieved. When set to true, it will return the schema for bulk data; when set to false, it will provide the schema for a single product. The default value is false.","in":"query","name":"bulk","schema":{"type":"boolean"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"A `slug` is a unique identifier for a particular template.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug, item_type=item_type, bulk=bulk)
        query_string = await create_query_string(item_type=item_type, bulk=bulk)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/validation/schema/", slug=slug, item_type=item_type, bulk=bulk), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TemplatesValidationResponseSchema
            schema = TemplatesValidationResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateProductTemplate")
                print(e)

        return response
    
    async def validateProductGlobalTemplate(self, item_type=None, bulk=None, request_headers:Dict={}):
        """Allows you to list all product templates global validation values for all the fields present in the database for a specific company.
        :param item_type : An `item_type` defines the type of item. The default value is standard. : type string
        :param bulk : This specification determines the schema type to be retrieved. When set to true, it will return the schema for bulk data; when set to false, it will provide the schema for a single product. The default value is false. : type boolean
        """
        payload = {}
        
        if item_type is not None:
            payload["item_type"] = item_type
        if bulk is not None:
            payload["bulk"] = bulk

        # Parameter validation
        schema = CatalogValidator.validateProductGlobalTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/validation/schema/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"An `item_type` defines the type of item. The default value is standard.","in":"query","name":"item_type","schema":{"type":"string","enum":["set","standard","composite","digital"]}},{"description":"This specification determines the schema type to be retrieved. When set to true, it will return the schema for bulk data; when set to false, it will provide the schema for a single product. The default value is false.","in":"query","name":"bulk","schema":{"type":"boolean"}}],"query":[{"description":"An `item_type` defines the type of item. The default value is standard.","in":"query","name":"item_type","schema":{"type":"string","enum":["set","standard","composite","digital"]}},{"description":"This specification determines the schema type to be retrieved. When set to true, it will return the schema for bulk data; when set to false, it will provide the schema for a single product. The default value is false.","in":"query","name":"bulk","schema":{"type":"boolean"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_type=item_type, bulk=bulk)
        query_string = await create_query_string(item_type=item_type, bulk=bulk)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/validation/schema/", item_type=item_type, bulk=bulk), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TemplatesGlobalValidationResponseSchema
            schema = TemplatesGlobalValidationResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateProductGlobalTemplate")
                print(e)

        return response
    
    async def getProductValidation(self, request_headers:Dict={}):
        """Retrieve validation data for products at company level.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getProductValidation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/validation/", """{"required":[{"description":"Validates data against given company","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Validates data against given company","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/validation/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ValidateProduct
            schema = ValidateProduct()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductValidation")
                print(e)

        return response
    
    async def getInventoryBySizeIdentifier(self, item_id=None, size_identifier=None, page_no=None, page_size=None, q=None, location_ids=None, request_headers:Dict={}):
        """Retrieve inventory data for a specific company, item ID, and seller identifier. The API supports search capabilities using store codes and location IDs.
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
        schema = CatalogValidator.getInventoryBySizeIdentifier()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/inventory/{size_identifier}", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"path","name":"size_identifier","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search with help of store code.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Search by store ids.","in":"query","name":"location_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search with help of store code.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Search by store ids.","in":"query","name":"location_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}}],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"path","name":"size_identifier","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/inventory/{size_identifier}", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventorySellerIdentifierResponsePaginated
            schema = InventorySellerIdentifierResponsePaginated()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInventoryBySizeIdentifier")
                print(e)

        return response
    
    async def getProductSize(self, item_code=None, item_id=None, brand_uid=None, uid=None, request_headers:Dict={}):
        """Retrieve data associated to a particular product size.
        :param item_code : Item code of the product size. : type string
        :param item_id : Item Id of the product size. : type integer
        :param brand_uid : Brand Id of the product size. : type integer
        :param uid : Id of the product size. : type integer
        """
        payload = {}
        
        if item_code is not None:
            payload["item_code"] = item_code
        if item_id is not None:
            payload["item_id"] = item_id
        if brand_uid is not None:
            payload["brand_uid"] = brand_uid
        if uid is not None:
            payload["uid"] = uid

        # Parameter validation
        schema = CatalogValidator.getProductSize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/", """{"required":[{"description":"Company Id of the product size.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item Id of the product size.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"Item code of the product size.","in":"query","name":"item_code","required":false,"schema":{"type":"string","x-not-enum":true}},{"description":"Brand Id of the product size.","in":"query","name":"brand_uid","required":false,"schema":{"type":"integer"}},{"description":"Id of the product size.","in":"query","name":"uid","required":false,"schema":{"type":"integer"}}],"query":[{"description":"Item code of the product size.","in":"query","name":"item_code","required":false,"schema":{"type":"string","x-not-enum":true}},{"description":"Brand Id of the product size.","in":"query","name":"brand_uid","required":false,"schema":{"type":"integer"}},{"description":"Id of the product size.","in":"query","name":"uid","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"Company Id of the product size.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item Id of the product size.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", item_code=item_code, item_id=item_id, brand_uid=brand_uid, uid=uid)
        query_string = await create_query_string(item_code=item_code, brand_uid=brand_uid, uid=uid)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/", item_code=item_code, item_id=item_id, brand_uid=brand_uid, uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductListingResponseSchema
            schema = ProductListingResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductSize")
                print(e)

        return response
    
    async def deleteSize(self, item_id=None, size=None, request_headers:Dict={}):
        """Allows to delete size associated with product.
        :param item_id : Item Id of the product associated with size to be deleted. : type integer
        :param size : size to be deleted. : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        if size is not None:
            payload["size"] = size

        # Parameter validation
        schema = CatalogValidator.deleteSize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", """{"required":[{"description":"Company Id of the company associated to size that is to be deleted.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item Id of the product associated with size to be deleted.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"size to be deleted.","in":"path","name":"size","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id of the company associated to size that is to be deleted.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item Id of the product associated with size to be deleted.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"size to be deleted.","in":"path","name":"size","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_id=item_id, size=size)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", item_id=item_id, size=size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductSizeDeleteResponseSchema
            schema = ProductSizeDeleteResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSize")
                print(e)

        return response
    
    async def getInventoryBySize(self, item_id=None, size=None, page_no=None, page_size=None, q=None, sellable=None, request_headers:Dict={}):
        """Retrieve inventory data for a specific company, item ID, and size. The API supports search capabilities based on selling location (store) code and product availability (in stock or not)."
        :param item_id : Item code of the product of which size is to be get. : type integer
        :param size : Size of which inventory is to get. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search with help of store code. : type string
        :param sellable : Filter on whether product is in stock or not. : type boolean
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        if size is not None:
            payload["size"] = size
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if sellable is not None:
            payload["sellable"] = sellable

        # Parameter validation
        schema = CatalogValidator.getInventoryBySize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size of which inventory is to get.","in":"path","name":"size","required":true,"schema":{"type":"string"}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search with help of store code.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Filter on whether product is in stock or not.","in":"query","name":"sellable","required":false,"schema":{"default":false,"type":"boolean"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"Search with help of store code.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Filter on whether product is in stock or not.","in":"query","name":"sellable","required":false,"schema":{"default":false,"type":"boolean"}}],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size of which inventory is to get.","in":"path","name":"size","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, sellable=sellable)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryResponsePaginated
            schema = InventoryResponsePaginated()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInventoryBySize")
                print(e)

        return response
    
    async def addInventory(self, item_id=None, size=None, body="", request_headers:Dict={}):
        """Allows add Inventory for particular size and selling location.
        :param item_id : Item id of the product of which size is to be get. : type integer
        :param size : Size in which inventory is to be added. : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        if size is not None:
            payload["size"] = size

        # Parameter validation
        schema = CatalogValidator.addInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryRequestSchema
        schema = InventoryRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item id of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size in which inventory is to be added.","in":"path","name":"size","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item id of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size in which inventory is to be added.","in":"path","name":"size","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_id=item_id, size=size)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", item_id=item_id, size=size), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addInventory")
                print(e)

        return response
    
    async def getVariantsOfProducts(self, item_id=None, variant_type=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve variants of a specific product.
        :param item_id : Get list of variants of item Id : type integer
        :param variant_type : Get multiple products filtered by variant type : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        if variant_type is not None:
            payload["variant_type"] = variant_type
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getVariantsOfProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/variants/{variant_type}", """{"required":[{"description":"Get list of products filtered by company Id","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Get list of variants of item Id","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Get multiple products filtered by variant type","in":"path","name":"variant_type","required":true,"schema":{"type":"string","x-not-enum":true}}],"optional":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}}],"query":[{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}}],"headers":[],"path":[{"description":"Get list of products filtered by company Id","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Get list of variants of item Id","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Get multiple products filtered by variant type","in":"path","name":"variant_type","required":true,"schema":{"type":"string","x-not-enum":true}}]}""", serverType="platform", item_id=item_id, variant_type=variant_type, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/variants/{variant_type}", item_id=item_id, variant_type=variant_type, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductVariantsResponseSchema
            schema = ProductVariantsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getVariantsOfProducts")
                print(e)

        return response
    
    async def getSizeGuides(self, active=None, q=None, tag=None, page_no=None, page_size=None, brand_id=None, request_headers:Dict={}):
        """Allows to view all the size guides associated to the seller. Each size guide contains meta deta like header values like for shoulder, head, etc. and measurement unit like cm and values contains sizes for the same.
        :param active : filter size guide on basis of active, in-active : type boolean
        :param q : Query that is to be searched. : type string
        :param tag : to filter size guide on basis of tag. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param brand_id : Brand id that is to be searched. : type integer
        """
        payload = {}
        
        if active is not None:
            payload["active"] = active
        if q is not None:
            payload["q"] = q
        if tag is not None:
            payload["tag"] = tag
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if brand_id is not None:
            payload["brand_id"] = brand_id

        # Parameter validation
        schema = CatalogValidator.getSizeGuides()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", """{"required":[{"description":"Id of the company for which the size guides are to be fetched.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"filter size guide on basis of active, in-active","in":"query","name":"active","required":false,"schema":{"type":"boolean"}},{"description":"Query that is to be searched.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"to filter size guide on basis of tag.","in":"query","name":"tag","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"Brand id that is to be searched.","in":"query","name":"brand_id","required":false,"schema":{"type":"integer"}}],"query":[{"description":"filter size guide on basis of active, in-active","in":"query","name":"active","required":false,"schema":{"type":"boolean"}},{"description":"Query that is to be searched.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"to filter size guide on basis of tag.","in":"query","name":"tag","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"Brand id that is to be searched.","in":"query","name":"brand_id","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"Id of the company for which the size guides are to be fetched.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", active=active, q=q, tag=tag, page_no=page_no, page_size=page_size, brand_id=brand_id)
        query_string = await create_query_string(active=active, q=q, tag=tag, page_no=page_no, page_size=page_size, brand_id=brand_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", active=active, q=q, tag=tag, page_no=page_no, page_size=page_size, brand_id=brand_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ListSizeGuide
            schema = ListSizeGuide()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSizeGuides")
                print(e)

        return response
    
    async def createSizeGuide(self, body="", request_headers:Dict={}):
        """Allows to create a size guide associated to a seller
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createSizeGuide()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateSizeGuide
        schema = ValidateSizeGuide()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", """{"required":[{"description":"Id of the company inside which the size guide is to be created.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company inside which the size guide is to be created.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSizeGuide")
                print(e)

        return response
    
    async def getSizeGuide(self, id=None, request_headers:Dict={}):
        """Retrieve data associated about a specific size guide. It contains meta deta like header values like for shoulder, head, etc. and measurement unit like cm and values contains sizes for the same.
        :param id : Id of the size guide to be viewed. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getSizeGuide()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", """{"required":[{"description":"Id of the company associated to size guide.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the size guide to be viewed.","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to size guide.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the size guide to be viewed.","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SizeGuideResponseSchema
            schema = SizeGuideResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSizeGuide")
                print(e)

        return response
    
    async def updateSizeGuide(self, id=None, body="", request_headers:Dict={}):
        """Allows to edit a specific size guide.
        :param id : Mongo id of the size guide to be edited : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.updateSizeGuide()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateSizeGuide
        schema = ValidateSizeGuide()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", """{"required":[{"description":"Id of the company.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Mongo id of the size guide to be edited","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Mongo id of the size guide to be edited","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSizeGuide")
                print(e)

        return response
    
    async def getAllProductHsnCodes(self, page_no=None, page_size=None, q=None, type=None, request_headers:Dict={}):
        """Retrieve all HSN codes associated with company products and provide search capabilities based on HSN code, reporting HSN, etc
        :param page_no : indicates current page number : type integer
        :param page_size : indicates page size : type integer
        :param q : search using hsn code, description, reporting_hsn : type string
        :param type : search using type : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = CatalogValidator.getAllProductHsnCodes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/", """{"required":[{"description":"Company Id for which HSN codes needs to be fetched","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"indicates current page number","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"indicates page size","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"search using hsn code, description, reporting_hsn","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"search using type","in":"query","name":"type","required":false,"schema":{"type":"string"}}],"query":[{"description":"indicates current page number","in":"query","name":"page_no","required":false,"schema":{"default":1,"type":"integer"}},{"description":"indicates page size","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}},{"description":"search using hsn code, description, reporting_hsn","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"search using type","in":"query","name":"type","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"Company Id for which HSN codes needs to be fetched","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q, type=type, )
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, type=type, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/", page_no=page_no, page_size=page_size, q=q, type=type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import HsnCodesListingResponseSchemaV2
            schema = HsnCodesListingResponseSchemaV2()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllProductHsnCodes")
                print(e)

        return response
    
    async def getSingleProductHSNCode(self, reporting_hsn=None, request_headers:Dict={}):
        """Retrieve HSN details associated with company ID and reporting HSN
        :param reporting_hsn : reporting_hsn : type string
        """
        payload = {}
        
        if reporting_hsn is not None:
            payload["reporting_hsn"] = reporting_hsn

        # Parameter validation
        schema = CatalogValidator.getSingleProductHSNCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/{reporting_hsn}", """{"required":[{"description":"reporting_hsn","in":"path","name":"reporting_hsn","required":true,"schema":{"type":"string"}},{"description":"Company Id for which HSN codes needs to be fetched","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"reporting_hsn","in":"path","name":"reporting_hsn","required":true,"schema":{"type":"string"}},{"description":"Company Id for which HSN codes needs to be fetched","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", reporting_hsn=reporting_hsn, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/{reporting_hsn}", reporting_hsn=reporting_hsn), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import HSNDataInsertV2
            schema = HSNDataInsertV2()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSingleProductHSNCode")
                print(e)

        return response
    
    async def updateInventories(self, body="", request_headers:Dict={}):
        """Allows to add Inventory for particular size and selling location. for associated companies
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateInventories()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryRequestSchemaV2
        schema = InventoryRequestSchemaV2()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryUpdateResponseSchema
            schema = InventoryUpdateResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateInventories")
                print(e)

        return response
    
    async def listInventoryExport(self, status=None, from_date=None, to_date=None, q=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve the history of inventory export jobs associated with the company
        :param status : Status of the export job.(Pending, Running, Success) : type string
        :param from_date : Inventory export history filtered according to from_date. : type string
        :param to_date : Inventory export history filtered according to from_date. : type string
        :param q : Inventory export history filtered according to task ID. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if status is not None:
            payload["status"] = status
        if from_date is not None:
            payload["from_date"] = from_date
        if to_date is not None:
            payload["to_date"] = to_date
        if q is not None:
            payload["q"] = q
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.listInventoryExport()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/", """{"required":[{"description":"It is the unique identifier of the company.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"Status of the export job.(Pending, Running, Success)","in":"query","name":"status","required":false,"schema":{"type":"string"}},{"description":"Inventory export history filtered according to from_date.","in":"query","name":"from_date","required":false,"schema":{"type":"string","format":"date"}},{"description":"Inventory export history filtered according to from_date.","in":"query","name":"to_date","required":false,"schema":{"type":"string","format":"date"}},{"description":"Inventory export history filtered according to task ID.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"query":[{"description":"Status of the export job.(Pending, Running, Success)","in":"query","name":"status","required":false,"schema":{"type":"string"}},{"description":"Inventory export history filtered according to from_date.","in":"query","name":"from_date","required":false,"schema":{"type":"string","format":"date"}},{"description":"Inventory export history filtered according to from_date.","in":"query","name":"to_date","required":false,"schema":{"type":"string","format":"date"}},{"description":"Inventory export history filtered according to task ID.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"headers":[],"path":[{"description":"It is the unique identifier of the company.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", status=status, from_date=from_date, to_date=to_date, q=q, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(status=status, from_date=from_date, to_date=to_date, q=q, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/", status=status, from_date=from_date, to_date=to_date, q=q, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryExportJobListResponseSchema
            schema = InventoryExportJobListResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for listInventoryExport")
                print(e)

        return response
    
    async def createInventoryExport(self, body="", request_headers:Dict={}):
        """creates export job for inventory data associated with a company
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createInventoryExport()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryCreateRequestSchema
        schema = InventoryCreateRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/", """{"required":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/download/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryExportResponseSchema
            schema = InventoryExportResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createInventoryExport")
                print(e)

        return response
    
    async def getProducts(self, brand_ids=None, category_ids=None, item_ids=None, department_ids=None, item_code=None, name=None, slug=None, all_identifiers=None, q=None, tags=None, page_no=None, page_size=None, page_type=None, sort_on=None, page_id=None, request_headers:Dict={}):
        """Retrieve a list of available products
        :param brand_ids : Get multiple products filtered by Brand Ids : type array
        :param category_ids : Get multiple products filtered by Category Ids : type array
        :param item_ids : Get multiple products filtered by Item Ids : type array
        :param department_ids : Get multiple products filtered by Department Ids : type array
        :param item_code : Get multiple products filtered by Item Code : type array
        :param name : Get multiple products filtered by Name (Pattern Match) : type string
        :param slug : Get multiple products filtered by Slug : type string
        :param all_identifiers : Get multiple products filtered by All Identifiers : type array
        :param q : Get multiple products filtered by q string : type string
        :param tags : Get multiple products filtered by tags : type array
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param page_type : For pagination type value can be cursor or number. Default is number. : type string
        :param sort_on : Field which is to be used for sorting, default is latest. Value can be latest (modified_on) or created (record id) : type string
        :param page_id : If page_type is cursor, each response will contain **next_id** param (datetime or id depending upon sort_on), which should be sent back as page_id to make cursor pagination work. : type string
        """
        payload = {}
        
        if brand_ids is not None:
            payload["brand_ids"] = brand_ids
        if category_ids is not None:
            payload["category_ids"] = category_ids
        if item_ids is not None:
            payload["item_ids"] = item_ids
        if department_ids is not None:
            payload["department_ids"] = department_ids
        if item_code is not None:
            payload["item_code"] = item_code
        if name is not None:
            payload["name"] = name
        if slug is not None:
            payload["slug"] = slug
        if all_identifiers is not None:
            payload["all_identifiers"] = all_identifiers
        if q is not None:
            payload["q"] = q
        if tags is not None:
            payload["tags"] = tags
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if page_type is not None:
            payload["page_type"] = page_type
        if sort_on is not None:
            payload["sort_on"] = sort_on
        if page_id is not None:
            payload["page_id"] = page_id

        # Parameter validation
        schema = CatalogValidator.getProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/", """{"required":[{"description":"Get list of products filtered by company Id","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"Get multiple products filtered by Brand Ids","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Category Ids","in":"query","name":"category_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Item Ids","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Department Ids","in":"query","name":"department_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Item Code","in":"query","name":"item_code","required":false,"schema":{"items":{"type":"string","x-not-enum":true},"type":"array"}},{"description":"Get multiple products filtered by Name (Pattern Match)","in":"query","name":"name","required":false,"schema":{"type":"string"}},{"description":"Get multiple products filtered by Slug","in":"query","name":"slug","required":false,"schema":{"type":"string"}},{"description":"Get multiple products filtered by All Identifiers","in":"query","name":"all_identifiers","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get multiple products filtered by q string","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Get multiple products filtered by tags","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"For pagination type value can be cursor or number. Default is number.","in":"query","name":"page_type","required":false,"schema":{"default":"number","type":"string","enum":["number","cursor"]}},{"description":"Field which is to be used for sorting, default is latest. Value can be latest (modified_on) or created (record id)","in":"query","name":"sort_on","required":false,"schema":{"default":"latest","type":"string"}},{"description":"If page_type is cursor, each response will contain **next_id** param (datetime or id depending upon sort_on), which should be sent back as page_id to make cursor pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}}],"query":[{"description":"Get multiple products filtered by Brand Ids","in":"query","name":"brand_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Category Ids","in":"query","name":"category_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Item Ids","in":"query","name":"item_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Department Ids","in":"query","name":"department_ids","required":false,"schema":{"items":{"type":"integer"},"type":"array"}},{"description":"Get multiple products filtered by Item Code","in":"query","name":"item_code","required":false,"schema":{"items":{"type":"string","x-not-enum":true},"type":"array"}},{"description":"Get multiple products filtered by Name (Pattern Match)","in":"query","name":"name","required":false,"schema":{"type":"string"}},{"description":"Get multiple products filtered by Slug","in":"query","name":"slug","required":false,"schema":{"type":"string"}},{"description":"Get multiple products filtered by All Identifiers","in":"query","name":"all_identifiers","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"Get multiple products filtered by q string","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"Get multiple products filtered by tags","in":"query","name":"tags","required":false,"schema":{"items":{"type":"string"},"type":"array"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 10.","in":"query","name":"page_size","required":false,"schema":{"default":10,"type":"integer"}},{"description":"For pagination type value can be cursor or number. Default is number.","in":"query","name":"page_type","required":false,"schema":{"default":"number","type":"string","enum":["number","cursor"]}},{"description":"Field which is to be used for sorting, default is latest. Value can be latest (modified_on) or created (record id)","in":"query","name":"sort_on","required":false,"schema":{"default":"latest","type":"string"}},{"description":"If page_type is cursor, each response will contain **next_id** param (datetime or id depending upon sort_on), which should be sent back as page_id to make cursor pagination work.","in":"query","name":"page_id","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"description":"Get list of products filtered by company Id","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, name=name, slug=slug, all_identifiers=all_identifiers, q=q, tags=tags, page_no=page_no, page_size=page_size, page_type=page_type, sort_on=sort_on, page_id=page_id)
        query_string = await create_query_string(brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, name=name, slug=slug, all_identifiers=all_identifiers, q=q, tags=tags, page_no=page_no, page_size=page_size, page_type=page_type, sort_on=sort_on, page_id=page_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/", brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, name=name, slug=slug, all_identifiers=all_identifiers, q=q, tags=tags, page_no=page_no, page_size=page_size, page_type=page_type, sort_on=sort_on, page_id=page_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductListingResponseV2
            schema = ProductListingResponseV2()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProducts")
                print(e)

        return response
    
    async def createProduct(self, body="", request_headers:Dict={}):
        """Users can create a product using this API, associating it with the provided company ID
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductCreateUpdateSchemaV2
        schema = ProductCreateUpdateSchemaV2()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseObject
            schema = SuccessResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createProduct")
                print(e)

        return response
    
    async def uploadBulkProducts(self, department=None, product_type=None, body="", request_headers:Dict={}):
        """Users can create multiple products by providing the required information needed for product creation in a CSV or Excel file format.
        :param department : Department of the product to be uploaded. : type string
        :param product_type : Product type of the product to be uploaded i.e. set, standard, digital. : type string
        """
        payload = {}
        
        if department is not None:
            payload["department"] = department
        if product_type is not None:
            payload["product_type"] = product_type

        # Parameter validation
        schema = CatalogValidator.uploadBulkProducts()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkProductJob
        schema = BulkProductJob()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/bulk", """{"required":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Department of the product to be uploaded.","in":"query","name":"department","required":true,"schema":{"type":"string"}},{"description":"Product type of the product to be uploaded i.e. set, standard, digital.","in":"query","name":"product_type","required":true,"schema":{"type":"string","enum":["set","digital","standard","composite"]}}],"optional":[],"query":[{"description":"Department of the product to be uploaded.","in":"query","name":"department","required":true,"schema":{"type":"string"}},{"description":"Product type of the product to be uploaded i.e. set, standard, digital.","in":"query","name":"product_type","required":true,"schema":{"type":"string","enum":["set","digital","standard","composite"]}}],"headers":[],"path":[{"description":"Company Id in which assets to be uploaded.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", department=department, product_type=product_type)
        query_string = await create_query_string(department=department, product_type=product_type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/bulk", department=department, product_type=product_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkResponseSchema
            schema = BulkResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for uploadBulkProducts")
                print(e)

        return response
    
    async def getProductExportJobs(self, status=None, from_date=None, to_date=None, q=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Get product export jobs specific to a company based on queries like query param, date range and status. View details including trigger data, task id , etc.
        :param status : This is a parameter used to find all the jobs with the specified status. : type string
        :param from_date : This is a parameter used to find the job from the date specified to the current date. : type string
        :param to_date : This is a parameter used to find the job from the from_date specified to the to_date. : type string
        :param q : It is a query parameter to search the export job with the task ID. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if status is not None:
            payload["status"] = status
        if from_date is not None:
            payload["from_date"] = from_date
        if to_date is not None:
            payload["to_date"] = to_date
        if q is not None:
            payload["q"] = q
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getProductExportJobs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"This is a parameter used to find all the jobs with the specified status.","in":"query","name":"status","required":false,"schema":{"type":"string"}},{"description":"This is a parameter used to find the job from the date specified to the current date.","in":"query","name":"from_date","required":false,"schema":{"format":"date","type":"string"}},{"description":"This is a parameter used to find the job from the from_date specified to the to_date.","in":"query","name":"to_date","required":false,"schema":{"format":"date","type":"string"}},{"description":"It is a query parameter to search the export job with the task ID.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"query":[{"description":"This is a parameter used to find all the jobs with the specified status.","in":"query","name":"status","required":false,"schema":{"type":"string"}},{"description":"This is a parameter used to find the job from the date specified to the current date.","in":"query","name":"from_date","required":false,"schema":{"format":"date","type":"string"}},{"description":"This is a parameter used to find the job from the from_date specified to the to_date.","in":"query","name":"to_date","required":false,"schema":{"format":"date","type":"string"}},{"description":"It is a query parameter to search the export job with the task ID.","in":"query","name":"q","required":false,"schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Number of items to retrieve in each page. Default is 12.","in":"query","name":"page_size","required":false,"schema":{"default":12,"type":"integer"}}],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", status=status, from_date=from_date, to_date=to_date, q=q, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(status=status, from_date=from_date, to_date=to_date, q=q, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/", status=status, from_date=from_date, to_date=to_date, q=q, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductDownloadsResponseSchema
            schema = ProductDownloadsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductExportJobs")
                print(e)

        return response
    
    async def createProductExportJob(self, body="", request_headers:Dict={}):
        """Allows to create a product export job for a company.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createProductExportJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductTemplateDownloadsExport
        schema = ProductTemplateDownloadsExport()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/", """{"required":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A `company_id` is a unique identifier for a particular seller account.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/downloads/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductDownloadsResponseSchema
            schema = ProductDownloadsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createProductExportJob")
                print(e)

        return response
    
    async def deleteProduct(self, item_id=None, body="", request_headers:Dict={}):
        """Users can delete a product by providing the item_id and company_id.
        :param item_id : Id of the product to be deleted. : type integer
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id

        # Parameter validation
        schema = CatalogValidator.deleteProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DeleteProductRequestBody
        schema = DeleteProductRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", """{"required":[{"description":"Company Id of the company associated with the product to be deleted.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the product to be deleted.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Company Id of the company associated with the product to be deleted.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the product to be deleted.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", item_id=item_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", item_id=item_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteProduct")
                print(e)

        return response
    
    async def getProduct(self, item_id=None, brand_uid=None, item_code=None, request_headers:Dict={}):
        """Retrieve data associated to a particular product.
        :param item_id : Item Id of the product. : type integer
        :param brand_uid : Brand Id of the product. : type integer
        :param item_code : Item code of the product. : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        if brand_uid is not None:
            payload["brand_uid"] = brand_uid
        if item_code is not None:
            payload["item_code"] = item_code

        # Parameter validation
        schema = CatalogValidator.getProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", """{"required":[{"description":"Company Id of the product.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item Id of the product.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}],"optional":[{"description":"Brand Id of the product.","in":"query","name":"brand_uid","required":false,"schema":{"type":"integer"}},{"description":"Item code of the product.","in":"query","name":"item_code","required":false,"schema":{"type":"string","x-not-enum":true}}],"query":[{"description":"Brand Id of the product.","in":"query","name":"brand_uid","required":false,"schema":{"type":"integer"}},{"description":"Item code of the product.","in":"query","name":"item_code","required":false,"schema":{"type":"string","x-not-enum":true}}],"headers":[],"path":[{"description":"Company Id of the product.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item Id of the product.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", item_id=item_id, brand_uid=brand_uid, item_code=item_code)
        query_string = await create_query_string(brand_uid=brand_uid, item_code=item_code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", item_id=item_id, brand_uid=brand_uid, item_code=item_code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SingleProductResponseSchema
            schema = SingleProductResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProduct")
                print(e)

        return response
    
    async def editProduct(self, item_id=None, body="", request_headers:Dict={}):
        """Modify the details and settings of an existing product in the catalog.
        :param item_id : Id of the product to be updated. : type integer
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id

        # Parameter validation
        schema = CatalogValidator.editProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductCreateUpdateSchemaV2
        schema = ProductCreateUpdateSchemaV2()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the product to be updated.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the product to be updated.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", item_id=item_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/", item_id=item_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponseSchema
            schema = SuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editProduct")
                print(e)

        return response
    
    async def allSizes(self, item_id=None, request_headers:Dict={}):
        """Retrieve all available sizes for a product.
        :param item_id : Id of the product to be updated. : type integer
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id

        # Parameter validation
        schema = CatalogValidator.allSizes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/all_sizes", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the product to be updated.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"Id of the product to be updated.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", item_id=item_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/all_sizes", item_id=item_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAllSizes
            schema = GetAllSizes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for allSizes")
                print(e)

        return response
    
    async def deleteRealtimeInventory(self, item_id=None, seller_identifier=None, body="", request_headers:Dict={}):
        """You can use this API to delete inventory linked to a particular product size. When you make the API call, the inventory associated with that size will be removed as part of api process.
        :param item_id : Item code of the product of which size is to be get. : type integer
        :param seller_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        if seller_identifier is not None:
            payload["seller_identifier"] = seller_identifier

        # Parameter validation
        schema = CatalogValidator.deleteRealtimeInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryRequestSchemaV2
        schema = InventoryRequestSchemaV2()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"path","name":"seller_identifier","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"path","name":"seller_identifier","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_id=item_id, seller_identifier=seller_identifier)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}", item_id=item_id, seller_identifier=seller_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryUpdateResponseSchema
            schema = InventoryUpdateResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteRealtimeInventory")
                print(e)

        return response
    
    async def updateRealtimeInventory(self, item_id=None, seller_identifier=None, body="", request_headers:Dict={}):
        """enables you to add inventory for a specific size and selling location (store). The inventory updates will be reflected instantly after the API call.
        :param item_id : Item code of the product of which size is to be get. : type integer
        :param seller_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        if seller_identifier is not None:
            payload["seller_identifier"] = seller_identifier

        # Parameter validation
        schema = CatalogValidator.updateRealtimeInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InventoryRequestSchemaV2
        schema = InventoryRequestSchemaV2()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}", """{"required":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"path","name":"seller_identifier","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to product that is to be viewed.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"Item code of the product of which size is to be get.","in":"path","name":"item_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","in":"path","name":"seller_identifier","required":true,"schema":{"type":"string"}}]}""", serverType="platform", item_id=item_id, seller_identifier=seller_identifier)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}", item_id=item_id, seller_identifier=seller_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InventoryUpdateResponseSchema
            schema = InventoryUpdateResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateRealtimeInventory")
                print(e)

        return response
    
    async def updateLocationPrice(self, store_id=None, seller_identifier=None, body="", request_headers:Dict={}):
        """enables you to update article price for a specific size and selling location (store). The price updates will be reflected instantly after the API call.
        :param store_id : The Store Id to update price of size for specific store. : type integer
        :param seller_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which article price is to update. : type string
        """
        payload = {}
        
        if store_id is not None:
            payload["store_id"] = store_id
        if seller_identifier is not None:
            payload["seller_identifier"] = seller_identifier

        # Parameter validation
        schema = CatalogValidator.updateLocationPrice()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import LocationPriceRequestSchema
        schema = LocationPriceRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/store/{store_id}/identifier/{seller_identifier}/price", """{"required":[{"description":"Id of the company associated to product for that article price to be updated.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"The Store Id to update price of size for specific store.","in":"path","name":"store_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which article price is to update.","in":"path","name":"seller_identifier","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to product for that article price to be updated.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"The Store Id to update price of size for specific store.","in":"path","name":"store_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which article price is to update.","in":"path","name":"seller_identifier","required":true,"schema":{"type":"string"}}]}""", serverType="platform", store_id=store_id, seller_identifier=seller_identifier)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/store/{store_id}/identifier/{seller_identifier}/price", store_id=store_id, seller_identifier=seller_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LocationPriceQuantitySuccessResponseSchema
            schema = LocationPriceQuantitySuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateLocationPrice")
                print(e)

        return response
    
    async def updateLocationQuantity(self, store_id=None, seller_identifier=None, body="", request_headers:Dict={}):
        """enables you to update article quantity for a specific size and selling location (store). The quantity updates will be reflected instantly after the API call.
        :param store_id : The Store Id to update quantity of size for specific store. : type integer
        :param seller_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which article quantity is to update. : type string
        """
        payload = {}
        
        if store_id is not None:
            payload["store_id"] = store_id
        if seller_identifier is not None:
            payload["seller_identifier"] = seller_identifier

        # Parameter validation
        schema = CatalogValidator.updateLocationQuantity()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import LocationQuantityRequestSchema
        schema = LocationQuantityRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/store/{store_id}/identifier/{seller_identifier}/quantity", """{"required":[{"description":"Id of the company associated to product for that article quantity to be updated.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"The Store Id to update quantity of size for specific store.","in":"path","name":"store_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which article quantity is to update.","in":"path","name":"seller_identifier","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to product for that article quantity to be updated.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"The Store Id to update quantity of size for specific store.","in":"path","name":"store_id","required":true,"schema":{"type":"integer"}},{"description":"Size Identifier (Seller Identifier or Primary Identifier) of which article quantity is to update.","in":"path","name":"seller_identifier","required":true,"schema":{"type":"string"}}]}""", serverType="platform", store_id=store_id, seller_identifier=seller_identifier)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/store/{store_id}/identifier/{seller_identifier}/quantity", store_id=store_id, seller_identifier=seller_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LocationPriceQuantitySuccessResponseSchema
            schema = LocationPriceQuantitySuccessResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateLocationQuantity")
                print(e)

        return response
    
    async def getMarketplaces(self, request_headers:Dict={}):
        """Allows to get all marketplaces information for a company.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getMarketplaces()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/channel", """{"required":[{"description":"Id of the company associated to the marketplace.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to the marketplace.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/channel", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAllMarketplaces
            schema = GetAllMarketplaces()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMarketplaces")
                print(e)

        return response
    
    async def updateMarketplaceOptin(self, marketplace_slug=None, body="", request_headers:Dict={}):
        """Allows to update marketplace optin for a company by marketplace_slug.
        :param marketplace_slug : Slug of the marketplace . : type string
        """
        payload = {}
        
        if marketplace_slug is not None:
            payload["marketplace_slug"] = marketplace_slug

        # Parameter validation
        schema = CatalogValidator.updateMarketplaceOptin()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateMarketplaceOptinRequestSchema
        schema = UpdateMarketplaceOptinRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/channel/{marketplace_slug}/opt-in", """{"required":[{"description":"Id of the company associated to the marketplace.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"Slug of the marketplace .","in":"path","name":"marketplace_slug","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"description":"Id of the company associated to the marketplace.","in":"path","name":"company_id","schema":{"type":"integer"},"required":true},{"description":"Slug of the marketplace .","in":"path","name":"marketplace_slug","schema":{"type":"string"},"required":true}]}""", serverType="platform", marketplace_slug=marketplace_slug)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/channel/{marketplace_slug}/opt-in", marketplace_slug=marketplace_slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateMarketplaceOptinResponseSchema
            schema = UpdateMarketplaceOptinResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateMarketplaceOptin")
                print(e)

        return response
    
    async def createMarketplaceOptin(self, marketplace_slug=None, body="", request_headers:Dict={}):
        """Allows to create opt-in information for a specific company.
        :param marketplace_slug : The marketplace for which the detail needs to be retrieved. : type string
        """
        payload = {}
        
        if marketplace_slug is not None:
            payload["marketplace_slug"] = marketplace_slug

        # Parameter validation
        schema = CatalogValidator.createMarketplaceOptin()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OptInPostRequestSchema
        schema = OptInPostRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/channel/{marketplace_slug}/opt-in", """{"required":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"The marketplace for which the detail needs to be retrieved.","in":"path","name":"marketplace_slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The company id for which the detail needs to be retrieved.","in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"description":"The marketplace for which the detail needs to be retrieved.","in":"path","name":"marketplace_slug","required":true,"schema":{"type":"string"}}]}""", serverType="platform", marketplace_slug=marketplace_slug)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/channel/{marketplace_slug}/opt-in", marketplace_slug=marketplace_slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateMarketplaceOptinResponseSchema
            schema = CreateMarketplaceOptinResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createMarketplaceOptin")
                print(e)

        return response
    