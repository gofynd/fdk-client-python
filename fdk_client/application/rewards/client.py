

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
            "getOfferByName": "/service/application/rewards/v1.0/offers/{name}/",
            "catalogueOrder": "/service/application/rewards/v1.0/catalogue/offer/order/",
            "getUserPointsHistory": "/service/application/rewards/v1.0/user/points/history/",
            "getUserPoints": "/service/application/rewards/v1.0/user/points/",
            "getUserReferralDetails": "/service/application/rewards/v1.0/user/referral/",
            "getOrderDiscount": "/service/application/rewards/v1.0/user/offer/order-discount/",
            "redeemReferralCode": "/service/application/rewards/v1.0/user/referral/redeem/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getOfferByName(self, name=None, body=""):
        """Use this API to get fetch the specific offer details and configuration by the name of the offer.
        :param name : The name given to the offer. : type string
        """
        payload = {}
        
        if name is not None:
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOfferByName"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/offers/{name}/", name=name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import Offer
            schema = Offer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOfferByName")
                print(e)

        

        return response
    
    async def catalogueOrder(self, body=""):
        """Use this API to evaluate the amount of reward points that could be earned on any catalogue product.
        """
        payload = {}
        
        # Parameter validation
        schema = RewardsValidator.catalogueOrder()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CatalogueOrderRequest
        schema = CatalogueOrderRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["catalogueOrder"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["catalogueOrder"]).netloc, "post", await create_url_without_domain("/service/application/rewards/v1.0/catalogue/offer/order/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CatalogueOrderResponse
            schema = CatalogueOrderResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for catalogueOrder")
                print(e)

        

        return response
    
    async def getUserPointsHistory(self, page_id=None, page_size=None, body=""):
        """Use this API to fetch a list of points transactions like giveaway points, signup points, referral points, order earn points, redeem points and expired points.
        :param page_id : PageID is the ID of the requested page. For first request it should be kept empty. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if page_id is not None:
            payload["page_id"] = page_id
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = RewardsValidator.getUserPointsHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserPointsHistory"], proccessed_params="""{"required":[],"optional":[{"name":"page_id","in":"query","description":"PageID is the ID of the requested page. For first request it should be kept empty.","schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","schema":{"type":"integer"}}],"query":[{"name":"page_id","in":"query","description":"PageID is the ID of the requested page. For first request it should be kept empty.","schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","schema":{"type":"integer"}}],"headers":[],"path":[]}""", page_id=page_id, page_size=page_size)
        query_string = await create_query_string(page_id=page_id, page_size=page_size)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getUserPointsHistory"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/user/points/history/", page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import PointsHistoryResponse
            schema = PointsHistoryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserPointsHistory")
                print(e)

        

        return response
    
    async def getUserPoints(self, body=""):
        """Use this API to retrieve total available points of a user for current application.
        """
        payload = {}
        
        # Parameter validation
        schema = RewardsValidator.getUserPoints()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserPoints"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getUserPoints"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/user/points/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import PointsResponse
            schema = PointsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserPoints")
                print(e)

        

        return response
    
    async def getUserReferralDetails(self, body=""):
        """Use this API to retrieve the referral details like referral code of a user.
        """
        payload = {}
        
        # Parameter validation
        schema = RewardsValidator.getUserReferralDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserReferralDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getUserReferralDetails"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/user/referral/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import ReferralDetailsResponse
            schema = ReferralDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserReferralDetails")
                print(e)

        

        return response
    
    async def getOrderDiscount(self, body=""):
        """Use this API to calculate the discount on the order amount, based on all the amount range configured in Order Discount offer.
        """
        payload = {}
        
        # Parameter validation
        schema = RewardsValidator.getOrderDiscount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OrderDiscountRequest
        schema = OrderDiscountRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderDiscount"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrderDiscount"]).netloc, "post", await create_url_without_domain("/service/application/rewards/v1.0/user/offer/order-discount/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import OrderDiscountResponse
            schema = OrderDiscountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrderDiscount")
                print(e)

        

        return response
    
    async def redeemReferralCode(self, body=""):
        """Use this API to enter a referral code following which, the configured points would be credited to a user's reward points account.
        """
        payload = {}
        
        # Parameter validation
        schema = RewardsValidator.redeemReferralCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RedeemReferralCodeRequest
        schema = RedeemReferralCodeRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["redeemReferralCode"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["redeemReferralCode"]).netloc, "post", await create_url_without_domain("/service/application/rewards/v1.0/user/referral/redeem/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import RedeemReferralCodeResponse
            schema = RedeemReferralCodeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for redeemReferralCode")
                print(e)

        

        return response
    

