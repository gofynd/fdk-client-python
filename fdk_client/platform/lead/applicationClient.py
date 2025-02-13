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

    
    async def getNewTickets(self, items=None, filters=None, q=None, status=None, priority=None, category=None, request_headers:Dict={}):
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
        schema = LeadValidator.getNewTickets()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}}],"optional":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}}],"query":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}}]}""", serverType="platform", items=items, filters=filters, q=q, status=status, priority=priority, category=category)
        query_string = await create_query_string(items=items, filters=filters, q=q, status=status, priority=priority, category=category)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket", items=items, filters=filters, q=q, status=status, priority=priority, category=category), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TicketList
            schema = TicketList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNewTickets")
                print(e)

        return response
    
    async def getNewTicket(self, id=None, request_headers:Dict={}):
        """Get ticket details of a application level ticket with ticket ID
        :param id : Tiket ID of the ticket to be fetched : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.getNewTicket()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Ticket
            schema = Ticket()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNewTicket")
                print(e)

        return response
    
    async def editNewTicket(self, id=None, body="", request_headers:Dict={}):
        """Edits ticket details of a application level ticket such as status, priority, category, tags, attachments, assigne & ticket content changes
        :param id : Ticket ID of ticket to be edited : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.editNewTicket()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditTicketPayload
        schema = EditTicketPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Ticket
            schema = Ticket()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editNewTicket")
                print(e)

        return response
    
    async def createNewHistory(self, id=None, body="", request_headers:Dict={}):
        """Create history for specific application level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param id : Ticket ID for which history is created : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.createNewHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TicketHistoryPayload
        schema = TicketHistoryPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TicketHistory
            schema = TicketHistory()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createNewHistory")
                print(e)

        return response
    
    async def getNewTicketHistory(self, id=None, request_headers:Dict={}):
        """Gets history list for specific application level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param id : Ticket ID for which history is to be fetched : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.getNewTicketHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID of application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TicketHistoryList
            schema = TicketHistoryList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNewTicketHistory")
                print(e)

        return response
    
    async def getCustomForm(self, slug=None, request_headers:Dict={}):
        """Get information about a custom form which includes corresponding field details and any validation regex required against that field or not
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = LeadValidator.getCustomForm()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Modify the content and associated settings of a custom form.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomForm
            schema = CustomForm()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editCustomForm")
                print(e)

        return response
    
    async def deleteCustomForm(self, slug=None, request_headers:Dict={}):
        """Delete a custom form using it's slug
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = LeadValidator.deleteCustomForm()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}]}""", serverType="platform", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomForm
            schema = CustomForm()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCustomForm")
                print(e)

        return response
    
    async def getCustomForms(self, request_headers:Dict={}):
        """List all available custom forms
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.getCustomForms()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Create a new custom form for application users to fill
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.createCustomForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateCustomFormPayload
        schema = CreateCustomFormPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomForm
            schema = CustomForm()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCustomForm")
                print(e)

        return response
    