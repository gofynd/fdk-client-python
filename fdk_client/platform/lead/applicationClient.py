"""Lead Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import LeadValidator

class Lead:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def getTickets(self, items=None, filters=None, q=None, status=None, priority=None, category=None, request_headers:Dict={}):
        """Gets the list of Application level Tickets and/or ticket filters
        :param items : Decides that the reponse will contain the list of tickets : type boolean
        :param filters : Decides that the reponse will contain the ticket filters : type boolean
        :param q : Search through ticket titles and description : type string
        :param status : Filter tickets on status : type string
        :param priority : Filter tickets on priority : type 
        :param category : Filter tickets on category : type string
        """
        payload = {}
        
        if items is not None:
            payload["items"] = items
        if filters is not None:
            payload["filters"] = filters
        if q is not None:
            payload["q"] = q
        if status is not None:
            payload["status"] = status
        if priority is not None:
            payload["priority"] = priority
        if category is not None:
            payload["category"] = category

        # Parameter validation
        schema = LeadValidator.getTickets()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}}],"optional":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}}],"query":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}}]}""", items=items, filters=filters, q=q, status=status, priority=priority, category=category)
        query_string = await create_query_string(items=items, filters=filters, q=q, status=status, priority=priority, category=category)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket", items=items, filters=filters, q=q, status=status, priority=priority, category=category), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import TicketList
            schema = TicketList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTickets")
                print(e)

        return response
    
    async def getTicket(self, id=None, request_headers:Dict={}):
        """Retreives ticket details of a application level ticket with ticket ID
        :param id : Tiket ID of the ticket to be fetched : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.getTicket()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import Ticket
            schema = Ticket()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTicket")
                print(e)

        return response
    
    async def editTicket(self, id=None, body="", request_headers:Dict={}):
        """Edits ticket details of a application level ticket such as status, priority, category, tags, attachments, assigne & ticket content changes
        :param id : Ticket ID of ticket to be edited : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.editTicket()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditTicketPayload
        schema = EditTicketPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import Ticket
            schema = Ticket()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editTicket")
                print(e)

        return response
    
    async def createHistory(self, id=None, body="", request_headers:Dict={}):
        """Create history for specific application level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param id : Ticket ID for which history is created : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.createHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TicketHistoryPayload
        schema = TicketHistoryPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import TicketHistory
            schema = TicketHistory()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createHistory")
                print(e)

        return response
    
    async def getTicketHistory(self, id=None, request_headers:Dict={}):
        """Gets history list for specific application level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param id : Ticket ID for which history is to be fetched : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.getTicketHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID of application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import TicketHistoryList
            schema = TicketHistoryList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTicketHistory")
                print(e)

        return response
    
    async def getCustomForm(self, slug=None, request_headers:Dict={}):
        """Get specific custom form using it's slug, this is used to view the form.
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = LeadValidator.getCustomForm()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}]}""", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomForm
            schema = CustomForm()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomForm")
                print(e)

        return response
    
    async def editCustomForm(self, slug=None, body="", request_headers:Dict={}):
        """Edit the given custom form field such as adding or deleting input, assignee, title, decription, notification and polling information.
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = LeadValidator.editCustomForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditCustomFormPayload
        schema = EditCustomFormPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}]}""", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomForm
            schema = CustomForm()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editCustomForm")
                print(e)

        return response
    
    async def getCustomForms(self, request_headers:Dict={}):
        """Get list of custom form for given application
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.getCustomForms()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomFormList
            schema = CustomFormList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomForms")
                print(e)

        return response
    
    async def createCustomForm(self, body="", request_headers:Dict={}):
        """Creates a new custom form for given application
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.createCustomForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateCustomFormPayload
        schema = CreateCustomFormPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomForm
            schema = CustomForm()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomForm")
                print(e)

        return response
    
    async def getTokenForVideoRoom(self, unique_name=None, request_headers:Dict={}):
        """Get Token to join a specific Video Room using it's unqiue name, this Token is your ticket to Room and also creates your identity there.
        :param unique_name : Unique name of video room : type string
        """
        payload = {}
        
        if unique_name is not None:
            payload["unique_name"] = unique_name

        # Parameter validation
        schema = LeadValidator.getTokenForVideoRoom()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}/token", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of video room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of video room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}/token", unique_name=unique_name), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetTokenForVideoRoomResponse
            schema = GetTokenForVideoRoomResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTokenForVideoRoom")
                print(e)

        return response
    
    async def getVideoParticipants(self, unique_name=None, request_headers:Dict={}):
        """Get participants of a specific Video Room using it's unique name, this can be used to check if people are already there in the room and also to show their names.
        :param unique_name : Unique name of Video Room : type string
        """
        payload = {}
        
        if unique_name is not None:
            payload["unique_name"] = unique_name

        # Parameter validation
        schema = LeadValidator.getVideoParticipants()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}/participants", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}/participants", unique_name=unique_name), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GetParticipantsInsideVideoRoomResponse
            schema = GetParticipantsInsideVideoRoomResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getVideoParticipants")
                print(e)

        return response
    
    async def openVideoRoom(self, body="", request_headers:Dict={}):
        """Open a video room.
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.openVideoRoom()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateVideoRoomPayload
        schema = CreateVideoRoomPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateVideoRoomResponse
            schema = CreateVideoRoomResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for openVideoRoom")
                print(e)

        return response
    
    async def closeVideoRoom(self, unique_name=None, request_headers:Dict={}):
        """Close the video room and force all participants to leave.
        :param unique_name : Unique name of Video Room : type string
        """
        payload = {}
        
        if unique_name is not None:
            payload["unique_name"] = unique_name

        # Parameter validation
        schema = LeadValidator.closeVideoRoom()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}", unique_name=unique_name), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CloseVideoRoomResponse
            schema = CloseVideoRoomResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for closeVideoRoom")
                print(e)

        return response
    