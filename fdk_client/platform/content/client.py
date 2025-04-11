"""Content Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import ContentValidator

class Content:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getCustomFieldTypes(self, request_headers:Dict={}):
        """Each custom field and custom field definition has a type, which defines the type of information that it can store. The custom field types have built-in validation. This api will give list of supported custom fields types
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getCustomFieldTypes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/types", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/types", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MetafieldTypesSchema
            schema = MetafieldTypesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFieldTypes")
                print(e)

        return response
    
    async def getResources(self, request_headers:Dict={}):
        """Use this API to retrieve the resources, such as products, collections, customers, selling locations, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getResources()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/resources", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/resources", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResourcesSchema
            schema = ResourcesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getResources")
                print(e)

        return response
    
    async def getCustomFieldDefinitions(self, page_no=None, page_size=None, resources=None, types=None, search=None, slugs=None, namespaces=None, request_headers:Dict={}):
        """Custom field definitions enable you to include data validation for custom fields, and enable sellers to add custom fields values for resources. With the help of this seller can retrive list of custom field definitions list.
        :param page_no :  : type string
        :param page_size :  : type string
        :param resources :  : type string
        :param types :  : type string
        :param search :  : type string
        :param slugs :  : type string
        :param namespaces :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if resources is not None:
            payload["resources"] = resources
        if types is not None:
            payload["types"] = types
        if search is not None:
            payload["search"] = search
        if slugs is not None:
            payload["slugs"] = slugs
        if namespaces is not None:
            payload["namespaces"] = namespaces

        # Parameter validation
        schema = ContentValidator.getCustomFieldDefinitions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/definition", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}}],"optional":[{"name":"resources","in":"query","required":false,"schema":{"type":"string","description":"This is the resource for which we are fetching definitions"}},{"name":"types","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}},{"name":"slugs","in":"query","required":false,"schema":{"type":"string","description":"This is the slug list to filter custom fields definitions, it will come comma separated"}},{"name":"namespaces","in":"query","required":false,"schema":{"type":"string","description":"This is the namespace list to filter custom fields definitions, it needs to be comma separated"}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"resources","in":"query","required":false,"schema":{"type":"string","description":"This is the resource for which we are fetching definitions"}},{"name":"types","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}},{"name":"slugs","in":"query","required":false,"schema":{"type":"string","description":"This is the slug list to filter custom fields definitions, it will come comma separated"}},{"name":"namespaces","in":"query","required":false,"schema":{"type":"string","description":"This is the namespace list to filter custom fields definitions, it needs to be comma separated"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, resources=resources, types=types, search=search, slugs=slugs, namespaces=namespaces)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, resources=resources, types=types, search=search, slugs=slugs, namespaces=namespaces)
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/definition", page_no=page_no, page_size=page_size, resources=resources, types=types, search=search, slugs=slugs, namespaces=namespaces), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionsSchema
            schema = CustomFieldDefinitionsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFieldDefinitions")
                print(e)

        return response
    
    async def getCustomFieldDefinitionByResource(self, page_no=None, page_size=None, resource=None, types=None, search=None, slugs=None, namespaces=None, request_headers:Dict={}):
        """Custom field definitions enable you to include data validation for custom fields, and enable sellers to add custom fields values for resources. With the help of this seller can retrive list of custom field definitions list.
        :param page_no :  : type string
        :param page_size :  : type string
        :param resource :  : type string
        :param types :  : type string
        :param search :  : type string
        :param slugs :  : type string
        :param namespaces :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if resource is not None:
            payload["resource"] = resource
        if types is not None:
            payload["types"] = types
        if search is not None:
            payload["search"] = search
        if slugs is not None:
            payload["slugs"] = slugs
        if namespaces is not None:
            payload["namespaces"] = namespaces

        # Parameter validation
        schema = ContentValidator.getCustomFieldDefinitionByResource()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/definition", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}}],"optional":[{"name":"types","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}},{"name":"slugs","in":"query","required":false,"schema":{"type":"string","description":"This is the slug list to filter custom fields definitions, it will come comma separated"}},{"name":"namespaces","in":"query","required":false,"schema":{"type":"string","description":"This is the namespace list to filter custom fields definitions, it needs to be comma separated"}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"types","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}},{"name":"slugs","in":"query","required":false,"schema":{"type":"string","description":"This is the slug list to filter custom fields definitions, it will come comma separated"}},{"name":"namespaces","in":"query","required":false,"schema":{"type":"string","description":"This is the namespace list to filter custom fields definitions, it needs to be comma separated"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}}]}""", serverType="platform", page_no=page_no, page_size=page_size, resource=resource, types=types, search=search, slugs=slugs, namespaces=namespaces)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, types=types, search=search, slugs=slugs, namespaces=namespaces)
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/definition", page_no=page_no, page_size=page_size, resource=resource, types=types, search=search, slugs=slugs, namespaces=namespaces), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionsSchema
            schema = CustomFieldDefinitionsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFieldDefinitionByResource")
                print(e)

        return response
    
    async def createCustomFieldDefinition(self, resource=None, body="", request_headers:Dict={}):
        """You can create custom fields definition to any resource so you can extend property of resource.
        :param resource :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource

        # Parameter validation
        schema = ContentValidator.createCustomFieldDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldDefinitionRequestSchema
        schema = CustomFieldDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/definition", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}}]}""", serverType="platform", resource=resource)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/definition", resource=resource), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionDetailResSchema
            schema = CustomFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomFieldDefinition")
                print(e)

        return response
    
    async def getCustomFieldDefinitionBySlug(self, slug=None, resource=None, namespace=None, request_headers:Dict={}):
        """Custom field definitions can be retrived from this using its slug, namespace and resource
        :param slug :  : type string
        :param resource :  : type string
        :param namespace :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if resource is not None:
            payload["resource"] = resource
        if namespace is not None:
            payload["namespace"] = namespace

        # Parameter validation
        schema = ContentValidator.getCustomFieldDefinitionBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}]}""", serverType="platform", slug=slug, resource=resource, namespace=namespace)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", slug=slug, resource=resource, namespace=namespace), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MetaFieldDefinitionDetailResSchema
            schema = MetaFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFieldDefinitionBySlug")
                print(e)

        return response
    
    async def updateCustomFieldDefinitionBySlug(self, slug=None, resource=None, namespace=None, body="", request_headers:Dict={}):
        """Custom fields definition can be update using this api, You can update custom field definition name and description.
        :param slug :  : type string
        :param resource :  : type string
        :param namespace :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if resource is not None:
            payload["resource"] = resource
        if namespace is not None:
            payload["namespace"] = namespace

        # Parameter validation
        schema = ContentValidator.updateCustomFieldDefinitionBySlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldDefinitionRequestSchema
        schema = CustomFieldDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}]}""", serverType="platform", slug=slug, resource=resource, namespace=namespace)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", slug=slug, resource=resource, namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionDetailResSchema
            schema = CustomFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCustomFieldDefinitionBySlug")
                print(e)

        return response
    
    async def deleteCustomFieldDefinitionBySlug(self, slug=None, resource=None, namespace=None, request_headers:Dict={}):
        """Custom field definition and its assosiated custom fields value can be deleted using this api on the basis of definition id.
        :param slug :  : type string
        :param resource :  : type string
        :param namespace :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if resource is not None:
            payload["resource"] = resource
        if namespace is not None:
            payload["namespace"] = namespace

        # Parameter validation
        schema = ContentValidator.deleteCustomFieldDefinitionBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}]}""", serverType="platform", slug=slug, resource=resource, namespace=namespace)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", slug=slug, resource=resource, namespace=namespace), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomDataDeleteSchema
            schema = CustomDataDeleteSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCustomFieldDefinitionBySlug")
                print(e)

        return response
    
    async def getCustomFieldsByResourceSlug(self, resource=None, resource_slug=None, request_headers:Dict={}):
        """Retrieves a list of custom fields attached to a particular resource by using the resource and resource slug.
        :param resource :  : type string
        :param resource_slug :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource
        if resource_slug is not None:
            payload["resource_slug"] = resource_slug

        # Parameter validation
        schema = ContentValidator.getCustomFieldsByResourceSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/{resource_slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_slug","in":"path","required":true,"schema":{"type":"string","description":"This is the resource slug for which custom fields created"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_slug","in":"path","required":true,"schema":{"type":"string","description":"This is the resource slug for which custom fields created"}}]}""", serverType="platform", resource=resource, resource_slug=resource_slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/{resource_slug}", resource=resource, resource_slug=resource_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldsResponseByResourceIdSchema
            schema = CustomFieldsResponseByResourceIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFieldsByResourceSlug")
                print(e)

        return response
    
    async def updateCustomFieldByResourceSlug(self, resource=None, resource_slug=None, body="", request_headers:Dict={}):
        """You can add a custom field using this endpoint to any resource by providing the resource slug.
        :param resource :  : type string
        :param resource_slug :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource
        if resource_slug is not None:
            payload["resource_slug"] = resource_slug

        # Parameter validation
        schema = ContentValidator.updateCustomFieldByResourceSlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldRequestSchema
        schema = CustomFieldRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/{resource_slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_slug","in":"path","required":true,"schema":{"type":"string","description":"This is the resource slug for which custom fields created"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_slug","in":"path","required":true,"schema":{"type":"string","description":"This is the resource slug for which custom fields created"}}]}""", serverType="platform", resource=resource, resource_slug=resource_slug)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customfields/resource/{resource}/{resource_slug}", resource=resource, resource_slug=resource_slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldsResponseByResourceIdSchema
            schema = CustomFieldsResponseByResourceIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCustomFieldByResourceSlug")
                print(e)

        return response
    
    async def createCustomObjectDefinition(self, body="", request_headers:Dict={}):
        """Create a custom object that will have a collection of custom fields and can be used anywhere in the custom field for any resource.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createCustomObjectDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectDefinitionRequestSchema
        schema = CustomObjectDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSlugSchema
            schema = CustomObjectDefinitionSlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomObjectDefinition")
                print(e)

        return response
    
    async def getCustomObjectDefinitions(self, page_no=None, page_size=None, search=None, request_headers:Dict={}):
        """Custom object definition lists can be obtained using this endpoint.
        :param page_no :  : type string
        :param page_size :  : type string
        :param search :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if search is not None:
            payload["search"] = search

        # Parameter validation
        schema = ContentValidator.getCustomObjectDefinitions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}}],"optional":[{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, search=search)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition", page_no=page_no, page_size=page_size, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionsSchema
            schema = CustomObjectDefinitionsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomObjectDefinitions")
                print(e)

        return response
    
    async def getCustomObjectDefinitionBySlug(self, slug=None, request_headers:Dict={}):
        """Custom object definitions can be fetched using their custom object definition slug.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getCustomObjectDefinitionBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSlugSchema
            schema = CustomObjectDefinitionSlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomObjectDefinitionBySlug")
                print(e)

        return response
    
    async def updateCustomObjectDefinitionBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Custom object definitions can be updated using this endpoint. You can update the name and description of the custom object and add more custom field definitions to the existing custom object.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.updateCustomObjectDefinitionBySlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectDefinitionUpdateRequestSchema
        schema = CustomObjectDefinitionUpdateRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSlugSchema
            schema = CustomObjectDefinitionSlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCustomObjectDefinitionBySlug")
                print(e)

        return response
    
    async def deleteCustomObjectDefinitionBySlug(self, slug=None, request_headers:Dict={}):
        """Custom object definitions can be deleted using this endpoint by providing the definition ID.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.deleteCustomObjectDefinitionBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionDeleteResponseSchema
            schema = CustomObjectDefinitionDeleteResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCustomObjectDefinitionBySlug")
                print(e)

        return response
    
    async def getCustomObjectsBySlug(self, page_no=None, page_size=None, definition_slug=None, request_headers:Dict={}):
        """Custom object entries can fetch using this endpoint.
        :param page_no :  : type string
        :param page_size :  : type string
        :param definition_slug :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if definition_slug is not None:
            payload["definition_slug"] = definition_slug

        # Parameter validation
        schema = ContentValidator.getCustomObjectsBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{definition_slug}/entries", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, definition_slug=definition_slug)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, )
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{definition_slug}/entries", page_no=page_no, page_size=page_size, definition_slug=definition_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectsSchema
            schema = CustomObjectsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomObjectsBySlug")
                print(e)

        return response
    
    async def createCustomObjectBySlug(self, definition_slug=None, body="", request_headers:Dict={}):
        """Custom object entries against the custom object definition can be added using this API.
        :param definition_slug :  : type string
        """
        payload = {}
        
        if definition_slug is not None:
            payload["definition_slug"] = definition_slug

        # Parameter validation
        schema = ContentValidator.createCustomObjectBySlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectRequestSchemaWithoutId
        schema = CustomObjectRequestSchemaWithoutId()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{definition_slug}/entries", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", definition_slug=definition_slug)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{definition_slug}/entries", definition_slug=definition_slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectSchema
            schema = CustomObjectSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomObjectBySlug")
                print(e)

        return response
    
    async def getCustomObjectBySlug(self, definition_slug=None, slug=None, request_headers:Dict={}):
        """Details of a custom object entry can be obtained using this endpoint.
        :param definition_slug :  : type string
        :param slug :  : type string
        """
        payload = {}
        
        if definition_slug is not None:
            payload["definition_slug"] = definition_slug
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getCustomObjectBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{definition_slug}/entries/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}]}""", serverType="platform", definition_slug=definition_slug, slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{definition_slug}/entries/{slug}", definition_slug=definition_slug, slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBySlugSchema
            schema = CustomObjectBySlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomObjectBySlug")
                print(e)

        return response
    
    async def deleteCustomObjectBySlug(self, definition_slug=None, slug=None, request_headers:Dict={}):
        """Custom object entries can be deleted by providing the delete ID using this endpoint.
        :param definition_slug :  : type string
        :param slug :  : type string
        """
        payload = {}
        
        if definition_slug is not None:
            payload["definition_slug"] = definition_slug
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.deleteCustomObjectBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{definition_slug}/entries/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}]}""", serverType="platform", definition_slug=definition_slug, slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{definition_slug}/entries/{slug}", definition_slug=definition_slug, slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomDataDeleteSchema
            schema = CustomDataDeleteSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCustomObjectBySlug")
                print(e)

        return response
    
    async def updateCustomObjectBySlug(self, definition_slug=None, slug=None, body="", request_headers:Dict={}):
        """Custom object entries can be updated using this endpoint.
        :param definition_slug :  : type string
        :param slug :  : type string
        """
        payload = {}
        
        if definition_slug is not None:
            payload["definition_slug"] = definition_slug
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.updateCustomObjectBySlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectRequestSchemaWithoutId
        schema = CustomObjectRequestSchemaWithoutId()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{definition_slug}/entries/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}]}""", serverType="platform", definition_slug=definition_slug, slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{definition_slug}/entries/{slug}", definition_slug=definition_slug, slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBySlugSchema
            schema = CustomObjectBySlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCustomObjectBySlug")
                print(e)

        return response
    
    async def getJobs(self, page_no=None, page_size=None, action_type=None, request_headers:Dict={}):
        """Custom object bulk import and export jobs status and details can be obtained using this endpoint.
        :param page_no :  : type string
        :param page_size :  : type string
        :param action_type :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if action_type is not None:
            payload["action_type"] = action_type

        # Parameter validation
        schema = ContentValidator.getJobs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/jobs", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"action_type","in":"query","required":true,"schema":{"type":"string","enum":["download","upload"],"description":"This is the action type"}}],"optional":[],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"action_type","in":"query","required":true,"schema":{"type":"string","enum":["download","upload"],"description":"This is the action type"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, action_type=action_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, action_type=action_type)
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/jobs", page_no=page_no, page_size=page_size, action_type=action_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBulkEntry
            schema = CustomObjectBulkEntry()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobs")
                print(e)

        return response
    
    async def importCustomObjectEntriesBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Custom object bulk import of bulk entries can be performed using this endpoint.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.importCustomObjectEntriesBySlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectBulkSchema
        schema = CustomObjectBulkSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}/bulk/upload", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}/bulk/upload", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectEntryBulkUploadDetails
            schema = CustomObjectEntryBulkUploadDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for importCustomObjectEntriesBySlug")
                print(e)

        return response
    
    async def exportCustomObjectEntriesBySlug(self, slug=None, request_headers:Dict={}):
        """Custom object bulk export of bulk entries can be perform using this endpoint.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.exportCustomObjectEntriesBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}/bulk/download", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}/bulk/download", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBulkEntryInitiateDownload
            schema = CustomObjectBulkEntryInitiateDownload()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for exportCustomObjectEntriesBySlug")
                print(e)

        return response
    
    async def sampleCustomObjectBulkEntryBySlug(self, slug=None, request_headers:Dict={}):
        """Sample files for custom object bulk import can be obtained from this endpoint.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.sampleCustomObjectBulkEntryBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}/bulk/sample", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/customobjects/definition/{slug}/bulk/sample", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    