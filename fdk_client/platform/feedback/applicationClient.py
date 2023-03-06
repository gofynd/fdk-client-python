

"""Feedback Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import FeedbackValidator

class Feedback:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getAttributes(self, page_no=None, page_size=None):
        """Provides a list of all attribute data.
        :param page_no : pagination page no : type integer
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = FeedbackValidator.getAttributes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/attributes/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"pagination page no","in":"query","name":"page_no","schema":{"type":"integer"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"pagination page no","in":"query","name":"page_no","schema":{"type":"integer"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/attributes/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCustomerReviews(self, id=None, entity_id=None, entity_type=None, user_id=None, media=None, rating=None, attribute_rating=None, facets=None, sort=None, next=None, start=None, limit=None, count=None, page_id=None, page_size=None):
        """The endpoint provides a list of customer reviews based on entity and provided filters
        :param id : review id : type string
        :param entity_id : entity id : type string
        :param entity_type : entity type : type string
        :param user_id : user id : type string
        :param media : media type e.g. image | video | video_file | video_link : type string
        :param rating : rating filter, 1-5 : type array
        :param attribute_rating : attribute rating filter with ma,e of attribute : type array
        :param facets : facets (true|false) : type boolean
        :param sort : sort by : default | top | recent : type string
        :param next : pagination next : type string
        :param start : pagination start : type string
        :param limit : pagination limit : type string
        :param count : pagination count : type string
        :param page_id : pagination page id : type string
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if entity_id:
            payload["entity_id"] = entity_id
        
        if entity_type:
            payload["entity_type"] = entity_type
        
        if user_id:
            payload["user_id"] = user_id
        
        if media:
            payload["media"] = media
        
        if rating:
            payload["rating"] = rating
        
        if attribute_rating:
            payload["attribute_rating"] = attribute_rating
        
        if facets:
            payload["facets"] = facets
        
        if sort:
            payload["sort"] = sort
        
        if next:
            payload["next"] = next
        
        if start:
            payload["start"] = start
        
        if limit:
            payload["limit"] = limit
        
        if count:
            payload["count"] = count
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = FeedbackValidator.getCustomerReviews()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"review id","in":"query","name":"id","schema":{"type":"string"}},{"description":"entity id","in":"query","name":"entity_id","schema":{"type":"string"}},{"description":"entity type","in":"query","name":"entity_type","schema":{"type":"string"}},{"description":"user id","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"media type e.g. image | video | video_file | video_link","in":"query","name":"media","schema":{"type":"string"}},{"description":"rating filter, 1-5","explode":false,"in":"query","name":"rating","schema":{"items":{"type":"number"},"type":"array"},"style":"form"},{"description":"attribute rating filter with ma,e of attribute","explode":false,"in":"query","name":"attribute_rating","schema":{"items":{"type":"string"},"type":"array"},"style":"form"},{"description":"facets (true|false)","in":"query","name":"facets","schema":{"type":"boolean"}},{"description":"sort by : default | top | recent","in":"query","name":"sort","schema":{"type":"string"}},{"description":"pagination next","in":"query","name":"next","schema":{"type":"string"}},{"description":"pagination start","in":"query","name":"start","schema":{"type":"string"}},{"description":"pagination limit","in":"query","name":"limit","schema":{"type":"string"}},{"description":"pagination count","in":"query","name":"count","schema":{"type":"string"}},{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"review id","in":"query","name":"id","schema":{"type":"string"}},{"description":"entity id","in":"query","name":"entity_id","schema":{"type":"string"}},{"description":"entity type","in":"query","name":"entity_type","schema":{"type":"string"}},{"description":"user id","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"media type e.g. image | video | video_file | video_link","in":"query","name":"media","schema":{"type":"string"}},{"description":"rating filter, 1-5","explode":false,"in":"query","name":"rating","schema":{"items":{"type":"number"},"type":"array"},"style":"form"},{"description":"attribute rating filter with ma,e of attribute","explode":false,"in":"query","name":"attribute_rating","schema":{"items":{"type":"string"},"type":"array"},"style":"form"},{"description":"facets (true|false)","in":"query","name":"facets","schema":{"type":"boolean"}},{"description":"sort by : default | top | recent","in":"query","name":"sort","schema":{"type":"string"}},{"description":"pagination next","in":"query","name":"next","schema":{"type":"string"}},{"description":"pagination start","in":"query","name":"start","schema":{"type":"string"}},{"description":"pagination limit","in":"query","name":"limit","schema":{"type":"string"}},{"description":"pagination count","in":"query","name":"count","schema":{"type":"string"}},{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", id=id, entity_id=entity_id, entity_type=entity_type, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, next=next, start=start, limit=limit, count=count, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(id=id, entity_id=entity_id, entity_type=entity_type, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, next=next, start=start, limit=limit, count=count, page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/", id=id, entity_id=entity_id, entity_type=entity_type, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, next=next, start=start, limit=limit, count=count, page_id=page_id, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateApprove(self, review_id=None, body=""):
        """The is used to update approve details like status and description text
        :param review_id : review id : type string
        """
        payload = {}
        
        if review_id:
            payload["review_id"] = review_id
        

        # Parameter validation
        schema = FeedbackValidator.updateApprove()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApproveRequest
        schema = ApproveRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/{review_id}/approve/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"review id","in":"path","name":"review_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"review id","in":"path","name":"review_id","required":true,"schema":{"type":"string"}}]}""", review_id=review_id)
        query_string = await create_query_string(review_id=review_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/{review_id}/approve/", review_id=review_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getHistory(self, review_id=None):
        """The is used to get the history details like status and description text
        :param review_id : review id : type string
        """
        payload = {}
        
        if review_id:
            payload["review_id"] = review_id
        

        # Parameter validation
        schema = FeedbackValidator.getHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/{review_id}/history/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"review id","in":"path","name":"review_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"review id","in":"path","name":"review_id","required":true,"schema":{"type":"string"}}]}""", review_id=review_id)
        query_string = await create_query_string(review_id=review_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/{review_id}/history/", review_id=review_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getApplicationTemplates(self, page_id=None, page_size=None):
        """Get all templates of application
        :param page_id : pagination page id : type string
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = FeedbackValidator.getApplicationTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", page_id=page_id, page_size=page_size)
        query_string = await create_query_string(page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/", page_id=page_id, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createTemplate(self, body=""):
        """Create a new template for review with following data:
- Enable media, rating and review
- Rating - active/inactive/selected rate choices, attributes, text on rate, comment for each rate, type
- Review - header, title, description, image and video meta, enable votes
        """
        payload = {}
        

        # Parameter validation
        schema = FeedbackValidator.createTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TemplateRequestList
        schema = TemplateRequestList()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getTemplateById(self, id=None):
        """Get the template for product or l3 type by ID
        :param id : template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = FeedbackValidator.getTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateTemplate(self, id=None, body=""):
        """Update existing template status, active/archive
        :param id : template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = FeedbackValidator.updateTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateTemplateRequest
        schema = UpdateTemplateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateTemplateStatus(self, id=None, body=""):
        """Update existing template status, active/archive
        :param id : template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = FeedbackValidator.updateTemplateStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateTemplateStatusRequest
        schema = UpdateTemplateStatusRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/status/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/status/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

