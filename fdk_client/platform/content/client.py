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
            from .models import CustomObjectByIdSchema
            schema = CustomObjectByIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFieldTypes")
                print(e)

        return response
    
    async def getResources(self, request_headers:Dict={}):
        """Each custom fields is assosiated with a resource such as product, promotion, coupon, selling location etc, This will gives list of supported resource list.
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
    
    async def getCustomFieldDefinitions(self, page_no=None, page_size=None, resource=None, type=None, search=None, request_headers:Dict={}):
        """Custom field definitions enable you to include data validation for custom fields, and enable sellers to add custom fields values for resources. With the help of this seller can retrive list of custom field definitions list.
        :param page_no :  : type string
        :param page_size :  : type string
        :param resource :  : type string
        :param type :  : type string
        :param search :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if resource is not None:
            payload["resource"] = resource
        if type is not None:
            payload["type"] = type
        if search is not None:
            payload["search"] = search

        # Parameter validation
        schema = ContentValidator.getCustomFieldDefinitions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}}],"optional":[{"name":"resource","in":"query","required":false,"schema":{"type":"string","description":"This is the resource for which we are fetching definitions"}},{"name":"type","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"resource","in":"query","required":false,"schema":{"type":"string","description":"This is the resource for which we are fetching definitions"}},{"name":"type","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, resource=resource, type=type, search=search)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, resource=resource, type=type, search=search)
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions", page_no=page_no, page_size=page_size, resource=resource, type=type, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionsSchema
            schema = CustomFieldDefinitionsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFieldDefinitions")
                print(e)

        return response
    
    async def createCustomFieldDefinition(self, body="", request_headers:Dict={}):
        """You can create custom fields definition to any resource so you can extend property of resource.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createCustomFieldDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldDefinitionRequestSchema
        schema = CustomFieldDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionDetailResSchema
            schema = CustomFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomFieldDefinition")
                print(e)

        return response
    
    async def getCustomFieldDefinition(self, definition_id=None, request_headers:Dict={}):
        """Custom field definitions can be fetch using definition id.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.getCustomFieldDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}]}""", serverType="platform", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions/{definition_id}", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionDetailResSchema
            schema = CustomFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFieldDefinition")
                print(e)

        return response
    
    async def updateCustomFieldDefinition(self, definition_id=None, body="", request_headers:Dict={}):
        """Custom fields definition can be update using this api, You can update custom field definition name and description.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.updateCustomFieldDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldDefinitionRequestSchema
        schema = CustomFieldDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}]}""", serverType="platform", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions/{definition_id}", definition_id=definition_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionDetailResSchema
            schema = CustomFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCustomFieldDefinition")
                print(e)

        return response
    
    async def deleteCustomFieldDefinition(self, definition_id=None, request_headers:Dict={}):
        """Custom field definition and its assosiated custom fields value can be deleted using this api on the basis of definition id.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.deleteCustomFieldDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}]}""", serverType="platform", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions/{definition_id}", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomDataDeleteSchema
            schema = CustomDataDeleteSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCustomFieldDefinition")
                print(e)

        return response
    
    async def getCustomFields(self, resource=None, request_headers:Dict={}):
        """Retrieves a list of custom fields attached to a particular resource by using the resource.
        :param resource :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource

        # Parameter validation
        schema = ContentValidator.getCustomFields()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/{resource}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."}}]}""", serverType="platform", resource=resource)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/{resource}", resource=resource), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldsResponseSchema
            schema = CustomFieldsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFields")
                print(e)

        return response
    
    async def getCustomFieldsByResourceId(self, resource=None, resource_id=None, request_headers:Dict={}):
        """Retrieves a list of custom fields attached to a particular resource by using the resource and resource id.
        :param resource :  : type string
        :param resource_id :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource
        if resource_id is not None:
            payload["resource_id"] = resource_id

        # Parameter validation
        schema = ContentValidator.getCustomFieldsByResourceId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/{resource}/{resource_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"}}]}""", serverType="platform", resource=resource, resource_id=resource_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/{resource}/{resource_id}", resource=resource, resource_id=resource_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldsResponseByResourceIdSchema
            schema = CustomFieldsResponseByResourceIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFieldsByResourceId")
                print(e)

        return response
    
    async def createCustomFieldByResourceId(self, resource=None, resource_id=None, body="", request_headers:Dict={}):
        """You can add a custom field using this endpoint to any resource by providing the resource ID.
        :param resource :  : type string
        :param resource_id :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource
        if resource_id is not None:
            payload["resource_id"] = resource_id

        # Parameter validation
        schema = ContentValidator.createCustomFieldByResourceId()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldRequestSchema
        schema = CustomFieldRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/{resource}/{resource_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"}}]}""", serverType="platform", resource=resource, resource_id=resource_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/{resource}/{resource_id}", resource=resource, resource_id=resource_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldsResponseByResourceIdSchema
            schema = CustomFieldsResponseByResourceIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomFieldByResourceId")
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSchema
            schema = CustomObjectDefinitionSchema()
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}}],"optional":[{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, search=search)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions", page_no=page_no, page_size=page_size, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionsSchema
            schema = CustomObjectDefinitionsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomObjectDefinitions")
                print(e)

        return response
    
    async def getCustomObjectDefinition(self, definition_id=None, request_headers:Dict={}):
        """Custom object definitions can be fetched using their definition ID.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.getCustomObjectDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}]}""", serverType="platform", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions/{definition_id}", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSchema
            schema = CustomObjectDefinitionSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomObjectDefinition")
                print(e)

        return response
    
    async def updateCustomObjectDefinition(self, definition_id=None, body="", request_headers:Dict={}):
        """Custom object definitions can be updated using this endpoint. You can update the name and description of the custom object and add more custom field definitions to the existing custom object.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.updateCustomObjectDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectDefinitionUpdateRequestSchema
        schema = CustomObjectDefinitionUpdateRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}]}""", serverType="platform", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions/{definition_id}", definition_id=definition_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSchema
            schema = CustomObjectDefinitionSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCustomObjectDefinition")
                print(e)

        return response
    
    async def deleteCustomObjectDefinition(self, definition_id=None, request_headers:Dict={}):
        """Custom object definitions can be deleted using this endpoint by providing the definition ID.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.deleteCustomObjectDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}]}""", serverType="platform", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions/{definition_id}", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionDeleteResponseSchema
            schema = CustomObjectDefinitionDeleteResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCustomObjectDefinition")
                print(e)

        return response
    
    async def getCustomObjects(self, definition_id=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Custom object entries can fetch using this endpoint.
        :param definition_id :  : type string
        :param page_no :  : type string
        :param page_size :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getCustomObjects()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}}],"optional":[{"name":"definition_id","in":"query","required":false,"schema":{"type":"string","description":"This is definition id"}}],"query":[{"name":"definition_id","in":"query","required":false,"schema":{"type":"string","description":"This is definition id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", definition_id=definition_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(definition_id=definition_id, page_no=page_no, page_size=page_size)
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects", definition_id=definition_id, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectsSchema
            schema = CustomObjectsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomObjects")
                print(e)

        return response
    
    async def createCustomObject(self, body="", request_headers:Dict={}):
        """Custom object entries against the custom object definition can be added using this API.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createCustomObject()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectRequestSchema
        schema = CustomObjectRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectSchema
            schema = CustomObjectSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomObject")
                print(e)

        return response
    
    async def getCustomObject(self, metaobject_id=None, request_headers:Dict={}):
        """Details of custom objects, their field details, definitions, and references can be obtained using this endpoint.
        :param metaobject_id :  : type string
        """
        payload = {}
        
        if metaobject_id is not None:
            payload["metaobject_id"] = metaobject_id

        # Parameter validation
        schema = ContentValidator.getCustomObject()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/{metaobject_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"}}]}""", serverType="platform", metaobject_id=metaobject_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/{metaobject_id}", metaobject_id=metaobject_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectByIdSchema
            schema = CustomObjectByIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomObject")
                print(e)

        return response
    
    async def deleteCustomObject(self, metaobject_id=None, request_headers:Dict={}):
        """Custom object entries can be deleted by providing the delete ID using this endpoint.
        :param metaobject_id :  : type string
        """
        payload = {}
        
        if metaobject_id is not None:
            payload["metaobject_id"] = metaobject_id

        # Parameter validation
        schema = ContentValidator.deleteCustomObject()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/{metaobject_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"}}]}""", serverType="platform", metaobject_id=metaobject_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/{metaobject_id}", metaobject_id=metaobject_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomDataDeleteSchema
            schema = CustomDataDeleteSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCustomObject")
                print(e)

        return response
    
    async def updateCustomObject(self, metaobject_id=None, body="", request_headers:Dict={}):
        """Custom object entries can be updated using this endpoint.
        :param metaobject_id :  : type string
        """
        payload = {}
        
        if metaobject_id is not None:
            payload["metaobject_id"] = metaobject_id

        # Parameter validation
        schema = ContentValidator.updateCustomObject()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectRequestSchema
        schema = CustomObjectRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/{metaobject_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"}}]}""", serverType="platform", metaobject_id=metaobject_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/{metaobject_id}", metaobject_id=metaobject_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectByIdSchema
            schema = CustomObjectByIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCustomObject")
                print(e)

        return response
    
    async def getJobs(self, page=None, page_size=None, action_type=None, request_headers:Dict={}):
        """Custom object bulk import and export jobs status and details can be obtained using this endpoint.
        :param page :  : type string
        :param page_size :  : type string
        :param action_type :  : type string
        """
        payload = {}
        
        if page is not None:
            payload["page"] = page
        if page_size is not None:
            payload["page_size"] = page_size
        if action_type is not None:
            payload["action_type"] = action_type

        # Parameter validation
        schema = ContentValidator.getJobs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/jobs", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"page","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"action_type","in":"query","required":true,"schema":{"type":"string","description":"This is the action type"}}],"optional":[],"query":[{"name":"page","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"action_type","in":"query","required":true,"schema":{"type":"string","description":"This is the action type"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}}]}""", serverType="platform", page=page, page_size=page_size, action_type=action_type)
        query_string = await create_query_string(page=page, page_size=page_size, action_type=action_type)
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/jobs", page=page, page_size=page_size, action_type=action_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBulkEntry
            schema = CustomObjectBulkEntry()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobs")
                print(e)

        return response
    
    async def importCustomObjectEntries(self, definition_id=None, body="", request_headers:Dict={}):
        """Custom object bulk import of bulk entries can be performed using this endpoint.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.importCustomObjectEntries()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectBulkSchema
        schema = CustomObjectBulkSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/bulk/{definition_id}/upload", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}]}""", serverType="platform", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/bulk/{definition_id}/upload", definition_id=definition_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectEntryBulkUploadResponse
            schema = CustomObjectEntryBulkUploadResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for importCustomObjectEntries")
                print(e)

        return response
    
    async def exportCustomObjectEntries(self, definition_id=None, request_headers:Dict={}):
        """Custom object bulk export of bulk entries can be perform using this endpoint.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.exportCustomObjectEntries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/bulk/{definition_id}/download", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}]}""", serverType="platform", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/bulk/{definition_id}/download", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBulkEntryInitiateDownload
            schema = CustomObjectBulkEntryInitiateDownload()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for exportCustomObjectEntries")
                print(e)

        return response
    
    async def sampleCustomObjectBulkEntry(self, definition_id=None, request_headers:Dict={}):
        """Sample files for custom object bulk import can be obtained from this endpoint.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.sampleCustomObjectBulkEntry()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/bulk/{definition_id}/sample", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}]}""", serverType="platform", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/bulk/{definition_id}/sample", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    