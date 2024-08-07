"""Rewards Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import RewardsValidator

class Rewards:
    def __init__(self, config: ApplicationConfig):
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
    
    async def getOfferByName(self, name=None, body="", request_headers:Dict={}):
        """Retrieves detailed information about an offer by its name.
        :param name : The name given to the offer. : type string
        """
        payload = {}
        
        if name is not None:
            payload["name"] = name

        # Parameter validation
        schema = RewardsValidator.getOfferByName()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOfferByName"], proccessed_params="""{"required":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"name","in":"path","description":"The name given to the offer.","required":true,"schema":{"type":"string"}}]}""", serverType="application", name=name)
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOfferByName"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/offers/{name}/", name=name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Offer
            schema = Offer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOfferByName")
                print(e)

        return response
    
    async def catalogueOrder(self, body="", request_headers:Dict={}):
        """Place an reward on order items available in the catalogue.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.catalogueOrder()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CatalogueOrderRequest
        schema = CatalogueOrderRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["catalogueOrder"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["catalogueOrder"]).netloc, "post", await create_url_without_domain("/service/application/rewards/v1.0/catalogue/offer/order/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CatalogueOrderResponse
            schema = CatalogueOrderResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for catalogueOrder")
                print(e)

        return response
    
    async def getUserPointsHistory(self, page_id=None, page_size=None, body="", request_headers:Dict={}):
        """Gets the historical data of points earned or spent by the user.
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserPointsHistory"], proccessed_params="""{"required":[],"optional":[{"name":"page_id","in":"query","description":"PageID is the ID of the requested page. For first request it should be kept empty.","schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","schema":{"type":"integer"}}],"query":[{"name":"page_id","in":"query","description":"PageID is the ID of the requested page. For first request it should be kept empty.","schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","schema":{"type":"integer"}}],"headers":[],"path":[]}""", serverType="application", page_id=page_id, page_size=page_size)
        query_string = await create_query_string(page_id=page_id, page_size=page_size)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getUserPointsHistory"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/user/points/history/", page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PointsHistoryResponse
            schema = PointsHistoryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserPointsHistory")
                print(e)

        return response
    
    async def getUserPoints(self, body="", request_headers:Dict={}):
        """Retrieves the current reward points balance for the user.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.getUserPoints()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserPoints"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getUserPoints"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/user/points/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PointsResponse
            schema = PointsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserPoints")
                print(e)

        return response
    
    async def getUserReferralDetails(self, body="", request_headers:Dict={}):
        """Gets the details of the user’s referral status and codes.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.getUserReferralDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserReferralDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getUserReferralDetails"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/user/referral/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ReferralDetailsResponse
            schema = ReferralDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserReferralDetails")
                print(e)

        return response
    
    async def getOrderDiscount(self, body="", request_headers:Dict={}):
        """Retrieve the discount applied to a specific order.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.getOrderDiscount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OrderDiscountRequest
        schema = OrderDiscountRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderDiscount"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrderDiscount"]).netloc, "post", await create_url_without_domain("/service/application/rewards/v1.0/user/offer/order-discount/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderDiscountResponse
            schema = OrderDiscountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrderDiscount")
                print(e)

        return response
    
    async def redeemReferralCode(self, body="", request_headers:Dict={}):
        """Applies a referral code to earn or redeem rewards.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.redeemReferralCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RedeemReferralCodeRequest
        schema = RedeemReferralCodeRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["redeemReferralCode"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["redeemReferralCode"]).netloc, "post", await create_url_without_domain("/service/application/rewards/v1.0/user/referral/redeem/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RedeemReferralCodeResponse
            schema = RedeemReferralCodeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for redeemReferralCode")
                print(e)

        return response
    