"""Rewards Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import RewardsValidator

class Rewards:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def showGiveaways(self, page_id=None, page_size=None, request_headers:Dict={}):
        """Retrieve and display available giveaways.
        :param page_id : pagination page id : type string
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if page_id is not None:
            payload["page_id"] = page_id
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = RewardsValidator.showGiveaways()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"page_id","in":"query","description":"pagination page id","required":true,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"pagination page size","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[{"name":"page_id","in":"query","description":"pagination page id","required":true,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"pagination page size","required":true,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_id=page_id, page_size=page_size)
        query_string = await create_query_string(page_id=page_id, page_size=page_size)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", page_id=page_id, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ListGiveaway
            schema = ListGiveaway()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for showGiveaways")
                print(e)

        return response
    
    async def saveGiveAway(self, body="", request_headers:Dict={}):
        """Store and manage details of a giveaway.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.saveGiveAway()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Giveaway
        schema = Giveaway()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Giveaway
            schema = Giveaway()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for saveGiveAway")
                print(e)

        return response
    
    async def getGiveawayById(self, id=None, request_headers:Dict={}):
        """Retrieve specific giveaway details by its unique identifier.
        :param id : Giveaway ID : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = RewardsValidator.getGiveawayById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Giveaway
            schema = Giveaway()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGiveawayById")
                print(e)

        return response
    
    async def updateGiveAway(self, id=None, body="", request_headers:Dict={}):
        """Modify and update information about a giveaway.
        :param id : Giveaway ID : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = RewardsValidator.updateGiveAway()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Giveaway
        schema = Giveaway()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Giveaway
            schema = Giveaway()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateGiveAway")
                print(e)

        return response
    
    async def showOffers(self, request_headers:Dict={}):
        """Display available offers for users.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.showOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getOfferByName(self, name=None, request_headers:Dict={}):
        """Retrieve an offer by its name.
        :param name : The name given to the offer. : type string
        """
        payload = {}
        
        if name is not None:
            payload["name"] = name

        # Parameter validation
        schema = RewardsValidator.getOfferByName()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", """{"required":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", name=name, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", name=name), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Offer
            schema = Offer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOfferByName")
                print(e)

        return response
    
    async def updateOfferByName(self, name=None, body="", request_headers:Dict={}):
        """Modify and manage an offer using its name.
        :param name : The name given to the offer. : type string
        """
        payload = {}
        
        if name is not None:
            payload["name"] = name

        # Parameter validation
        schema = RewardsValidator.updateOfferByName()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Offer
        schema = Offer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", """{"required":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", name=name, )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", name=name), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Offer
            schema = Offer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateOfferByName")
                print(e)

        return response
    
    async def updateUserStatus(self, user_id=None, body="", request_headers:Dict={}):
        """Change and update the status of a user in the rewards system.
        :param user_id : user id : type string
        """
        payload = {}
        
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = RewardsValidator.updateUserStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppUser
        schema = AppUser()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", """{"required":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", user_id=user_id, )
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", user_id=user_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppUser
            schema = AppUser()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateUserStatus")
                print(e)

        return response
    
    async def getUserDetails(self, user_id=None, request_headers:Dict={}):
        """Retrieve comprehensive details about a user in the rewards program.
        :param user_id : user id : type string
        """
        payload = {}
        
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = RewardsValidator.getUserDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", """{"required":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", user_id=user_id, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", user_id=user_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserRes
            schema = UserRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserDetails")
                print(e)

        return response
    
    async def getUserPointsHistory(self, user_id=None, page_id=None, page_size=None, request_headers:Dict={}):
        """Retrieve the history of points earned and redeemed by a user.
        :param user_id : user id : type string
        :param page_id : PageID is the ID of the requested page. For first request it should be kept empty. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if user_id is not None:
            payload["user_id"] = user_id
        if page_id is not None:
            payload["page_id"] = page_id
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = RewardsValidator.getUserPointsHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/points/history/", """{"required":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_id","in":"query","description":"PageID is the ID of the requested page. For first request it should be kept empty.","schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","schema":{"type":"integer"}}],"query":[{"name":"page_id","in":"query","description":"PageID is the ID of the requested page. For first request it should be kept empty.","schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","schema":{"type":"integer"}}],"headers":[],"path":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", user_id=user_id, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(page_id=page_id, page_size=page_size)

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/points/history/", user_id=user_id, page_id=page_id, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import HistoryRes
            schema = HistoryRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserPointsHistory")
                print(e)

        return response
    
    async def getRewardsConfiguration(self, request_headers:Dict={}):
        """Retrieve the configuration settings for the rewards program.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.getRewardsConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration/", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration/", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigurationRes
            schema = ConfigurationRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRewardsConfiguration")
                print(e)

        return response
    
    async def setRewardsConfiguration(self, body="", request_headers:Dict={}):
        """Configure and modify the settings for the rewards program.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.setRewardsConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SetConfiguration
        schema = SetConfiguration()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration/", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SetConfigurationRes
            schema = SetConfigurationRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setRewardsConfiguration")
                print(e)

        return response
    