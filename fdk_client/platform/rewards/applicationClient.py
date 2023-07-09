

"""Rewards Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import RewardsValidator

class Rewards:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId

    
    async def getGiveaways(self, page_id=None, page_size=None):
        """List of giveaways of the current application.
        :param page_id : pagination page id : type string
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if page_id is not None:
            payload["page_id"] = page_id
        
        if page_size is not None:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = RewardsValidator.getGiveaways()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", page_id=page_id, page_size=page_size)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/", page_id=page_id, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GiveawayResponse
            schema = GiveawayResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGiveaways")
                print(e)

        

        return response
    
    async def createGiveaway(self, body=""):
        """Adds a new giveaway.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.createGiveaway()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Giveaway
        schema = Giveaway()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import Giveaway
            schema = Giveaway()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createGiveaway")
                print(e)

        

        return response
    
    async def getGiveawayByID(self, id=None):
        """Get giveaway by ID.
        :param id : Giveaway ID : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = RewardsValidator.getGiveawayByID()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Giveaway ID","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Giveaway ID","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import Giveaway
            schema = Giveaway()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGiveawayByID")
                print(e)

        

        return response
    
    async def updateGiveaway(self, id=None, body=""):
        """Updates the giveaway by it's ID.
        :param id : Giveaway ID : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        

        # Parameter validation
        schema = RewardsValidator.updateGiveaway()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Giveaway
        schema = Giveaway()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Giveaway ID","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Giveaway ID","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import Giveaway
            schema = Giveaway()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateGiveaway")
                print(e)

        

        return response
    
    async def getOffers(self, ):
        """List of offer of the current application.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.getOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        return response
    
    async def getOfferByName(self, cookie=None, name=None):
        """Get offer by name.
        :param cookie : User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation. : type string
        :param name : Offer name : type string
        """
        payload = {}
        
        if cookie is not None:
            payload["cookie"] = cookie
        
        if name is not None:
            payload["name"] = name
        

        # Parameter validation
        schema = RewardsValidator.getOfferByName()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation.","in":"header","name":"cookie","required":true,"schema":{"type":"string"}},{"description":"Offer name","in":"path","name":"name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[{"description":"User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation.","in":"header","name":"cookie","required":true,"schema":{"type":"string"}}],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Offer name","in":"path","name":"name","required":true,"schema":{"type":"string"}}]}""", cookie=cookie, name=name)
        query_string = await create_query_string(cookie=cookie, name=name)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", cookie=cookie, name=name), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import Offer
            schema = Offer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOfferByName")
                print(e)

        

        return response
    
    async def updateOfferByName(self, name=None, body=""):
        """Updates the offer by name.
        :param name : Offer name : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Offer name","in":"path","name":"name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Offer name","in":"path","name":"name","required":true,"schema":{"type":"string"}}]}""", name=name)
        query_string = await create_query_string(name=name)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
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
    
    async def getUserAvailablePoints(self, user_id=None):
        """User's reward details.
        :param user_id : user id : type string
        """
        payload = {}
        
        if user_id is not None:
            payload["user_id"] = user_id
        

        # Parameter validation
        schema = RewardsValidator.getUserAvailablePoints()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}]}""", user_id=user_id)
        query_string = await create_query_string(user_id=user_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
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
                print("Response Validation failed for getUserAvailablePoints")
                print(e)

        

        return response
    
    async def updateUserStatus(self, user_id=None, body=""):
        """Update user status, active/archive
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}]}""", user_id=user_id)
        query_string = await create_query_string(user_id=user_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
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
    
    async def getUserPointsHistory(self, user_id=None, page_id=None, page_limit=None, page_size=None):
        """Get list of points transactions.
The list of points history is paginated.
        :param user_id : user id : type string
        :param page_id : PageID is the ID of the requested page. For first request it should be kept empty. : type string
        :param page_limit : PageLimit is the number of requested items in response. : type integer
        :param page_size : PageSize is the number of requested items in response. : type integer
        """
        payload = {}
        
        if user_id is not None:
            payload["user_id"] = user_id
        
        if page_id is not None:
            payload["page_id"] = page_id
        
        if page_limit is not None:
            payload["page_limit"] = page_limit
        
        if page_size is not None:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = RewardsValidator.getUserPointsHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/points/history/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"PageID is the ID of the requested page. For first request it should be kept empty.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"PageLimit is the number of requested items in response.","in":"query","name":"page_limit","schema":{"type":"integer"}},{"description":"PageSize is the number of requested items in response.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"PageID is the ID of the requested page. For first request it should be kept empty.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"PageLimit is the number of requested items in response.","in":"query","name":"page_limit","schema":{"type":"integer"}},{"description":"PageSize is the number of requested items in response.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}]}""", user_id=user_id, page_id=page_id, page_limit=page_limit, page_size=page_size)
        query_string = await create_query_string(user_id=user_id, page_id=page_id, page_limit=page_limit, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/points/history/", user_id=user_id, page_id=page_id, page_limit=page_limit, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import HistoryRes
            schema = HistoryRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserPointsHistory")
                print(e)

        

        return response
    

