

"""Rewards Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import RewardsValidator

class Rewards:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def showGiveaways(self, page_id=None, page_size=None):
        """List of giveaways of the current application.
        :param page_id : pagination page id : type string
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = RewardsValidator.showGiveaways()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"page_id","in":"query","description":"pagination page id","required":true,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"pagination page size","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[{"name":"page_id","in":"query","description":"pagination page id","required":true,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"pagination page size","required":true,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", page_id=page_id, page_size=page_size)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", page_id=page_id, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def saveGiveAway(self, body=""):
        """Adds a new giveaway.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.saveGiveAway()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.Giveaway import Giveaway
        schema = Giveaway()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getGiveawayById(self, id=None):
        """Get giveaway by ID.
        :param id : Giveaway ID : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = RewardsValidator.getGiveawayById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateGiveAway(self, id=None, body=""):
        """Updates the giveaway by it's ID.
        :param id : Giveaway ID : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = RewardsValidator.updateGiveAway()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.Giveaway import Giveaway
        schema = Giveaway()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Giveaway ID","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getGiveawayAudienceStatus(self, audience_id=None):
        """Get giveaway audience status
        :param audience_id : audience id : type string
        """
        payload = {}
        
        if audience_id:
            payload["audience_id"] = audience_id
        

        # Parameter validation
        schema = RewardsValidator.getGiveawayAudienceStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/audience/{audience_id}/status", """{"required":[{"name":"audience_id","in":"path","description":"audience id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"audience_id","in":"path","description":"audience id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", audience_id=audience_id, )
        query_string = await create_query_string(audience_id=audience_id, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/audience/{audience_id}/status", audience_id=audience_id, ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def showOffers(self, ):
        """List of offers of the current application.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.showOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/", """{"required":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOfferByName(self, name=None, cookie=None):
        """Use this API to get the offer details and configuration by entering the name of the offer.
        :param name : The name given to the offer. : type string
        :param cookie : User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation. : type string
        """
        payload = {}
        
        if name:
            payload["name"] = name
        
        if cookie:
            payload["cookie"] = cookie
        

        # Parameter validation
        schema = RewardsValidator.getOfferByName()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", """{"required":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}},{"name":"cookie","in":"header","description":"User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[{"name":"cookie","in":"header","description":"User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation.","required":true,"schema":{"type":"string"}}],"path":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", name=name, cookie=cookie)
        query_string = await create_query_string(name=name, cookie=cookie)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", name=name, cookie=cookie), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateOfferByName(self, name=None, body=""):
        """Use this API to update the offer details
        :param name : The name given to the offer. : type string
        """
        payload = {}
        
        if name:
            payload["name"] = name
        

        # Parameter validation
        schema = RewardsValidator.updateOfferByName()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.Offer import Offer
        schema = Offer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", """{"required":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", name=name, )
        query_string = await create_query_string(name=name, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", name=name, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateUserStatus(self, user_id=None, body=""):
        """Use this API to update the user status active/archive
        :param user_id : user id : type string
        """
        payload = {}
        
        if user_id:
            payload["user_id"] = user_id
        

        # Parameter validation
        schema = RewardsValidator.updateUserStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AppUser import AppUser
        schema = AppUser()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", """{"required":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", user_id=user_id, )
        query_string = await create_query_string(user_id=user_id, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", user_id=user_id, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def user(self, user_id=None):
        """Use this API to get the user reward details
        :param user_id : user id : type string
        """
        payload = {}
        
        if user_id:
            payload["user_id"] = user_id
        

        # Parameter validation
        schema = RewardsValidator.user()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", """{"required":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", user_id=user_id, )
        query_string = await create_query_string(user_id=user_id, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", user_id=user_id, ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getPointsHistory(self, page_id=None, page_size=None, user_id=None):
        """Use this API to get a list of points transactions.
        :param page_id : PageID is the ID of the requested page. For first request it should be kept empty. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        :param user_id : user id : type string
        """
        payload = {}
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        if user_id:
            payload["user_id"] = user_id
        

        # Parameter validation
        schema = RewardsValidator.getPointsHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/points/history/", """{"required":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_id","in":"query","description":"PageID is the ID of the requested page. For first request it should be kept empty.","schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","schema":{"type":"integer"}}],"query":[{"name":"page_id","in":"query","description":"PageID is the ID of the requested page. For first request it should be kept empty.","schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","schema":{"type":"integer"}}],"headers":[],"path":[{"name":"user_id","in":"path","description":"user id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", page_id=page_id, page_size=page_size, user_id=user_id, )
        query_string = await create_query_string(page_id=page_id, page_size=page_size, user_id=user_id, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/points/history/", page_id=page_id, page_size=page_size, user_id=user_id, ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

