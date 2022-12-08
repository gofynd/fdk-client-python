

"""Configuration Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import ConfigurationValidator

class Configuration:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getBuildConfig(self, platform_type=None):
        """Fetch latest build configuration, such as app name, landing page image, splash image used in a mobile build.
        :param platform_type : The device platform for which the mobile app was built, e.g. android, ios. : type string
        """
        payload = {}
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.getBuildConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app was built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app was built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}]}""", platform_type=platform_type)
        query_string = await create_query_string(platform_type=platform_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", platform_type=platform_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateBuildConfig(self, platform_type=None, body=""):
        """It Updates the build configuration for next build. It updates the details such as app name, landing page image, splash image used in a mobile build.
        :param platform_type : The device current platform name for which the app was built, e.g. android, ios. : type string
        """
        payload = {}
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.updateBuildConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.MobileAppConfigRequest import MobileAppConfigRequest
        schema = MobileAppConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device current platform name for which the app was built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device current platform name for which the app was built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}]}""", platform_type=platform_type)
        query_string = await create_query_string(platform_type=platform_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", platform_type=platform_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getPreviousVersions(self, platform_type=None):
        """It gives previous build versions info. It contains the details about platform type, build status, version name, and version code in previous build versions.
Builed status - It shows application build status. Build status can be pending or cancelled or failed or success.
    * pending
    * cancelled
    * failed
    * success

        :param platform_type : The device current platform name for which the app was built, e.g. android, ios. : type string
        """
        payload = {}
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.getPreviousVersions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/versions", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device current platform name for which the app was built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device current platform name for which the app was built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}]}""", platform_type=platform_type)
        query_string = await create_query_string(platform_type=platform_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/versions", platform_type=platform_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getAppFeatures(self, ):
        """It gives the features of sales channel. Moreover, get the details about product details, landing page, registration page, home page, listing page, reward points and many more properties.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppFeatures()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateAppFeatures(self, body=""):
        """It saves or Updates the features of sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppFeatures()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AppFeatureRequest import AppFeatureRequest
        schema = AppFeatureRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAppBasicDetails(self, ):
        """Get basic sales channel details like name, description, logo, domain ,company id and other related information.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppBasicDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateAppBasicDetails(self, body=""):
        """Add or update sales channel basic details like name, description, logo, domain ,company id and other information.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppBasicDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ApplicationDetail import ApplicationDetail
        schema = ApplicationDetail()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAppContactInfo(self, ):
        """Get sales channel Current Information. This includes information about social links, address and contact information of company/seller/brand of the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppContactInfo()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateAppContactInfo(self, body=""):
        """Save or update the sales channel current information. This includes information about social links, address and contact information of an application.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppContactInfo()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ApplicationInformation import ApplicationInformation
        schema = ApplicationInformation()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAppApiTokens(self, ):
        """Get social tokens for the sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppApiTokens()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateAppApiTokens(self, body=""):
        """Add social tokens for the sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppApiTokens()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.TokenResponse import TokenResponse
        schema = TokenResponse()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAppCompanies(self, uid=None, page_no=None, page_size=None):
        """Get sales channel inventory enabled companies. Company has information about company name, uid and company type.
        :param uid : uid of companies to be fetched : type integer
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getAppCompanies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/companies", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"uid","in":"query","schema":{"type":"integer"},"description":"uid of companies to be fetched"},{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"uid","in":"query","schema":{"type":"integer"},"description":"uid of companies to be fetched"},{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", uid=uid, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(uid=uid, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/companies", uid=uid, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getAppStores(self, page_no=None, page_size=None):
        """Get sales channel inventory enabled stores. Inventory enabled store has information about uid, name, display name, store type, store code and company id.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getAppStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stores", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stores", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getInventoryConfig(self, ):
        """Get sales channel configuration for various features and data
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getInventoryConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateInventoryConfig(self, body=""):
        """Update sales channel configuration for various features and data
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateInventoryConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ApplicationInventory import ApplicationInventory
        schema = ApplicationInventory()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def partiallyUpdateInventoryConfig(self, body=""):
        """Partially update sales channel configuration for various features and data
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.partiallyUpdateInventoryConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AppInventoryPartialUpdate import AppInventoryPartialUpdate
        schema = AppInventoryPartialUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAppCurrencyConfig(self, ):
        """It gives all enabled currency list for the current sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppCurrencyConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateAppCurrencyConfig(self, body=""):
        """Update sales channel supported currency for various features and data. Default INR will be enabled.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppCurrencyConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AppSupportedCurrency import AppSupportedCurrency
        schema = AppSupportedCurrency()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAppSupportedCurrency(self, ):
        """Use this API to get a list of currencies allowed in the current application. Moreover, get the name, code, symbol, and the decimal digits of the currencies.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppSupportedCurrency()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency/supported", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency/supported", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOrderingStoresByFilter(self, page_no=None, page_size=None, body=""):
        """Get ordering store from all stores by filter
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getOrderingStoresByFilter()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.FilterOrderingStoreRequest import FilterOrderingStoreRequest
        schema = FilterOrderingStoreRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/stores/filter", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/stores/filter", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateOrderingStoreConfig(self, body=""):
        """Add/Update ordering store config.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateOrderingStoreConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OrderingStoreConfig import OrderingStoreConfig
        schema = OrderingStoreConfig()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getStaffOrderingStores(self, page_no=None, page_size=None, q=None):
        """Use this API to retrieve the details of all stores access given to the staff member (the selling locations where the application will be utilized for placing orders).
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param q : Store code or name of the ordering store. : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ConfigurationValidator.getStaffOrderingStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/staff-stores", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size, q=q)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/staff-stores", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getDomains(self, ):
        """Gives the domains list attached with the current sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getDomains()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def addDomain(self, body=""):
        """Add a new domain to current sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.addDomain()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DomainAddRequest import DomainAddRequest
        schema = DomainAddRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def removeDomainById(self, id=None):
        """Remove attached domain with current sales channel. It will disable user's access to website, shared links and other associated features to this domain.
        :param id : The unique identifier of the domain : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.removeDomainById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"description":"The unique identifier of the domain","schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"description":"The unique identifier of the domain","schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def changeDomainType(self, body=""):
        """Change a domain to Primary or Shortlink domain for the current sales channel
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.changeDomainType()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateDomainTypeRequest import UpdateDomainTypeRequest
        schema = UpdateDomainTypeRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/set-domain", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/set-domain", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getDomainStatus(self, body=""):
        """Get domain connected status. Check if domain is live and mapped to appropriate IP to fynd servers.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getDomainStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DomainStatusRequest import DomainStatusRequest
        schema = DomainStatusRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/domain-status", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/domain-status", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getApplicationById(self, ):
        """Get sales channel data from sales channel id under current company
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getApplicationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

