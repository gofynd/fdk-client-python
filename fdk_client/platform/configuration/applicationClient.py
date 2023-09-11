"""Configuration Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import ConfigurationValidator

class Configuration:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def getBuildConfig(self, platform_type=None, request_headers:Dict={}):
        """Fetch latest build configuration, such as app name, landing page image, splash image used in a mobile build.
        :param platform_type : The device platform for which the mobile app is built, e.g. android, ios. : type string
        """
        payload = {}
        
        if platform_type is not None:
            payload["platform_type"] = platform_type

        # Parameter validation
        schema = ConfigurationValidator.getBuildConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app is built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app is built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}]}""", platform_type=platform_type)
        query_string = await create_query_string(platform_type=platform_type)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", platform_type=platform_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import MobileAppConfiguration
            schema = MobileAppConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBuildConfig")
                print(e)

        return response
    
    async def updateBuildConfig(self, platform_type=None, body="", request_headers:Dict={}):
        """Modify the existing build configuration, such as app name, landing page image, splash image used in a mobile build.
        :param platform_type : The device platform for which the mobile app is built, e.g. android, ios. : type string
        """
        payload = {}
        
        if platform_type is not None:
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", platform_type=platform_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import MobileAppConfiguration
            schema = MobileAppConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateBuildConfig")
                print(e)

        return response
    
    async def getPreviousVersions(self, platform_type=None, request_headers:Dict={}):
        """Fetch version details of the app, this includes the build status, build date, version name, latest version, and a lot more.
        :param platform_type : The device platform for which the mobile app is built, e.g. android, ios. : type string
        """
        payload = {}
        
        if platform_type is not None:
            payload["platform_type"] = platform_type

        # Parameter validation
        schema = ConfigurationValidator.getPreviousVersions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/versions", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app is built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"The device platform for which the mobile app is built, e.g. android, ios.","in":"path","required":true,"name":"platform_type"}]}""", platform_type=platform_type)
        query_string = await create_query_string(platform_type=platform_type)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/versions", platform_type=platform_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import BuildVersionHistory
            schema = BuildVersionHistory()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPreviousVersions")
                print(e)

        return response
    
    async def getAppFeatures(self, request_headers:Dict={}):
        """Shows feature configuration of sales channel websites, such as product detail, landing page, options in the login/registration screen, home page, listing page, reward points, communication opt-in, cart options and many more.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppFeatures()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import AppFeatureResponse
            schema = AppFeatureResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppFeatures")
                print(e)

        return response
    
    async def updateAppFeatures(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import AppFeature
            schema = AppFeature()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppFeatures")
                print(e)

        return response
    
    async def modifyAppFeatures(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import AppFeature
            schema = AppFeature()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for modifyAppFeatures")
                print(e)

        return response
    
    async def getAppBasicDetails(self, request_headers:Dict={}):
        """Shows basic sales channel details like name, description, logo, domain, company ID, and other related information.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppBasicDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationDetail
            schema = ApplicationDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppBasicDetails")
                print(e)

        return response
    
    async def updateAppBasicDetails(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationDetail
            schema = ApplicationDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppBasicDetails")
                print(e)

        return response
    
    async def getAppContactInfo(self, request_headers:Dict={}):
        """Fetch data such as social links, copyright text, business highlights, address and contact information of the company/seller/brand operating the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppContactInfo()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationInformation
            schema = ApplicationInformation()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppContactInfo")
                print(e)

        return response
    
    async def updateAppContactInfo(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationInformation
            schema = ApplicationInformation()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppContactInfo")
                print(e)

        return response
    
    async def getAppApiTokens(self, request_headers:Dict={}):
        """Use this API to retrieve the tokens used for integrating Firebase, MoEngage, Segment, GTM, Freshchat, Safetynet, Google Map, Google, and Facebook auth. **Note** - Token values are encrypted with AES encryption using a secret key.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppApiTokens()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import TokenResponse
            schema = TokenResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppApiTokens")
                print(e)

        return response
    
    async def updateAppApiTokens(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import TokenResponse
            schema = TokenResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppApiTokens")
                print(e)

        return response
    
    async def getAppCompanies(self, uid=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Fetch info of all the companies (e.g. name, uid, and company type) whose inventory is fetched into the current sales channel application
        :param uid : UID of companies to be fetched : type integer
        :param page_no : The current page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if uid is not None:
            payload["uid"] = uid
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ConfigurationValidator.getAppCompanies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/companies", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"uid","in":"query","schema":{"type":"integer"},"description":"UID of companies to be fetched"},{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The current page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"uid","in":"query","schema":{"type":"integer"},"description":"UID of companies to be fetched"},{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The current page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", uid=uid, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(uid=uid, page_no=page_no, page_size=page_size)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/companies", uid=uid, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CompaniesResponse
            schema = CompaniesResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCompanies")
                print(e)

        return response
    
    async def getAppStores(self, page_no=None, page_size=None, request_headers:Dict={}):
        """Fetch info of all the companies (e.g. uid, name, display name, store type, store code and company id) whose inventory is fetched into the current sales channel application
        :param page_no : The current page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ConfigurationValidator.getAppStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stores", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The current page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The current page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stores", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import StoresResponse
            schema = StoresResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppStores")
                print(e)

        return response
    
    async def getInventoryConfig(self, request_headers:Dict={}):
        """Use this API to fetch configuration details of authentication, inventory, article assignment rules, reward points, cart, payment, order, logistics, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getInventoryConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationInventory
            schema = ApplicationInventory()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInventoryConfig")
                print(e)

        return response
    
    async def updateInventoryConfig(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationInventory
            schema = ApplicationInventory()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateInventoryConfig")
                print(e)

        return response
    
    async def partiallyUpdateInventoryConfig(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationInventory
            schema = ApplicationInventory()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for partiallyUpdateInventoryConfig")
                print(e)

        return response
    
    async def getAppCurrencyConfig(self, request_headers:Dict={}):
        """Get a list of currencies supported in the current sales channel. Moreover, get the cuurency that is set as the default one in the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppCurrencyConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import AppSupportedCurrency
            schema = AppSupportedCurrency()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCurrencyConfig")
                print(e)

        return response
    
    async def updateAppCurrencyConfig(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import AppSupportedCurrency
            schema = AppSupportedCurrency()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCurrencyConfig")
                print(e)

        return response
    
    async def getAppSupportedCurrency(self, request_headers:Dict={}):
        """Use this API to get a list of currencies allowed in the current application. Moreover, get the name, code, symbol, and the decimal digits of the currencies.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppSupportedCurrency()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency/supported", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency/supported", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import AppCurrencyResponse
            schema = AppCurrencyResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppSupportedCurrency")
                print(e)

        return response
    
    async def getOrderingStoresByFilter(self, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Use this API to use filters and retrieve the details of the deployment stores (the selling locations where the application will be utilised for placing orders).
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/stores/filter", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderingStores
            schema = OrderingStores()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrderingStoresByFilter")
                print(e)

        return response
    
    async def updateOrderingStoreConfig(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import DeploymentMeta
            schema = DeploymentMeta()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateOrderingStoreConfig")
                print(e)

        return response
    
    async def getOrderingStoreConfig(self, request_headers:Dict={}):
        """Fetch the details of the deployment stores (the selling locations where the application will be utilised for placing orders).
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getOrderingStoreConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderingStoreConfig
            schema = OrderingStoreConfig()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrderingStoreConfig")
                print(e)

        return response
    
    async def getStaffOrderingStores(self, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Use this API to retrieve the details of all stores access given to the staff member (the selling locations where the application will be utilized for placing orders).
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param q : Store code or name of the ordering store. : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = ConfigurationValidator.getStaffOrderingStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/staff-stores", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/staff-stores", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderingStoresResponse
            schema = OrderingStoresResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStaffOrderingStores")
                print(e)

        return response
    
    async def getDomains(self, request_headers:Dict={}):
        """Get list of domains
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getDomains()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import DomainsResponse
            schema = DomainsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDomains")
                print(e)

        return response
    
    async def addDomain(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import Domain
            schema = Domain()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addDomain")
                print(e)

        return response
    
    async def removeDomainById(self, id=None, request_headers:Dict={}):
        """Delete a domain (secondary or shortlink domain) added to a sales channel. It will disable user's access to website, shared links, and other features associated with this domain.
        :param id : The unique identifier (24-digit Mongo Object ID) of the domain : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ConfigurationValidator.removeDomainById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/{id}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"description":"The unique identifier (24-digit Mongo Object ID) of the domain","schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"description":"The unique identifier (24-digit Mongo Object ID) of the domain","schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessageResponse
            schema = SuccessMessageResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeDomainById")
                print(e)

        return response
    
    async def changeDomainType(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/set-domain", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import DomainsResponse
            schema = DomainsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for changeDomainType")
                print(e)

        return response
    
    async def getDomainStatus(self, body="", request_headers:Dict={}):
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

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/domain-status", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import DomainStatusResponse
            schema = DomainStatusResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDomainStatus")
                print(e)

        return response
    
    async def getApplicationById(self, request_headers:Dict={}):
        """Use application ID to get the current sales channel details which includes channel name, description, banner, logo, favicon, domain details, token, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getApplicationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}", """{"required":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account","in":"path","required":true,"name":"application_id"}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import Application
            schema = Application()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationById")
                print(e)

        return response
    