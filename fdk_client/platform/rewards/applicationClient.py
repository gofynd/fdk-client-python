

"""Rewards Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import RewardsValidator

class Rewards:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
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
    

