"""Content Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import ContentValidator

class Content:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "getAnnouncements": "/service/application/content/v1.0/announcements",
            "getBlog": "/service/application/content/v1.0/blogs/{slug}",
            "getBlogs": "/service/application/content/v1.0/blogs",
            "getDataLoaders": "/service/application/content/v1.0/data-loader",
            "getFaqs": "/service/application/content/v1.0/faq",
            "getFaqCategories": "/service/application/content/v1.0/faq/categories",
            "getFaqBySlug": "/service/application/content/v1.0/faq/{slug}",
            "getFaqCategoryBySlug": "/service/application/content/v1.0/faq/category/{slug}",
            "getFaqsByCategorySlug": "/service/application/content/v1.0/faq/category/{slug}/faqs",
            "getLandingPage": "/service/application/content/v1.0/landing-page",
            "getLegalInformation": "/service/application/content/v1.0/legal",
            "getNavigations": "/service/application/content/v1.0/navigations",
            "getSEOConfiguration": "/service/application/content/v1.0/seo",
            "getSEOMarkupSchemas": "/service/application/content/v1.0/seo/schema",
            "getSupportInformation": "/service/application/content/v1.0/support",
            "getTags": "/service/application/content/v1.0/tags",
            "getPages": "/service/application/content/v2.0/pages",
            "getPage": "/service/application/content/v2.0/pages/{slug}",
            "getWellKnownUrl": "/service/application/content/v1.0/well-known/{slug}",
            "getCustomObject": "/service/application/content/v1.0/metaobjects/{id}",
            "getCustomObjects": "/service/application/content/v1.0/metaobjects",
            "getCustomFieldDefinitions": "/service/application/content/v1.0/metafields/definitions",
            "getCustomFieldDefinition": "/service/application/content/v1.0/metafields/definitions/{id}",
            "getCustomFields": "/service/application/content/v1.0/metafields/{resource}"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getAnnouncements(self, body="", request_headers:Dict={}):
        """List all current announcements in the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getAnnouncements()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAnnouncements"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAnnouncements"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/announcements", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AnnouncementsResponseSchema
            schema = AnnouncementsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAnnouncements")
                print(e)

        return response
    
    async def getBlog(self, slug=None, root_id=None, body="", request_headers:Dict={}):
        """Get information related to a specific blog such as it's contents, author, publish date, SEO related information.
        :param slug : A short, human-readable, URL-friendly identifier of a blog. You can get slug value from the endpoint /service/application/content/v1.0/blogs/. : type string
        :param root_id : ID given to the HTML element : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if root_id is not None:
            payload["root_id"] = root_id

        # Parameter validation
        schema = ContentValidator.getBlog()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBlog"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog. You can get slug value from the endpoint /service/application/content/v1.0/blogs/.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"query":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog. You can get slug value from the endpoint /service/application/content/v1.0/blogs/.","required":true,"schema":{"type":"string"}}]}""", serverType="application", slug=slug, root_id=root_id)
        query_string = await create_query_string(root_id=root_id)
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getBlog"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/blogs/{slug}", slug=slug, root_id=root_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogSchema
            schema = BlogSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBlog")
                print(e)

        return response
    
    async def getBlogs(self, page_no=None, page_size=None, tags=None, search=None, body="", request_headers:Dict={}):
        """List all the blogs against an application.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        :param tags : Blogs retrieve based on the list of tags passed. : type string
        :param search : Blogs retrieve based on the title. : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if tags is not None:
            payload["tags"] = tags
        if search is not None:
            payload["search"] = search

        # Parameter validation
        schema = ContentValidator.getBlogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBlogs"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}},{"name":"tags","in":"query","description":"Blogs retrieve based on the list of tags passed.","required":false,"schema":{"type":"string","description":"Comma separated list of tags."},"style":"form","explode":false},{"name":"search","in":"query","description":"Blogs retrieve based on the title.","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}},{"name":"tags","in":"query","description":"Blogs retrieve based on the list of tags passed.","required":false,"schema":{"type":"string","description":"Comma separated list of tags."},"style":"form","explode":false},{"name":"search","in":"query","description":"Blogs retrieve based on the title.","required":false,"schema":{"type":"string"}}],"headers":[],"path":[]}""", serverType="application", page_no=page_no, page_size=page_size, tags=tags, search=search)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, tags=tags, search=search)
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getBlogs"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/blogs", page_no=page_no, page_size=page_size, tags=tags, search=search), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogGetResponse
            schema = BlogGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBlogs")
                print(e)

        return response
    
    async def getDataLoaders(self, body="", request_headers:Dict={}):
        """List all the data loaders that are enabled for an application.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getDataLoaders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getDataLoaders"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getDataLoaders"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/data-loader", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DataLoadersSchema
            schema = DataLoadersSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDataLoaders")
                print(e)

        return response
    
    async def getFaqs(self, body="", request_headers:Dict={}):
        """List frequently asked questions and answers.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getFaqs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqs"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFaqs"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FaqResponseSchema
            schema = FaqResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFaqs")
                print(e)

        return response
    
    async def getFaqCategories(self, body="", request_headers:Dict={}):
        """List categories for organizing FAQs.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getFaqCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqCategories"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFaqCategories"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/categories", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetFaqCategoriesSchema
            schema = GetFaqCategoriesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFaqCategories")
                print(e)

        return response
    
    async def getFaqBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Get a specific FAQ using its slug identifier.
        :param slug : A short, human-readable, URL-friendly identifier of an FAQ. You can get slug value from the endpoint /service/application/content/v1.0/faq. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getFaqBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ. You can get slug value from the endpoint /service/application/content/v1.0/faq.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ. You can get slug value from the endpoint /service/application/content/v1.0/faq.","required":true,"schema":{"type":"string"}}]}""", serverType="application", slug=slug)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFaqBySlug"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FaqSchema
            schema = FaqSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFaqBySlug")
                print(e)

        return response
    
    async def getFaqCategoryBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Get a specific FAQ category using its slug.
        :param slug : A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getFaqCategoryBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqCategoryBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}]}""", serverType="application", slug=slug)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFaqCategoryBySlug"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/category/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetFaqCategoryBySlugSchema
            schema = GetFaqCategoryBySlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFaqCategoryBySlug")
                print(e)

        return response
    
    async def getFaqsByCategorySlug(self, slug=None, body="", request_headers:Dict={}):
        """Get FAQs belonging to a specific category slug.
        :param slug : A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getFaqsByCategorySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqsByCategorySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}]}""", serverType="application", slug=slug)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFaqsByCategorySlug"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/category/{slug}/faqs", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetFaqSchema
            schema = GetFaqSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFaqsByCategorySlug")
                print(e)

        return response
    
    async def getLandingPage(self, body="", request_headers:Dict={}):
        """Gets the content of the application's landing page.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getLandingPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLandingPage"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLandingPage"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/landing-page", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LandingPageSchema
            schema = LandingPageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLandingPage")
                print(e)

        return response
    
    async def getLegalInformation(self, body="", request_headers:Dict={}):
        """Get legal policies for an application which includes Terms and conditions, return policy, shipping policy and privacy policy.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getLegalInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLegalInformation"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLegalInformation"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/legal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationLegal
            schema = ApplicationLegal()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLegalInformation")
                print(e)

        return response
    
    async def getNavigations(self, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Get the navigation link items which can be powered to generate menus on application's website or equivalent mobile apps.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getNavigations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getNavigations"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[]}""", serverType="application", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getNavigations"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/navigations", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import NavigationGetResponse
            schema = NavigationGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNavigations")
                print(e)

        return response
    
    async def getSEOConfiguration(self, body="", request_headers:Dict={}):
        """Get search engine optimization configurations of an application. Details include the title, description and an image.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSEOConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSEOConfiguration"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getSEOConfiguration"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/seo", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SeoComponent
            schema = SeoComponent()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSEOConfiguration")
                print(e)

        return response
    
    async def getSEOMarkupSchemas(self, page_type=None, active=None, body="", request_headers:Dict={}):
        """Get all SEO Markup schema Templates setup for an application.
        :param page_type : The type of page against which schema template was created : type string
        :param active : Boolean value for fetching seo schema. : type boolean
        """
        payload = {}
        
        if page_type is not None:
            payload["page_type"] = page_type
        if active is not None:
            payload["active"] = active

        # Parameter validation
        schema = ContentValidator.getSEOMarkupSchemas()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSEOMarkupSchemas"], proccessed_params="""{"required":[],"optional":[{"name":"page_type","in":"query","description":"The type of page against which schema template was created","required":false,"schema":{"type":"string"}},{"name":"active","in":"query","description":"Boolean value for fetching seo schema.","required":false,"schema":{"type":"boolean","default":true}}],"query":[{"name":"page_type","in":"query","description":"The type of page against which schema template was created","required":false,"schema":{"type":"string"}},{"name":"active","in":"query","description":"Boolean value for fetching seo schema.","required":false,"schema":{"type":"boolean","default":true}}],"headers":[],"path":[]}""", serverType="application", page_type=page_type, active=active)
        query_string = await create_query_string(page_type=page_type, active=active)
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getSEOMarkupSchemas"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/seo/schema", page_type=page_type, active=active), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SeoSchemaComponent
            schema = SeoSchemaComponent()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSEOMarkupSchemas")
                print(e)

        return response
    
    async def getSupportInformation(self, body="", request_headers:Dict={}):
        """Get customer support contact details. Contact Details can be either a phone number or an email-id or both.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSupportInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSupportInformation"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getSupportInformation"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/support", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Support
            schema = Support()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSupportInformation")
                print(e)

        return response
    
    async def getTags(self, body="", request_headers:Dict={}):
        """Lists HTML tags to power additional functionalities within an application.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getTags"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getTags"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/tags", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TagsSchema
            schema = TagsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTags")
                print(e)

        return response
    
    async def getPages(self, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Lists all Custom Pages
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPages"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[]}""", serverType="application", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPages"]).netloc, "get", await create_url_without_domain("/service/application/content/v2.0/pages", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PageGetResponse
            schema = PageGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPages")
                print(e)

        return response
    
    async def getPage(self, slug=None, root_id=None, body="", request_headers:Dict={}):
        """Get detailed information about a specific page using its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value from the endpoint /service/application/content/v2.0/pages/. : type string
        :param root_id : ID given to the HTML element : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if root_id is not None:
            payload["root_id"] = root_id

        # Parameter validation
        schema = ContentValidator.getPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPage"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value from the endpoint /service/application/content/v2.0/pages/.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"query":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value from the endpoint /service/application/content/v2.0/pages/.","required":true,"schema":{"type":"string"}}]}""", serverType="application", slug=slug, root_id=root_id)
        query_string = await create_query_string(root_id=root_id)
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPage"]).netloc, "get", await create_url_without_domain("/service/application/content/v2.0/pages/{slug}", slug=slug, root_id=root_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PageSchema
            schema = PageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPage")
                print(e)

        return response
    
    async def getWellKnownUrl(self, slug=None, body="", request_headers:Dict={}):
        """Retrieves the details of a specific well-known URL by its slug.
        :param slug : The unique identifier/path of the well-known URL (e.g., assetlinks.json) : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getWellKnownUrl()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getWellKnownUrl"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"The unique identifier/path of the well-known URL (e.g., assetlinks.json)","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"The unique identifier/path of the well-known URL (e.g., assetlinks.json)","required":true,"schema":{"type":"string"}}]}""", serverType="application", slug=slug)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getWellKnownUrl"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/well-known/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import WellKnownResponse
            schema = WellKnownResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getWellKnownUrl")
                print(e)

        return response
    
    async def getCustomObject(self, id=None, body="", request_headers:Dict={}):
        """Details of custom objects, their field details, definitions, and references can be obtained using this endpoint.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.getCustomObject()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomObject"], proccessed_params="""{"required":[{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"}}]}""", serverType="application", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCustomObject"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/metaobjects/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectByIdSchema
            schema = CustomObjectByIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomObject")
                print(e)

        return response
    
    async def getCustomObjects(self, definition_id=None, page_no=None, page_size=None, type=None, ids=None, search=None, body="", request_headers:Dict={}):
        """Use this API to retrieve the custom objects.
        :param definition_id :  : type string
        :param page_no :  : type string
        :param page_size :  : type string
        :param type :  : type string
        :param ids :  : type string
        :param search :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if type is not None:
            payload["type"] = type
        if ids is not None:
            payload["ids"] = ids
        if search is not None:
            payload["search"] = search

        # Parameter validation
        schema = ContentValidator.getCustomObjects()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomObjects"], proccessed_params="""{"required":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}}],"optional":[{"name":"definition_id","in":"query","required":false,"schema":{"type":"string","description":"This is definition id"}},{"name":"type","in":"query","required":false,"schema":{"type":"string","description":"This is the slug"}},{"name":"ids","in":"query","required":false,"schema":{"type":"string","description":"This is meta object id"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is search query for custom entry name"}}],"query":[{"name":"definition_id","in":"query","required":false,"schema":{"type":"string","description":"This is definition id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"type","in":"query","required":false,"schema":{"type":"string","description":"This is the slug"}},{"name":"ids","in":"query","required":false,"schema":{"type":"string","description":"This is meta object id"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is search query for custom entry name"}}],"headers":[],"path":[]}""", serverType="application", definition_id=definition_id, page_no=page_no, page_size=page_size, type=type, ids=ids, search=search)
        query_string = await create_query_string(definition_id=definition_id, page_no=page_no, page_size=page_size, type=type, ids=ids, search=search)
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCustomObjects"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/metaobjects", definition_id=definition_id, page_no=page_no, page_size=page_size, type=type, ids=ids, search=search), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectsSchema
            schema = CustomObjectsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomObjects")
                print(e)

        return response
    
    async def getCustomFieldDefinitions(self, body="", request_headers:Dict={}):
        """Use this API to retrieve the definitions of custom fields.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getCustomFieldDefinitions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomFieldDefinitions"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCustomFieldDefinitions"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/metafields/definitions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionsSchema
            schema = CustomFieldDefinitionsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFieldDefinitions")
                print(e)

        return response
    
    async def getCustomFieldDefinition(self, id=None, body="", request_headers:Dict={}):
        """Use this API to retrieve the definitions of custom fields using definition_id.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.getCustomFieldDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomFieldDefinition"], proccessed_params="""{"required":[{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"}}]}""", serverType="application", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCustomFieldDefinition"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/metafields/definitions/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionDetailResSchema
            schema = CustomFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFieldDefinition")
                print(e)

        return response
    
    async def getCustomFields(self, resource=None, resource_ids=None, body="", request_headers:Dict={}):
        """Use this API to retrieve the custom fields for given resource and resource_ids in param
        :param resource :  : type string
        :param resource_ids :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource
        if resource_ids is not None:
            payload["resource_ids"] = resource_ids

        # Parameter validation
        schema = ContentValidator.getCustomFields()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomFields"], proccessed_params="""{"required":[{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_ids","in":"query","required":true,"schema":{"type":"string","description":"This is the resource ids for which custom fields created with comma separated."}}],"optional":[],"query":[{"name":"resource_ids","in":"query","required":true,"schema":{"type":"string","description":"This is the resource ids for which custom fields created with comma separated."}}],"headers":[],"path":[{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."}}]}""", serverType="application", resource=resource, resource_ids=resource_ids)
        query_string = await create_query_string(resource_ids=resource_ids)
        if query_string:
            url_with_params += "?" + query_string

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCustomFields"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/metafields/{resource}", resource=resource, resource_ids=resource_ids), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldsResponseByResourceIdSchema
            schema = CustomFieldsResponseByResourceIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomFields")
                print(e)

        return response
    