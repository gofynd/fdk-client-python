"""Configuration Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import ConfigurationValidator

class Configuration:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def createApplication(self, body="", request_headers:Dict={}):
        """Generate and add a new application. Applications are sales channel websites which can be configured, personalized and customized. Use this API to create a new application in the current company.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.createApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateApplicationRequest
        schema = CreateApplicationRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAppResponse
            schema = CreateAppResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createApplication")
                print(e)

        return response
    
    async def getApplications(self, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Retrieve a list of available applications. Applications are sales channel websites which can be configured, personalized and customised. Use this API to fetch a list of applications created within a company.
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param q : Search param by name or domain : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = ConfigurationValidator.getApplications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}],"optional":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"name":"page_size","schema":{"type":"integer"},"in":"query"},{"name":"q","schema":{"type":"string"},"in":"query","description":"Search param by name or domain"}],"query":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"name":"page_size","schema":{"type":"integer"},"in":"query"},{"name":"q","schema":{"type":"string"},"in":"query","description":"Search param by name or domain"}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}]}""", page_no=page_no, page_size=page_size, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationsResponse
            schema = ApplicationsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplications")
                print(e)

        return response
    
    async def getCurrencies(self, request_headers:Dict={}):
        """Retrieve a list of available currencies. Use this API to get a list of currencies allowed in the company. Moreover, get the name, code, symbol, and the decimal digits of the currencies.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getCurrencies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/currencies", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/currencies", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CurrenciesResponse
            schema = CurrenciesResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCurrencies")
                print(e)

        return response
    
    async def getDomainAvailibility(self, body="", request_headers:Dict={}):
        """Check the availability of a specific domain. Use this API to check the domain availability before linking it to application. Also sends domain suggestions that are similar to the queried domain. Note - Custom domain search is currently powered by GoDaddy provider.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getDomainAvailibility()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DomainSuggestionsRequest
        schema = DomainSuggestionsRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/domain/suggestions", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/domain/suggestions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import DomainSuggestionsResponse
            schema = DomainSuggestionsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDomainAvailibility")
                print(e)

        return response
    
    async def getIntegrationById(self, id=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific integration. Retrieve the details of an integration (such as Ginesys, SAP, etc.) using its ID.
        :param id : Integration id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration/{id}", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"404":{"value":2},"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true,"examples":{"404":{"value":"652c0a61d25ec5b4acd798c2"},"success":{"value":"6524d9e195f3c8e3d36b6977"}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"404":{"value":2},"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true,"examples":{"404":{"value":"652c0a61d25ec5b4acd798c2"},"success":{"value":"6524d9e195f3c8e3d36b6977"}}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import Integration
            schema = Integration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getIntegrationById")
                print(e)

        return response
    
    async def getAvailableOptIns(self, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve a list of available opt-ins.  Retrieve a list of all available integrations in a company. 
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ConfigurationValidator.getAvailableOptIns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/available", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/available", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetIntegrationsOptInsResponse
            schema = GetIntegrationsOptInsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAvailableOptIns")
                print(e)

        return response
    
    async def getSelectedOptIns(self, level=None, uid=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve a list of selected opt-ins. Retrieve the store-level/company-level integrations configured in a company
        :param level : store or company : type string
        :param uid : Unique identifier of the selected integration level. : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if level is not None:
            payload["level"] = level
        if uid is not None:
            payload["uid"] = uid
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ConfigurationValidator.getSelectedOptIns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/selected/{level}/{uid}", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"store or company","required":true,"examples":{"success":{"value":"store"}}},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of the selected integration level.","required":true,"examples":{"success":{"value":2}}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"store or company","required":true,"examples":{"success":{"value":"store"}}},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of the selected integration level.","required":true,"examples":{"success":{"value":2}}}]}""", level=level, uid=uid, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(level=level, uid=uid, page_no=page_no, page_size=page_size)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/selected/{level}/{uid}", level=level, uid=uid, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetIntegrationsOptInsResponse
            schema = GetIntegrationsOptInsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSelectedOptIns")
                print(e)

        return response
    
    async def getIntegrationLevelConfig(self, id=None, level=None, opted=None, check_permission=None, request_headers:Dict={}):
        """Retrieve configuration settings for integration levels. Retrieve the configuration details of an integration such as token, permissions, level, opted value, uid, meta, location ID, etc.
        :param id : Integration ID (24-digit Mongo Object ID) : type string
        :param level : store or company : type string
        :param opted : True means get the opted stores. False means get the stores that aren't opted. : type boolean
        :param check_permission : Filter on if permissions (for inventory/order) are present : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if level is not None:
            payload["level"] = level
        if opted is not None:
            payload["opted"] = opted
        if check_permission is not None:
            payload["check_permission"] = check_permission

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationLevelConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true,"examples":{"success":{"value":"6524d9e195f3c8e3d36b6977"}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"store or company","required":true,"examples":{"success":{"value":"company"}}}],"optional":[{"name":"opted","in":"query","schema":{"type":"boolean"},"description":"True means get the opted stores. False means get the stores that aren't opted.","required":false},{"name":"check_permission","in":"query","schema":{"type":"boolean"},"description":"Filter on if permissions (for inventory/order) are present","required":false}],"query":[{"name":"opted","in":"query","schema":{"type":"boolean"},"description":"True means get the opted stores. False means get the stores that aren't opted.","required":false},{"name":"check_permission","in":"query","schema":{"type":"boolean"},"description":"Filter on if permissions (for inventory/order) are present","required":false}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true,"examples":{"success":{"value":"6524d9e195f3c8e3d36b6977"}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"store or company","required":true,"examples":{"success":{"value":"company"}}}]}""", id=id, level=level, opted=opted, check_permission=check_permission)
        query_string = await create_query_string(id=id, level=level, opted=opted, check_permission=check_permission)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}", id=id, level=level, opted=opted, check_permission=check_permission), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import IntegrationConfigResponse
            schema = IntegrationConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getIntegrationLevelConfig")
                print(e)

        return response
    
    async def updateLevelIntegration(self, id=None, level=None, body="", request_headers:Dict={}):
        """Modify level integration. Update the configuration details of an integration such as token, permissions, level, opted value, uid, meta, location ID, etc. at a particular level (store/company).
        :param id : Integration ID (24-digit Mongo Object ID) : type string
        :param level : Integration level, `store` or `company` : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if level is not None:
            payload["level"] = level

        # Parameter validation
        schema = ConfigurationValidator.updateLevelIntegration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateIntegrationLevelRequest
        schema = UpdateIntegrationLevelRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true,"examples":{"success":{"value":"000000000000000000000001"}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true,"examples":{"success":{"value":"company"}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true,"examples":{"success":{"value":"000000000000000000000001"}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true,"examples":{"success":{"value":"company"}}}]}""", id=id, level=level)
        query_string = await create_query_string(id=id, level=level)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}", id=id, level=level), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import IntegrationLevel
            schema = IntegrationLevel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateLevelIntegration")
                print(e)

        return response
    
    async def getIntegrationByLevelId(self, id=None, level=None, uid=None, request_headers:Dict={}):
        """Retrieve integration details for a specific level. Retrieve the configuration details of an integration such as token, permissions, level, opted value, uid, meta, location ID, etc. at a particular level (store/company).
        :param id : Integration ID (24-digit Mongo Object ID) : type string
        :param level : Integration level, `store` or `company` : type string
        :param uid : Unique identifier of integration level (store/company) : type integer
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if level is not None:
            payload["level"] = level
        if uid is not None:
            payload["uid"] = uid

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationByLevelId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true,"examples":{"success":{"value":"6524d9e195f3c8e3d36b6977"}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true,"examples":{"success":{"value":"company"}}},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true,"examples":{"success":{"value":2}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true,"examples":{"success":{"value":"6524d9e195f3c8e3d36b6977"}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true,"examples":{"success":{"value":"company"}}},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true,"examples":{"success":{"value":2}}}]}""", id=id, level=level, uid=uid)
        query_string = await create_query_string(id=id, level=level, uid=uid)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", id=id, level=level, uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import IntegrationLevel
            schema = IntegrationLevel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getIntegrationByLevelId")
                print(e)

        return response
    
    async def updateLevelUidIntegration(self, id=None, level=None, uid=None, body="", request_headers:Dict={}):
        """Modify UID-based integration. Update the level of integration by store UID
        :param id : Integration ID (24-digit Mongo Object ID) : type string
        :param level : Integration level, `store` or `company` : type string
        :param uid : Unique identifier of integration level (store/company) : type integer
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if level is not None:
            payload["level"] = level
        if uid is not None:
            payload["uid"] = uid

        # Parameter validation
        schema = ConfigurationValidator.updateLevelUidIntegration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import IntegrationLevel
        schema = IntegrationLevel()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true,"examples":{"success":{"value":"000000000000000000000001"}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true,"examples":{"success":{"value":"company"}}},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true,"examples":{"success":{"value":2}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true,"examples":{"success":{"value":"000000000000000000000001"}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true,"examples":{"success":{"value":"company"}}},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true,"examples":{"success":{"value":2}}}]}""", id=id, level=level, uid=uid)
        query_string = await create_query_string(id=id, level=level, uid=uid)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", id=id, level=level, uid=uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import IntegrationLevel
            schema = IntegrationLevel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateLevelUidIntegration")
                print(e)

        return response
    
    async def getLevelActiveIntegrations(self, id=None, level=None, uid=None, request_headers:Dict={}):
        """Check if a store is already opted-in for any integration
        :param id : Integration ID (24-digit Mongo Object ID) : type string
        :param level : Integration level, `store` or `company` : type string
        :param uid : Unique identifier of integration level (store/company) : type integer
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if level is not None:
            payload["level"] = level
        if uid is not None:
            payload["uid"] = uid

        # Parameter validation
        schema = ConfigurationValidator.getLevelActiveIntegrations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/check/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true,"examples":{"success":{"value":"6524d9e195f3c8e3d36b6977"}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true,"examples":{"success":{"value":"company"}}},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true,"examples":{"success":{"value":11081}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true,"examples":{"success":{"value":"6524d9e195f3c8e3d36b6977"}}},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true,"examples":{"success":{"value":"company"}}},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true,"examples":{"success":{"value":11081}}}]}""", id=id, level=level, uid=uid)
        query_string = await create_query_string(id=id, level=level, uid=uid)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/check/configuration/{id}/{level}/{uid}", id=id, level=level, uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import OptedStoreIntegration
            schema = OptedStoreIntegration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLevelActiveIntegrations")
                print(e)

        return response
    
    async def getBrandsByCompany(self, q=None, request_headers:Dict={}):
        """Retrieve all the brands added in a company. Get all the brand names, along with URLs of their logo, banner, and portrait image.
        :param q : Search text for brand name : type string
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = ConfigurationValidator.getBrandsByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/brands-by-companies", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}],"optional":[{"name":"q","in":"query","schema":{"type":"string"},"description":"Search text for brand name"}],"query":[{"name":"q","in":"query","schema":{"type":"string"},"description":"Search text for brand name"}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}]}""", q=q)
        query_string = await create_query_string(q=q)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/brands-by-companies", q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import BrandsByCompanyResponse
            schema = BrandsByCompanyResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBrandsByCompany")
                print(e)

        return response
    
    async def getCompanyByBrands(self, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Retrieve companies associated with specific brands. Retrieve a list of companies by the brands they deal.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ConfigurationValidator.getCompanyByBrands()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CompanyByBrandsRequest
        schema = CompanyByBrandsRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/companies-by-brands", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/companies-by-brands", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyByBrandsResponse
            schema = CompanyByBrandsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCompanyByBrands")
                print(e)

        return response
    
    async def getStoreByBrands(self, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Retrieve stores associated with specific brands. Retrieve a list of selling locations (stores) by the brands they deal. Store has information about store name, store type, store code, store address, and company detail.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ConfigurationValidator.getStoreByBrands()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StoreByBrandsRequest
        schema = StoreByBrandsRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/stores-by-brands", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/stores-by-brands", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreByBrandsResponse
            schema = StoreByBrandsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStoreByBrands")
                print(e)

        return response
    
    async def getOtherSellerApplications(self, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve applications from other sellers. Retrieve all other seller applications that were not created within the current company. but have opted for the current company's inventory.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ConfigurationValidator.getOtherSellerApplications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"success":{"value":2}}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import OtherSellerApplications
            schema = OtherSellerApplications()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOtherSellerApplications")
                print(e)

        return response
    
    async def getOtherSellerApplicationById(self, id=None, request_headers:Dict={}):
        """Retrieve details of a seller application that was not created within the current company. but has opted for the current company's inventory
        :param id : Application Id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ConfigurationValidator.getOtherSellerApplicationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"404":{"value":2},"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true,"examples":{"404":{"value":"000000000000000000000005"},"success":{"value":"000000000000000000000001"}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"404":{"value":2},"success":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true,"examples":{"404":{"value":"000000000000000000000005"},"success":{"value":"000000000000000000000001"}}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import OptedApplicationResponse
            schema = OptedApplicationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOtherSellerApplicationById")
                print(e)

        return response
    
    async def optOutFromApplication(self, id=None, body="", request_headers:Dict={}):
        """Choose to opt-out your company or store from other seller application. The specific seller application will no longer fetch inventory from your company or store.
        :param id : Alphanumeric ID allotted to an application (sales channel website) created within a business account. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ConfigurationValidator.optOutFromApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OptOutInventory
        schema = OptOutInventory()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}/opt_out", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"404":{"value":2},"success":{"value":2},"Missing parameter":{"value":2},"Company other than current company sent for opt out":{"value":2},"Store other than current company sent for opt out":{"value":2},"Inventory not configured for sent application id":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account.","required":true,"examples":{"404":{"value":"000000000000000000000005"},"success":{"value":"000000000000000000000001"},"Missing parameter":{"value":"000000000000000000000001"},"Company other than current company sent for opt out":{"value":"000000000000000000000001"},"Store other than current company sent for opt out":{"value":"000000000000000000000001"},"Inventory not configured for sent application id":{"value":"000000000000000000000002"}}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id","examples":{"404":{"value":2},"success":{"value":2},"Missing parameter":{"value":2},"Company other than current company sent for opt out":{"value":2},"Store other than current company sent for opt out":{"value":2},"Inventory not configured for sent application id":{"value":2}}},{"name":"id","in":"path","schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account.","required":true,"examples":{"404":{"value":"000000000000000000000005"},"success":{"value":"000000000000000000000001"},"Missing parameter":{"value":"000000000000000000000001"},"Company other than current company sent for opt out":{"value":"000000000000000000000001"},"Store other than current company sent for opt out":{"value":"000000000000000000000001"},"Inventory not configured for sent application id":{"value":"000000000000000000000002"}}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}/opt_out", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessageResponse
            schema = SuccessMessageResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for optOutFromApplication")
                print(e)

        return response
    