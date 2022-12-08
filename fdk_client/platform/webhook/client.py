

""" Webhook Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import WebhookValidator

class Webhook:
    def __init__(self, config):
        self._conf = config
    
    async def getSubscribersByCompany(self, page_no=None, page_size=None, extension_id=None):
        """Get Subscribers By CompanyId
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param extension_id : Extension ID : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if extension_id:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = WebhookValidator.getSubscribersByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"extension_id","in":"query","description":"Extension ID","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"extension_id","in":"query","description":"Extension ID","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}]}""", page_no=page_no, page_size=page_size, extension_id=extension_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, extension_id=extension_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", page_no=page_no, page_size=page_size, extension_id=extension_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def registerSubscriberToEvent(self, body=""):
        """Register Subscriber
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.registerSubscriberToEvent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SubscriberConfig import SubscriberConfig
        schema = SubscriberConfig()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company Id of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id of the application","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateSubscriberConfig(self, body=""):
        """Update Subscriber
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.updateSubscriberConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SubscriberConfig import SubscriberConfig
        schema = SubscriberConfig()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSubscribersByExtensionId(self, page_no=None, page_size=None, extension_id=None):
        """Get Subscribers By ExtensionID
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param extension_id : Extension ID : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if extension_id:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = WebhookValidator.getSubscribersByExtensionId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"extension_id","in":"path","description":"Extension ID","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"extension_id","in":"path","description":"Extension ID","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, extension_id=extension_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, extension_id=extension_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscriber", page_no=page_no, page_size=page_size, extension_id=extension_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSubscriberById(self, subscriber_id=None):
        """Get Subscriber By Subscriber ID
        :param subscriber_id : Subscriber ID : type integer
        """
        payload = {}
        
        if subscriber_id:
            payload["subscriber_id"] = subscriber_id
        

        # Parameter validation
        schema = WebhookValidator.getSubscriberById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/{subscriber_id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"subscriber_id","in":"path","description":"Subscriber ID","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"subscriber_id","in":"path","description":"Subscriber ID","required":true,"schema":{"type":"integer","format":"int32"}}]}""", subscriber_id=subscriber_id)
        query_string = await create_query_string(subscriber_id=subscriber_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/{subscriber_id}", subscriber_id=subscriber_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def fetchAllEventConfigurations(self, ):
        """Get All Webhook Events
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.fetchAllEventConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/events", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/events", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

