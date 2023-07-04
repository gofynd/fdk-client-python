

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
        :param platform_type : The device platform for which the mobile app is built, e.g. android, ios. : type string
        """
        payload = {}
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.getBuildConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app is built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app is built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}]}""", platform_type=platform_type)
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
        """Modify the existing build configuration, such as app name, landing page image, splash image used in a mobile build.
        :param platform_type : The device platform for which the mobile app is built, e.g. android, ios. : type string
        """
        payload = {}
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.updateBuildConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MobileAppConfigRequest
        schema = MobileAppConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app is built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app is built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}]}""", platform_type=platform_type)
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
        """Fetch version details of the app, this includes the build status, build date, version name, latest version, and a lot more.
        :param platform_type : The device platform for which the mobile app is built, e.g. android, ios. : type string
        """
        payload = {}
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.getPreviousVersions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/versions", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app is built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app is built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}]}""", platform_type=platform_type)
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
        """Shows feature configuration of sales channel websites, such as product detail, landing page, options in the login/registration screen, home page, listing page, reward points, communication opt-in, cart options and many more.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppFeatures()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Modify the feature configuration of sales channel websites, such as product detail, landing page, options in the login/registration screen, home page, listing page, reward points, communication opt-in, cart options and many more.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppFeatures()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppFeatureRequest
        schema = AppFeatureRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
    
    async def modifyAppFeatures(self, body=""):
        """Update features of application
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.modifyAppFeatures()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppFeatureRequest
        schema = AppFeatureRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAppBasicDetails(self, ):
        """Shows basic sales channel details like name, description, logo, domain, company ID, and other related information.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppBasicDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Modify sales channel details like name, description, logo, domain, company ID, and other related information.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppBasicDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationDetail
        schema = ApplicationDetail()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Fetch data such as social links, copyright text, business highlights, address and contact information of the company/seller/brand operating the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppContactInfo()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Modify the social links, copyright text, business highlights, address and contact information of the company/seller/brand operating the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppContactInfo()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationInformation
        schema = ApplicationInformation()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Use this API to retrieve the tokens used for integrating Firebase, MoEngage, Segment, GTM, Freshchat, Safetynet, Google Map, Google, and Facebook auth. **Note** - Token values are encrypted with AES encryption using a secret key.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppApiTokens()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Use this API to add or edit the tokens used for integrating Firebase, MoEngage, Segment, GTM, Freshchat, Safetynet, Google Map, Google and Facebook auth.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppApiTokens()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TokenResponse
        schema = TokenResponse()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Fetch info of all the companies (e.g. name, uid, and company type) whose inventory is fetched into the current sales channel application
        :param uid : UID of companies to be fetched : type integer
        :param page_no : The current page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/companies", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"uid","in":"query","schema":{"type":"integer"},"description":"UID of companies to be fetched"},{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The current page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"uid","in":"query","schema":{"type":"integer"},"description":"UID of companies to be fetched"},{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The current page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", uid=uid, page_no=page_no, page_size=page_size)
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
        """Fetch info of all the companies (e.g. uid, name, display name, store type, store code and company id) whose inventory is fetched into the current sales channel application
        :param page_no : The current page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getAppStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stores", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The current page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The current page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size)
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
        """Use this API to fetch configuration details of authentication, inventory, article assignment rules, reward points, cart, payment, order, logistics, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getInventoryConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Modify the configuration details of authentication, inventory, article assignment rules, reward points, cart, payment, order, logistics, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateInventoryConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationInventory
        schema = ApplicationInventory()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Partially update the configuration details of authentication, inventory, article assignment rules, reward points, cart, payment, order, logistics, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.partiallyUpdateInventoryConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppInventoryPartialUpdate
        schema = AppInventoryPartialUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Get a list of currencies supported in the current sales channel. Moreover, get the cuurency that is set as the default one in the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppCurrencyConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Use this API to add and edit the currencies supported in the application. Initially, INR will be enabled by default.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppCurrencyConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppSupportedCurrency
        schema = AppSupportedCurrency()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency/supported", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Use this API to use filters and retrieve the details of the deployment stores (the selling locations where the application will be utilised for placing orders).
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
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
        from .models import FilterOrderingStoreRequest
        schema = FilterOrderingStoreRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/stores/filter", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size)
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
        """Use this API to edit the details of the deployment stores (the selling locations where the application will be utilised for placing orders)
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateOrderingStoreConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OrderingStoreConfig
        schema = OrderingStoreConfig()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/staff-stores", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size, q=q)
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
        """Get list of domains
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getDomains()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Add a new domain to current sales channel, including pre-defined domain (free domain) or custom domain (owned by the brand)
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.addDomain()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DomainAddRequest
        schema = DomainAddRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Delete a domain (secondary or shortlink domain) added to a sales channel. It will disable user's access to website, shared links, and other features associated with this domain.
        :param id : The unique identifier (24-digit Mongo Object ID) of the domain : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.removeDomainById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/{id}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"description":"The unique identifier (24-digit Mongo Object ID) of the domain","schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"description":"The unique identifier (24-digit Mongo Object ID) of the domain","schema":{"type":"string"}}]}""", id=id)
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
        """Primary domain is used as the URL of your website. Short link domain is comparatively smaller and used while generating short links. Use this API to change a domain to either Primary or a Shortlink domain.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.changeDomainType()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateDomainTypeRequest
        schema = UpdateDomainTypeRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/set-domain", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Shows if the A records and TXT records of the domain correctly points to appropriate IP on Fynd Servers.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getDomainStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DomainStatusRequest
        schema = DomainStatusRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/domain-status", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
        """Use application ID to get the current sales channel details which includes channel name, description, banner, logo, favicon, domain details, token, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getApplicationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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
    

