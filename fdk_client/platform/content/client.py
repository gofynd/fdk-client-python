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
        """Use this API to retrieve the custom field types 
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getCustomFieldTypes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/types", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}]}""", serverType="platform", )
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
        """Use this API to retrieve the resources, such as products, collections, customers, selling locations, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getResources()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/resources", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}]}""", serverType="platform", )
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
        """Use this API to retrieve the definitions of custom fields.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}}],"optional":[{"name":"resource","in":"query","required":false,"schema":{"type":"string","description":"This is the resource for which we are fetching definitions"},"examples":{"success":{"value":"product"},"failure":{"value":"some"}}},{"name":"type","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"},"examples":{"success":{"value":"string_single_line"},"failure":{"value":"string_single"}}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"},"examples":{"success":{"value":"sometext"},"failure":{"value":"sometext"}}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}},{"name":"resource","in":"query","required":false,"schema":{"type":"string","description":"This is the resource for which we are fetching definitions"},"examples":{"success":{"value":"product"},"failure":{"value":"some"}}},{"name":"type","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"},"examples":{"success":{"value":"string_single_line"},"failure":{"value":"string_single"}}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"},"examples":{"success":{"value":"sometext"},"failure":{"value":"sometext"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}]}""", serverType="platform", page_no=page_no, page_size=page_size, resource=resource, type=type, search=search)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, resource=resource, type=type, search=search)

        headers = {}
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
        """Use this API to create a custom field definition for your application.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createCustomFieldDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldDefinitionRequestSchema
        schema = CustomFieldDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}]}""", serverType="platform", )
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
        """Use this API to retrieve the definitions of custom fields using definition_id.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.getCustomFieldDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", definition_id=definition_id)
        query_string = await create_query_string(definition_id=definition_id)

        headers = {}
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
        """Use this API to update a custom field definition for your application.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", definition_id=definition_id)
        query_string = await create_query_string(definition_id=definition_id)

        headers = {}
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
        """Use this API to delete the definitions of custom fields using definition_id. This will also delete related custom fields entries related to this definition.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.deleteCustomFieldDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", definition_id=definition_id)
        query_string = await create_query_string(definition_id=definition_id)

        headers = {}
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
        """Use this API to retrieve the custom fields for given resource in param.
        :param resource :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource

        # Parameter validation
        schema = ContentValidator.getCustomFields()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/{resource}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}}]}""", serverType="platform", resource=resource)
        query_string = await create_query_string(resource=resource)

        headers = {}
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
        """Use this API to retrieve the custom fields for given resource in param.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/{resource}/{resource_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"},"examples":{"success":{"value":"64bb987e9a3c4b6c29d676bc"},"failure":{"value":"64bb987e9a3c4b6c29d67eee"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"},"examples":{"success":{"value":"64bb987e9a3c4b6c29d676bc"},"failure":{"value":"64bb987e9a3c4b6c29d67eee"}}}]}""", serverType="platform", resource=resource, resource_id=resource_id)
        query_string = await create_query_string(resource=resource, resource_id=resource_id)

        headers = {}
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
        """Use this API to create the custom field entry for given resource and resource_id in param.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metafields/{resource}/{resource_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"},"examples":{"success":{"value":"64bb987e9a3c4b6c29d676bc"},"failure":{"value":"64bb987e9a3c4b6c29d67eee"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"},"examples":{"success":{"value":"64bb987e9a3c4b6c29d676bc"},"failure":{"value":"64bb987e9a3c4b6c29d67eee"}}}]}""", serverType="platform", resource=resource, resource_id=resource_id)
        query_string = await create_query_string(resource=resource, resource_id=resource_id)

        headers = {}
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
        """Use this API to create custom object defintion
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createCustomObjectDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectDefinitionRequestSchema
        schema = CustomObjectDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}]}""", serverType="platform", )
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
        """Use this API to retrieve the custom object definitions
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}}],"optional":[{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"},"examples":{"success":{"value":"sometext"},"failure":{"value":"sometext"}}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"},"examples":{"success":{"value":"sometext"},"failure":{"value":"sometext"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}]}""", serverType="platform", page_no=page_no, page_size=page_size, search=search)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, search=search)

        headers = {}
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
        """Use this API to update a custom object definition for your application.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.getCustomObjectDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", definition_id=definition_id)
        query_string = await create_query_string(definition_id=definition_id)

        headers = {}
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
        """Use this API to update a custom object definition for your application.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", definition_id=definition_id)
        query_string = await create_query_string(definition_id=definition_id)

        headers = {}
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
        """Use this API to delete a custom object definition and related data for your application.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.deleteCustomObjectDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", definition_id=definition_id)
        query_string = await create_query_string(definition_id=definition_id)

        headers = {}
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
        """Use this API to retrieve the custom objects.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}}],"optional":[{"name":"definition_id","in":"query","required":false,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"query":[{"name":"definition_id","in":"query","required":false,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}]}""", serverType="platform", definition_id=definition_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(definition_id=definition_id, page_no=page_no, page_size=page_size)

        headers = {}
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
        """Use this API to create the custom object entry.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createCustomObject()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectRequestSchema
        schema = CustomObjectRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}]}""", serverType="platform", )
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
        """Use this API to retrieve the custom object details and their fields details and definitions and references.
        :param metaobject_id :  : type string
        """
        payload = {}
        
        if metaobject_id is not None:
            payload["metaobject_id"] = metaobject_id

        # Parameter validation
        schema = ContentValidator.getCustomObject()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/{metaobject_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", metaobject_id=metaobject_id)
        query_string = await create_query_string(metaobject_id=metaobject_id)

        headers = {}
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
        """Use this API to delete the custom object entry by id. This will also delete related custom fields entries related to this custom object.
        :param metaobject_id :  : type string
        """
        payload = {}
        
        if metaobject_id is not None:
            payload["metaobject_id"] = metaobject_id

        # Parameter validation
        schema = ContentValidator.deleteCustomObject()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/{metaobject_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", metaobject_id=metaobject_id)
        query_string = await create_query_string(metaobject_id=metaobject_id)

        headers = {}
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
        """Use this API to update a custom object detail for your application.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/{metaobject_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", metaobject_id=metaobject_id)
        query_string = await create_query_string(metaobject_id=metaobject_id)

        headers = {}
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
        """Use this api to get list of jobs of bulk import and exports
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/jobs", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"page","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}},{"name":"action_type","in":"query","required":true,"schema":{"type":"string","description":"This is the action type"},"examples":{"success":{"value":"upload"},"failure":{"value":"upload"}}}],"optional":[],"query":[{"name":"page","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}},{"name":"action_type","in":"query","required":true,"schema":{"type":"string","description":"This is the action type"},"examples":{"success":{"value":"upload"},"failure":{"value":"upload"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}}]}""", serverType="platform", page=page, page_size=page_size, action_type=action_type)
        query_string = await create_query_string(page=page, page_size=page_size, action_type=action_type)

        headers = {}
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
        """Use this API to upload custom object entries
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/bulk/{definition_id}/upload", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", definition_id=definition_id)
        query_string = await create_query_string(definition_id=definition_id)

        headers = {}
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
        """Use this api to initiate download of bulk entries
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.exportCustomObjectEntries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/bulk/{definition_id}/download", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", definition_id=definition_id)
        query_string = await create_query_string(definition_id=definition_id)

        headers = {}
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
        """Use this api to get sample csv file 
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.sampleCustomObjectBulkEntry()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/metaobjects/bulk/{definition_id}/sample", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", serverType="platform", definition_id=definition_id)
        query_string = await create_query_string(definition_id=definition_id)

        headers = {}
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
    