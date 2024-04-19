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
            "getBlogs": "/service/application/content/v1.0/blogs/",
            "getDataLoaders": "/service/application/content/v1.0/data-loader",
            "getFaqs": "/service/application/content/v1.0/faq",
            "getFaqCategories": "/service/application/content/v1.0/faq/categories",
            "getFaqBySlug": "/service/application/content/v1.0/faq/{slug}",
            "getFaqCategoryBySlug": "/service/application/content/v1.0/faq/category/{slug}",
            "getFaqsByCategorySlug": "/service/application/content/v1.0/faq/category/{slug}/faqs",
            "getLandingPage": "/service/application/content/v1.0/landing-page",
            "getLegalInformation": "/service/application/content/v1.0/legal",
            "getNavigations": "/service/application/content/v1.0/navigations/",
            "getSEOConfiguration": "/service/application/content/v1.0/seo",
            "getSlideshows": "/service/application/content/v1.0/slideshow/",
            "getSlideshow": "/service/application/content/v1.0/slideshow/{slug}",
            "getSupportInformation": "/service/application/content/v1.0/support",
            "getTags": "/service/application/content/v1.0/tags",
            "getPage": "/service/application/content/v2.0/pages/{slug}",
            "getPages": "/service/application/content/v2.0/pages/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getAnnouncements(self, body="", request_headers:Dict={}):
        """Announcements are useful to highlight a message or information on top of a webpage. Use this API to retrieve live announcements. Get announcements on individual pages or for all pages.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getAnnouncements()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAnnouncements"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAnnouncements"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/announcements", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """Use this API to get the details of a blog using its slug. Details include the title, reading time, publish status, feature image, tags, author, etc.
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBlog"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog. You can get slug value from the endpoint /service/application/content/v1.0/blogs/.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"query":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog. You can get slug value from the endpoint /service/application/content/v1.0/blogs/.","required":true,"schema":{"type":"string"}}]}""", slug=slug, root_id=root_id)
        query_string = await create_query_string(slug=slug, root_id=root_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getBlog"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/blogs/{slug}", slug=slug, root_id=root_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogSchema
            schema = BlogSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBlog")
                print(e)

        return response
    
    async def getBlogs(self, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Use this API to get all the blogs.
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getBlogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBlogs"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getBlogs"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/blogs/", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """Use this API to get all selected data loaders of the application in the form of tags.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getDataLoaders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getDataLoaders"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getDataLoaders"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/data-loader", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """Use this API to get a list of frequently asked questions. Users will benefit from it when facing any issue with the website.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getFaqs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqs"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFaqs"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """FAQs can be divided into categories. Use this API to get a list of FAQ categories.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getFaqCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqCategories"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFaqCategories"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/categories", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """Use this API to get a particular FAQ by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of an FAQ. You can get slug value from the endpoint /service/application/content/v1.0/faq. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getFaqBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ. You can get slug value from the endpoint /service/application/content/v1.0/faq.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ. You can get slug value from the endpoint /service/application/content/v1.0/faq.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFaqBySlug"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """FAQs can be divided into categories. Use this API to get the category to which an FAQ belongs.
        :param slug : A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getFaqCategoryBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqCategoryBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFaqCategoryBySlug"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/category/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """FAQs can be divided into categories. Use this API to get all the FAQs belonging to a category by using the category slug.
        :param slug : A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getFaqsByCategorySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqsByCategorySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFaqsByCategorySlug"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/category/{slug}/faqs", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """Landing page is the first page that a prospect lands upon while visiting a website. Use this API to fetch the details of a landing page.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getLandingPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLandingPage"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLandingPage"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/landing-page", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """Use this API to get the legal information of an application, which includes Privacy Policy, Terms and Conditions, Shipping Policy and FAQs regarding the usage of the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getLegalInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLegalInformation"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLegalInformation"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/legal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """Use this API to fetch the navigations details which includes the items of the navigation panel. It also shows the links and sub-navigations.
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getNavigations"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getNavigations"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/navigations/", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """Use this API to get the SEO details of an application, which includes a robot.txt, meta-tags and sitemap.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSEOConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSEOConfiguration"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getSEOConfiguration"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/seo", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import SeoComponent
            schema = SeoComponent()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSEOConfiguration")
                print(e)

        return response
    
    async def getSlideshows(self, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Use this API to get a list of slideshows along with their details.
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getSlideshows()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSlideshows"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getSlideshows"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/slideshow/", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import SlideshowGetResponse
            schema = SlideshowGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSlideshows")
                print(e)

        return response
    
    async def getSlideshow(self, slug=None, body="", request_headers:Dict={}):
        """A slideshow is a group of images, videos or a combination of both that are shown on the website in the form of slides. Use this API to fetch a slideshow using its `slug`.
        :param slug : A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value from the endpoint /service/application/content/v1.0/slideshow/. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getSlideshow()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSlideshow"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value from the endpoint /service/application/content/v1.0/slideshow/.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value from the endpoint /service/application/content/v1.0/slideshow/.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getSlideshow"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/slideshow/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import SlideshowSchema
            schema = SlideshowSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSlideshow")
                print(e)

        return response
    
    async def getSupportInformation(self, body="", request_headers:Dict={}):
        """Use this API to get contact details for customer support including emails and phone numbers.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSupportInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSupportInformation"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getSupportInformation"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/support", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

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
        """Use this API to get all the CSS and JS injected in the application in the form of tags.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getTags"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getTags"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/tags", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import TagsSchema
            schema = TagsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTags")
                print(e)

        return response
    
    async def getPage(self, slug=None, root_id=None, body="", request_headers:Dict={}):
        """Use this API to get the details of a page using its slug. Details include the title, seo, publish status, feature image, tags, meta, etc.
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPage"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value from the endpoint /service/application/content/v2.0/pages/.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"query":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value from the endpoint /service/application/content/v2.0/pages/.","required":true,"schema":{"type":"string"}}]}""", slug=slug, root_id=root_id)
        query_string = await create_query_string(slug=slug, root_id=root_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPage"]).netloc, "get", await create_url_without_domain("/service/application/content/v2.0/pages/{slug}", slug=slug, root_id=root_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import PageSchema
            schema = PageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPage")
                print(e)

        return response
    
    async def getPages(self, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Use this API to get a list of pages.
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPages"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPages"]).netloc, "get", await create_url_without_domain("/service/application/content/v2.0/pages/", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import PageGetResponse
            schema = PageGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPages")
                print(e)

        return response
    