"""Content Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import ContentValidator

class Content:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def getAnnouncementsList(self, page_no=None, page_size=None, request_headers:Dict={}):
        """Lists all announcements
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getAnnouncementsList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAnnouncementListSchema
            schema = GetAnnouncementListSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAnnouncementsList")
                print(e)

        return response
    
    async def createAnnouncement(self, body="", request_headers:Dict={}):
        """Generate and add a new announcement.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createAnnouncement()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AdminAnnouncementSchema
        schema = AdminAnnouncementSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAnnouncementSchema
            schema = CreateAnnouncementSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAnnouncement")
                print(e)

        return response
    
    async def getAnnouncementById(self, announcement_id=None, request_headers:Dict={}):
        """Get detailed information about a specific announcement
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id is not None:
            payload["announcement_id"] = announcement_id

        # Parameter validation
        schema = ContentValidator.getAnnouncementById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", announcement_id=announcement_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AdminAnnouncementSchema
            schema = AdminAnnouncementSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAnnouncementById")
                print(e)

        return response
    
    async def updateAnnouncement(self, announcement_id=None, body="", request_headers:Dict={}):
        """Modify the content and settings of a specific announcement.
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id is not None:
            payload["announcement_id"] = announcement_id

        # Parameter validation
        schema = ContentValidator.updateAnnouncement()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AdminAnnouncementSchema
        schema = AdminAnnouncementSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", announcement_id=announcement_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAnnouncementSchema
            schema = CreateAnnouncementSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAnnouncement")
                print(e)

        return response
    
    async def updateAnnouncementSchedule(self, announcement_id=None, body="", request_headers:Dict={}):
        """Modify the scheduling of a specific announcement.
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id is not None:
            payload["announcement_id"] = announcement_id

        # Parameter validation
        schema = ContentValidator.updateAnnouncementSchedule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ScheduleSchema
        schema = ScheduleSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", announcement_id=announcement_id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAnnouncementSchema
            schema = CreateAnnouncementSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAnnouncementSchedule")
                print(e)

        return response
    
    async def deleteAnnouncement(self, announcement_id=None, request_headers:Dict={}):
        """Remove a specific announcement.
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id is not None:
            payload["announcement_id"] = announcement_id

        # Parameter validation
        schema = ContentValidator.deleteAnnouncement()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", announcement_id=announcement_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAnnouncementSchema
            schema = CreateAnnouncementSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAnnouncement")
                print(e)

        return response
    
    async def createBlog(self, body="", request_headers:Dict={}):
        """Generate and add a new blog.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createBlog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BlogPayload
        schema = BlogPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogSchema
            schema = BlogSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createBlog")
                print(e)

        return response
    
    async def getBlogs(self, page_no=None, page_size=None, tags=None, q=None, slug=None, title=None, status=None, request_headers:Dict={}):
        """List all blogs
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param tags : Blogs retrieve based on the list of tags passed. : type string
        :param q : Blogs retrieve based on the title or slug passed. : type string
        :param slug : Blogs retrieve based on the slug passed. : type string
        :param title : Blogs retrieve based on the title passed. : type string
        :param status : Blogs retrieve based on the status passed. : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if tags is not None:
            payload["tags"] = tags
        if q is not None:
            payload["q"] = q
        if slug is not None:
            payload["slug"] = slug
        if title is not None:
            payload["title"] = title
        if status is not None:
            payload["status"] = status

        # Parameter validation
        schema = ContentValidator.getBlogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"tags","in":"query","description":"Blogs retrieve based on the list of tags passed.","required":false,"schema":{"type":"string","description":"Comma separated list of tags."},"style":"form","explode":false},{"name":"q","in":"query","description":"Blogs retrieve based on the title or slug passed.","required":false,"schema":{"type":"string"}},{"name":"slug","in":"query","description":"Blogs retrieve based on the slug passed.","required":false,"schema":{"type":"string"}},{"name":"title","in":"query","description":"Blogs retrieve based on the title passed.","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Blogs retrieve based on the status passed.","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"tags","in":"query","description":"Blogs retrieve based on the list of tags passed.","required":false,"schema":{"type":"string","description":"Comma separated list of tags."},"style":"form","explode":false},{"name":"q","in":"query","description":"Blogs retrieve based on the title or slug passed.","required":false,"schema":{"type":"string"}},{"name":"slug","in":"query","description":"Blogs retrieve based on the slug passed.","required":false,"schema":{"type":"string"}},{"name":"title","in":"query","description":"Blogs retrieve based on the title passed.","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Blogs retrieve based on the status passed.","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, tags=tags, q=q, slug=slug, title=title, status=status)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, tags=tags, q=q, slug=slug, title=title, status=status)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", page_no=page_no, page_size=page_size, tags=tags, q=q, slug=slug, title=title, status=status), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogGetDetails
            schema = BlogGetDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBlogs")
                print(e)

        return response
    
    async def updateBlog(self, id=None, body="", request_headers:Dict={}):
        """Modify the content and settings of a specific blog.
        :param id : ID allotted to the blog. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.updateBlog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BlogPayload
        schema = BlogPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogSchema
            schema = BlogSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateBlog")
                print(e)

        return response
    
    async def deleteBlog(self, id=None, request_headers:Dict={}):
        """Remove a specific blog.
        :param id : ID allotted to the blog. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deleteBlog()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogSchema
            schema = BlogSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteBlog")
                print(e)

        return response
    
    async def addDataLoader(self, body="", request_headers:Dict={}):
        """Create and add a new data loader.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.addDataLoader()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DataLoaderSchema
        schema = DataLoaderSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DataLoaderResponseSchema
            schema = DataLoaderResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addDataLoader")
                print(e)

        return response
    
    async def getDataLoaders(self, request_headers:Dict={}):
        """List all Dataloaders
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getDataLoaders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DataLoadersSchema
            schema = DataLoadersSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDataLoaders")
                print(e)

        return response
    
    async def deleteDataLoader(self, data_loader_id=None, request_headers:Dict={}):
        """Remove a specific data loader.
        :param data_loader_id : ID allotted to the data loader. : type string
        """
        payload = {}
        
        if data_loader_id is not None:
            payload["data_loader_id"] = data_loader_id

        # Parameter validation
        schema = ContentValidator.deleteDataLoader()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", data_loader_id=data_loader_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", data_loader_id=data_loader_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DataLoaderResponseSchema
            schema = DataLoaderResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteDataLoader")
                print(e)

        return response
    
    async def editDataLoader(self, data_loader_id=None, body="", request_headers:Dict={}):
        """Modify the settings of a specific data loader.
        :param data_loader_id : ID allotted to the data loader. : type string
        """
        payload = {}
        
        if data_loader_id is not None:
            payload["data_loader_id"] = data_loader_id

        # Parameter validation
        schema = ContentValidator.editDataLoader()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DataLoaderSchema
        schema = DataLoaderSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", data_loader_id=data_loader_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", data_loader_id=data_loader_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DataLoaderResponseSchema
            schema = DataLoaderResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editDataLoader")
                print(e)

        return response
    
    async def getDataLoadersByService(self, service_name=None, request_headers:Dict={}):
        """Use this to get all data loaders of an application by service name
        :param service_name : Service name of the data loader.. : type string
        """
        payload = {}
        
        if service_name is not None:
            payload["service_name"] = service_name

        # Parameter validation
        schema = ContentValidator.getDataLoadersByService()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/service/{service_name}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string","example":"13741"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"name":"service_name","in":"path","description":"Service name of the data loader..","required":true,"schema":{"type":"string","example":"catalog"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string","example":"13741"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"name":"service_name","in":"path","description":"Service name of the data loader..","required":true,"schema":{"type":"string","example":"catalog"}}]}""", serverType="platform", service_name=service_name)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/service/{service_name}", service_name=service_name), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DataLoaderResponseSchema
            schema = DataLoaderResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDataLoadersByService")
                print(e)

        return response
    
    async def selectDataLoader(self, data_loader_id=None, request_headers:Dict={}):
        """Choose and set a data loader for use.
        :param data_loader_id : ID allotted to the data loader. : type string
        """
        payload = {}
        
        if data_loader_id is not None:
            payload["data_loader_id"] = data_loader_id

        # Parameter validation
        schema = ContentValidator.selectDataLoader()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}/select", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", data_loader_id=data_loader_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}/select", data_loader_id=data_loader_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DataLoaderResponseSchema
            schema = DataLoaderResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for selectDataLoader")
                print(e)

        return response
    
    async def resetDataLoader(self, service=None, operation_id=None, request_headers:Dict={}):
        """Clear and reset data loader settings.
        :param service : Name of service. : type string
        :param operation_id : Name of operation id of the service. : type string
        """
        payload = {}
        
        if service is not None:
            payload["service"] = service
        if operation_id is not None:
            payload["operation_id"] = operation_id

        # Parameter validation
        schema = ContentValidator.resetDataLoader()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{service}/{operation_id}/reset", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"service","in":"path","description":"Name of service.","required":true,"schema":{"type":"string"}},{"name":"operation_id","in":"path","description":"Name of operation id of the service.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"service","in":"path","description":"Name of service.","required":true,"schema":{"type":"string"}},{"name":"operation_id","in":"path","description":"Name of operation id of the service.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", service=service, operation_id=operation_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{service}/{operation_id}/reset", service=service, operation_id=operation_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DataLoaderResetResponseSchema
            schema = DataLoaderResetResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for resetDataLoader")
                print(e)

        return response
    
    async def getFaqCategories(self, request_headers:Dict={}):
        """List all FAQ Categories
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getFaqCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/categories", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/categories", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetFaqCategoriesSchema
            schema = GetFaqCategoriesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFaqCategories")
                print(e)

        return response
    
    async def getFaqCategoryBySlugOrId(self, id_or_slug=None, request_headers:Dict={}):
        """Get detailed information about a specific FAQ category
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug is not None:
            payload["id_or_slug"] = id_or_slug

        # Parameter validation
        schema = ContentValidator.getFaqCategoryBySlugOrId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id_or_slug=id_or_slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}", id_or_slug=id_or_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetFaqCategoryBySlugSchema
            schema = GetFaqCategoryBySlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFaqCategoryBySlugOrId")
                print(e)

        return response
    
    async def createFaqCategory(self, body="", request_headers:Dict={}):
        """Generate and add a new FAQ category.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createFaqCategory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateFaqCategoryRequestSchema
        schema = CreateFaqCategoryRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateFaqCategorySchema
            schema = CreateFaqCategorySchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createFaqCategory")
                print(e)

        return response
    
    async def updateFaqCategory(self, id=None, body="", request_headers:Dict={}):
        """Modify the content and settings of a specific FAQ category.
        :param id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.updateFaqCategory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateFaqCategoryRequestSchema
        schema = UpdateFaqCategoryRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateFaqCategorySchema
            schema = CreateFaqCategorySchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateFaqCategory")
                print(e)

        return response
    
    async def deleteFaqCategory(self, id=None, request_headers:Dict={}):
        """Remove a specific FAQ category.
        :param id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deleteFaqCategory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FaqSchema
            schema = FaqSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteFaqCategory")
                print(e)

        return response
    
    async def getFaqsByCategoryIdOrSlug(self, id_or_slug=None, request_headers:Dict={}):
        """Retrieve a list of FAQs within a specific category.
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug is not None:
            payload["id_or_slug"] = id_or_slug

        # Parameter validation
        schema = ContentValidator.getFaqsByCategoryIdOrSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}/faqs", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id_or_slug=id_or_slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}/faqs", id_or_slug=id_or_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetFaqSchema
            schema = GetFaqSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFaqsByCategoryIdOrSlug")
                print(e)

        return response
    
    async def addFaq(self, category_id=None, body="", request_headers:Dict={}):
        """Create and add a new FAQ.
        :param category_id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if category_id is not None:
            payload["category_id"] = category_id

        # Parameter validation
        schema = ContentValidator.addFaq()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateFaqSchema
        schema = CreateFaqSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", category_id=category_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq", category_id=category_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateFaqResponseSchema
            schema = CreateFaqResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addFaq")
                print(e)

        return response
    
    async def updateFaq(self, category_id=None, faq_id=None, body="", request_headers:Dict={}):
        """Modify the content and settings of a specific FAQ.
        :param category_id : ID allotted to an FAQ category. : type string
        :param faq_id : ID allotted to an FAQ. : type string
        """
        payload = {}
        
        if category_id is not None:
            payload["category_id"] = category_id
        if faq_id is not None:
            payload["faq_id"] = faq_id

        # Parameter validation
        schema = ContentValidator.updateFaq()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateFaqSchema
        schema = CreateFaqSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", category_id=category_id, faq_id=faq_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", category_id=category_id, faq_id=faq_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateFaqResponseSchema
            schema = CreateFaqResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateFaq")
                print(e)

        return response
    
    async def deleteFaq(self, category_id=None, faq_id=None, request_headers:Dict={}):
        """Remove a specific FAQ.
        :param category_id : ID allotted to an FAQ category. : type string
        :param faq_id : ID allotted to an FAQ. : type string
        """
        payload = {}
        
        if category_id is not None:
            payload["category_id"] = category_id
        if faq_id is not None:
            payload["faq_id"] = faq_id

        # Parameter validation
        schema = ContentValidator.deleteFaq()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", category_id=category_id, faq_id=faq_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", category_id=category_id, faq_id=faq_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateFaqResponseSchema
            schema = CreateFaqResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteFaq")
                print(e)

        return response
    
    async def getFaqByIdOrSlug(self, id_or_slug=None, request_headers:Dict={}):
        """Get detailed information about a specific FAQ
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug is not None:
            payload["id_or_slug"] = id_or_slug

        # Parameter validation
        schema = ContentValidator.getFaqByIdOrSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/{id_or_slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id_or_slug=id_or_slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/{id_or_slug}", id_or_slug=id_or_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateFaqResponseSchema
            schema = CreateFaqResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFaqByIdOrSlug")
                print(e)

        return response
    
    async def generateSEOTitle(self, type=None, body="", request_headers:Dict={}):
        """Create an SEO-friendly title for content.
        :param type : String representing the type of SEO content to be generated. Possible values are: title, description : type 
        """
        payload = {}
        
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = ContentValidator.generateSEOTitle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GenerateSEOContent
        schema = GenerateSEOContent()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/generate-seo/{type}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"type","in":"path","description":"String representing the type of SEO content to be generated. Possible values are: title, description","required":true,"schema":{"$ref":"#/components/schemas/GenerationEntityType"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"type","in":"path","description":"String representing the type of SEO content to be generated. Possible values are: title, description","required":true,"schema":{"$ref":"#/components/schemas/GenerationEntityType"}}]}""", serverType="platform", type=type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/generate-seo/{type}", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GeneratedSEOContent
            schema = GeneratedSEOContent()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for generateSEOTitle")
                print(e)

        return response
    
    async def getLandingPages(self, page_no=None, page_size=None, request_headers:Dict={}):
        """Lists a list landing pages as per device types
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getLandingPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LandingPageGetDetails
            schema = LandingPageGetDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLandingPages")
                print(e)

        return response
    
    async def createLandingPage(self, body="", request_headers:Dict={}):
        """Generate and add a new landing page.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createLandingPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import LandingPageSchema
        schema = LandingPageSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LandingPageSchema
            schema = LandingPageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createLandingPage")
                print(e)

        return response
    
    async def updateLandingPage(self, id=None, body="", request_headers:Dict={}):
        """Modify the content and settings of a specific landing page.
        :param id : ID allotted to a landing page. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.updateLandingPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import LandingPageSchema
        schema = LandingPageSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LandingPageSchema
            schema = LandingPageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateLandingPage")
                print(e)

        return response
    
    async def deleteLandingPage(self, id=None, request_headers:Dict={}):
        """Remove a specific landing page.
        :param id : ID allotted to a landing page. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deleteLandingPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LandingPageSchema
            schema = LandingPageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteLandingPage")
                print(e)

        return response
    
    async def getLegalInformation(self, request_headers:Dict={}):
        """Get legal information and terms
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getLegalInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationLegal
            schema = ApplicationLegal()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLegalInformation")
                print(e)

        return response
    
    async def updateLegalInformation(self, body="", request_headers:Dict={}):
        """Modify legal information and terms.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateLegalInformation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationLegal
        schema = ApplicationLegal()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationLegal
            schema = ApplicationLegal()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateLegalInformation")
                print(e)

        return response
    
    async def getNavigations(self, device_platform=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve a list of navigational elements.
        :param device_platform : Filter navigations by platform. Acceptable values are: web, android, ios, all : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if device_platform is not None:
            payload["device_platform"] = device_platform
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getNavigations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", device_platform=device_platform, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(device_platform=device_platform, page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", device_platform=device_platform, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import NavigationGetDetails
            schema = NavigationGetDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNavigations")
                print(e)

        return response
    
    async def createNavigation(self, body="", request_headers:Dict={}):
        """Generate and add a new navigation element.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createNavigation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import NavigationPayload
        schema = NavigationPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import NavigationSchema
            schema = NavigationSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createNavigation")
                print(e)

        return response
    
    async def getDefaultNavigations(self, request_headers:Dict={}):
        """Retrieve default navigation elements.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getDefaultNavigations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/default", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/default", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DefaultNavigationDetails
            schema = DefaultNavigationDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDefaultNavigations")
                print(e)

        return response
    
    async def getNavigationBySlug(self, slug=None, device_platform=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific navigation element.
        :param slug : A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API. : type string
        :param device_platform : Filter navigations by platform. Acceptable values are: web, android, ios. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if device_platform is not None:
            payload["device_platform"] = device_platform

        # Parameter validation
        schema = ContentValidator.getNavigationBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios.","required":false,"schema":{"type":"string","enum":["ios","web","android"]}}],"query":[{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios.","required":false,"schema":{"type":"string","enum":["ios","web","android"]}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug, device_platform=device_platform)
        query_string = await create_query_string(device_platform=device_platform)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{slug}", slug=slug, device_platform=device_platform), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import NavigationSchema
            schema = NavigationSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNavigationBySlug")
                print(e)

        return response
    
    async def updateNavigation(self, id=None, body="", request_headers:Dict={}):
        """Modify the content and settings of a specific navigation element.
        :param id : ID allotted to the navigation. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.updateNavigation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import NavigationPayload
        schema = NavigationPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import NavigationSchema
            schema = NavigationSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateNavigation")
                print(e)

        return response
    
    async def deleteNavigation(self, id=None, request_headers:Dict={}):
        """Remove a specific navigation element.
        :param id : ID allotted to the navigation. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deleteNavigation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import NavigationSchema
            schema = NavigationSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteNavigation")
                print(e)

        return response
    
    async def getPageMeta(self, request_headers:Dict={}):
        """Use this API to Get metadata for a specific page.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getPageMeta()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/meta", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/meta", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PageMetaSchema
            schema = PageMetaSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPageMeta")
                print(e)

        return response
    
    async def getPageSpec(self, request_headers:Dict={}):
        """Use this API to Get specifications and details for a specific page
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getPageSpec()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/spec", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/spec", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PageSpec
            schema = PageSpec()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPageSpec")
                print(e)

        return response
    
    async def createPagePreview(self, body="", request_headers:Dict={}):
        """Generate and add a new page preview.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createPagePreview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PagePayload
        schema = PagePayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/preview/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/preview/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PageSchema
            schema = PageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPagePreview")
                print(e)

        return response
    
    async def updatePagePreview(self, slug=None, body="", request_headers:Dict={}):
        """Modify the content and settings of a specific page preview.
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.updatePagePreview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PagePublishPayload
        schema = PagePublishPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/publish/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/publish/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PageSchema
            schema = PageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePagePreview")
                print(e)

        return response
    
    async def deletePage(self, id=None, request_headers:Dict={}):
        """Remove a page from the platform.
        :param id : ID allotted to the page. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PageSchema
            schema = PageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deletePage")
                print(e)

        return response
    
    async def addPathRedirectionRules(self, body="", request_headers:Dict={}):
        """Create and add rules for path redirection.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.addPathRedirectionRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PathMappingSchema
        schema = PathMappingSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PathMappingSchema
            schema = PathMappingSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addPathRedirectionRules")
                print(e)

        return response
    
    async def getPathRedirectionRules(self, page_size=None, page_no=None, request_headers:Dict={}):
        """Use this API to List Path Redirection Rules
        :param page_size : The number of items to retrieve in each page. Default value is 5.  : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        """
        payload = {}
        
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no

        # Parameter validation
        schema = ContentValidator.getPathRedirectionRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 5. ","required":false,"schema":{"type":"integer","default":5}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 5. ","required":false,"schema":{"type":"integer","default":5}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_size=page_size, page_no=page_no)
        query_string = await create_query_string(page_size=page_size, page_no=page_no)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PathMappingSchema
            schema = PathMappingSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPathRedirectionRules")
                print(e)

        return response
    
    async def getPathRedirectionRule(self, path_id=None, request_headers:Dict={}):
        """Use this API to Get detailed information about a specific path redirection rule
        :param path_id : ID allotted to the path redirection rule. : type string
        """
        payload = {}
        
        if path_id is not None:
            payload["path_id"] = path_id

        # Parameter validation
        schema = ContentValidator.getPathRedirectionRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", path_id=path_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", path_id=path_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PathMappingSchema
            schema = PathMappingSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPathRedirectionRule")
                print(e)

        return response
    
    async def updatePathRedirectionRules(self, path_id=None, body="", request_headers:Dict={}):
        """Modify settings for path redirection rules.
        :param path_id : ID allotted to the path redirection rule. : type string
        """
        payload = {}
        
        if path_id is not None:
            payload["path_id"] = path_id

        # Parameter validation
        schema = ContentValidator.updatePathRedirectionRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PathMappingSchema
        schema = PathMappingSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", path_id=path_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", path_id=path_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PathMappingSchema
            schema = PathMappingSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePathRedirectionRules")
                print(e)

        return response
    
    async def deletePathRedirectionRules(self, path_id=None, request_headers:Dict={}):
        """Remove specific path redirection rules.
        :param path_id : ID allotted to the path redirection rule. : type string
        """
        payload = {}
        
        if path_id is not None:
            payload["path_id"] = path_id

        # Parameter validation
        schema = ContentValidator.deletePathRedirectionRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", path_id=path_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", path_id=path_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getSEOConfiguration(self, request_headers:Dict={}):
        """Retrieve configuration settings for SEO.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSEOConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SeoComponent
            schema = SeoComponent()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSEOConfiguration")
                print(e)

        return response
    
    async def updateSEOConfiguration(self, body="", request_headers:Dict={}):
        """Modify configuration settings for SEO.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateSEOConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SeoComponent
        schema = SeoComponent()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SeoSchema
            schema = SeoSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSEOConfiguration")
                print(e)

        return response
    
    async def getDefaultSEOMarkupSchema(self, page_type=None, request_headers:Dict={}):
        """Use this API to List default SEO Markup Schemas
        :param page_type : The type of page against which schema template was created : type string
        """
        payload = {}
        
        if page_type is not None:
            payload["page_type"] = page_type

        # Parameter validation
        schema = ContentValidator.getDefaultSEOMarkupSchema()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/default", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_type","in":"query","description":"The type of page against which schema template was created","required":false,"schema":{"type":"string","enum":["about-us","addresses","blog","brands","cards","cart","categories","brand","category","collection","collections","contact-us","external","faq","freshchat","home","notification-settings","orders","page","policy","product","product-request","products","profile","profile-order-shipment","profile-basic","profile-company","profile-emails","profile-phones","rate-us","refer-earn","settings","shared-cart","tnc","track-order","wishlist","sections","form","cart-delivery","cart-payment","cart-review","login","register","shipping-policy","return-policy","order-status"]}}],"query":[{"name":"page_type","in":"query","description":"The type of page against which schema template was created","required":false,"schema":{"type":"string","enum":["about-us","addresses","blog","brands","cards","cart","categories","brand","category","collection","collections","contact-us","external","faq","freshchat","home","notification-settings","orders","page","policy","product","product-request","products","profile","profile-order-shipment","profile-basic","profile-company","profile-emails","profile-phones","rate-us","refer-earn","settings","shared-cart","tnc","track-order","wishlist","sections","form","cart-delivery","cart-payment","cart-review","login","register","shipping-policy","return-policy","order-status"]}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_type=page_type)
        query_string = await create_query_string(page_type=page_type)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/default", page_type=page_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DefaultSchemaComponent
            schema = DefaultSchemaComponent()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDefaultSEOMarkupSchema")
                print(e)

        return response
    
    async def getSEOMarkupSchemas(self, title=None, active=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Use this API to List default SEO Markup Schemas
        :param title : Title of the seo schema. : type string
        :param active : Boolean value for fetching seo schema. : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if title is not None:
            payload["title"] = title
        if active is not None:
            payload["active"] = active
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getSEOMarkupSchemas()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"title","in":"query","description":"Title of the seo schema.","required":false,"schema":{"type":"string"}},{"name":"active","in":"query","description":"Boolean value for fetching seo schema.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"title","in":"query","description":"Title of the seo schema.","required":false,"schema":{"type":"string"}},{"name":"active","in":"query","description":"Boolean value for fetching seo schema.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", title=title, active=active, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(title=title, active=active, page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema", title=title, active=active, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SeoSchemaComponent
            schema = SeoSchemaComponent()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSEOMarkupSchemas")
                print(e)

        return response
    
    async def createSEOMarkupSchema(self, body="", request_headers:Dict={}):
        """Use this API to Create SEO Markup Schema
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createSEOMarkupSchema()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SEOSchemaMarkupTemplateRequestBody
        schema = SEOSchemaMarkupTemplateRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SEOSchemaMarkupTemplate
            schema = SEOSchemaMarkupTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSEOMarkupSchema")
                print(e)

        return response
    
    async def getSEOMarkupSchema(self, id=None, request_headers:Dict={}):
        """Use this API to Get SEO Markup Schema
        :param id : Alphanumeric ID allotted to a SEO Markup Schema Template created within a business. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.getSEOMarkupSchema()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SEOSchemaMarkupTemplate
            schema = SEOSchemaMarkupTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSEOMarkupSchema")
                print(e)

        return response
    
    async def editSEOMarkupSchema(self, id=None, body="", request_headers:Dict={}):
        """Use this API to Get SEO Markup Schema
        :param id : Alphanumeric ID allotted to a SEO Markup Schema Template created within a business. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.editSEOMarkupSchema()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SEOSchemaMarkupTemplateRequestBody
        schema = SEOSchemaMarkupTemplateRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SEOSchemaMarkupTemplate
            schema = SEOSchemaMarkupTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editSEOMarkupSchema")
                print(e)

        return response
    
    async def deleteSEOMarkupSchema(self, id=None, request_headers:Dict={}):
        """Use this API to Delete SEO Markup Schema
        :param id : Alphanumeric ID allotted to a SEO Markup Schema Template created within a business. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deleteSEOMarkupSchema()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SEOSchemaMarkupTemplate
            schema = SEOSchemaMarkupTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSEOMarkupSchema")
                print(e)

        return response
    
    async def getSlideshows(self, device_platform=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Use this API to list all Slideshows
        :param device_platform : Filter slideshows by platform. Acceptable values are: web, android, ios and all : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if device_platform is not None:
            payload["device_platform"] = device_platform
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getSlideshows()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", device_platform=device_platform, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(device_platform=device_platform, page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows", device_platform=device_platform, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SlideshowGetDetails
            schema = SlideshowGetDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSlideshows")
                print(e)

        return response
    
    async def createSlideshow(self, body="", request_headers:Dict={}):
        """Use this API to create a slideshow.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createSlideshow()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SlideshowPayload
        schema = SlideshowPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SlideshowSchema
            schema = SlideshowSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSlideshow")
                print(e)

        return response
    
    async def getSlideshowBySlug(self, slug=None, device_platform=None, request_headers:Dict={}):
        """Use this API to get the details of a slideshow by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API. : type string
        :param device_platform : Filter slideshows by platform. Acceptable values are: web, android, ios and all : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if device_platform is not None:
            payload["device_platform"] = device_platform

        # Parameter validation
        schema = ContentValidator.getSlideshowBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug, device_platform=device_platform)
        query_string = await create_query_string(device_platform=device_platform)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{slug}", slug=slug, device_platform=device_platform), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SlideshowSchema
            schema = SlideshowSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSlideshowBySlug")
                print(e)

        return response
    
    async def updateSlideshow(self, id=None, body="", request_headers:Dict={}):
        """Use this API to Update Slideshow
        :param id : ID allotted to the slideshow. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.updateSlideshow()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SlideshowPayload
        schema = SlideshowPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SlideshowSchema
            schema = SlideshowSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSlideshow")
                print(e)

        return response
    
    async def deleteSlideshow(self, id=None, request_headers:Dict={}):
        """Use this API to delete an existing slideshow.
        :param id : ID allotted to the slideshow. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deleteSlideshow()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SlideshowSchema
            schema = SlideshowSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSlideshow")
                print(e)

        return response
    
    async def getSupportInformation(self, request_headers:Dict={}):
        """Retrieve information related to customer support.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSupportInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Support
            schema = Support()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSupportInformation")
                print(e)

        return response
    
    async def updateSupportInformation(self, body="", request_headers:Dict={}):
        """Modify information related to customer support.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateSupportInformation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Support
        schema = Support()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Support
            schema = Support()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSupportInformation")
                print(e)

        return response
    
    async def updateInjectableTag(self, body="", request_headers:Dict={}):
        """Modify settings for an injectable tag.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateTagRequestSchema
        schema = CreateTagRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TagsSchema
            schema = TagsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateInjectableTag")
                print(e)

        return response
    
    async def getInjectableTags(self, all=None, request_headers:Dict={}):
        """Retrieve a list of injectable tags.
        :param all : Get all tags irrespective of the creator of tags : type boolean
        """
        payload = {}
        
        if all is not None:
            payload["all"] = all

        # Parameter validation
        schema = ContentValidator.getInjectableTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"all","in":"query","description":"Get all tags irrespective of the creator of tags","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"name":"all","in":"query","description":"Get all tags irrespective of the creator of tags","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", all=all)
        query_string = await create_query_string(all=all)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", all=all), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TagsSchema
            schema = TagsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInjectableTags")
                print(e)

        return response
    
    async def addInjectableTag(self, body="", request_headers:Dict={}):
        """Create and add a new injectable tag.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.addInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateTagRequestSchema
        schema = CreateTagRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/add", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/add", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TagsSchema
            schema = TagsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addInjectableTag")
                print(e)

        return response
    
    async def removeInjectableTag(self, body="", request_headers:Dict={}):
        """Delete a specific injectable tag.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.removeInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RemoveHandpickedSchema
        schema = RemoveHandpickedSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/remove/handpicked", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/remove/handpicked", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TagDeleteSuccessDetails
            schema = TagDeleteSuccessDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeInjectableTag")
                print(e)

        return response
    
    async def editInjectableTag(self, tag_id=None, body="", request_headers:Dict={}):
        """Modify settings for an injectable tag.
        :param tag_id : ID allotted to the tag. : type string
        """
        payload = {}
        
        if tag_id is not None:
            payload["tag_id"] = tag_id

        # Parameter validation
        schema = ContentValidator.editInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateHandpickedSchema
        schema = UpdateHandpickedSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/edit/handpicked/{tag_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"tag_id","in":"path","description":"ID allotted to the tag.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"tag_id","in":"path","description":"ID allotted to the tag.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", tag_id=tag_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/edit/handpicked/{tag_id}", tag_id=tag_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TagsSchema
            schema = TagsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editInjectableTag")
                print(e)

        return response
    
    async def getBlogBySlug(self, slug=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific blog using its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getBlogBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogSchema
            schema = BlogSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBlogBySlug")
                print(e)

        return response
    
    async def createPage(self, body="", request_headers:Dict={}):
        """Generate and add a new page to the platform.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PagePayload
        schema = PagePayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PageSchema
            schema = PageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPage")
                print(e)

        return response
    
    async def getPages(self, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve a list of available pages.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PageGetDetails
            schema = PageGetDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPages")
                print(e)

        return response
    
    async def updatePage(self, id=None, body="", request_headers:Dict={}):
        """Modify and update the content of a page.
        :param id : ID allotted to the page. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.updatePage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PageSchema
        schema = PageSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PageSchema
            schema = PageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePage")
                print(e)

        return response
    
    async def getPageBySlug(self, slug=None, request_headers:Dict={}):
        """Get detailed information about a specific page using its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getPageBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PageSchema
            schema = PageSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPageBySlug")
                print(e)

        return response
    
    async def getAppCustomFieldTypes(self, request_headers:Dict={}):
        """Each custom field and custom field definition has a type, which defines the type of information that it can store. The custom field types have built-in validation. This api will give list of supported custom fields types
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getAppCustomFieldTypes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/types", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/types", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MetafieldTypesSchema
            schema = MetafieldTypesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomFieldTypes")
                print(e)

        return response
    
    async def getAppResources(self, request_headers:Dict={}):
        """Each custom fields is assosiated with a resource such as product, promotion, coupon, selling location etc, This will gives list of supported resource list.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getAppResources()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/resources", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/resources", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResourcesSchema
            schema = ResourcesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppResources")
                print(e)

        return response
    
    async def getAppCustomFieldDefinitions(self, page_no=None, page_size=None, resources=None, types=None, search=None, slugs=None, namespaces=None, request_headers:Dict={}):
        """Custom field definitions enable you to include data validation for custom fields, and enable sellers to add custom fields values for resources. With the help of this seller can retrive list of custom field definitions list.
        :param page_no :  : type string
        :param page_size :  : type string
        :param resources :  : type string
        :param types :  : type string
        :param search :  : type string
        :param slugs :  : type string
        :param namespaces :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if resources is not None:
            payload["resources"] = resources
        if types is not None:
            payload["types"] = types
        if search is not None:
            payload["search"] = search
        if slugs is not None:
            payload["slugs"] = slugs
        if namespaces is not None:
            payload["namespaces"] = namespaces

        # Parameter validation
        schema = ContentValidator.getAppCustomFieldDefinitions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/definition", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}}],"optional":[{"name":"resources","in":"query","required":false,"schema":{"type":"string","description":"This is the resource for which we are fetching definitions"}},{"name":"types","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}},{"name":"slugs","in":"query","required":false,"schema":{"type":"string","description":"This is the slug list to filter custom fields definitions, it will come comma separated"}},{"name":"namespaces","in":"query","required":false,"schema":{"type":"string","description":"This is the namespace list to filter custom fields definitions, it needs to be comma separated"}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"resources","in":"query","required":false,"schema":{"type":"string","description":"This is the resource for which we are fetching definitions"}},{"name":"types","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}},{"name":"slugs","in":"query","required":false,"schema":{"type":"string","description":"This is the slug list to filter custom fields definitions, it will come comma separated"}},{"name":"namespaces","in":"query","required":false,"schema":{"type":"string","description":"This is the namespace list to filter custom fields definitions, it needs to be comma separated"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, resources=resources, types=types, search=search, slugs=slugs, namespaces=namespaces)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, resources=resources, types=types, search=search, slugs=slugs, namespaces=namespaces)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/definition", page_no=page_no, page_size=page_size, resources=resources, types=types, search=search, slugs=slugs, namespaces=namespaces), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionsSchema
            schema = CustomFieldDefinitionsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomFieldDefinitions")
                print(e)

        return response
    
    async def getAppCustomFieldDefinitionByResource(self, page_no=None, page_size=None, resource=None, types=None, search=None, slugs=None, namespaces=None, request_headers:Dict={}):
        """Custom field definitions enable you to include data validation for custom fields, and enable sellers to add custom fields values for resources. With the help of this seller can retrive list of custom field definitions list.
        :param page_no :  : type string
        :param page_size :  : type string
        :param resource :  : type string
        :param types :  : type string
        :param search :  : type string
        :param slugs :  : type string
        :param namespaces :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if resource is not None:
            payload["resource"] = resource
        if types is not None:
            payload["types"] = types
        if search is not None:
            payload["search"] = search
        if slugs is not None:
            payload["slugs"] = slugs
        if namespaces is not None:
            payload["namespaces"] = namespaces

        # Parameter validation
        schema = ContentValidator.getAppCustomFieldDefinitionByResource()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/definition", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}}],"optional":[{"name":"types","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}},{"name":"slugs","in":"query","required":false,"schema":{"type":"string","description":"This is the slug list to filter custom fields definitions, it will come comma separated"}},{"name":"namespaces","in":"query","required":false,"schema":{"type":"string","description":"This is the namespace list to filter custom fields definitions, it needs to be comma separated"}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"types","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}},{"name":"slugs","in":"query","required":false,"schema":{"type":"string","description":"This is the slug list to filter custom fields definitions, it will come comma separated"}},{"name":"namespaces","in":"query","required":false,"schema":{"type":"string","description":"This is the namespace list to filter custom fields definitions, it needs to be comma separated"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}}]}""", serverType="platform", page_no=page_no, page_size=page_size, resource=resource, types=types, search=search, slugs=slugs, namespaces=namespaces)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, types=types, search=search, slugs=slugs, namespaces=namespaces)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/definition", page_no=page_no, page_size=page_size, resource=resource, types=types, search=search, slugs=slugs, namespaces=namespaces), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionsSchema
            schema = CustomFieldDefinitionsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomFieldDefinitionByResource")
                print(e)

        return response
    
    async def createAppCustomFieldDefinition(self, resource=None, body="", request_headers:Dict={}):
        """You can create custom fields definition to any resource so you can extend property of resource.
        :param resource :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource

        # Parameter validation
        schema = ContentValidator.createAppCustomFieldDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldDefinitionRequestSchema
        schema = CustomFieldDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/definition", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}}]}""", serverType="platform", resource=resource)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/definition", resource=resource), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionDetailResSchema
            schema = CustomFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppCustomFieldDefinition")
                print(e)

        return response
    
    async def getAppCustomFieldDefinitionBySlug(self, slug=None, resource=None, namespace=None, request_headers:Dict={}):
        """Custom field definitions can be retrived from this using its slug, namespace and resource
        :param slug :  : type string
        :param resource :  : type string
        :param namespace :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if resource is not None:
            payload["resource"] = resource
        if namespace is not None:
            payload["namespace"] = namespace

        # Parameter validation
        schema = ContentValidator.getAppCustomFieldDefinitionBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}]}""", serverType="platform", slug=slug, resource=resource, namespace=namespace)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", slug=slug, resource=resource, namespace=namespace), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MetaFieldDefinitionDetailResSchema
            schema = MetaFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomFieldDefinitionBySlug")
                print(e)

        return response
    
    async def updateAppCustomFieldDefinitionBySlug(self, slug=None, resource=None, namespace=None, body="", request_headers:Dict={}):
        """Custom fields definition can be update using this api, You can update custom field definition name and description.
        :param slug :  : type string
        :param resource :  : type string
        :param namespace :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if resource is not None:
            payload["resource"] = resource
        if namespace is not None:
            payload["namespace"] = namespace

        # Parameter validation
        schema = ContentValidator.updateAppCustomFieldDefinitionBySlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldDefinitionRequestSchema
        schema = CustomFieldDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}]}""", serverType="platform", slug=slug, resource=resource, namespace=namespace)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", slug=slug, resource=resource, namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionDetailResSchema
            schema = CustomFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCustomFieldDefinitionBySlug")
                print(e)

        return response
    
    async def deleteAppCustomFieldDefinitionBySlug(self, slug=None, resource=None, namespace=None, request_headers:Dict={}):
        """Custom field definition and its assosiated custom fields value can be deleted using this api on the basis of definition id.
        :param slug :  : type string
        :param resource :  : type string
        :param namespace :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if resource is not None:
            payload["resource"] = resource
        if namespace is not None:
            payload["namespace"] = namespace

        # Parameter validation
        schema = ContentValidator.deleteAppCustomFieldDefinitionBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom field definition slug"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"namespace","in":"path","required":true,"schema":{"type":"string","description":"This is namespace for a custom field"}}]}""", serverType="platform", slug=slug, resource=resource, namespace=namespace)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/namespace/{namespace}/definition/{slug}", slug=slug, resource=resource, namespace=namespace), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomDataDeleteSchema
            schema = CustomDataDeleteSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAppCustomFieldDefinitionBySlug")
                print(e)

        return response
    
    async def getAppCustomFieldsByResourceSlug(self, resource=None, resource_slug=None, request_headers:Dict={}):
        """Retrieves a list of custom fields attached to a particular resource by using the resource and resource slug.
        :param resource :  : type string
        :param resource_slug :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource
        if resource_slug is not None:
            payload["resource_slug"] = resource_slug

        # Parameter validation
        schema = ContentValidator.getAppCustomFieldsByResourceSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/{resource_slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_slug","in":"path","required":true,"schema":{"type":"string","description":"This is the resource slug for which custom fields created"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_slug","in":"path","required":true,"schema":{"type":"string","description":"This is the resource slug for which custom fields created"}}]}""", serverType="platform", resource=resource, resource_slug=resource_slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/{resource_slug}", resource=resource, resource_slug=resource_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldsResponseByResourceIdSchema
            schema = CustomFieldsResponseByResourceIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomFieldsByResourceSlug")
                print(e)

        return response
    
    async def updateAppCustomFieldByResourceSlug(self, resource=None, resource_slug=None, body="", request_headers:Dict={}):
        """You can add a custom field using this endpoint to any resource by providing the resource slug.
        :param resource :  : type string
        :param resource_slug :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource
        if resource_slug is not None:
            payload["resource_slug"] = resource_slug

        # Parameter validation
        schema = ContentValidator.updateAppCustomFieldByResourceSlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldRequestSchema
        schema = CustomFieldRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/{resource_slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_slug","in":"path","required":true,"schema":{"type":"string","description":"This is the resource slug for which custom fields created"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the type of resource for which you want to fetch custom fields eg. product, collection, customer etc."}},{"name":"resource_slug","in":"path","required":true,"schema":{"type":"string","description":"This is the resource slug for which custom fields created"}}]}""", serverType="platform", resource=resource, resource_slug=resource_slug)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customfields/resource/{resource}/{resource_slug}", resource=resource, resource_slug=resource_slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldsResponseByResourceIdSchema
            schema = CustomFieldsResponseByResourceIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCustomFieldByResourceSlug")
                print(e)

        return response
    
    async def createAppCustomObjectDefinition(self, body="", request_headers:Dict={}):
        """Create a custom object that will have a collection of custom fields and can be used anywhere in the custom field for any resource.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createAppCustomObjectDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectDefinitionRequestSchema
        schema = CustomObjectDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSlugSchema
            schema = CustomObjectDefinitionSlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppCustomObjectDefinition")
                print(e)

        return response
    
    async def getAppCustomObjectDefinitions(self, page_no=None, page_size=None, search=None, request_headers:Dict={}):
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
        schema = ContentValidator.getAppCustomObjectDefinitions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}}],"optional":[{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, search=search)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition", page_no=page_no, page_size=page_size, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionsSchema
            schema = CustomObjectDefinitionsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomObjectDefinitions")
                print(e)

        return response
    
    async def getAppCustomObjectDefinitionBySlug(self, slug=None, request_headers:Dict={}):
        """Custom object definitions can be fetched using their custom object definition slug.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getAppCustomObjectDefinitionBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSlugSchema
            schema = CustomObjectDefinitionSlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomObjectDefinitionBySlug")
                print(e)

        return response
    
    async def updateAppCustomObjectDefinitionBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Custom object definitions can be updated using this endpoint. You can update the name and description of the custom object and add more custom field definitions to the existing custom object.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.updateAppCustomObjectDefinitionBySlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectDefinitionUpdateRequestSchema
        schema = CustomObjectDefinitionUpdateRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSlugSchema
            schema = CustomObjectDefinitionSlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCustomObjectDefinitionBySlug")
                print(e)

        return response
    
    async def deleteAppCustomObjectDefinitionBySlug(self, slug=None, request_headers:Dict={}):
        """Custom object definitions can be deleted using this endpoint by providing the definition ID.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.deleteAppCustomObjectDefinitionBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionDeleteResponseSchema
            schema = CustomObjectDefinitionDeleteResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAppCustomObjectDefinitionBySlug")
                print(e)

        return response
    
    async def getAppCustomObjectsBySlug(self, page_no=None, page_size=None, definition_slug=None, request_headers:Dict={}):
        """Custom object entries can fetch using this endpoint.
        :param page_no :  : type string
        :param page_size :  : type string
        :param definition_slug :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if definition_slug is not None:
            payload["definition_slug"] = definition_slug

        # Parameter validation
        schema = ContentValidator.getAppCustomObjectsBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{definition_slug}/entries", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, definition_slug=definition_slug)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, )

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{definition_slug}/entries", page_no=page_no, page_size=page_size, definition_slug=definition_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectsSchema
            schema = CustomObjectsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomObjectsBySlug")
                print(e)

        return response
    
    async def createAppCustomObjectBySlug(self, definition_slug=None, body="", request_headers:Dict={}):
        """Custom object entries against the custom object definition can be added using this API.
        :param definition_slug :  : type string
        """
        payload = {}
        
        if definition_slug is not None:
            payload["definition_slug"] = definition_slug

        # Parameter validation
        schema = ContentValidator.createAppCustomObjectBySlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectRequestSchemaWithoutId
        schema = CustomObjectRequestSchemaWithoutId()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{definition_slug}/entries", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", definition_slug=definition_slug)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{definition_slug}/entries", definition_slug=definition_slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectSchema
            schema = CustomObjectSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppCustomObjectBySlug")
                print(e)

        return response
    
    async def getAppCustomObjectBySlug(self, definition_slug=None, slug=None, request_headers:Dict={}):
        """Details of a custom object entry can be obtained using this endpoint.
        :param definition_slug :  : type string
        :param slug :  : type string
        """
        payload = {}
        
        if definition_slug is not None:
            payload["definition_slug"] = definition_slug
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getAppCustomObjectBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{definition_slug}/entries/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}]}""", serverType="platform", definition_slug=definition_slug, slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{definition_slug}/entries/{slug}", definition_slug=definition_slug, slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBySlugSchema
            schema = CustomObjectBySlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomObjectBySlug")
                print(e)

        return response
    
    async def deleteAppCustomObjectBySlug(self, definition_slug=None, slug=None, request_headers:Dict={}):
        """A Custom object entry can be deleted by providing the custom object definition slug and custom object entry slug using this endpoint.
        :param definition_slug :  : type string
        :param slug :  : type string
        """
        payload = {}
        
        if definition_slug is not None:
            payload["definition_slug"] = definition_slug
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.deleteAppCustomObjectBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{definition_slug}/entries/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}]}""", serverType="platform", definition_slug=definition_slug, slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{definition_slug}/entries/{slug}", definition_slug=definition_slug, slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomDataDeleteSchema
            schema = CustomDataDeleteSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAppCustomObjectBySlug")
                print(e)

        return response
    
    async def updateAppCustomObjectBySlug(self, definition_slug=None, slug=None, body="", request_headers:Dict={}):
        """Custom object entries can be updated using this endpoint.
        :param definition_slug :  : type string
        :param slug :  : type string
        """
        payload = {}
        
        if definition_slug is not None:
            payload["definition_slug"] = definition_slug
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.updateAppCustomObjectBySlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectRequestSchemaWithoutId
        schema = CustomObjectRequestSchemaWithoutId()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{definition_slug}/entries/{slug}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"definition_slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object entry slug"}}]}""", serverType="platform", definition_slug=definition_slug, slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{definition_slug}/entries/{slug}", definition_slug=definition_slug, slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBySlugSchema
            schema = CustomObjectBySlugSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCustomObjectBySlug")
                print(e)

        return response
    
    async def getAppJobs(self, page=None, page_size=None, action_type=None, request_headers:Dict={}):
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
        schema = ContentValidator.getAppJobs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/jobs", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"page","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"action_type","in":"query","required":true,"schema":{"type":"string","enum":["download","upload"],"description":"This is the action type"}}],"optional":[],"query":[{"name":"page","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"}},{"name":"action_type","in":"query","required":true,"schema":{"type":"string","enum":["download","upload"],"description":"This is the action type"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}}]}""", serverType="platform", page=page, page_size=page_size, action_type=action_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/jobs", page=page, page_size=page_size, action_type=action_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBulkEntry
            schema = CustomObjectBulkEntry()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppJobs")
                print(e)

        return response
    
    async def importAppCustomObjectEntriesBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Custom object bulk import of bulk entries can be performed using this endpoint.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.importAppCustomObjectEntriesBySlug()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectBulkSchema
        schema = CustomObjectBulkSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}/bulk/upload", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}/bulk/upload", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectEntryBulkUploadDetails
            schema = CustomObjectEntryBulkUploadDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for importAppCustomObjectEntriesBySlug")
                print(e)

        return response
    
    async def exportAppCustomObjectEntriesBySlug(self, slug=None, request_headers:Dict={}):
        """Custom object bulk export of bulk entries can be perform using this endpoint.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.exportAppCustomObjectEntriesBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}/bulk/download", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}/bulk/download", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBulkEntryInitiateDownload
            schema = CustomObjectBulkEntryInitiateDownload()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for exportAppCustomObjectEntriesBySlug")
                print(e)

        return response
    
    async def sampleAppCustomObjectBulkEntryBySlug(self, slug=None, request_headers:Dict={}):
        """Sample files for custom object bulk import can be obtained from this endpoint.
        :param slug :  : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.sampleAppCustomObjectBulkEntryBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}/bulk/sample", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"}},{"name":"slug","in":"path","required":true,"schema":{"type":"string","description":"This is custom object definition slug"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/customobjects/definition/{slug}/bulk/sample", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    