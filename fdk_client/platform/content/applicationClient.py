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
        """Announcements are useful to highlight a message or information on top of a webpage. Use this API to retrieve a list of announcements.	
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Announcements are useful to highlight a message or information on top of a webpage. Use this API to create an announcement.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createAnnouncement()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AdminAnnouncementSchema
        schema = AdminAnnouncementSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to retrieve an announcement and its details such as the target platform and pages on which it's applicable
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id is not None:
            payload["announcement_id"] = announcement_id

        # Parameter validation
        schema = ContentValidator.getAnnouncementById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", announcement_id=announcement_id)
        query_string = await create_query_string(announcement_id=announcement_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to edit an existing announcement and its details such as the target platform and pages on which it's applicable
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", announcement_id=announcement_id)
        query_string = await create_query_string(announcement_id=announcement_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to edit the duration, i.e. start date-time and end date-time of an announcement. Moreover, you can enable/disable an announcement using this API.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", announcement_id=announcement_id)
        query_string = await create_query_string(announcement_id=announcement_id)

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to delete an existing announcement.
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id is not None:
            payload["announcement_id"] = announcement_id

        # Parameter validation
        schema = ContentValidator.deleteAnnouncement()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", announcement_id=announcement_id)
        query_string = await create_query_string(announcement_id=announcement_id)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to create a blog.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createBlog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BlogRequest
        schema = BlogRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogSchema
            schema = BlogSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createBlog")
                print(e)

        return response
    
    async def getBlogs(self, page_no=None, page_size=None, request_headers:Dict={}):
        """Use this API to get a list of blogs along with their details, such as the title, reading time, publish status, feature image, tags, author, etc.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ContentValidator.getBlogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogGetResponse
            schema = BlogGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBlogs")
                print(e)

        return response
    
    async def updateBlog(self, id=None, body="", request_headers:Dict={}):
        """Use this API to update the details of an existing blog which includes title, feature image, content, SEO details, expiry, etc.
        :param id : ID allotted to the blog. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.updateBlog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BlogRequest
        schema = BlogRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to delete a blog.
        :param id : ID allotted to the blog. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deleteBlog()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogSchema
            schema = BlogSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteBlog")
                print(e)

        return response
    
    async def getComponentById(self, slug=None, request_headers:Dict={}):
        """Use this API to retrieve the components of a blog, such as title, slug, feature image, content, schedule, publish status, author, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getComponentById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import BlogSchema
            schema = BlogSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getComponentById")
                print(e)

        return response
    
    async def addDataLoader(self, body="", request_headers:Dict={}):
        """Use this API to add data loader. This includes the data loader name, operationId, service name and its type (url/function) with corresponding value.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.addDataLoader()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DataLoaderSchema
        schema = DataLoaderSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this to get all data loaders of an application
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getDataLoaders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to delete data loader.
        :param data_loader_id : ID allotted to the data loader. : type string
        """
        payload = {}
        
        if data_loader_id is not None:
            payload["data_loader_id"] = data_loader_id

        # Parameter validation
        schema = ContentValidator.deleteDataLoader()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}]}""", data_loader_id=data_loader_id)
        query_string = await create_query_string(data_loader_id=data_loader_id)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", data_loader_id=data_loader_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to edit the details of an existing data loader by its ID.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}]}""", data_loader_id=data_loader_id)
        query_string = await create_query_string(data_loader_id=data_loader_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", data_loader_id=data_loader_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/service/{service_name}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string","example":"13741"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"name":"service_name","in":"path","description":"Service name of the data loader..","required":true,"schema":{"type":"string","example":"catalog"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string","example":"13741"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"name":"service_name","in":"path","description":"Service name of the data loader..","required":true,"schema":{"type":"string","example":"catalog"}}]}""", service_name=service_name)
        query_string = await create_query_string(service_name=service_name)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/service/{service_name}", service_name=service_name), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to select a data loader to be used in applications.
        :param data_loader_id : ID allotted to the data loader. : type string
        """
        payload = {}
        
        if data_loader_id is not None:
            payload["data_loader_id"] = data_loader_id

        # Parameter validation
        schema = ContentValidator.selectDataLoader()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}/select", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}]}""", data_loader_id=data_loader_id)
        query_string = await create_query_string(data_loader_id=data_loader_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}/select", data_loader_id=data_loader_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to reselect a data loader.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{service}/{operation_id}/reset", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"service","in":"path","description":"Name of service.","required":true,"schema":{"type":"string"}},{"name":"operation_id","in":"path","description":"Name of operation id of the service.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"service","in":"path","description":"Name of service.","required":true,"schema":{"type":"string"}},{"name":"operation_id","in":"path","description":"Name of operation id of the service.","required":true,"schema":{"type":"string"}}]}""", service=service, operation_id=operation_id)
        query_string = await create_query_string(service=service, operation_id=operation_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{service}/{operation_id}/reset", service=service, operation_id=operation_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """FAQs can be divided into categories. Use this API to get a list of FAQ categories.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getFaqCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/categories", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/categories", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """FAQs can be divided into categories. Use this API to get an FAQ categories using its slug or ID.
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug is not None:
            payload["id_or_slug"] = id_or_slug

        # Parameter validation
        schema = ContentValidator.getFaqCategoryBySlugOrId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", id_or_slug=id_or_slug)
        query_string = await create_query_string(id_or_slug=id_or_slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}", id_or_slug=id_or_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """FAQs help users to solve an issue or know more about a process. FAQs can be categorized separately, for e.g. some questions can be related to payment, some could be related to purchase, shipping, navigating, etc. Use this API to create an FAQ category.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createFaqCategory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateFaqCategoryRequestSchema
        schema = CreateFaqCategoryRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to edit an existing FAQ category.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to delete an FAQ category.
        :param id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deleteFaqCategory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to retrieve all the commonly asked question and answers belonging to an FAQ category.
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug is not None:
            payload["id_or_slug"] = id_or_slug

        # Parameter validation
        schema = ContentValidator.getFaqsByCategoryIdOrSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}/faqs", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", id_or_slug=id_or_slug)
        query_string = await create_query_string(id_or_slug=id_or_slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}/faqs", id_or_slug=id_or_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """FAQs help users to solve an issue or know more about a process. Use this API to create an FAQ for a given FAQ category.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}]}""", category_id=category_id)
        query_string = await create_query_string(category_id=category_id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq", category_id=category_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to edit an existing FAQ.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}]}""", category_id=category_id, faq_id=faq_id)
        query_string = await create_query_string(category_id=category_id, faq_id=faq_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", category_id=category_id, faq_id=faq_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to delete an existing FAQ.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}]}""", category_id=category_id, faq_id=faq_id)
        query_string = await create_query_string(category_id=category_id, faq_id=faq_id)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", category_id=category_id, faq_id=faq_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to retrieve a specific FAQ. You will get the question and answer of that FAQ.
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug is not None:
            payload["id_or_slug"] = id_or_slug

        # Parameter validation
        schema = ContentValidator.getFaqByIdOrSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/{id_or_slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", id_or_slug=id_or_slug)
        query_string = await create_query_string(id_or_slug=id_or_slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/{id_or_slug}", id_or_slug=id_or_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to get GPT3 generated SEO meta tag title for content
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/generate-seo/{type}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"type","in":"path","description":"String representing the type of SEO content to be generated. Possible values are: title, description","required":true,"schema":{"$ref":"#/components/schemas/GenerationEntityType"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"type","in":"path","description":"String representing the type of SEO content to be generated. Possible values are: title, description","required":true,"schema":{"$ref":"#/components/schemas/GenerationEntityType"}}]}""", type=type)
        query_string = await create_query_string(type=type)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/generate-seo/{type}", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Landing page is the first page that a prospect lands upon while visiting a website. Use this API to fetch a list of landing pages.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import LandingPageGetResponse
            schema = LandingPageGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLandingPages")
                print(e)

        return response
    
    async def createLandingPage(self, body="", request_headers:Dict={}):
        """Landing page is the first page that a prospect lands upon while visiting a website. Use this API to create a landing page.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createLandingPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import LandingPageSchema
        schema = LandingPageSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to edit the details of an existing landing page.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to delete an existing landing page.
        :param id : ID allotted to a landing page. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deleteLandingPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to get the legal information of an application, which includes Policy, Terms and Conditions, Shipping Policy and FAQ regarding the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getLegalInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to edit, update and save the legal information of an application, which includes Policy, Terms and Conditions, Shipping Policy and FAQ regarding the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateLegalInformation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplicationLegal
        schema = ApplicationLegal()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to fetch the navigations details which includes the items of the navigation pane. It also shows the orientation, links, sub-navigations, etc.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", device_platform=device_platform, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", device_platform=device_platform, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import NavigationGetResponse
            schema = NavigationGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNavigations")
                print(e)

        return response
    
    async def createNavigation(self, body="", request_headers:Dict={}):
        """Navigation is the arrangement of navigational items to ease the accessibility of resources for users on a website. Use this API to create a navigation.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createNavigation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import NavigationRequest
        schema = NavigationRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """On any website (application), there are navigations that are present by default. Use this API to retrieve those default navigations.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getDefaultNavigations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/default", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/default", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import DefaultNavigationResponse
            schema = DefaultNavigationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDefaultNavigations")
                print(e)

        return response
    
    async def getNavigationBySlug(self, slug=None, device_platform=None, request_headers:Dict={}):
        """Use this API to retrieve a navigation by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API. : type string
        :param device_platform : Filter navigations by platform. Acceptable values are: web, android, ios, all : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if device_platform is not None:
            payload["device_platform"] = device_platform

        # Parameter validation
        schema = ContentValidator.getNavigationBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug, device_platform=device_platform)
        query_string = await create_query_string(slug=slug, device_platform=device_platform)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{slug}", slug=slug, device_platform=device_platform), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to edit the details of an existing navigation.
        :param id : ID allotted to the navigation. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.updateNavigation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import NavigationRequest
        schema = NavigationRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to delete an existing navigation.
        :param id : ID allotted to the navigation. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deleteNavigation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to get the meta of custom pages (blog, page) and default system pages (e.g. home/brand/category/collection).
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getPageMeta()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/meta", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/meta", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to get the specifications of a page, such as page type, display name, params and query.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getPageSpec()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/spec", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/spec", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to create a page preview to check the appearance of a custom page.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createPagePreview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PageRequest
        schema = PageRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/preview/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/preview/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to change the publish status of an existing page. Allows you to publish and unpublish the page.
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.updatePagePreview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PagePublishRequest
        schema = PagePublishRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/publish/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/publish/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to delete an existing page.
        :param id : ID allotted to the page. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to add redirection rules
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.addPathRedirectionRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PathMappingSchema
        schema = PathMappingSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to get path based redirection rules.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 5. ","required":false,"schema":{"type":"integer","default":5}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 5. ","required":false,"schema":{"type":"integer","default":5}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_size=page_size, page_no=page_no)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to get path based redirection rule.
        :param path_id : ID allotted to the path redirection rule. : type string
        """
        payload = {}
        
        if path_id is not None:
            payload["path_id"] = path_id

        # Parameter validation
        schema = ContentValidator.getPathRedirectionRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}]}""", path_id=path_id)
        query_string = await create_query_string(path_id=path_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", path_id=path_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to update redirection rules
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}]}""", path_id=path_id)
        query_string = await create_query_string(path_id=path_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", path_id=path_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to delete redirection rules
        :param path_id : ID allotted to the path redirection rule. : type string
        """
        payload = {}
        
        if path_id is not None:
            payload["path_id"] = path_id

        # Parameter validation
        schema = ContentValidator.deletePathRedirectionRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}]}""", path_id=path_id)
        query_string = await create_query_string(path_id=path_id)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", path_id=path_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        return response
    
    async def getSEOConfiguration(self, request_headers:Dict={}):
        """Use this API to know how the SEO is configured in the application. This includes the sitemap, robot.txt, custom meta tags, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSEOConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to edit the SEO details of an application. This includes the sitemap, robot.txt, custom meta tags, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateSEOConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SeoComponent
        schema = SeoComponent()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to get the Default SEO Markup schema Templates setup for an application
        :param page_type : The type of page against which schema template was created : type string
        """
        payload = {}
        
        if page_type is not None:
            payload["page_type"] = page_type

        # Parameter validation
        schema = ContentValidator.getDefaultSEOMarkupSchema()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/default", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_type","in":"query","description":"The type of page against which schema template was created","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_type","in":"query","description":"The type of page against which schema template was created","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_type=page_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/default", page_type=page_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to get all SEO Markup schema Templates setup for an application
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"title","in":"query","description":"Title of the seo schema.","required":false,"schema":{"type":"string"}},{"name":"active","in":"query","description":"Boolean value for fetching seo schema.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"title","in":"query","description":"Title of the seo schema.","required":false,"schema":{"type":"string"}},{"name":"active","in":"query","description":"Boolean value for fetching seo schema.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", title=title, active=active, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema", title=title, active=active, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to create a SEO Markup schema Template inside an application
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createSEOMarkupSchema()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SEOSchemaMarkupTemplateRequestBody
        schema = SEOSchemaMarkupTemplateRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to get a existing SEO Markup schema an application
        :param id : Alphanumeric ID allotted to a SEO Markup Schema Template created within a business. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.getSEOMarkupSchema()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to edit an existing SEO Markup schema an application
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to delete an existing SEO Markup schema an application
        :param id : Alphanumeric ID allotted to a SEO Markup Schema Template created within a business. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.deleteSEOMarkupSchema()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Alphanumeric ID allotted to a SEO Markup Schema Template created within a business.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo/schema/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """A slideshow is a group of images, videos or a combination of both that are shown on the website in the form of slides. Use this API to fetch a list of slideshows.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", device_platform=device_platform, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows", device_platform=device_platform, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import SlideshowGetResponse
            schema = SlideshowGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSlideshows")
                print(e)

        return response
    
    async def createSlideshow(self, body="", request_headers:Dict={}):
        """A slideshow is a group of images, videos or a combination of both that are shown on the website in the form of slides. Use this API to create a slideshow.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createSlideshow()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SlideshowRequest
        schema = SlideshowRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to retrieve the details of a slideshow by its slug.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug, device_platform=device_platform)
        query_string = await create_query_string(slug=slug, device_platform=device_platform)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{slug}", slug=slug, device_platform=device_platform), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to edit the details of an existing slideshow.
        :param id : ID allotted to the slideshow. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ContentValidator.updateSlideshow()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SlideshowRequest
        schema = SlideshowRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to get the contact details for customer support, including emails and phone numbers.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSupportInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to edit the existing contact details for customer support, including emails and phone numbers.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateSupportInformation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Support
        schema = Support()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to edit and override all existing tags. All existing tags will be replaced by the new tags provided in body. 
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateTagRequestSchema
        schema = CreateTagRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to get the CSS and JS injected in the application in the form of tags.
        :param all : Get all tags irrespective of the creator of tags : type boolean
        """
        payload = {}
        
        if all is not None:
            payload["all"] = all

        # Parameter validation
        schema = ContentValidator.getInjectableTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"all","in":"query","description":"Get all tags irrespective of the creator of tags","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"name":"all","in":"query","description":"Get all tags irrespective of the creator of tags","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", all=all)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", all=all), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """CSS and JS can be injected in the application (website) with the help of tags. Use this API to create such tags by entering the tag name, tag type (css/js), url and position of the tag.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.addInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateTagRequestSchema
        schema = CreateTagRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/add", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/add", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to delete an existing tag.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.removeInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RemoveHandpickedSchema
        schema = RemoveHandpickedSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/remove/handpicked", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/remove/handpicked", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import TagDeleteSuccessResponse
            schema = TagDeleteSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeInjectableTag")
                print(e)

        return response
    
    async def editInjectableTag(self, tag_id=None, body="", request_headers:Dict={}):
        """Use this API to edit the details of an existing tag by its ID.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/edit/handpicked/{tag_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"tag_id","in":"path","description":"ID allotted to the tag.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"tag_id","in":"path","description":"ID allotted to the tag.","required":true,"schema":{"type":"string"}}]}""", tag_id=tag_id)
        query_string = await create_query_string(tag_id=tag_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/edit/handpicked/{tag_id}", tag_id=tag_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to retrieve the components of a blog, such as title, slug, feature image, content, schedule, publish status, author, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getBlogBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to create a custom page using a title, seo, publish status, feature image, tags, meta, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PageRequest
        schema = PageRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to retrieve a list of pages.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import PageGetResponse
            schema = PageGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPages")
                print(e)

        return response
    
    async def updatePage(self, id=None, body="", request_headers:Dict={}):
        """Use this API to edit the details of an existing page, such as its title, seo, publish status, feature image, tags, schedule, etc.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to retrieve the components of a page, such as its title, seo, publish status, feature image, tags, schedule, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = ContentValidator.getPageBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to retrieve the custom field types 
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getAppCustomFieldTypes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/types", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/types", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectByIdSchema
            schema = CustomObjectByIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomFieldTypes")
                print(e)

        return response
    
    async def getAppResources(self, request_headers:Dict={}):
        """Use this API to retrieve the resources, such as products, collections, customers, selling locations, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getAppResources()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/resources", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/resources", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ResourcesSchema
            schema = ResourcesSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppResources")
                print(e)

        return response
    
    async def getAppCustomFieldDefinitions(self, page_no=None, page_size=None, resource=None, type=None, search=None, request_headers:Dict={}):
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
        schema = ContentValidator.getAppCustomFieldDefinitions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}}],"optional":[{"name":"resource","in":"query","required":false,"schema":{"type":"string","description":"This is the resource for which we are fetching definitions"},"examples":{"success":{"value":"product"},"failure":{"value":"some"}}},{"name":"type","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"},"examples":{"success":{"value":"string_single_line"},"failure":{"value":"string_single"}}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"},"examples":{"success":{"value":"sometext"},"failure":{"value":"sometext"}}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}},{"name":"resource","in":"query","required":false,"schema":{"type":"string","description":"This is the resource for which we are fetching definitions"},"examples":{"success":{"value":"product"},"failure":{"value":"some"}}},{"name":"type","in":"query","required":false,"schema":{"type":"string","description":"This is the type of the custom fields definitions"},"examples":{"success":{"value":"string_single_line"},"failure":{"value":"string_single"}}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"},"examples":{"success":{"value":"sometext"},"failure":{"value":"sometext"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", page_no=page_no, page_size=page_size, resource=resource, type=type, search=search)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/definitions", page_no=page_no, page_size=page_size, resource=resource, type=type, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionsSchema
            schema = CustomFieldDefinitionsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomFieldDefinitions")
                print(e)

        return response
    
    async def createAppCustomFieldDefinition(self, body="", request_headers:Dict={}):
        """Use this API to create a custom field definition for your application.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createAppCustomFieldDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldDefinitionRequestSchema
        schema = CustomFieldDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/definitions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionDetailResSchema
            schema = CustomFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppCustomFieldDefinition")
                print(e)

        return response
    
    async def getAppCustomFieldDefinition(self, definition_id=None, request_headers:Dict={}):
        """Use this API to retrieve the definitions of custom fields using definition_id.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.getAppCustomFieldDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/definitions/{definition_id}", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionDetailResSchema
            schema = CustomFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomFieldDefinition")
                print(e)

        return response
    
    async def updateAppCustomFieldDefinition(self, definition_id=None, body="", request_headers:Dict={}):
        """Use this API to update a custom field definition for your application.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.updateAppCustomFieldDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldDefinitionRequestSchema
        schema = CustomFieldDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/definitions/{definition_id}", definition_id=definition_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldDefinitionDetailResSchema
            schema = CustomFieldDefinitionDetailResSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCustomFieldDefinition")
                print(e)

        return response
    
    async def deleteAppCustomFieldDefinition(self, definition_id=None, request_headers:Dict={}):
        """Use this API to delete the definitions of custom fields using definition_id. This will also delete related custom fields entries related to this definition.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.deleteAppCustomFieldDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/definitions/{definition_id}", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomDataDeleteSchema
            schema = CustomDataDeleteSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAppCustomFieldDefinition")
                print(e)

        return response
    
    async def getAppCustomFields(self, resource=None, request_headers:Dict={}):
        """Use this API to retrieve the custom fields for given resource in param.
        :param resource :  : type string
        """
        payload = {}
        
        if resource is not None:
            payload["resource"] = resource

        # Parameter validation
        schema = ContentValidator.getAppCustomFields()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/{resource}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}}]}""", resource=resource)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/{resource}", resource=resource), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldsResponseSchema
            schema = CustomFieldsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomFields")
                print(e)

        return response
    
    async def getAppCustomFieldsByResourceId(self, resource=None, resource_id=None, request_headers:Dict={}):
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
        schema = ContentValidator.getAppCustomFieldsByResourceId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/{resource}/{resource_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"},"examples":{"success":{"value":"64bb987e9a3c4b6c29d676bc"},"failure":{"value":"64bb987e9a3c4b6c29d67eee"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"},"examples":{"success":{"value":"64bb987e9a3c4b6c29d676bc"},"failure":{"value":"64bb987e9a3c4b6c29d67eee"}}}]}""", resource=resource, resource_id=resource_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/{resource}/{resource_id}", resource=resource, resource_id=resource_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldsResponseByResourceIdSchema
            schema = CustomFieldsResponseByResourceIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomFieldsByResourceId")
                print(e)

        return response
    
    async def createAppCustomFieldByResourceId(self, resource=None, resource_id=None, body="", request_headers:Dict={}):
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
        schema = ContentValidator.createAppCustomFieldByResourceId()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFieldRequestSchema
        schema = CustomFieldRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/{resource}/{resource_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"},"examples":{"success":{"value":"64bb987e9a3c4b6c29d676bc"},"failure":{"value":"64bb987e9a3c4b6c29d67eee"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"resource","in":"path","required":true,"schema":{"type":"string","description":"This is the name of resource for which you want to fetch custom fields eg. product, collection, customer etc."},"examples":{"success":{"value":"product"},"failure":{"value":"inventory"}}},{"name":"resource_id","in":"path","required":true,"schema":{"type":"string","description":"This is the resource id for which custom fields created"},"examples":{"success":{"value":"64bb987e9a3c4b6c29d676bc"},"failure":{"value":"64bb987e9a3c4b6c29d67eee"}}}]}""", resource=resource, resource_id=resource_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metafields/{resource}/{resource_id}", resource=resource, resource_id=resource_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFieldsResponseByResourceIdSchema
            schema = CustomFieldsResponseByResourceIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppCustomFieldByResourceId")
                print(e)

        return response
    
    async def createAppCustomObjectDefinition(self, body="", request_headers:Dict={}):
        """Use this API to create custom object defintion
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createAppCustomObjectDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectDefinitionRequestSchema
        schema = CustomObjectDefinitionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/definitions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSchema
            schema = CustomObjectDefinitionSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppCustomObjectDefinition")
                print(e)

        return response
    
    async def getAppCustomObjectDefinitions(self, page_no=None, page_size=None, search=None, request_headers:Dict={}):
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
        schema = ContentValidator.getAppCustomObjectDefinitions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/definitions", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}}],"optional":[{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"},"examples":{"success":{"value":"sometext"},"failure":{"value":"sometext"}}}],"query":[{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}},{"name":"search","in":"query","required":false,"schema":{"type":"string","description":"This is the search text to filter custom fields definitions"},"examples":{"success":{"value":"sometext"},"failure":{"value":"sometext"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", page_no=page_no, page_size=page_size, search=search)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/definitions", page_no=page_no, page_size=page_size, search=search), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionsSchema
            schema = CustomObjectDefinitionsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomObjectDefinitions")
                print(e)

        return response
    
    async def getAppCustomObjectDefinition(self, definition_id=None, request_headers:Dict={}):
        """Use this API to update a custom object definition for your application.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.getAppCustomObjectDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/definitions/{definition_id}", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSchema
            schema = CustomObjectDefinitionSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomObjectDefinition")
                print(e)

        return response
    
    async def updateAppCustomObjectDefinition(self, definition_id=None, body="", request_headers:Dict={}):
        """Use this API to update a custom object definition for your application.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.updateAppCustomObjectDefinition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectDefinitionUpdateRequestSchema
        schema = CustomObjectDefinitionUpdateRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/definitions/{definition_id}", definition_id=definition_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionSchema
            schema = CustomObjectDefinitionSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCustomObjectDefinition")
                print(e)

        return response
    
    async def deleteAppCustomObjectDefinition(self, definition_id=None, request_headers:Dict={}):
        """Use this API to delete a custom object definition and related data for your application.
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.deleteAppCustomObjectDefinition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/definitions/{definition_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/definitions/{definition_id}", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectDefinitionDeleteResponseSchema
            schema = CustomObjectDefinitionDeleteResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAppCustomObjectDefinition")
                print(e)

        return response
    
    async def getAppCustomObjects(self, definition_id=None, page_no=None, page_size=None, request_headers:Dict={}):
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
        schema = ContentValidator.getAppCustomObjects()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}}],"optional":[{"name":"definition_id","in":"query","required":false,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"query":[{"name":"definition_id","in":"query","required":false,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"page_no","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", definition_id=definition_id, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects", definition_id=definition_id, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectsSchema
            schema = CustomObjectsSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomObjects")
                print(e)

        return response
    
    async def createAppCustomObject(self, body="", request_headers:Dict={}):
        """Use this API to create the custom object entry.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createAppCustomObject()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectRequestSchema
        schema = CustomObjectRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectSchema
            schema = CustomObjectSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppCustomObject")
                print(e)

        return response
    
    async def getAppCustomObject(self, metaobject_id=None, request_headers:Dict={}):
        """Use this API to retrieve the custom object details and their fields details and definitions and references.
        :param metaobject_id :  : type string
        """
        payload = {}
        
        if metaobject_id is not None:
            payload["metaobject_id"] = metaobject_id

        # Parameter validation
        schema = ContentValidator.getAppCustomObject()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/{metaobject_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", metaobject_id=metaobject_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/{metaobject_id}", metaobject_id=metaobject_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectByIdSchema
            schema = CustomObjectByIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCustomObject")
                print(e)

        return response
    
    async def deleteAppCustomObject(self, metaobject_id=None, request_headers:Dict={}):
        """Use this API to delete the custom object entry by id. This will also delete related custom fields entries related to this custom object.
        :param metaobject_id :  : type string
        """
        payload = {}
        
        if metaobject_id is not None:
            payload["metaobject_id"] = metaobject_id

        # Parameter validation
        schema = ContentValidator.deleteAppCustomObject()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/{metaobject_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", metaobject_id=metaobject_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/{metaobject_id}", metaobject_id=metaobject_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomDataDeleteSchema
            schema = CustomDataDeleteSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAppCustomObject")
                print(e)

        return response
    
    async def updateAppCustomObject(self, metaobject_id=None, body="", request_headers:Dict={}):
        """Use this API to update a custom object detail for your application.
        :param metaobject_id :  : type string
        """
        payload = {}
        
        if metaobject_id is not None:
            payload["metaobject_id"] = metaobject_id

        # Parameter validation
        schema = ContentValidator.updateAppCustomObject()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectRequestSchema
        schema = CustomObjectRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/{metaobject_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"metaobject_id","in":"path","required":true,"schema":{"type":"string","description":"This is meta object id"},"examples":{"success":{"value":"65392bd912376081aafa90ff"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", metaobject_id=metaobject_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/{metaobject_id}", metaobject_id=metaobject_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectByIdSchema
            schema = CustomObjectByIdSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppCustomObject")
                print(e)

        return response
    
    async def getAppJobs(self, page=None, page_size=None, action_type=None, request_headers:Dict={}):
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
        schema = ContentValidator.getAppJobs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/jobs", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"page","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}},{"name":"action_type","in":"query","required":true,"schema":{"type":"string","description":"This is the action type"},"examples":{"success":{"value":"upload"},"failure":{"value":"upload"}}}],"optional":[],"query":[{"name":"page","in":"query","required":true,"schema":{"type":"string","description":"This is the page number"},"examples":{"success":{"value":1},"failure":{"value":1}}},{"name":"page_size","in":"query","required":true,"schema":{"type":"string","description":"This is the page size"},"examples":{"success":{"value":10},"failure":{"value":10}}},{"name":"action_type","in":"query","required":true,"schema":{"type":"string","description":"This is the action type"},"examples":{"success":{"value":"upload"},"failure":{"value":"upload"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", page=page, page_size=page_size, action_type=action_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/jobs", page=page, page_size=page_size, action_type=action_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBulkEntry
            schema = CustomObjectBulkEntry()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppJobs")
                print(e)

        return response
    
    async def importAppCustomObjectEntries(self, definition_id=None, body="", request_headers:Dict={}):
        """Use this API to upload custom object entries
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.importAppCustomObjectEntries()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomObjectBulkSchema
        schema = CustomObjectBulkSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/bulk/{definition_id}/upload", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/bulk/{definition_id}/upload", definition_id=definition_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectEntryBulkUploadResponse
            schema = CustomObjectEntryBulkUploadResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for importAppCustomObjectEntries")
                print(e)

        return response
    
    async def exportAppCustomObjectEntries(self, definition_id=None, request_headers:Dict={}):
        """Use this api to initiate download of bulk entries
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.exportAppCustomObjectEntries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/bulk/{definition_id}/download", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/bulk/{definition_id}/download", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomObjectBulkEntryInitiateDownload
            schema = CustomObjectBulkEntryInitiateDownload()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for exportAppCustomObjectEntries")
                print(e)

        return response
    
    async def sampleAppCustomObjectBulkEntry(self, definition_id=None, request_headers:Dict={}):
        """Use this api to get sample csv file 
        :param definition_id :  : type string
        """
        payload = {}
        
        if definition_id is not None:
            payload["definition_id"] = definition_id

        # Parameter validation
        schema = ContentValidator.sampleAppCustomObjectBulkEntry()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/bulk/{definition_id}/sample", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"This is company id"},"examples":{"success":{"value":1},"failure":{"value":10},"success1":{"value":1},"success2":{"value":2},"duplicateFieldExample":{"value":11},"validationErrorExample":{"value":12},"failure2":{"value":10}}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string","description":"This is application id"},"examples":{"success":{"value":"5eda528b97457fe43a733ace"},"failure":{"value":"5eda528b97457fe43a733acd"}}},{"name":"definition_id","in":"path","required":true,"schema":{"type":"string","description":"This is definition id"},"examples":{"success":{"value":"65369afad436ae0e54147e86"},"failure":{"value":"5eda528b97457fe43a733acd"}}}]}""", definition_id=definition_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/metaobjects/bulk/{definition_id}/sample", definition_id=definition_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        return response
    