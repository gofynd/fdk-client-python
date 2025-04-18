"""Communication Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import CommunicationValidator

class Communication:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def sendEngineCommunicationSynchronously(self, body="", request_headers:Dict={}):
        """Initiate and send communication with the option for asynchronous processing.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.sendEngineCommunicationSynchronously()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EngineRequest
        schema = EngineRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-sync", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-sync", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SendInstantResponse
            schema = SendInstantResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendEngineCommunicationSynchronously")
                print(e)

        return response
    
    async def sendCommunicationAsynchronously(self, body="", request_headers:Dict={}):
        """Initiate and send communication with the option for asynchronous processing.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.sendCommunicationAsynchronously()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EngineRequest
        schema = EngineRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-async", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-async", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EngineResponse
            schema = EngineResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendCommunicationAsynchronously")
                print(e)

        return response
    
    async def sendCommunicationSynchronously(self, body="", request_headers:Dict={}):
        """Initiate and send communication in real-time.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.sendCommunicationSynchronously()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EngineRequest
        schema = EngineRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-instant", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-instant", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SendInstantResponse
            schema = SendInstantResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendCommunicationSynchronously")
                print(e)

        return response
    
    async def getEventSubscriptions(self, page_no=None, page_size=None, populate=None, request_headers:Dict={}):
        """Retrieve a list of event subscriptions related to communication.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param populate : Populate Fields : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if populate is not None:
            payload["populate"] = populate

        # Parameter validation
        schema = CommunicationValidator.getEventSubscriptions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"populate","description":"Populate Fields","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"populate","description":"Populate Fields","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, populate=populate)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, populate=populate)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", page_no=page_no, page_size=page_size, populate=populate), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventSubscriptions
            schema = EventSubscriptions()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEventSubscriptions")
                print(e)

        return response
    
    async def createEventSubscriptions(self, body="", request_headers:Dict={}):
        """Create event subscriptions
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEventSubscriptions()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionsObject
        schema = SubscriptionsObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventSubscription
            schema = EventSubscription()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createEventSubscriptions")
                print(e)

        return response
    
    async def createEventSubscriptionsByBulk(self, body="", request_headers:Dict={}):
        """Create event subscriptions by bulk
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEventSubscriptionsByBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EventSubscriptionsBulkUpdateRequest
        schema = EventSubscriptionsBulkUpdateRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/bulkUpdate", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/bulkUpdate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getEventSubscriptionsById(self, populate=None, id=None, request_headers:Dict={}):
        """Get event subscriptions by id
        :param populate : Populate Fields : type string
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if populate is not None:
            payload["populate"] = populate
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getEventSubscriptionsById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"populate","description":"Populate Fields","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"populate","description":"Populate Fields","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", populate=populate, id=id)
        query_string = await create_query_string(populate=populate, )
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", populate=populate, id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventSubscription
            schema = EventSubscription()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEventSubscriptionsById")
                print(e)

        return response
    
    async def editEventSubscriptions(self, id=None, body="", request_headers:Dict={}):
        """Create event subscriptions
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.editEventSubscriptions()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionsObjectRequest
        schema = SubscriptionsObjectRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventSubscription
            schema = EventSubscription()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editEventSubscriptions")
                print(e)

        return response
    
    async def deleteEventSubscriptionsById(self, id=None, request_headers:Dict={}):
        """Create event subscriptions
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteEventSubscriptionsById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventSubscription
            schema = EventSubscription()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteEventSubscriptionsById")
                print(e)

        return response
    
    async def getEmailTemplates(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieve a list of available email communication templates.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type string
        :param query : To search based on plain text : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailTemplates
            schema = EmailTemplates()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEmailTemplates")
                print(e)

        return response
    
    async def createEmailTemplate(self, body="", request_headers:Dict={}):
        """Generate and add a new email communication template.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEmailTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailTemplateReq
        schema = EmailTemplateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailTemplate
            schema = EmailTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createEmailTemplate")
                print(e)

        return response
    
    async def getEmailTemplateById(self, id=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific email communication template.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getEmailTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailTemplate
            schema = EmailTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEmailTemplateById")
                print(e)

        return response
    
    async def updateEmailTemplateById(self, id=None, body="", request_headers:Dict={}):
        """Modify the content and settings of a specific email communication template.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateEmailTemplateById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailTemplateReq
        schema = EmailTemplateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailTemplate
            schema = EmailTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateEmailTemplateById")
                print(e)

        return response
    
    async def deleteEmailTemplateById(self, id=None, request_headers:Dict={}):
        """Email templates are predefined formats linked to various events for delivering messages to users. Remove a specific email communication template by its ID.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteEmailTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BasicDelete
            schema = BasicDelete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteEmailTemplateById")
                print(e)

        return response
    
    async def getSystemEmailTemplates(self, request_headers:Dict={}):
        """Retrieve system-defined email communication templates.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getSystemEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/system-templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/system-templates", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getSubscribedEmailTemplates(self, page_no=None, page_size=None, query=None, request_headers:Dict={}):
        """Retrieve email communication templates that are subscribed to.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param query : To search based on plain text : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getSubscribedEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/subscribedTemplates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, query=query)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/subscribedTemplates", page_no=page_no, page_size=page_size, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscribedEmailTemplates
            schema = SubscribedEmailTemplates()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSubscribedEmailTemplates")
                print(e)

        return response
    
    async def getEmailProviders(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieve a list of email communication providers.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type string
        :param query : To search based on plain text : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getEmailProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailProviders
            schema = EmailProviders()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEmailProviders")
                print(e)

        return response
    
    async def createEmailProvider(self, body="", request_headers:Dict={}):
        """Generate and add a new email communication provider.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEmailProvider()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailProviderReq
        schema = EmailProviderReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailProvider
            schema = EmailProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createEmailProvider")
                print(e)

        return response
    
    async def getEmailProviderById(self, id=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific email communication provider.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getEmailProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailProvider
            schema = EmailProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEmailProviderById")
                print(e)

        return response
    
    async def updateEmailProviderById(self, id=None, body="", request_headers:Dict={}):
        """Modify the settings of a specific email communication provider.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateEmailProviderById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailProviderReq
        schema = EmailProviderReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailProvider
            schema = EmailProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateEmailProviderById")
                print(e)

        return response
    
    async def deleteEmailProviderById(self, id=None, request_headers:Dict={}):
        """Remove a specific email communication provider from the platform.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteEmailProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BasicDelete
            schema = BasicDelete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteEmailProviderById")
                print(e)

        return response
    
    async def getDefaultEmailProviders(self, request_headers:Dict={}):
        """Retrieve a list of app  providers.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getDefaultEmailProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/default-providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/default-providers", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getSmsProviders(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieve a list of SMS communication providers.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type string
        :param query : To search based on plain text : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getSmsProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsProviders
            schema = SmsProviders()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSmsProviders")
                print(e)

        return response
    
    async def createSmsProvider(self, body="", request_headers:Dict={}):
        """Add a new SMS communication provider.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createSmsProvider()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsProviderReq
        schema = SmsProviderReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsProvider
            schema = SmsProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSmsProvider")
                print(e)

        return response
    
    async def getSmsProviderById(self, id=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific SMS communication provider.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getSmsProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsProvider
            schema = SmsProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSmsProviderById")
                print(e)

        return response
    
    async def updateSmsProviderById(self, id=None, body="", request_headers:Dict={}):
        """Modify specific SMS communication provider.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateSmsProviderById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsProviderReq
        schema = SmsProviderReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsProvider
            schema = SmsProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSmsProviderById")
                print(e)

        return response
    
    async def deleteSmsProviderById(self, id=None, request_headers:Dict={}):
        """Remove a specific SMS communication provider.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteSmsProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BasicDelete
            schema = BasicDelete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSmsProviderById")
                print(e)

        return response
    
    async def getDefaultSmsProviders(self, request_headers:Dict={}):
        """Retrieve the default SMS communication providers.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getDefaultSmsProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/default-providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/default-providers", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getSmsTemplates(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieve a list of available SMS communication templates.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type string
        :param query : To search based on plain text : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getSmsTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsTemplates
            schema = SmsTemplates()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSmsTemplates")
                print(e)

        return response
    
    async def createSmsTemplate(self, body="", request_headers:Dict={}):
        """Add a new SMS communication template.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createSmsTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsTemplateReq
        schema = SmsTemplateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsTemplate
            schema = SmsTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSmsTemplate")
                print(e)

        return response
    
    async def getSmsTemplateById(self, id=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific SMS communication template.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getSmsTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsTemplate
            schema = SmsTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSmsTemplateById")
                print(e)

        return response
    
    async def updateSmsTemplateById(self, id=None, body="", request_headers:Dict={}):
        """Modify the content and settings of a specific SMS communication template.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateSmsTemplateById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsTemplateReq
        schema = SmsTemplateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsTemplate
            schema = SmsTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSmsTemplateById")
                print(e)

        return response
    
    async def deleteSmsTemplateById(self, id=None, request_headers:Dict={}):
        """Remove a specific SMS communication template.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteSmsTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BasicDelete
            schema = BasicDelete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSmsTemplateById")
                print(e)

        return response
    
    async def getSystemSmsTemplates(self, request_headers:Dict={}):
        """Retrieve system-defined SMS communication templates.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getSystemSmsTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/system-templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/system-templates", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getSubscribedSmsTemplates(self, page_no=None, page_size=None, query=None, request_headers:Dict={}):
        """Retrieve SMS communication templates that are subscribed to.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param query : To search based on plain text : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getSubscribedSmsTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/subscribedTemplates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, query=query)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/subscribedTemplates", page_no=page_no, page_size=page_size, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscribedSmsTemplates
            schema = SubscribedSmsTemplates()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSubscribedSmsTemplates")
                print(e)

        return response
    
    async def triggerCampaignJob(self, body="", request_headers:Dict={}):
        """Initiate a job to execute a communication campaign.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.triggerCampaignJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TriggerJobRequest
        schema = TriggerJobRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/trigger-job", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/trigger-job", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TriggerJobResponse
            schema = TriggerJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for triggerCampaignJob")
                print(e)

        return response
    
    async def getJobs(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieve a list of communication jobs.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type string
        :param query : To search based on plain text : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getJobs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Jobs
            schema = Jobs()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobs")
                print(e)

        return response
    
    async def createJobs(self, body="", request_headers:Dict={}):
        """Create jobs
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createJobs()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateJobsReq
        schema = CreateJobsReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateJobsRes
            schema = CreateJobsRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createJobs")
                print(e)

        return response
    
    async def getJobLogs(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieve logs and details related to communication jobs.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type string
        :param query : To search based on plain text : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getJobLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/logs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/logs", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import JobLogs
            schema = JobLogs()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobLogs")
                print(e)

        return response
    
    async def getGlobalVariables(self, request_headers:Dict={}):
        """Retrieve global variables used in communication.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getGlobalVariables()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/global-variables", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/global-variables", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GlobalVariablesGetResponse
            schema = GlobalVariablesGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGlobalVariables")
                print(e)

        return response
    
    async def postGlobalVariables(self, body="", request_headers:Dict={}):
        """Update and post global variables for communication.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.postGlobalVariables()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GlobalVariablesReq
        schema = GlobalVariablesReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/global-variables", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/global-variables", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GlobalVariablesPostResponse
            schema = GlobalVariablesPostResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for postGlobalVariables")
                print(e)

        return response
    
    async def getCommunicationLogs(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieve logs and records of communication activities.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type string
        :param query :  : type object
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getCommunicationLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/log", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"name":"query","in":"query","schema":{"type":"object"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"name":"query","in":"query","schema":{"type":"object"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/log", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Logs
            schema = Logs()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCommunicationLogs")
                print(e)

        return response
    
    async def updateAppProviders(self, body="", request_headers:Dict={}):
        """Modify provider information for the platform.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.updateAppProviders()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppProviderReq
        schema = AppProviderReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/update-provider", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/update-provider", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppProvider
            schema = AppProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppProviders")
                print(e)

        return response
    
    async def getAppProviders(self, request_headers:Dict={}):
        """Retrieve a list of providers associated with the platform.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getAppProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/get-provider", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/get-provider", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppProvider
            schema = AppProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppProviders")
                print(e)

        return response
    
    async def getGlobalProviders(self, request_headers:Dict={}):
        """Retrieve a list of global communication providers.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getGlobalProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/global-providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/global-providers", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GlobalProviders
            schema = GlobalProviders()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGlobalProviders")
                print(e)

        return response
    
    async def updateAppProvidersGlobalProvider(self, body="", request_headers:Dict={}):
        """Retrieve a list of global app  providers.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.updateAppProvidersGlobalProvider()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppProvidersGlobalProviderRequest
        schema = AppProvidersGlobalProviderRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/global-providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/global-providers", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateAppProvidersGlobalProviderResponse
            schema = UpdateAppProvidersGlobalProviderResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppProvidersGlobalProvider")
                print(e)

        return response
    
    async def getDummyDatasourcesMeta(self, id=None, request_headers:Dict={}):
        """Retrieve metadata information about dummy data sources.
        :param id : Dummy datasources meta ID : type integer
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getDummyDatasourcesMeta()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasource/dummy-data-source-meta", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"query","name":"id","description":"Dummy datasources meta ID","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[{"in":"query","name":"id","description":"Dummy datasources meta ID","required":true,"schema":{"type":"integer","format":"int32"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string(id=id)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasource/dummy-data-source-meta", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DummyDatasourcesMeta
            schema = DummyDatasourcesMeta()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDummyDatasourcesMeta")
                print(e)

        return response
    
    async def getDummyDatasources(self, request_headers:Dict={}):
        """Retrieve a list of dummy data sources for testing.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getDummyDatasources()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasource/dummy-data-sources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasource/dummy-data-sources", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getAudiences(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Audience is used to import CSV files containing emails, phone numbers, and other variables in order to populate email/SMS templates for bulk delivery via a Campaign.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type string
        :param query : To search based on plain text : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getAudiences()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Audiences
            schema = Audiences()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAudiences")
                print(e)

        return response
    
    async def createAudience(self, body="", request_headers:Dict={}):
        """Add audience which is used to import CSV files containing emails, phone numbers, and other variables in order to populate email/SMS templates for bulk delivery via a Campaign. 
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createAudience()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Audience
            schema = Audience()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAudience")
                print(e)

        return response
    
    async def getAudienceById(self, id=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific custom communication audience.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getAudienceById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Audience
            schema = Audience()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAudienceById")
                print(e)

        return response
    
    async def updateAudienceById(self, id=None, body="", request_headers:Dict={}):
        """Modify the settings of a specific custom communication audience.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateAudienceById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Audience
            schema = Audience()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAudienceById")
                print(e)

        return response
    
    async def deleteAudienceById(self, id=None, body="", request_headers:Dict={}):
        """Remove a specific custom communication audience.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteAudienceById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BasicDelete
            schema = BasicDelete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAudienceById")
                print(e)

        return response
    
    async def getNSampleRecordsFromCsvByGet(self, count=None, header=None, url=None, request_headers:Dict={}):
        """Retrieve a specified number of sample records from a CSV data source using a GET request.
        :param count : number or records : type integer
        :param header : header needed : type boolean
        :param url : url of file : type string
        """
        payload = {}
        
        if count is not None:
            payload["count"] = count
        if header is not None:
            payload["header"] = header
        if url is not None:
            payload["url"] = url

        # Parameter validation
        schema = CommunicationValidator.getNSampleRecordsFromCsvByGet()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"count","description":"number or records","schema":{"type":"integer"}},{"in":"query","name":"header","description":"header needed","schema":{"type":"boolean"}},{"in":"query","name":"url","description":"url of file","schema":{"type":"string"}}],"query":[{"in":"query","name":"count","description":"number or records","schema":{"type":"integer"}},{"in":"query","name":"header","description":"header needed","schema":{"type":"boolean"}},{"in":"query","name":"url","description":"url of file","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", count=count, header=header, url=url)
        query_string = await create_query_string(count=count, header=header, url=url)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", count=count, header=header, url=url), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetNRecordsCsvRes
            schema = GetNRecordsCsvRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNSampleRecordsFromCsvByGet")
                print(e)

        return response
    
    async def getNSampleRecordsFromCsv(self, body="", request_headers:Dict={}):
        """Retrieve a specified number of sample records from a CSV data source.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getNSampleRecordsFromCsv()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetNRecordsCsvReq
        schema = GetNRecordsCsvReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetNRecordsCsvRes
            schema = GetNRecordsCsvRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNSampleRecordsFromCsv")
                print(e)

        return response
    
    async def getCampaigns(self, query=None, page_no=None, page_size=None, sort=None, request_headers:Dict={}):
        """Retrieve a list of communication campaigns.
        :param query : To search based on plain text : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type string
        """
        payload = {}
        
        if query is not None:
            payload["query"] = query
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort

        # Parameter validation
        schema = CommunicationValidator.getCampaigns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}}],"query":[{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"string","description":"Sort by creation date in descending order."}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", query=query, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(query=query, page_no=page_no, page_size=page_size, sort=sort)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", query=query, page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Campaigns
            schema = Campaigns()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCampaigns")
                print(e)

        return response
    
    async def createCampaign(self, body="", request_headers:Dict={}):
        """Add a new communication campaign.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createCampaign()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CampaignReq
        schema = CampaignReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Campaign
            schema = Campaign()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCampaign")
                print(e)

        return response
    
    async def getCampaignById(self, id=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific communication campaign.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getCampaignById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Campaign
            schema = Campaign()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCampaignById")
                print(e)

        return response
    
    async def updateCampaignById(self, id=None, body="", request_headers:Dict={}):
        """Modify the settings of a specific communication campaign.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateCampaignById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CampaignReq
        schema = CampaignReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Campaign
            schema = Campaign()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCampaignById")
                print(e)

        return response
    
    async def deleteCampaignById(self, id=None, request_headers:Dict={}):
        """Modify the settings of a specific communication campaign.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteCampaignById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BasicDelete
            schema = BasicDelete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCampaignById")
                print(e)

        return response
    
    async def getStatsOfCampaignById(self, id=None, request_headers:Dict={}):
        """Retrieve statistical data for a specific communication campaign.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getStatsOfCampaignById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/get-stats/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/get-stats/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetStats
            schema = GetStats()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStatsOfCampaignById")
                print(e)

        return response
    
    async def sendOtp(self, ci=None, body="", request_headers:Dict={}):
        """Send a one-time password (OTP) for authentication or verification.
        :param ci : Common Information : type boolean
        """
        payload = {}
        
        if ci is not None:
            payload["ci"] = ci

        # Parameter validation
        schema = CommunicationValidator.sendOtp()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendOtpCommsReq
        schema = SendOtpCommsReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/send-otp-comms", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"ci","description":"Common Information","required":false,"schema":{"type":"boolean","example":false}}],"query":[{"in":"query","name":"ci","description":"Common Information","required":false,"schema":{"type":"boolean","example":false}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", ci=ci)
        query_string = await create_query_string(ci=ci)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/send-otp-comms", ci=ci), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SendOtpCommsRes
            schema = SendOtpCommsRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendOtp")
                print(e)

        return response
    
    async def verfiyOtp(self, body="", request_headers:Dict={}):
        """Verify the one-time password (OTP) for authentication or verification.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.verfiyOtp()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyOtpCommsReq
        schema = VerifyOtpCommsReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/verify-otp-comms", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/verify-otp-comms", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyOtpCommsSuccessRes
            schema = VerifyOtpCommsSuccessRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verfiyOtp")
                print(e)

        return response
    
    async def getOtpConfiguration(self, request_headers:Dict={}):
        """Get otp-configuration
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getOtpConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/otp-configuration", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/otp-configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OtpConfiguration
            schema = OtpConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOtpConfiguration")
                print(e)

        return response
    
    async def updateOtpConfiguration(self, body="", request_headers:Dict={}):
        """Update otp-configuration
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.updateOtpConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OtpConfiguration
        schema = OtpConfiguration()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/otp-configuration", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/otp-configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OtpConfiguration
            schema = OtpConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateOtpConfiguration")
                print(e)

        return response
    
    async def createAppPushtoken(self, body="", request_headers:Dict={}):
        """Create the push token of the user. 
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createAppPushtoken()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PushtokenReq
        schema = PushtokenReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pn/tokens", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pn/tokens", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PushtokenRes
            schema = PushtokenRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAppPushtoken")
                print(e)

        return response
    