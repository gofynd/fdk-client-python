

"""Content Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import ContentValidator

class Content:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getAnnouncementsList(self, page_no=None, page_size=None):
        """Announcements are useful to highlight a message or information on top of a webpage. Use this API to retrieve a list of announcements.	
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getAnnouncementsList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createAnnouncement(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAnnouncementById(self, announcement_id=None):
        """Use this API to retrieve an announcement and its details such as the target platform and pages on which it's applicable
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id:
            payload["announcement_id"] = announcement_id
        

        # Parameter validation
        schema = ContentValidator.getAnnouncementById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", announcement_id=announcement_id)
        query_string = await create_query_string(announcement_id=announcement_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateAnnouncement(self, announcement_id=None, body=""):
        """Use this API to edit an existing announcement and its details such as the target platform and pages on which it's applicable
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateAnnouncementSchedule(self, announcement_id=None, body=""):
        """Use this API to edit the duration, i.e. start date-time and end date-time of an announcement. Moreover, you can enable/disable an announcement using this API.
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteAnnouncement(self, announcement_id=None):
        """Use this API to delete an existing announcement.
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id:
            payload["announcement_id"] = announcement_id
        

        # Parameter validation
        schema = ContentValidator.deleteAnnouncement()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", announcement_id=announcement_id)
        query_string = await create_query_string(announcement_id=announcement_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createBlog(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getBlogs(self, page_no=None, page_size=None):
        """Use this API to get a list of blogs along with their details, such as the title, reading time, publish status, feature image, tags, author, etc.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getBlogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateBlog(self, id=None, body=""):
        """Use this API to update the details of an existing blog which includes title, feature image, content, SEO details, expiry, etc.
        :param id : ID allotted to the blog. : type string
        """
        payload = {}
        
        if id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteBlog(self, id=None):
        """Use this API to delete a blog.
        :param id : ID allotted to the blog. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteBlog()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getComponentById(self, slug=None):
        """Use this API to retrieve the components of a blog, such as title, slug, feature image, content, schedule, publish status, author, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = ContentValidator.getComponentById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def addDataLoader(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getDataLoaders(self, ):
        """Use this to get all data loaders of an application
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getDataLoaders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def deleteDataLoader(self, data_loader_id=None):
        """Use this API to delete data loader.
        :param data_loader_id : ID allotted to the data loader. : type string
        """
        payload = {}
        
        if data_loader_id:
            payload["data_loader_id"] = data_loader_id
        

        # Parameter validation
        schema = ContentValidator.deleteDataLoader()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}]}""", data_loader_id=data_loader_id)
        query_string = await create_query_string(data_loader_id=data_loader_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", data_loader_id=data_loader_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def editDataLoader(self, data_loader_id=None, body=""):
        """Use this API to edit the details of an existing data loader by its ID.
        :param data_loader_id : ID allotted to the data loader. : type string
        """
        payload = {}
        
        if data_loader_id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", data_loader_id=data_loader_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def selectDataLoader(self, data_loader_id=None):
        """Use this API to select a data loader to be used in applications.
        :param data_loader_id : ID allotted to the data loader. : type string
        """
        payload = {}
        
        if data_loader_id:
            payload["data_loader_id"] = data_loader_id
        

        # Parameter validation
        schema = ContentValidator.selectDataLoader()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}/select", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}]}""", data_loader_id=data_loader_id)
        query_string = await create_query_string(data_loader_id=data_loader_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}/select", data_loader_id=data_loader_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def resetDataLoader(self, service=None, operation_id=None):
        """Use this API to reselect a data loader.
        :param service : Name of service. : type string
        :param operation_id : Name of operation id of the service. : type string
        """
        payload = {}
        
        if service:
            payload["service"] = service
        
        if operation_id:
            payload["operation_id"] = operation_id
        

        # Parameter validation
        schema = ContentValidator.resetDataLoader()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{service}/{operation_id}/reset", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"service","in":"path","description":"Name of service.","required":true,"schema":{"type":"string"}},{"name":"operation_id","in":"path","description":"Name of operation id of the service.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"service","in":"path","description":"Name of service.","required":true,"schema":{"type":"string"}},{"name":"operation_id","in":"path","description":"Name of operation id of the service.","required":true,"schema":{"type":"string"}}]}""", service=service, operation_id=operation_id)
        query_string = await create_query_string(service=service, operation_id=operation_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{service}/{operation_id}/reset", service=service, operation_id=operation_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getFaqCategories(self, ):
        """FAQs can be divided into categories. Use this API to get a list of FAQ categories.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getFaqCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/categories", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/categories", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getFaqCategoryBySlugOrId(self, id_or_slug=None):
        """FAQs can be divided into categories. Use this API to get an FAQ categories using its slug or ID.
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug:
            payload["id_or_slug"] = id_or_slug
        

        # Parameter validation
        schema = ContentValidator.getFaqCategoryBySlugOrId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", id_or_slug=id_or_slug)
        query_string = await create_query_string(id_or_slug=id_or_slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}", id_or_slug=id_or_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createFaqCategory(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateFaqCategory(self, id=None, body=""):
        """Use this API to edit an existing FAQ category.
        :param id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteFaqCategory(self, id=None):
        """Use this API to delete an FAQ category.
        :param id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteFaqCategory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getFaqsByCategoryIdOrSlug(self, id_or_slug=None):
        """Use this API to retrieve all the commonly asked question and answers belonging to an FAQ category.
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug:
            payload["id_or_slug"] = id_or_slug
        

        # Parameter validation
        schema = ContentValidator.getFaqsByCategoryIdOrSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}/faqs", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", id_or_slug=id_or_slug)
        query_string = await create_query_string(id_or_slug=id_or_slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}/faqs", id_or_slug=id_or_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def addFaq(self, category_id=None, body=""):
        """FAQs help users to solve an issue or know more about a process. Use this API to create an FAQ for a given FAQ category.
        :param category_id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if category_id:
            payload["category_id"] = category_id
        

        # Parameter validation
        schema = ContentValidator.addFaq()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateFaqSchema
        schema = CreateFaqSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faqs", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}]}""", category_id=category_id)
        query_string = await create_query_string(category_id=category_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faqs", category_id=category_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateFaq(self, category_id=None, faq_id=None, body=""):
        """Use this API to edit an existing FAQ.
        :param category_id : ID allotted to an FAQ category. : type string
        :param faq_id : ID allotted to an FAQ. : type string
        """
        payload = {}
        
        if category_id:
            payload["category_id"] = category_id
        
        if faq_id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", category_id=category_id, faq_id=faq_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteFaq(self, category_id=None, faq_id=None):
        """Use this API to delete an existing FAQ.
        :param category_id : ID allotted to an FAQ category. : type string
        :param faq_id : ID allotted to an FAQ. : type string
        """
        payload = {}
        
        if category_id:
            payload["category_id"] = category_id
        
        if faq_id:
            payload["faq_id"] = faq_id
        

        # Parameter validation
        schema = ContentValidator.deleteFaq()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}]}""", category_id=category_id, faq_id=faq_id)
        query_string = await create_query_string(category_id=category_id, faq_id=faq_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", category_id=category_id, faq_id=faq_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getFaqByIdOrSlug(self, id_or_slug=None):
        """Use this API to retrieve a specific FAQ. You will get the question and answer of that FAQ.
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug:
            payload["id_or_slug"] = id_or_slug
        

        # Parameter validation
        schema = ContentValidator.getFaqByIdOrSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/{id_or_slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", id_or_slug=id_or_slug)
        query_string = await create_query_string(id_or_slug=id_or_slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/{id_or_slug}", id_or_slug=id_or_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def generateSEOTitle(self, type=None, body=""):
        """Use this API to get GPT3 generated SEO meta tag title for content
        :param type : String representing the type of SEO content to be generated. Possible values are: title, description : type 
        """
        payload = {}
        
        if type:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/generate-seo/{type}", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getLandingPages(self, page_no=None, page_size=None):
        """Landing page is the first page that a prospect lands upon while visiting a website. Use this API to fetch a list of landing pages.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getLandingPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createLandingPage(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateLandingPage(self, id=None, body=""):
        """Use this API to edit the details of an existing landing page.
        :param id : ID allotted to a landing page. : type string
        """
        payload = {}
        
        if id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteLandingPage(self, id=None):
        """Use this API to delete an existing landing page.
        :param id : ID allotted to a landing page. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteLandingPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getLegalInformation(self, ):
        """Use this API to get the legal information of an application, which includes Policy, Terms and Conditions, Shipping Policy and FAQ regarding the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getLegalInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateLegalInformation(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getNavigations(self, device_platform=None, page_no=None, page_size=None):
        """Use this API to fetch the navigations details which includes the items of the navigation pane. It also shows the orientation, links, sub-navigations, etc.
        :param device_platform : Filter navigations by platform. Acceptable values are: web, android, ios, all : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if device_platform:
            payload["device_platform"] = device_platform
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getNavigations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", device_platform=device_platform, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(device_platform=device_platform, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", device_platform=device_platform, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createNavigation(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getDefaultNavigations(self, ):
        """On any website (application), there are navigations that are present by default. Use this API to retrieve those default navigations.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getDefaultNavigations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/default", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/default", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getNavigationBySlug(self, slug=None, device_platform=None):
        """Use this API to retrieve a navigation by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API. : type string
        :param device_platform : Filter navigations by platform. Acceptable values are: web, android, ios, all : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if device_platform:
            payload["device_platform"] = device_platform
        

        # Parameter validation
        schema = ContentValidator.getNavigationBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug, device_platform=device_platform)
        query_string = await create_query_string(slug=slug, device_platform=device_platform)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{slug}", slug=slug, device_platform=device_platform), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateNavigation(self, id=None, body=""):
        """Use this API to edit the details of an existing navigation.
        :param id : ID allotted to the navigation. : type string
        """
        payload = {}
        
        if id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteNavigation(self, id=None):
        """Use this API to delete an existing navigation.
        :param id : ID allotted to the navigation. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteNavigation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getPageMeta(self, page_type=None, cart_pages=None):
        """Use this API to get the meta of custom pages (blog, page) and default system pages (e.g. home/brand/category/collection).
        :param page_type : Fetch meta by page type. Acceptable values are: system, custom and all : type string
        :param cart_pages : Pass this param value as `true` to fetch meta with cart pages : type boolean
        """
        payload = {}
        
        if page_type:
            payload["page_type"] = page_type
        
        if cart_pages:
            payload["cart_pages"] = cart_pages
        

        # Parameter validation
        schema = ContentValidator.getPageMeta()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/meta", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_type","in":"query","description":"Fetch meta by page type. Acceptable values are: system, custom and all","required":false,"schema":{"type":"string","default":"all"}},{"name":"cart_pages","in":"query","description":"Pass this param value as `true` to fetch meta with cart pages","required":false,"schema":{"type":"boolean","default":"false"}}],"query":[{"name":"page_type","in":"query","description":"Fetch meta by page type. Acceptable values are: system, custom and all","required":false,"schema":{"type":"string","default":"all"}},{"name":"cart_pages","in":"query","description":"Pass this param value as `true` to fetch meta with cart pages","required":false,"schema":{"type":"boolean","default":"false"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_type=page_type, cart_pages=cart_pages)
        query_string = await create_query_string(page_type=page_type, cart_pages=cart_pages)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/meta", page_type=page_type, cart_pages=cart_pages), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getPageSpec(self, ):
        """Use this API to get the specifications of a page, such as page type, display name, params and query.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getPageSpec()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/spec", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/spec", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updatePagePreview(self, slug=None, body=""):
        """Use this API to change the publish status of an existing page. Allows you to publish and unpublish the page.
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API. : type string
        """
        payload = {}
        
        if slug:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/publish/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deletePage(self, id=None):
        """Use this API to delete an existing page.
        :param id : ID allotted to the page. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def addPathRedirectionRules(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getPathRedirectionRules(self, page_size=None, page_no=None):
        """Use this API to get path based redirection rules.
        :param page_size : The number of items to retrieve in each page. Default value is 5.  : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        """
        payload = {}
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = ContentValidator.getPathRedirectionRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 5. ","required":false,"schema":{"type":"integer","default":5}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 5. ","required":false,"schema":{"type":"integer","default":5}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_size=page_size, page_no=page_no)
        query_string = await create_query_string(page_size=page_size, page_no=page_no)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", page_size=page_size, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getPathRedirectionRule(self, path_id=None):
        """Use this API to get path based redirection rule.
        :param path_id : ID allotted to the path redirection rule. : type string
        """
        payload = {}
        
        if path_id:
            payload["path_id"] = path_id
        

        # Parameter validation
        schema = ContentValidator.getPathRedirectionRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}]}""", path_id=path_id)
        query_string = await create_query_string(path_id=path_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", path_id=path_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updatePathRedirectionRules(self, path_id=None, body=""):
        """Use this API to update redirection rules
        :param path_id : ID allotted to the path redirection rule. : type string
        """
        payload = {}
        
        if path_id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", path_id=path_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deletePathRedirectionRules(self, path_id=None):
        """Use this API to delete redirection rules
        :param path_id : ID allotted to the path redirection rule. : type string
        """
        payload = {}
        
        if path_id:
            payload["path_id"] = path_id
        

        # Parameter validation
        schema = ContentValidator.deletePathRedirectionRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"path_id","in":"path","description":"ID allotted to the path redirection rule.","required":true,"schema":{"type":"string"}}]}""", path_id=path_id)
        query_string = await create_query_string(path_id=path_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings/{path_id}", path_id=path_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSEOConfiguration(self, ):
        """Use this API to know how the SEO is configured in the application. This includes the sitemap, robot.txt, custom meta tags, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSEOConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateSEOConfiguration(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSlideshows(self, device_platform=None, page_no=None, page_size=None):
        """A slideshow is a group of images, videos or a combination of both that are shown on the website in the form of slides. Use this API to fetch a list of slideshows.
        :param device_platform : Filter slideshows by platform. Acceptable values are: web, android, ios and all : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if device_platform:
            payload["device_platform"] = device_platform
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getSlideshows()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", device_platform=device_platform, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(device_platform=device_platform, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/", device_platform=device_platform, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createSlideshow(self, body=""):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSlideshowBySlug(self, slug=None, device_platform=None):
        """Use this API to retrieve the details of a slideshow by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API. : type string
        :param device_platform : Filter slideshows by platform. Acceptable values are: web, android, ios and all : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if device_platform:
            payload["device_platform"] = device_platform
        

        # Parameter validation
        schema = ContentValidator.getSlideshowBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug, device_platform=device_platform)
        query_string = await create_query_string(slug=slug, device_platform=device_platform)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{slug}", slug=slug, device_platform=device_platform), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateSlideshow(self, id=None, body=""):
        """Use this API to edit the details of an existing slideshow.
        :param id : ID allotted to the slideshow. : type string
        """
        payload = {}
        
        if id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteSlideshow(self, id=None):
        """Use this API to delete an existing slideshow.
        :param id : ID allotted to the slideshow. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteSlideshow()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSupportInformation(self, ):
        """Use this API to get the contact details for customer support, including emails and phone numbers.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSupportInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateSupportInformation(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateInjectableTag(self, body=""):
        """Use this API to edit the details of an existing tag. This includes the tag name, tag type (css/js), url and position of the tag.
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deleteAllInjectableTags(self, ):
        """Use this API to delete all the existing tags at once.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.deleteAllInjectableTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getInjectableTags(self, ):
        """Use this API to get all the CSS and JS injected in the application in the form of tags.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getInjectableTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def addInjectableTag(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/add", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def removeInjectableTag(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/remove/handpicked", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def editInjectableTag(self, tag_id=None, body=""):
        """Use this API to edit the details of an existing tag by its ID.
        :param tag_id : ID allotted to the tag. : type string
        """
        payload = {}
        
        if tag_id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/edit/handpicked/{tag_id}", tag_id=tag_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def createPage(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getPages(self, page_no=None, page_size=None):
        """Use this API to retrieve a list of pages.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updatePage(self, id=None, body=""):
        """Use this API to edit the details of an existing page, such as its title, seo, publish status, feature image, tags, schedule, etc.
        :param id : ID allotted to the page. : type string
        """
        payload = {}
        
        if id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getPageBySlug(self, slug=None):
        """Use this API to retrieve the components of a page, such as its title, seo, publish status, feature image, tags, schedule, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = ContentValidator.getPageBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

