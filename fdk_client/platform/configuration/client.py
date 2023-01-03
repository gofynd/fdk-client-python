

""" Configuration Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import ConfigurationValidator

class Configuration:
    def __init__(self, config):
        self._conf = config
    
    async def createApplication(self, body=""):
        """Applications are sales channel websites which can be configured, personalized and customized. Use this API to create a new application in the current company.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.createApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateApplicationRequest import CreateApplicationRequest
        schema = CreateApplicationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getApplications(self, page_no=None, page_size=None, q=None):
        """Applications are sales channel websites which can be configured, personalized and customised. Use this API to fetch a list of applications created within a company.
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param q : Url encoded object used as mongodb query : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ConfigurationValidator.getApplications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"name":"page_size","schema":{"type":"integer"},"in":"query"},{"name":"q","schema":{"type":"string"},"in":"query","description":"Url encoded object used as mongodb query"}],"query":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"name":"page_size","schema":{"type":"integer"},"in":"query"},{"name":"q","schema":{"type":"string"},"in":"query","description":"Url encoded object used as mongodb query"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", page_no=page_no, page_size=page_size, q=q)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCurrencies(self, ):
        """Use this API to get a list of currencies allowed in the company. Moreover, get the name, code, symbol, and the decimal digits of the currencies.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getCurrencies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/currencies", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/currencies", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getDomainAvailibility(self, body=""):
        """Use this API to check the domain availability before linking it to application. Also sends domain suggestions that are similar to the queried domain. Note - Custom domain search is currently powered by GoDaddy provider.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getDomainAvailibility()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DomainSuggestionsRequest import DomainSuggestionsRequest
        schema = DomainSuggestionsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/domain/suggestions", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/domain/suggestions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getIntegrationById(self, id=None):
        """Use this API to fetch the details of an integration (such as Ginesys, SAP, etc.) using its ID
        :param id : Integration id : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration/{id}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"integer"},"description":"Integration id","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"integer"},"description":"Integration id","required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getAvailableOptIns(self, page_no=None, page_size=None):
        """Use this API to get a list of all available integrations in a company
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getAvailableOptIns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/available", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", page_no=page_no, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/available", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSelectedOptIns(self, level=None, uid=None, page_no=None, page_size=None):
        """Use this API to get the store-level/company-level integrations configured in a company
        :param level : store or company : type string
        :param uid : Unique identifier of the selected integration level. : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getSelectedOptIns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/selected/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"level","in":"path","schema":{"type":"string"},"description":"store or company","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of the selected integration level.","required":true}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"level","in":"path","schema":{"type":"string"},"description":"store or company","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of the selected integration level.","required":true}]}""", level=level, uid=uid, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(level=level, uid=uid, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/selected/{level}/{uid}", level=level, uid=uid, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getIntegrationLevelConfig(self, id=None, level=None, opted=None, check_permission=None):
        """Get integration/integration-opt-in level config
        :param id : Integration id : type string
        :param level : Integration level : type string
        :param opted : Filter on opted stores : type boolean
        :param check_permission : Filter on if permissions are present : type boolean
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if opted:
            payload["opted"] = opted
        
        if check_permission:
            payload["check_permission"] = check_permission
        

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationLevelConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/new/{id}/{level}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true}],"optional":[{"name":"opted","in":"query","schema":{"type":"boolean"},"description":"Filter on opted stores","required":false},{"name":"check_permission","in":"query","schema":{"type":"boolean"},"description":"Filter on if permissions are present","required":false}],"query":[{"name":"opted","in":"query","schema":{"type":"boolean"},"description":"Filter on opted stores","required":false},{"name":"check_permission","in":"query","schema":{"type":"boolean"},"description":"Filter on if permissions are present","required":false}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true}]}""", id=id, level=level, opted=opted, check_permission=check_permission)
        query_string = await create_query_string(id=id, level=level, opted=opted, check_permission=check_permission)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/new/{id}/{level}", id=id, level=level, opted=opted, check_permission=check_permission), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getIntegrationByLevelId(self, id=None, level=None, uid=None):
        """Use this API to get the configuration details of an integration such as token, permissions, level, opted value, uid, meta, location ID, etc. at a particular level (store/company).
        :param id : Integration ID (24-digit Mongo Object ID) : type string
        :param level : Integration level, `store` or `company` : type string
        :param uid : Unique identifier of integration level (store/company) : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationByLevelId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true}]}""", id=id, level=level, uid=uid)
        query_string = await create_query_string(id=id, level=level, uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", id=id, level=level, uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateLevelUidIntegration(self, id=None, level=None, uid=None, body=""):
        """Update the level of integration by store UID
        :param id : Integration ID (24-digit Mongo Object ID) : type string
        :param level : Integration level, `store` or `company` : type string
        :param uid : Unique identifier of integration level (store/company) : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = ConfigurationValidator.updateLevelUidIntegration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.IntegrationLevel import IntegrationLevel
        schema = IntegrationLevel()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true}]}""", id=id, level=level, uid=uid)
        query_string = await create_query_string(id=id, level=level, uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", id=id, level=level, uid=uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getLevelActiveIntegrations(self, id=None, level=None, uid=None, permission=None):
        """Use this API to check if a store is already opted-in for any integration
        :param id : Integration ID (24-digit Mongo Object ID) : type string
        :param level : Integration level, `store` or `company` : type string
        :param uid : Unique identifier of integration level (store/company) : type integer
        :param permission : Check opt-in for specific integration permissions : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        
        if permission:
            payload["permission"] = permission
        

        # Parameter validation
        schema = ConfigurationValidator.getLevelActiveIntegrations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/check/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true}],"optional":[{"name":"permission","in":"query","schema":{"type":"string"},"description":"Check opt-in for specific integration permissions","required":false}],"query":[{"name":"permission","in":"query","schema":{"type":"string"},"description":"Check opt-in for specific integration permissions","required":false}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Unique identifier of integration level (store/company)","required":true}]}""", id=id, level=level, uid=uid, permission=permission)
        query_string = await create_query_string(id=id, level=level, uid=uid, permission=permission)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/check/configuration/{id}/{level}/{uid}", id=id, level=level, uid=uid, permission=permission), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateLevelIntegration(self, id=None, level=None, body=""):
        """Use this API to update the configuration details of an integration such as token, permissions, level, opted value, uid, meta, location ID, etc. at a particular level (store/company).
        :param id : Integration ID (24-digit Mongo Object ID) : type string
        :param level : Integration level, `store` or `company` : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        

        # Parameter validation
        schema = ConfigurationValidator.updateLevelIntegration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateIntegrationLevelRequest import UpdateIntegrationLevelRequest
        schema = UpdateIntegrationLevelRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration ID (24-digit Mongo Object ID)","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level, `store` or `company`","required":true}]}""", id=id, level=level)
        query_string = await create_query_string(id=id, level=level)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}", id=id, level=level), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getBrandsByCompany(self, q=None):
        """Use this API to get all the brands added in a company. Get all the brand names, along with URLs of their logo, banner, and portrait image.
        :param q : Search text for brand name : type string
        """
        payload = {}
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ConfigurationValidator.getBrandsByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/brands-by-companies", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"q","in":"query","schema":{"type":"string"},"description":"Search text for brand name"}],"query":[{"name":"q","in":"query","schema":{"type":"string"},"description":"Search text for brand name"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", q=q)
        query_string = await create_query_string(q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/brands-by-companies", q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCompanyByBrands(self, page_no=None, page_size=None, body=""):
        """Use this API to get a list of companies by the brands they deal
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getCompanyByBrands()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CompanyByBrandsRequest import CompanyByBrandsRequest
        schema = CompanyByBrandsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/companies-by-brands", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", page_no=page_no, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/companies-by-brands", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getStoreByBrands(self, page_no=None, page_size=None, body=""):
        """Use this API to get a list of selling locations (stores) by the brands they deal. Store has information about store name, store type, store code, store address, and company detail.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getStoreByBrands()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.StoreByBrandsRequest import StoreByBrandsRequest
        schema = StoreByBrandsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/stores-by-brands", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", page_no=page_no, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/stores-by-brands", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getOtherSellerApplications(self, page_no=None, page_size=None):
        """Use this API to fetch all other seller applications that were not created within the current company. but have opted for the current company's inventory
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getOtherSellerApplications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", page_no=page_no, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOtherSellerApplicationById(self, id=None):
        """Use application ID to fetch details of a seller application that was not created within the current company. but has opted for the current company's inventory
        :param id : Application Id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.getOtherSellerApplicationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def optOutFromApplication(self, id=None, body=""):
        """Use this API to opt-out your company or store from other seller application. The specific seller application will no longer fetch inventory from your company or store.
        :param id : Alphanumeric ID allotted to an application (sales channel website) created within a business account. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.optOutFromApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OptOutInventory import OptOutInventory
        schema = OptOutInventory()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}/opt_out", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account.","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account.","required":true}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}/opt_out", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

