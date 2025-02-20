"""Content Public Client"""

from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PublicConfig import PublicConfig

from .validator import ContentValidator

class Content:
    def __init__(self, config: PublicConfig):
        self._conf = config
        self._relativeUrls = {
            "getBasicDetails": "/service/public/content/basic-details",
            "getMenuContent": "/service/public/content/menu",
            "getMenuContentByType": "/service/public/content/menu/{type}",
            "getAnalyticsTags": "/service/public/content/analytics-tags",
            "getCustomPage": "/service/public/content/custom-pages/{slug}",
            "getFooterContent": "/service/public/content/footer",
            "getHomePageContent": "/service/public/content/home-page",
            "getNavbar": "/service/public/content/navbar",
            "getPricingBanner": "/service/public/content/pricing-banner",
            "getAllTags": "/service/public/content/tags",
            "getCredentialsByEntity": "/service/public/content/credentials/{entity_type}"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getBasicDetails(self, body="", request_headers:Dict={}):
        """get basic platform information on Admin panel like Common Settings, Appereance of  Authentication Page, Text on Seller Login or Register Page, Business Account Restrictions, Seller Support Details and Footer Details
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getBasicDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBasicDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getBasicDetails"]).netloc, "get", await create_url_without_domain("/service/public/content/basic-details", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BasicDetailsPayloadSchema
            schema = BasicDetailsPayloadSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBasicDetails")
                print(e)

        return response
    
    async def getMenuContent(self, body="", request_headers:Dict={}):
        """Retrieves the desktop menu content.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getMenuContent()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getMenuContent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getMenuContent"]).netloc, "get", await create_url_without_domain("/service/public/content/menu", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MenusSchema
            schema = MenusSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMenuContent")
                print(e)

        return response
    
    async def getMenuContentByType(self, type=None, body="", request_headers:Dict={}):
        """Retrieves the desktop menu content.
        :param type : type param is type of device  : type string
        """
        payload = {}
        
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = ContentValidator.getMenuContentByType()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getMenuContentByType"], proccessed_params="""{"required":[{"name":"type","in":"path","description":"type param is type of device ","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"type","in":"path","description":"type param is type of device ","required":true,"schema":{"type":"string"}}]}""", serverType="public", type=type)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getMenuContentByType"]).netloc, "get", await create_url_without_domain("/service/public/content/menu/{type}", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MenuTypeSchema
            schema = MenuTypeSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMenuContentByType")
                print(e)

        return response
    
    async def getAnalyticsTags(self, body="", request_headers:Dict={}):
        """Retrieve analytics tags.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getAnalyticsTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAnalyticsTags"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAnalyticsTags"]).netloc, "get", await create_url_without_domain("/service/public/content/analytics-tags", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AnalyticsTagsSchema
            schema = AnalyticsTagsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAnalyticsTags")
                print(e)

        return response
    
    async def getCustomPage(self, slug=None, body="", request_headers:Dict={}):
        """Retrieve info of custom pagee to develop and manage custom webpages.
        :param slug : unique identifier created for each feature object in the schema. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getCustomPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomPage"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"unique identifier created for each feature object in the schema.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"unique identifier created for each feature object in the schema.","required":true,"schema":{"type":"string"}}]}""", serverType="public", slug=slug)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCustomPage"]).netloc, "get", await create_url_without_domain("/service/public/content/custom-pages/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomPageBySlugSchema
            schema = CustomPageBySlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomPage")
                print(e)

        return response
    
    async def getFooterContent(self, body="", request_headers:Dict={}):
        """Retrieve footer content.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getFooterContent()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFooterContent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFooterContent"]).netloc, "get", await create_url_without_domain("/service/public/content/footer", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FooterSchema
            schema = FooterSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFooterContent")
                print(e)

        return response
    
    async def getHomePageContent(self, page_type=None, body="", request_headers:Dict={}):
        """Retrieve home page content for a specific page type.
        :param page_type : The type of the page (e.g., pricing). : type string
        """
        payload = {}
        
        if page_type is not None:
            payload["page_type"] = page_type

        # Parameter validation
        schema = ContentValidator.getHomePageContent()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getHomePageContent"], proccessed_params="""{"required":[{"name":"page_type","in":"query","description":"The type of the page (e.g., pricing).","required":true,"schema":{"type":"string","enum":["home","features","pricing","theme"]}}],"optional":[],"query":[{"name":"page_type","in":"query","description":"The type of the page (e.g., pricing).","required":true,"schema":{"type":"string","enum":["home","features","pricing","theme"]}}],"headers":[],"path":[]}""", serverType="public", page_type=page_type)
        query_string = await create_query_string(page_type=page_type)
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getHomePageContent"]).netloc, "get", await create_url_without_domain("/service/public/content/home-page", page_type=page_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import HomePageContentSchema
            schema = HomePageContentSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getHomePageContent")
                print(e)

        return response
    
    async def getNavbar(self, body="", request_headers:Dict={}):
        """Retrieve navbar information.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getNavbar()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getNavbar"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getNavbar"]).netloc, "get", await create_url_without_domain("/service/public/content/navbar", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import NavbarSchema
            schema = NavbarSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNavbar")
                print(e)

        return response
    
    async def getPricingBanner(self, body="", request_headers:Dict={}):
        """Retrieve pricing banner information.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getPricingBanner()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPricingBanner"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPricingBanner"]).netloc, "get", await create_url_without_domain("/service/public/content/pricing-banner", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PricingBannerSchema
            schema = PricingBannerSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPricingBanner")
                print(e)

        return response
    
    async def getAllTags(self, body="", request_headers:Dict={}):
        """Retrieve custom tag with injected css/javascript info.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getAllTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAllTags"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="public" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAllTags"]).netloc, "get", await create_url_without_domain("/service/public/content/tags", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TagsSchema
            schema = TagsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllTags")
                print(e)

        return response
    
    async def getCredentialsByEntity(self, entity_type=None, body="", request_headers:Dict={}):
        """Get credentials for support system
        :param entity_type : Server Type : type string
        """
        payload = {}
        
        if entity_type is not None:
            payload["entity_type"] = entity_type

        # Parameter validation
        schema = ContentValidator.getCredentialsByEntity()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCredentialsByEntity"], proccessed_params="""{"required":[{"name":"entity_type","in":"path","description":"Server Type","required":true,"schema":{"type":"string","enum":["partner","platform"]}}],"optional":[],"query":[],"headers":[],"path":[{"name":"entity_type","in":"path","description":"Server Type","required":true,"schema":{"type":"string","enum":["partner","platform"]}}]}""", serverType="public", entity_type=entity_type)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCredentialsByEntity"]).netloc, "get", await create_url_without_domain("/service/public/content/credentials/{entity_type}", entity_type=entity_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CredentialsSchema
            schema = CredentialsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCredentialsByEntity")
                print(e)

        return response
    