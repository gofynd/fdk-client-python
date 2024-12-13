"""Lead Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import LeadValidator

class Lead:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getPlatformTickets(self, items=None, filters=None, q=None, status=None, priority=None, category=None, page_no=None, page_size=None, request_headers:Dict={}):
        """List all tickets created within the platform at company level
        :param items : Decides that the reponse will contain the list of tickets : type boolean
        :param filters : Decides that the reponse will contain the ticket filters : type boolean
        :param q : Search through ticket titles and description : type string
        :param status : Filter tickets on status : type string
        :param priority : Filter tickets on priority : type 
        :param category : Filter tickets on category : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
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
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = LeadValidator.getPlatformTickets()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket", """{"required":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}}],"optional":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"name":"page_size","in":"query","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"name":"page_size","in":"query","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}}]}""", serverType="platform", items=items, filters=filters, q=q, status=status, priority=priority, category=category, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(items=items, filters=filters, q=q, status=status, priority=priority, category=category, page_no=page_no, page_size=page_size)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket", items=items, filters=filters, q=q, status=status, priority=priority, category=category, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TicketList
            schema = TicketList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPlatformTickets")
                print(e)

        return response
    
    async def createTicket(self, body="", request_headers:Dict={}):
        """Create a new ticket at application level
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.createTicket()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddTicketPayload
        schema = AddTicketPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket", """{"required":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Ticket
            schema = Ticket()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createTicket")
                print(e)

        return response
    
    async def getPlatformTicket(self, id=None, request_headers:Dict={}):
        """Get detailed information about a specific ticket which is raised at company level
        :param id : Tiket ID of the ticket to be fetched : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.getPlatformTicket()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Ticket
            schema = Ticket()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPlatformTicket")
                print(e)

        return response
    
    async def editPlatformTicket(self, id=None, body="", request_headers:Dict={}):
        """Modify the content and settings of a specific company level ticket.
        :param id : Ticket ID of ticket to be edited : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.editPlatformTicket()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditTicketPayload
        schema = EditTicketPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Ticket
            schema = Ticket()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editPlatformTicket")
                print(e)

        return response
    
    async def createPlatformTicketHistory(self, id=None, body="", request_headers:Dict={}):
        """Create futher interactions on a company level ticket such as changing it's status, priority or replying to a ticket via a thread.
        :param id : Ticket ID for which history is created : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.createPlatformTicketHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TicketHistoryPayload
        schema = TicketHistoryPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/history", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TicketHistory
            schema = TicketHistory()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPlatformTicketHistory")
                print(e)

        return response
    
    async def getPlatformTicketHistory(self, id=None, request_headers:Dict={}):
        """List history records for a company level ticket.
        :param id : Ticket ID for which history is to be fetched : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.getPlatformTicketHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/history", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TicketHistoryList
            schema = TicketHistoryList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPlatformTicketHistory")
                print(e)

        return response
    
    async def getFeedbacks(self, id=None, request_headers:Dict={}):
        """Get feedback information related to a ticket.
        :param id : Ticket ID for which feedbacks are to be fetched : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.getFeedbacks()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/feedback", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which feedbacks are to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which feedbacks are to be fetched","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/feedback", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TicketFeedbackList
            schema = TicketFeedbackList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFeedbacks")
                print(e)

        return response
    
    async def submitFeedback(self, id=None, body="", request_headers:Dict={}):
        """Provide feedback on a ticket and it's resolution.
        :param id : Ticket ID for which feedback is to be submitted : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = LeadValidator.submitFeedback()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TicketFeedbackPayload
        schema = TicketFeedbackPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/feedback", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which feedback is to be submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which feedback is to be submitted","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/feedback", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TicketFeedback
            schema = TicketFeedback()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for submitFeedback")
                print(e)

        return response
    
    async def getGeneralConfig(self, request_headers:Dict={}):
        """Get general configuration settings related to support system for company tickets
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.getGeneralConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/general-config", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/general-config", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GeneralConfigResponse
            schema = GeneralConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGeneralConfig")
                print(e)

        return response
    