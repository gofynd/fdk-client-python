

"""Lead Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import LeadValidator

class Lead:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getTicket": "/service/application/lead/v1.0/ticket/{id}",
            "createHistory": "/service/application/lead/v1.0/ticket/{id}/history",
            "createTicket": "/service/application/lead/v1.0/ticket/",
            "getCustomForm": "/service/application/lead/v1.0/form/{slug}",
            "submitCustomForm": "/service/application/lead/v1.0/form/{slug}/submit",
            "getParticipantsInsideVideoRoom": "/service/application/lead/v1.0/video/room/{unique_name}/participants",
            "getTokenForVideoRoom": "/service/application/lead/v1.0/video/room/{unique_name}/token"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getTicket(self, id=None, body=""):
        """Get Ticket with the specific id, this is used to view the ticket details
        :param id : ID of ticket to be retrieved : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        
        # Parameter validation
        schema = LeadValidator.getTicket()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getTicket"], proccessed_params="""{"required":[{"name":"id","in":"path","description":"ID of ticket to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","in":"path","description":"ID of ticket to be retrieved","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getTicket"]).netloc, "get", await create_url_without_domain("/service/application/lead/v1.0/ticket/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import Ticket
            schema = Ticket()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTicket")
                print(e)

        

        return response
    
    async def createHistory(self, id=None, body=""):
        """Create history for specific Ticket, this history is seen on ticket detail page, this can be comment, log or rating.
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["createHistory"], proccessed_params="""{"required":[{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["createHistory"]).netloc, "post", await create_url_without_domain("/service/application/lead/v1.0/ticket/{id}/history", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import TicketHistory
            schema = TicketHistory()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createHistory")
                print(e)

        

        return response
    
    async def createTicket(self, body=""):
        """This is used to Create Ticket.
        """
        payload = {}
        
        # Parameter validation
        schema = LeadValidator.createTicket()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddTicketPayload
        schema = AddTicketPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createTicket"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["createTicket"]).netloc, "post", await create_url_without_domain("/service/application/lead/v1.0/ticket/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import Ticket
            schema = Ticket()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createTicket")
                print(e)

        

        return response
    
    async def getCustomForm(self, slug=None, body=""):
        """Get specific Custom Form using it's slug, this is used to view the form.
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        
        # Parameter validation
        schema = LeadValidator.getCustomForm()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomForm"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCustomForm"]).netloc, "get", await create_url_without_domain("/service/application/lead/v1.0/form/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CustomForm
            schema = CustomForm()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomForm")
                print(e)

        

        return response
    
    async def submitCustomForm(self, slug=None, body=""):
        """Submit Response for a specific Custom Form using it's slug, this response is then used to create a ticket on behalf of the user.
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        
        # Parameter validation
        schema = LeadValidator.submitCustomForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomFormSubmissionPayload
        schema = CustomFormSubmissionPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["submitCustomForm"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["submitCustomForm"]).netloc, "post", await create_url_without_domain("/service/application/lead/v1.0/form/{slug}/submit", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import SubmitCustomFormResponse
            schema = SubmitCustomFormResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for submitCustomForm")
                print(e)

        

        return response
    
    async def getParticipantsInsideVideoRoom(self, unique_name=None, body=""):
        """Get participants of a specific Video Room using it's unique name, this can be used to check if people are already there in the room and also to show their names.
        :param unique_name : Unique name of Video Room : type string
        """
        payload = {}
        
        if unique_name is not None:
            payload["unique_name"] = unique_name
        
        # Parameter validation
        schema = LeadValidator.getParticipantsInsideVideoRoom()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getParticipantsInsideVideoRoom"], proccessed_params="""{"required":[{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getParticipantsInsideVideoRoom"]).netloc, "get", await create_url_without_domain("/service/application/lead/v1.0/video/room/{unique_name}/participants", unique_name=unique_name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import GetParticipantsInsideVideoRoomResponse
            schema = GetParticipantsInsideVideoRoomResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getParticipantsInsideVideoRoom")
                print(e)

        

        return response
    
    async def getTokenForVideoRoom(self, unique_name=None, body=""):
        """Get Token to join a specific Video Room using it's unqiue name, this Token is your ticket to Room and also creates your identity there.
        :param unique_name : Unique name of Video Room : type string
        """
        payload = {}
        
        if unique_name is not None:
            payload["unique_name"] = unique_name
        
        # Parameter validation
        schema = LeadValidator.getTokenForVideoRoom()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getTokenForVideoRoom"], proccessed_params="""{"required":[{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getTokenForVideoRoom"]).netloc, "get", await create_url_without_domain("/service/application/lead/v1.0/video/room/{unique_name}/token", unique_name=unique_name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import GetTokenForVideoRoomResponse
            schema = GetTokenForVideoRoomResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTokenForVideoRoom")
                print(e)

        

        return response
    

