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
        """Fetch the detailed compilation of live, completed, and scheduled point-based giveaways created.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"page_id","in":"query","description":"pagination page id","required":true,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"pagination page size","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[{"name":"page_id","in":"query","description":"pagination page id","required":true,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"pagination page size","required":true,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", page_id=page_id, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", page_id=page_id, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import GiveawayResponse
            schema = GiveawayResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for showGiveaways")
                print(e)

        return response
    
    async def saveGiveAway(self, body="", request_headers:Dict={}):
        """Creates a new giveaway in the current application, specifying the target audience, points allocation, as well as the name and display name of the giveaway.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.saveGiveAway()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Giveaway
        schema = Giveaway()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Retrieve the specific giveaway by giveaway ID. It will show all the details of the requested giveaway.
        :param id : Giveaway ID : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = RewardsValidator.getGiveawayById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Make the necessary updates to the giveaway based on its giveaway ID.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}]}""", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Retrieve the list of offers within the current application, including order_discount, order, sign_up, and referral, along with their respective details.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.showOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        return response
    
    async def getOfferByName(self, name=None, request_headers:Dict={}):
        """Fetch the specific offer details and configuration by the name of the offer.
        :param name : The name given to the offer. : type string
        """
        payload = {}
        
        if name is not None:
            payload["name"] = name

        # Parameter validation
        schema = RewardsValidator.getOfferByName()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", """{"required":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", name=name, )
        query_string = await create_query_string(name=name, )

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", name=name), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Update the specific offer details and its configuration by offer name.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", """{"required":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", name=name, )
        query_string = await create_query_string(name=name, )

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", name=name), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Update the user status by marking them as a block or unblock. It can be done by changing the active flag in request body.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", """{"required":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", user_id=user_id, )
        query_string = await create_query_string(user_id=user_id, )

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", user_id=user_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Fetches the user details and the user reward details with their current reward points for the specific user.
        :param user_id : user id : type string
        """
        payload = {}
        
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = RewardsValidator.getUserDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", """{"required":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", user_id=user_id, )
        query_string = await create_query_string(user_id=user_id, )

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", user_id=user_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Fetches a list of points transactions like giveaway points, signup points, referral points, order earn points, redeem points and expired points.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/points/history/", """{"required":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_id","in":"query","description":"PageID is the ID of the requested page. For first request it should be kept empty.","schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","schema":{"type":"integer"}}],"query":[{"name":"page_id","in":"query","description":"PageID is the ID of the requested page. For first request it should be kept empty.","schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","schema":{"type":"integer"}}],"headers":[],"path":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", user_id=user_id, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(user_id=user_id, page_id=page_id, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/points/history/", user_id=user_id, page_id=page_id, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to get a list of valid android paths required by the Rewards INIT API to validate a fraudulent device.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.getRewardsConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration/", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Updates the configuration or inserts new records with the given android paths.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.setRewardsConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ConfigurationRequest
        schema = ConfigurationRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration/", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import SetConfigurationRes
            schema = SetConfigurationRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setRewardsConfiguration")
                print(e)

        return response
    