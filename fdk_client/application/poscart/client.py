"""PosCart Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import PosCartValidator

class PosCart:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "getCart": "/service/application/pos/cart/v1.0/detail",
            "getCartLastModified": "/service/application/pos/cart/v1.0/detail",
            "addItems": "/service/application/pos/cart/v1.0/detail",
            "updateCart": "/service/application/pos/cart/v1.0/detail",
            "getItemCount": "/service/application/pos/cart/v1.0/basic",
            "getCoupons": "/service/application/pos/cart/v1.0/coupon",
            "applyCoupon": "/service/application/pos/cart/v1.0/coupon",
            "removeCoupon": "/service/application/pos/cart/v1.0/coupon",
            "getBulkDiscountOffers": "/service/application/pos/cart/v1.0/bulk-price",
            "applyRewardPoints": "/service/application/pos/cart/v1.0/redeem/points/",
            "getAddresses": "/service/application/pos/cart/v1.0/address",
            "addAddress": "/service/application/pos/cart/v1.0/address",
            "getAddressById": "/service/application/pos/cart/v1.0/address/{id}",
            "updateAddress": "/service/application/pos/cart/v1.0/address/{id}",
            "removeAddress": "/service/application/pos/cart/v1.0/address/{id}",
            "selectAddress": "/service/application/pos/cart/v1.0/select-address",
            "selectPaymentMode": "/service/application/pos/cart/v1.0/payment",
            "validateCouponForPayment": "/service/application/pos/cart/v1.0/payment/validate/",
            "getShipments": "/service/application/pos/cart/v1.0/shipment",
            "updateShipments": "/service/application/pos/cart/v1.0/shipment",
            "checkoutCart": "/service/application/pos/cart/v1.0/checkout",
            "updateCartMeta": "/service/application/pos/cart/v1.0/meta",
            "getAvailableDeliveryModes": "/service/application/pos/cart/v1.0/available-delivery-mode",
            "getStoreAddressByUid": "/service/application/pos/cart/v1.0/store-address",
            "getCartShareLink": "/service/application/pos/cart/v1.0/share-cart",
            "getCartSharedItems": "/service/application/pos/cart/v1.0/share-cart/{token}",
            "updateCartWithSharedItems": "/service/application/pos/cart/v1.0/share-cart/{token}/{action}"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getCart(self, id=None, i=None, b=None, c=None, assign_card_id=None, area_code=None, buy_now=None, body="", request_headers:Dict={}):
        """Use this API to get details of all the items added to a cart.
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        :param c :  : type boolean
        :param assign_card_id :  : type integer
        :param area_code :  : type string
        :param buy_now :  : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if i is not None:
            payload["i"] = i
        if b is not None:
            payload["b"] = b
        if c is not None:
            payload["c"] = c
        if assign_card_id is not None:
            payload["assign_card_id"] = assign_card_id
        if area_code is not None:
            payload["area_code"] = area_code
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = PosCartValidator.getCart()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"c","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the cod charges in breakup of cart items."}},{"in":"query","name":"assign_card_id","schema":{"type":"integer","description":"Token of user's debit or credit card"}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"c","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the cod charges in breakup of cart items."}},{"in":"query","name":"assign_card_id","schema":{"type":"integer","description":"Token of user's debit or credit card"}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}}],"headers":[],"path":[]}""", id=id, i=i, b=b, c=c, assign_card_id=assign_card_id, area_code=area_code, buy_now=buy_now)
        query_string = await create_query_string(id=id, i=i, b=b, c=c, assign_card_id=assign_card_id, area_code=area_code, buy_now=buy_now)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCart"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/detail", id=id, i=i, b=b, c=c, assign_card_id=assign_card_id, area_code=area_code, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCart")
                print(e)

        return response
    
    async def getCartLastModified(self, id=None, body="", request_headers:Dict={}):
        """Use this API to fetch Last-Modified timestamp in header metadata.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = PosCartValidator.getCartLastModified()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartLastModified"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("HEAD", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCartLastModified"]).netloc, "head", await create_url_without_domain("/service/application/pos/cart/v1.0/detail", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        return response
    
    async def addItems(self, i=None, b=None, area_code=None, buy_now=None, id=None, body="", request_headers:Dict={}):
        """Use this API to add items to the cart.
        :param i :  : type boolean
        :param b :  : type boolean
        :param area_code :  : type string
        :param buy_now :  : type boolean
        :param id :  : type string
        """
        payload = {}
        
        if i is not None:
            payload["i"] = i
        if b is not None:
            payload["b"] = b
        if area_code is not None:
            payload["area_code"] = area_code
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = PosCartValidator.addItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddCartRequest
        schema = AddCartRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["addItems"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", i=i, b=b, area_code=area_code, buy_now=buy_now, id=id)
        query_string = await create_query_string(i=i, b=b, area_code=area_code, buy_now=buy_now, id=id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addItems"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/detail", i=i, b=b, area_code=area_code, buy_now=buy_now, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import AddCartDetailResponse
            schema = AddCartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addItems")
                print(e)

        return response
    
    async def updateCart(self, id=None, i=None, b=None, area_code=None, buy_now=None, body="", request_headers:Dict={}):
        """Use this API to update items added to the cart with the help of a request object containing attributes like item_quantity and item_size.
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        :param area_code :  : type string
        :param buy_now :  : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if i is not None:
            payload["i"] = i
        if b is not None:
            payload["b"] = b
        if area_code is not None:
            payload["area_code"] = area_code
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = PosCartValidator.updateCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCartRequest
        schema = UpdateCartRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["updateCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}}],"headers":[],"path":[]}""", id=id, i=i, b=b, area_code=area_code, buy_now=buy_now)
        query_string = await create_query_string(id=id, i=i, b=b, area_code=area_code, buy_now=buy_now)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateCart"]).netloc, "put", await create_url_without_domain("/service/application/pos/cart/v1.0/detail", id=id, i=i, b=b, area_code=area_code, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateCartDetailResponse
            schema = UpdateCartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCart")
                print(e)

        return response
    
    async def getItemCount(self, id=None, buy_now=None, body="", request_headers:Dict={}):
        """Use this API to get the total number of items present in cart.
        :param id : The unique identifier of the cart. : type string
        :param buy_now :  : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = PosCartValidator.getItemCount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getItemCount"], proccessed_params="""{"required":[],"optional":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"Boolean value to get buy_now cart."}}],"query":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"Boolean value to get buy_now cart."}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getItemCount"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/basic", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartItemCountResponse
            schema = CartItemCountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getItemCount")
                print(e)

        return response
    
    async def getCoupons(self, id=None, buy_now=None, body="", request_headers:Dict={}):
        """Use this API to get a list of available coupons along with their details.
        :param id :  : type string
        :param buy_now :  : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = PosCartValidator.getCoupons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCoupons"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart."}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart."}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCoupons"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/coupon", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCouponResponse
            schema = GetCouponResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCoupons")
                print(e)

        return response
    
    async def applyCoupon(self, i=None, b=None, p=None, id=None, buy_now=None, body="", request_headers:Dict={}):
        """Use this API to apply coupons on items in the cart.
        :param i :  : type boolean
        :param b :  : type boolean
        :param p :  : type boolean
        :param id :  : type string
        :param buy_now :  : type boolean
        """
        payload = {}
        
        if i is not None:
            payload["i"] = i
        if b is not None:
            payload["b"] = b
        if p is not None:
            payload["p"] = p
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = PosCartValidator.applyCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplyCouponRequest
        schema = ApplyCouponRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["applyCoupon"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"p","schema":{"type":"boolean","description":"This is a boolean value. Select `true` for getting a payment option in response."}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"p","schema":{"type":"boolean","description":"This is a boolean value. Select `true` for getting a payment option in response."}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", i=i, b=b, p=p, id=id, buy_now=buy_now)
        query_string = await create_query_string(i=i, b=b, p=p, id=id, buy_now=buy_now)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["applyCoupon"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/coupon", i=i, b=b, p=p, id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for applyCoupon")
                print(e)

        return response
    
    async def removeCoupon(self, id=None, buy_now=None, body="", request_headers:Dict={}):
        """Remove Coupon applied on the cart by passing uid in request body.
        :param id :  : type string
        :param buy_now :  : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = PosCartValidator.removeCoupon()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeCoupon"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["removeCoupon"]).netloc, "delete", await create_url_without_domain("/service/application/pos/cart/v1.0/coupon", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeCoupon")
                print(e)

        return response
    
    async def getBulkDiscountOffers(self, item_id=None, article_id=None, uid=None, slug=None, body="", request_headers:Dict={}):
        """Use this API to get a list of applicable offers along with current, next and best offer for given product. Either one of uid, item_id, slug should be present.
        :param item_id : The Item ID of the product : type integer
        :param article_id : Article Mongo ID : type string
        :param uid : UID of the product : type integer
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        if article_id is not None:
            payload["article_id"] = article_id
        if uid is not None:
            payload["uid"] = uid
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = PosCartValidator.getBulkDiscountOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBulkDiscountOffers"], proccessed_params="""{"required":[],"optional":[{"name":"item_id","description":"The Item ID of the product","in":"query","schema":{"type":"integer"}},{"name":"article_id","description":"Article Mongo ID","in":"query","schema":{"type":"string"}},{"name":"uid","description":"UID of the product","in":"query","schema":{"type":"integer"}},{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}}],"query":[{"name":"item_id","description":"The Item ID of the product","in":"query","schema":{"type":"integer"}},{"name":"article_id","description":"Article Mongo ID","in":"query","schema":{"type":"string"}},{"name":"uid","description":"UID of the product","in":"query","schema":{"type":"integer"}},{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", item_id=item_id, article_id=article_id, uid=uid, slug=slug)
        query_string = await create_query_string(item_id=item_id, article_id=article_id, uid=uid, slug=slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getBulkDiscountOffers"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/bulk-price", item_id=item_id, article_id=article_id, uid=uid, slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkPriceResponse
            schema = BulkPriceResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkDiscountOffers")
                print(e)

        return response
    
    async def applyRewardPoints(self, id=None, i=None, b=None, buy_now=None, body="", request_headers:Dict={}):
        """Use this API to redeem a fixed no. of reward points by applying it to the cart.
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        :param buy_now :  : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if i is not None:
            payload["i"] = i
        if b is not None:
            payload["b"] = b
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = PosCartValidator.applyRewardPoints()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RewardPointRequest
        schema = RewardPointRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["applyRewardPoints"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", id=id, i=i, b=b, buy_now=buy_now)
        query_string = await create_query_string(id=id, i=i, b=b, buy_now=buy_now)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["applyRewardPoints"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/redeem/points/", id=id, i=i, b=b, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for applyRewardPoints")
                print(e)

        return response
    
    async def getAddresses(self, cart_id=None, buy_now=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, body="", request_headers:Dict={}):
        """Use this API to get all the addresses associated with an account. If successful, returns a Address resource in the response body specified in GetAddressesResponse.attibutes listed below are optional 
        :param cart_id :  : type string
        :param buy_now :  : type boolean
        :param mobile_no :  : type string
        :param checkout_mode :  : type string
        :param tags :  : type string
        :param is_default :  : type boolean
        """
        payload = {}
        
        if cart_id is not None:
            payload["cart_id"] = cart_id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if mobile_no is not None:
            payload["mobile_no"] = mobile_no
        if checkout_mode is not None:
            payload["checkout_mode"] = checkout_mode
        if tags is not None:
            payload["tags"] = tags
        if is_default is not None:
            payload["is_default"] = is_default

        # Parameter validation
        schema = PosCartValidator.getAddresses()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAddresses"], proccessed_params="""{"required":[],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"headers":[],"path":[]}""", cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        query_string = await create_query_string(cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAddresses"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/address", cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAddressesResponse
            schema = GetAddressesResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAddresses")
                print(e)

        return response
    
    async def addAddress(self, body="", request_headers:Dict={}):
        """Use this API to add an address to an account.
        """
        payload = {}
        

        # Parameter validation
        schema = PosCartValidator.addAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Address
        schema = Address()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["addAddress"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addAddress"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/address", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import SaveAddressResponse
            schema = SaveAddressResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addAddress")
                print(e)

        return response
    
    async def getAddressById(self, id=None, cart_id=None, buy_now=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, body="", request_headers:Dict={}):
        """Use this API to get an addresses using its ID. If successful, returns a Address resource in the response body specified in `Address`. Attibutes listed below are optional 
        :param id :  : type string
        :param cart_id :  : type string
        :param buy_now :  : type boolean
        :param mobile_no :  : type string
        :param checkout_mode :  : type string
        :param tags :  : type string
        :param is_default :  : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if cart_id is not None:
            payload["cart_id"] = cart_id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if mobile_no is not None:
            payload["mobile_no"] = mobile_no
        if checkout_mode is not None:
            payload["checkout_mode"] = checkout_mode
        if tags is not None:
            payload["tags"] = tags
        if is_default is not None:
            payload["is_default"] = is_default

        # Parameter validation
        schema = PosCartValidator.getAddressById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAddressById"], proccessed_params="""{"required":[{"name":"id","in":"path","schema":{"type":"string","description":"ID allotted to the selected address"},"required":true}],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"headers":[],"path":[{"name":"id","in":"path","schema":{"type":"string","description":"ID allotted to the selected address"},"required":true}]}""", id=id, cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        query_string = await create_query_string(id=id, cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAddressById"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/address/{id}", id=id, cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import Address
            schema = Address()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAddressById")
                print(e)

        return response
    
    async def updateAddress(self, id=None, body="", request_headers:Dict={}):
        """Use this API to update an existing address in the account. Request object should contain attributes mentioned in Address  can be updated.
        :param id : ID allotted to the selected address : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = PosCartValidator.updateAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Address
        schema = Address()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["updateAddress"], proccessed_params="""{"required":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateAddress"]).netloc, "put", await create_url_without_domain("/service/application/pos/cart/v1.0/address/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateAddressResponse
            schema = UpdateAddressResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAddress")
                print(e)

        return response
    
    async def removeAddress(self, id=None, body="", request_headers:Dict={}):
        """Use this API to delete an address by its ID. This will returns an object that will indicate whether the address was deleted successfully or not.
        :param id : ID allotted to the selected address : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = PosCartValidator.removeAddress()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeAddress"], proccessed_params="""{"required":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["removeAddress"]).netloc, "delete", await create_url_without_domain("/service/application/pos/cart/v1.0/address/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteAddressResponse
            schema = DeleteAddressResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeAddress")
                print(e)

        return response
    
    async def selectAddress(self, cart_id=None, buy_now=None, i=None, b=None, body="", request_headers:Dict={}):
        """Select Address from all addresses associated with the account in order to ship the cart items to that address, otherwise default address will be selected implicitly. See `SelectCartAddressRequest` in schema of request body for the list of attributes needed to select Address from account. On successful request, this API returns a Cart object. 
        :param cart_id :  : type string
        :param buy_now :  : type boolean
        :param i :  : type boolean
        :param b :  : type boolean
        """
        payload = {}
        
        if cart_id is not None:
            payload["cart_id"] = cart_id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if i is not None:
            payload["i"] = i
        if b is not None:
            payload["b"] = b

        # Parameter validation
        schema = PosCartValidator.selectAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SelectCartAddressRequest
        schema = SelectCartAddressRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["selectAddress"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"cart_id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"cart_id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[]}""", cart_id=cart_id, buy_now=buy_now, i=i, b=b)
        query_string = await create_query_string(cart_id=cart_id, buy_now=buy_now, i=i, b=b)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["selectAddress"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/select-address", cart_id=cart_id, buy_now=buy_now, i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for selectAddress")
                print(e)

        return response
    
    async def selectPaymentMode(self, id=None, buy_now=None, body="", request_headers:Dict={}):
        """Use this API to update cart payment.
        :param id :  : type string
        :param buy_now :  : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = PosCartValidator.selectPaymentMode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCartPaymentRequest
        schema = UpdateCartPaymentRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["selectPaymentMode"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["selectPaymentMode"]).netloc, "put", await create_url_without_domain("/service/application/pos/cart/v1.0/payment", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for selectPaymentMode")
                print(e)

        return response
    
    async def validateCouponForPayment(self, id=None, buy_now=None, address_id=None, payment_mode=None, payment_identifier=None, aggregator_name=None, merchant_code=None, iin=None, network=None, type=None, card_id=None, body="", request_headers:Dict={}):
        """Use this API to validate a coupon against the payment mode such as NetBanking, Wallet, UPI etc.
        :param id :  : type string
        :param buy_now :  : type boolean
        :param address_id :  : type string
        :param payment_mode :  : type string
        :param payment_identifier :  : type string
        :param aggregator_name :  : type string
        :param merchant_code :  : type string
        :param iin :  : type string
        :param network :  : type string
        :param type :  : type string
        :param card_id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if address_id is not None:
            payload["address_id"] = address_id
        if payment_mode is not None:
            payload["payment_mode"] = payment_mode
        if payment_identifier is not None:
            payload["payment_identifier"] = payment_identifier
        if aggregator_name is not None:
            payload["aggregator_name"] = aggregator_name
        if merchant_code is not None:
            payload["merchant_code"] = merchant_code
        if iin is not None:
            payload["iin"] = iin
        if network is not None:
            payload["network"] = network
        if type is not None:
            payload["type"] = type
        if card_id is not None:
            payload["card_id"] = card_id

        # Parameter validation
        schema = PosCartValidator.validateCouponForPayment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["validateCouponForPayment"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"address_id","schema":{"type":"string","description":"ID allotted to an address"}},{"in":"query","name":"payment_mode","schema":{"type":"string","description":"Payment mode selected by the customer"}},{"in":"query","name":"payment_identifier","schema":{"type":"string","description":"Identifier of payment like ICIC, PAYTM"}},{"in":"query","name":"aggregator_name","schema":{"type":"string","description":"Payment gateway identifier"}},{"in":"query","name":"merchant_code","schema":{"type":"string","description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM"}},{"in":"query","name":"iin","schema":{"type":"string","description":"Debit/Credit card prefix (first 6 digit)"}},{"in":"query","name":"network","schema":{"type":"string","description":"Credit/Debit card issuer, e.g. VISA, MASTERCARD, RUPAY"}},{"in":"query","name":"type","schema":{"type":"string","description":"card type, e.g. Credit, Debit"}},{"in":"query","name":"card_id","schema":{"type":"string","description":"saved card token reference id"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"address_id","schema":{"type":"string","description":"ID allotted to an address"}},{"in":"query","name":"payment_mode","schema":{"type":"string","description":"Payment mode selected by the customer"}},{"in":"query","name":"payment_identifier","schema":{"type":"string","description":"Identifier of payment like ICIC, PAYTM"}},{"in":"query","name":"aggregator_name","schema":{"type":"string","description":"Payment gateway identifier"}},{"in":"query","name":"merchant_code","schema":{"type":"string","description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM"}},{"in":"query","name":"iin","schema":{"type":"string","description":"Debit/Credit card prefix (first 6 digit)"}},{"in":"query","name":"network","schema":{"type":"string","description":"Credit/Debit card issuer, e.g. VISA, MASTERCARD, RUPAY"}},{"in":"query","name":"type","schema":{"type":"string","description":"card type, e.g. Credit, Debit"}},{"in":"query","name":"card_id","schema":{"type":"string","description":"saved card token reference id"}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id)
        query_string = await create_query_string(id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["validateCouponForPayment"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/payment/validate/", id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentCouponValidate
            schema = PaymentCouponValidate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateCouponForPayment")
                print(e)

        return response
    
    async def getShipments(self, pick_at_store_uid=None, ordering_store_id=None, p=None, id=None, address_id=None, area_code=None, order_type=None, body="", request_headers:Dict={}):
        """Use this API to get shipment details, expected delivery date, items and price breakup of the shipment.
        :param pick_at_store_uid :  : type integer
        :param ordering_store_id :  : type integer
        :param p : This is a boolean value. Select `true` for getting a payment option in response. : type boolean
        :param id : The unique identifier of the cart : type string
        :param address_id : ID allotted to the selected address : type string
        :param area_code : The PIN Code of the destination address, e.g. 400059 : type string
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        """
        payload = {}
        
        if pick_at_store_uid is not None:
            payload["pick_at_store_uid"] = pick_at_store_uid
        if ordering_store_id is not None:
            payload["ordering_store_id"] = ordering_store_id
        if p is not None:
            payload["p"] = p
        if id is not None:
            payload["id"] = id
        if address_id is not None:
            payload["address_id"] = address_id
        if area_code is not None:
            payload["area_code"] = area_code
        if order_type is not None:
            payload["order_type"] = order_type

        # Parameter validation
        schema = PosCartValidator.getShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipments"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"pick_at_store_uid","required":false,"schema":{"type":"integer","description":"ID of the store from where the order will be picked up by the customer, assuming the order_type is `PickAtStore`. This may or may not be the same as the ID of the ordering store."}},{"in":"query","name":"ordering_store_id","required":false,"schema":{"type":"integer","description":"ID of the store where the customer is ordering from."}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to the selected address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string"}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]}}],"query":[{"in":"query","name":"pick_at_store_uid","required":false,"schema":{"type":"integer","description":"ID of the store from where the order will be picked up by the customer, assuming the order_type is `PickAtStore`. This may or may not be the same as the ID of the ordering store."}},{"in":"query","name":"ordering_store_id","required":false,"schema":{"type":"integer","description":"ID of the store where the customer is ordering from."}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to the selected address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string"}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]}}],"headers":[],"path":[]}""", pick_at_store_uid=pick_at_store_uid, ordering_store_id=ordering_store_id, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type)
        query_string = await create_query_string(pick_at_store_uid=pick_at_store_uid, ordering_store_id=ordering_store_id, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getShipments"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/shipment", pick_at_store_uid=pick_at_store_uid, ordering_store_id=ordering_store_id, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartShipmentsResponse
            schema = CartShipmentsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipments")
                print(e)

        return response
    
    async def updateShipments(self, i=None, p=None, id=None, address_id=None, area_code=None, order_type=None, body="", request_headers:Dict={}):
        """Use this API to update the delivery type and quantity as per customer's preference for either store pick-up or home-delivery.
        :param i : This is a boolean value. Select `true` to retrieve all the items added in the cart. : type boolean
        :param p : This is a boolean value. Select `true` for getting a payment option in response. : type boolean
        :param id : The unique identifier of the cart : type string
        :param address_id : ID allotted to an address : type string
        :param area_code : The PIN Code of the destination address, e.g. 400059 : type string
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        """
        payload = {}
        
        if i is not None:
            payload["i"] = i
        if p is not None:
            payload["p"] = p
        if id is not None:
            payload["id"] = id
        if address_id is not None:
            payload["address_id"] = address_id
        if area_code is not None:
            payload["area_code"] = area_code
        if order_type is not None:
            payload["order_type"] = order_type

        # Parameter validation
        schema = PosCartValidator.updateShipments()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCartShipmentRequest
        schema = UpdateCartShipmentRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["updateShipments"], proccessed_params="""{"required":[],"optional":[{"name":"i","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart.","in":"query","schema":{"type":"boolean"}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to an address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string"}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string"}}],"query":[{"name":"i","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart.","in":"query","schema":{"type":"boolean"}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to an address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string"}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", i=i, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type)
        query_string = await create_query_string(i=i, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateShipments"]).netloc, "put", await create_url_without_domain("/service/application/pos/cart/v1.0/shipment", i=i, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartShipmentsResponse
            schema = CartShipmentsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateShipments")
                print(e)

        return response
    
    async def checkoutCart(self, id=None, body="", request_headers:Dict={}):
        """Use this API to checkout all items in the cart for payment and order generation. For COD, order will be generated directly, whereas for other checkout modes, user will be redirected to a payment gateway.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = PosCartValidator.checkoutCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CartPosCheckoutDetailRequest
        schema = CartPosCheckoutDetailRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["checkoutCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","required":false,"schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"id","required":false,"schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["checkoutCart"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/checkout", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartCheckoutResponse
            schema = CartCheckoutResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkoutCart")
                print(e)

        return response
    
    async def updateCartMeta(self, id=None, buy_now=None, body="", request_headers:Dict={}):
        """Use this API to update cart meta like checkout_mode and gstin.
        :param id :  : type string
        :param buy_now :  : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = PosCartValidator.updateCartMeta()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CartMetaRequest
        schema = CartMetaRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["updateCartMeta"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"this is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"this is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateCartMeta"]).netloc, "put", await create_url_without_domain("/service/application/pos/cart/v1.0/meta", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartMetaResponse
            schema = CartMetaResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCartMeta")
                print(e)

        return response
    
    async def getAvailableDeliveryModes(self, area_code=None, id=None, body="", request_headers:Dict={}):
        """Use this API to get the delivery modes (home-delivery/store-pickup) along with a list of pickup stores available for a given cart at a given PIN Code. User can then view the address of a pickup store with the help of store-address API.
        :param area_code :  : type string
        :param id :  : type string
        """
        payload = {}
        
        if area_code is not None:
            payload["area_code"] = area_code
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = PosCartValidator.getAvailableDeliveryModes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAvailableDeliveryModes"], proccessed_params="""{"required":[{"in":"query","name":"area_code","required":true,"schema":{"type":"string","description":"The PIN Code of the destination address, e.g. 400059"}}],"optional":[{"name":"id","in":"query","required":false,"schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"area_code","required":true,"schema":{"type":"string","description":"The PIN Code of the destination address, e.g. 400059"}},{"name":"id","in":"query","required":false,"schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", area_code=area_code, id=id)
        query_string = await create_query_string(area_code=area_code, id=id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAvailableDeliveryModes"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/available-delivery-mode", area_code=area_code, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDeliveryModesResponse
            schema = CartDeliveryModesResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAvailableDeliveryModes")
                print(e)

        return response
    
    async def getStoreAddressByUid(self, store_uid=None, body="", request_headers:Dict={}):
        """Use this API to get the store details by entering the unique identifier of the pickup stores shown in the response of available-delivery-mode API.
        :param store_uid :  : type integer
        """
        payload = {}
        
        if store_uid is not None:
            payload["store_uid"] = store_uid

        # Parameter validation
        schema = PosCartValidator.getStoreAddressByUid()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getStoreAddressByUid"], proccessed_params="""{"required":[{"in":"query","name":"store_uid","required":true,"schema":{"type":"integer","description":"The unique identifier of the store"}}],"optional":[],"query":[{"in":"query","name":"store_uid","required":true,"schema":{"type":"integer","description":"The unique identifier of the store"}}],"headers":[],"path":[]}""", store_uid=store_uid)
        query_string = await create_query_string(store_uid=store_uid)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getStoreAddressByUid"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/store-address", store_uid=store_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreDetailsResponse
            schema = StoreDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStoreAddressByUid")
                print(e)

        return response
    
    async def getCartShareLink(self, body="", request_headers:Dict={}):
        """Use this API to generate a shared cart snapshot and return a shortlink token. The link can be shared with other users for getting the same items in their cart.
        """
        payload = {}
        

        # Parameter validation
        schema = PosCartValidator.getCartShareLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetShareCartLinkRequest
        schema = GetShareCartLinkRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["getCartShareLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCartShareLink"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/share-cart", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import GetShareCartLinkResponse
            schema = GetShareCartLinkResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCartShareLink")
                print(e)

        return response
    
    async def getCartSharedItems(self, token=None, body="", request_headers:Dict={}):
        """Use this API to get the shared cart details as per the token generated using the share-cart API.
        :param token : Token of the shared short link : type string
        """
        payload = {}
        
        if token is not None:
            payload["token"] = token

        # Parameter validation
        schema = PosCartValidator.getCartSharedItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartSharedItems"], proccessed_params="""{"required":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true}]}""", token=token)
        query_string = await create_query_string(token=token)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCartSharedItems"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/share-cart/{token}", token=token), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import SharedCartResponse
            schema = SharedCartResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCartSharedItems")
                print(e)

        return response
    
    async def updateCartWithSharedItems(self, token=None, action=None, body="", request_headers:Dict={}):
        """Use this API to merge the shared cart with existing cart, or replace the existing cart with the shared cart. The `action` parameter is used to indicate the operation Merge or Replace.
        :param token : Token of the shared short link : type string
        :param action : Operation to perform on the existing cart merge or replace. : type string
        """
        payload = {}
        
        if token is not None:
            payload["token"] = token
        if action is not None:
            payload["action"] = action

        # Parameter validation
        schema = PosCartValidator.updateCartWithSharedItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateCartWithSharedItems"], proccessed_params="""{"required":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}]}""", token=token, action=action)
        query_string = await create_query_string(token=token, action=action)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateCartWithSharedItems"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/share-cart/{token}/{action}", token=token, action=action), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import SharedCartResponse
            schema = SharedCartResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCartWithSharedItems")
                print(e)

        return response
    