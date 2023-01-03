

"""Rewards Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import RewardsValidator

class Rewards:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getOfferByName": "/service/application/rewards/v1.0/offers/{name}/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getOfferByName(self, name=None, body=""):
        """Use this API to get the offer details and configuration by entering the name of the offer.
        :param name : The name given to the offer. : type string
        """
        payload = {}
        
        if name:
            payload["name"] = name
        
        # Parameter validation
        schema = RewardsValidator.getOfferByName()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOfferByName"], proccessed_params="""{"required":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}}]}""", name=name)
        query_string = await create_query_string(name=name)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOfferByName"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/offers/{name}/", name=name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

