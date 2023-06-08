

"""Cart Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import CartValidator

class Cart:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getCart": "/service/application/cart/v1.0/detail",
            "getCartLastModified": "/service/application/cart/v1.0/detail",
            "addItems": "/service/application/cart/v1.0/detail",
            "updateCart": "/service/application/cart/v1.0/detail",
            "getItemCount": "/service/application/cart/v1.0/basic",
            "getCoupons": "/service/application/cart/v1.0/coupon",
            "applyCoupon": "/service/application/cart/v1.0/coupon",
            "removeCoupon": "/service/application/cart/v1.0/coupon",
            "getBulkDiscountOffers": "/service/application/cart/v1.0/bulk-price",
            "applyRewardPoints": "/service/application/cart/v1.0/redeem/points/",
            "getAddresses": "/service/application/cart/v1.0/address",
            "addAddress": "/service/application/cart/v1.0/address",
            "getAddressById": "/service/application/cart/v1.0/address/{id}",
            "updateAddress": "/service/application/cart/v1.0/address/{id}",
            "removeAddress": "/service/application/cart/v1.0/address/{id}",
            "selectAddress": "/service/application/cart/v1.0/select-address",
            "selectPaymentMode": "/service/application/cart/v1.0/payment",
            "validateCouponForPayment": "/service/application/cart/v1.0/payment/validate/",
            "getShipments": "/service/application/cart/v1.0/shipment",
            "checkoutCart": "/service/application/cart/v1.0/checkout",
            "updateCartMeta": "/service/application/cart/v1.0/meta",
            "getCartShareLink": "/service/application/cart/v1.0/share-cart",
            "getCartSharedItems": "/service/application/cart/v1.0/share-cart/{token}",
            "updateCartWithSharedItems": "/service/application/cart/v1.0/share-cart/{token}/{action}",
            "getPromotionOffers": "/service/application/cart/v1.0/available-promotions",
            "getLadderOffers": "/service/application/cart/v1.0/available-ladder-prices"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getCart(self, id=None, i=None, b=None, assign_card_id=None, area_code=None, buy_now=None, body=""):
        """Use this API to get details of all the items added to a cart.
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
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
        
        if assign_card_id is not None:
            payload["assign_card_id"] = assign_card_id
        
        if area_code is not None:
            payload["area_code"] = area_code
        
        if buy_now is not None:
            payload["buy_now"] = buy_now
        
        # Parameter validation
        schema = CartValidator.getCart()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"assign_card_id","schema":{"type":"integer","description":"Token of user's debit or credit card"}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"assign_card_id","schema":{"type":"integer","description":"Token of user's debit or credit card"}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}}],"headers":[],"path":[]}""", id=id, i=i, b=b, assign_card_id=assign_card_id, area_code=area_code, buy_now=buy_now)
        query_string = await create_query_string(id=id, i=i, b=b, assign_card_id=assign_card_id, area_code=area_code, buy_now=buy_now)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCart"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/detail", id=id, i=i, b=b, assign_card_id=assign_card_id, area_code=area_code, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCart")
                print(e)

        

        return response
    
    async def getCartLastModified(self, id=None, body=""):
        """Use this API to fetch Last-Modified timestamp in header metadata.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.getCartLastModified()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartLastModified"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("HEAD", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCartLastModified"]).netloc, "head", await create_url_without_domain("/service/application/cart/v1.0/detail", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        return response
    
    async def addItems(self, i=None, b=None, area_code=None, buy_now=None, body=""):
        """Use this API to add items to the cart.
        :param i :  : type boolean
        :param b :  : type boolean
        :param area_code :  : type string
        :param buy_now :  : type boolean
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
        
        # Parameter validation
        schema = CartValidator.addItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddCartRequest
        schema = AddCartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addItems"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}}],"query":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}}],"headers":[],"path":[]}""", i=i, b=b, area_code=area_code, buy_now=buy_now)
        query_string = await create_query_string(i=i, b=b, area_code=area_code, buy_now=buy_now)
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addItems"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/detail", i=i, b=b, area_code=area_code, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import AddCartDetailResponse
            schema = AddCartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addItems")
                print(e)

        

        return response
    
    async def updateCart(self, id=None, i=None, b=None, area_code=None, buy_now=None, body=""):
        """<p>Use this API to update items added to the cart with the help of a request object containing attributes like item_quantity and item_size. These attributes will be fetched from the following APIs</p> <ul> <li><font color="monochrome">operation</font> Operation for current api call. <b>update_item</b> for update items. <b>remove_item</b> for removing items.</li> <li> <font color="monochrome">item_id</font>  "/platform/content/v1/products/"</li> <li> <font color="monochrome">item_size</font>   "/platform/content/v1/products/:slug/sizes/"</li> <li> <font color="monochrome">quantity</font>  item quantity (must be greater than or equal to 1)</li> <li> <font color="monochrome">article_id</font>   "/content​/v1​/products​/:identifier​/sizes​/price​/"</li> <li> <font color="monochrome">item_index</font>  item position in the cart (must be greater than or equal to 0)</li> </ul>
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
        schema = CartValidator.updateCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCartRequest
        schema = UpdateCartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"area_code","schema":{"type":"string","description":"Customer servicable area_code"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is a boolen value. Select `true` to set/initialize buy now cart"}}],"headers":[],"path":[]}""", id=id, i=i, b=b, area_code=area_code, buy_now=buy_now)
        query_string = await create_query_string(id=id, i=i, b=b, area_code=area_code, buy_now=buy_now)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateCart"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/detail", id=id, i=i, b=b, area_code=area_code, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateCartDetailResponse
            schema = UpdateCartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCart")
                print(e)

        

        return response
    
    async def getItemCount(self, id=None, buy_now=None, body=""):
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
        schema = CartValidator.getItemCount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getItemCount"], proccessed_params="""{"required":[],"optional":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"Boolean value to get buy_now cart."}}],"query":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"Boolean value to get buy_now cart."}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getItemCount"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/basic", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CartItemCountResponse
            schema = CartItemCountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getItemCount")
                print(e)

        

        return response
    
    async def getCoupons(self, id=None, buy_now=None, body=""):
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
        schema = CartValidator.getCoupons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCoupons"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart."}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart."}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCoupons"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/coupon", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import GetCouponResponse
            schema = GetCouponResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCoupons")
                print(e)

        

        return response
    
    async def applyCoupon(self, i=None, b=None, p=None, id=None, buy_now=None, body=""):
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
        schema = CartValidator.applyCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplyCouponRequest
        schema = ApplyCouponRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["applyCoupon"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"p","schema":{"type":"boolean","description":"This is a boolean value. Select `true` for getting a payment option in response."}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"p","schema":{"type":"boolean","description":"This is a boolean value. Select `true` for getting a payment option in response."}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", i=i, b=b, p=p, id=id, buy_now=buy_now)
        query_string = await create_query_string(i=i, b=b, p=p, id=id, buy_now=buy_now)
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["applyCoupon"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/coupon", i=i, b=b, p=p, id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for applyCoupon")
                print(e)

        

        return response
    
    async def removeCoupon(self, id=None, buy_now=None, body=""):
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
        schema = CartValidator.removeCoupon()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeCoupon"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)
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
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["removeCoupon"]).netloc, "delete", await create_url_without_domain("/service/application/cart/v1.0/coupon", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeCoupon")
                print(e)

        

        return response
    
    async def getBulkDiscountOffers(self, item_id=None, article_id=None, uid=None, slug=None, body=""):
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
        schema = CartValidator.getBulkDiscountOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBulkDiscountOffers"], proccessed_params="""{"required":[],"optional":[{"name":"item_id","description":"The Item ID of the product","in":"query","schema":{"type":"integer"}},{"name":"article_id","description":"Article Mongo ID","in":"query","schema":{"type":"string"}},{"name":"uid","description":"UID of the product","in":"query","schema":{"type":"integer"}},{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}}],"query":[{"name":"item_id","description":"The Item ID of the product","in":"query","schema":{"type":"integer"}},{"name":"article_id","description":"Article Mongo ID","in":"query","schema":{"type":"string"}},{"name":"uid","description":"UID of the product","in":"query","schema":{"type":"integer"}},{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", item_id=item_id, article_id=article_id, uid=uid, slug=slug)
        query_string = await create_query_string(item_id=item_id, article_id=article_id, uid=uid, slug=slug)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getBulkDiscountOffers"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/bulk-price", item_id=item_id, article_id=article_id, uid=uid, slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import BulkPriceResponse
            schema = BulkPriceResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkDiscountOffers")
                print(e)

        

        return response
    
    async def applyRewardPoints(self, id=None, i=None, b=None, buy_now=None, body=""):
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
        schema = CartValidator.applyRewardPoints()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RewardPointRequest
        schema = RewardPointRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["applyRewardPoints"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", id=id, i=i, b=b, buy_now=buy_now)
        query_string = await create_query_string(id=id, i=i, b=b, buy_now=buy_now)
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["applyRewardPoints"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/redeem/points/", id=id, i=i, b=b, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for applyRewardPoints")
                print(e)

        

        return response
    
    async def getAddresses(self, cart_id=None, buy_now=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, body=""):
        """Use this API to get all the addresses associated with an account. If successful, returns a Address resource in the response body specified in GetAddressesResponse.attibutes listed below are optional <ul> <li> <font color="monochrome">uid</font></li> <li> <font color="monochrome">address_id</font></li> <li> <font color="monochrome">mobile_no</font></li> <li> <font color="monochrome">checkout_mode</font></li> <li> <font color="monochrome">tags</font></li> <li> <font color="monochrome">default</font></li> </ul>
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
        schema = CartValidator.getAddresses()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAddresses"], proccessed_params="""{"required":[],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"headers":[],"path":[]}""", cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        query_string = await create_query_string(cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAddresses"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/address", cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import GetAddressesResponse
            schema = GetAddressesResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAddresses")
                print(e)

        

        return response
    
    async def addAddress(self, body=""):
        """Use this API to add an address to an account.
        """
        payload = {}
        
        # Parameter validation
        schema = CartValidator.addAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Address
        schema = Address()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addAddress"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addAddress"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/address", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import SaveAddressResponse
            schema = SaveAddressResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addAddress")
                print(e)

        

        return response
    
    async def getAddressById(self, id=None, cart_id=None, buy_now=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, body=""):
        """Use this API to get an addresses using its ID. If successful, returns a Address resource in the response body specified in `Address`. Attibutes listed below are optional <ul> <li> <font color="monochrome">mobile_no</font></li> <li> <font color="monochrome">checkout_mode</font></li> <li> <font color="monochrome">tags</font></li> <li> <font color="monochrome">default</font></li> </ul>
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
        schema = CartValidator.getAddressById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAddressById"], proccessed_params="""{"required":[{"name":"id","in":"path","schema":{"type":"string","description":"ID allotted to the selected address"},"required":true}],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"headers":[],"path":[{"name":"id","in":"path","schema":{"type":"string","description":"ID allotted to the selected address"},"required":true}]}""", id=id, cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        query_string = await create_query_string(id=id, cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAddressById"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/address/{id}", id=id, cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import Address
            schema = Address()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAddressById")
                print(e)

        

        return response
    
    async def updateAddress(self, id=None, body=""):
        """<p>Use this API to update an existing address in the account. Request object should contain attributes mentioned in  <font color="blue">Address </font> can be updated. These attributes are:</p> <ul> <li> <font color="monochrome">is_default_address</font></li> <li> <font color="monochrome">landmark</font></li> <li> <font color="monochrome">area</font></li> <li> <font color="monochrome">pincode</font></li> <li> <font color="monochrome">email</font></li> <li> <font color="monochrome">address_type</font></li> <li> <font color="monochrome">name</font></li> <li> <font color="monochrome">address_id</font></li> <li> <font color="monochrome">address</font></li> </ul>
        :param id : ID allotted to the selected address : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.updateAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Address
        schema = Address()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateAddress"], proccessed_params="""{"required":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateAddress"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/address/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateAddressResponse
            schema = UpdateAddressResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAddress")
                print(e)

        

        return response
    
    async def removeAddress(self, id=None, body=""):
        """Use this API to delete an address by its ID. This will returns an object that will indicate whether the address was deleted successfully or not.
        :param id : ID allotted to the selected address : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.removeAddress()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeAddress"], proccessed_params="""{"required":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["removeAddress"]).netloc, "delete", await create_url_without_domain("/service/application/cart/v1.0/address/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteAddressResponse
            schema = DeleteAddressResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeAddress")
                print(e)

        

        return response
    
    async def selectAddress(self, cart_id=None, buy_now=None, i=None, b=None, body=""):
        """<p>Select Address from all addresses associated with the account in order to ship the cart items to that address, otherwise default address will be selected implicitly. See `SelectCartAddressRequest` in schema of request body for the list of attributes needed to select Address from account. On successful request, this API returns a Cart object. Below address attributes are required. <ul> <li> <font color="monochrome">address_id</font></li> <li> <font color="monochrome">billing_address_id</font></li> <li> <font color="monochrome">uid</font></li> </ul></p>
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
        schema = CartValidator.selectAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SelectCartAddressRequest
        schema = SelectCartAddressRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["selectAddress"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"cart_id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"cart_id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[]}""", cart_id=cart_id, buy_now=buy_now, i=i, b=b)
        query_string = await create_query_string(cart_id=cart_id, buy_now=buy_now, i=i, b=b)
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["selectAddress"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/select-address", cart_id=cart_id, buy_now=buy_now, i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for selectAddress")
                print(e)

        

        return response
    
    async def selectPaymentMode(self, id=None, buy_now=None, body=""):
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
        schema = CartValidator.selectPaymentMode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCartPaymentRequest
        schema = UpdateCartPaymentRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["selectPaymentMode"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["selectPaymentMode"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/payment", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponse
            schema = CartDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for selectPaymentMode")
                print(e)

        

        return response
    
    async def validateCouponForPayment(self, id=None, buy_now=None, address_id=None, payment_mode=None, payment_identifier=None, aggregator_name=None, merchant_code=None, iin=None, network=None, type=None, card_id=None, body=""):
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
        schema = CartValidator.validateCouponForPayment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["validateCouponForPayment"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"address_id","schema":{"type":"string","description":"ID allotted to an address"}},{"in":"query","name":"payment_mode","schema":{"type":"string","description":"Payment mode selected by the customer"}},{"in":"query","name":"payment_identifier","schema":{"type":"string","description":"Identifier of payment like ICIC, PAYTM"}},{"in":"query","name":"aggregator_name","schema":{"type":"string","description":"Payment gateway identifier"}},{"in":"query","name":"merchant_code","schema":{"type":"string","description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM"}},{"in":"query","name":"iin","schema":{"type":"string","description":"Debit/Credit card prefix (first 6 digit)"}},{"in":"query","name":"network","schema":{"type":"string","description":"Credit/Debit card issuer, e.g. VISA, MASTERCARD, RUPAY"}},{"in":"query","name":"type","schema":{"type":"string","description":"card type, e.g. Credit, Debit"}},{"in":"query","name":"card_id","schema":{"type":"string","description":"saved card token reference id"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"address_id","schema":{"type":"string","description":"ID allotted to an address"}},{"in":"query","name":"payment_mode","schema":{"type":"string","description":"Payment mode selected by the customer"}},{"in":"query","name":"payment_identifier","schema":{"type":"string","description":"Identifier of payment like ICIC, PAYTM"}},{"in":"query","name":"aggregator_name","schema":{"type":"string","description":"Payment gateway identifier"}},{"in":"query","name":"merchant_code","schema":{"type":"string","description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM"}},{"in":"query","name":"iin","schema":{"type":"string","description":"Debit/Credit card prefix (first 6 digit)"}},{"in":"query","name":"network","schema":{"type":"string","description":"Credit/Debit card issuer, e.g. VISA, MASTERCARD, RUPAY"}},{"in":"query","name":"type","schema":{"type":"string","description":"card type, e.g. Credit, Debit"}},{"in":"query","name":"card_id","schema":{"type":"string","description":"saved card token reference id"}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id)
        query_string = await create_query_string(id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["validateCouponForPayment"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/payment/validate/", id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentCouponValidate
            schema = PaymentCouponValidate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateCouponForPayment")
                print(e)

        

        return response
    
    async def getShipments(self, p=None, id=None, buy_now=None, address_id=None, area_code=None, body=""):
        """Use this API to get shipment details, expected delivery date, items and price breakup of the shipment.
        :param p : This is a boolean value. Select `true` for getting a payment option in response. : type boolean
        :param id : The unique identifier of the cart : type string
        :param buy_now :  : type boolean
        :param address_id : ID allotted to the selected address : type string
        :param area_code : The PIN Code of the destination address, e.g. 400059 : type string
        """
        payload = {}
        
        if p is not None:
            payload["p"] = p
        
        if id is not None:
            payload["id"] = id
        
        if buy_now is not None:
            payload["buy_now"] = buy_now
        
        if address_id is not None:
            payload["address_id"] = address_id
        
        if area_code is not None:
            payload["area_code"] = area_code
        
        # Parameter validation
        schema = CartValidator.getShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipments"], proccessed_params="""{"required":[],"optional":[{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"name":"address_id","description":"ID allotted to the selected address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string"}}],"query":[{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"name":"address_id","description":"ID allotted to the selected address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", p=p, id=id, buy_now=buy_now, address_id=address_id, area_code=area_code)
        query_string = await create_query_string(p=p, id=id, buy_now=buy_now, address_id=address_id, area_code=area_code)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getShipments"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/shipment", p=p, id=id, buy_now=buy_now, address_id=address_id, area_code=area_code), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CartShipmentsResponse
            schema = CartShipmentsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipments")
                print(e)

        

        return response
    
    async def checkoutCart(self, buy_now=None, body=""):
        """Use this API to checkout all items in the cart for payment and order generation. For COD, order will be directly generated, whereas for other checkout modes, user will be redirected to a payment gateway.
        :param buy_now : This indicates the type of cart to checkout : type boolean
        """
        payload = {}
        
        if buy_now is not None:
            payload["buy_now"] = buy_now
        
        # Parameter validation
        schema = CartValidator.checkoutCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CartCheckoutDetailRequest
        schema = CartCheckoutDetailRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["checkoutCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"buy_now","description":"This indicates the type of cart to checkout","schema":{"type":"boolean"}}],"query":[{"in":"query","name":"buy_now","description":"This indicates the type of cart to checkout","schema":{"type":"boolean"}}],"headers":[],"path":[]}""", buy_now=buy_now)
        query_string = await create_query_string(buy_now=buy_now)
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["checkoutCart"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/checkout", buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CartCheckoutResponse
            schema = CartCheckoutResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkoutCart")
                print(e)

        

        return response
    
    async def updateCartMeta(self, id=None, buy_now=None, body=""):
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
        schema = CartValidator.updateCartMeta()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CartMetaRequest
        schema = CartMetaRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateCartMeta"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"this is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"this is boolean to get buy_now cart"}}],"headers":[],"path":[]}""", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateCartMeta"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/meta", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import CartMetaResponse
            schema = CartMetaResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCartMeta")
                print(e)

        

        return response
    
    async def getCartShareLink(self, body=""):
        """Use this API to generate a shared cart snapshot and return a shortlink token. The link can be shared with other users for getting the same items in their cart.
        """
        payload = {}
        
        # Parameter validation
        schema = CartValidator.getCartShareLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetShareCartLinkRequest
        schema = GetShareCartLinkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartShareLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCartShareLink"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/share-cart", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import GetShareCartLinkResponse
            schema = GetShareCartLinkResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCartShareLink")
                print(e)

        

        return response
    
    async def getCartSharedItems(self, token=None, body=""):
        """Use this API to get the shared cart details as per the token generated using the share-cart API.
        :param token : Token of the shared short link : type string
        """
        payload = {}
        
        if token is not None:
            payload["token"] = token
        
        # Parameter validation
        schema = CartValidator.getCartSharedItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartSharedItems"], proccessed_params="""{"required":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true}]}""", token=token)
        query_string = await create_query_string(token=token)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCartSharedItems"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/share-cart/{token}", token=token), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import SharedCartResponse
            schema = SharedCartResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCartSharedItems")
                print(e)

        

        return response
    
    async def updateCartWithSharedItems(self, token=None, action=None, body=""):
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
        schema = CartValidator.updateCartWithSharedItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateCartWithSharedItems"], proccessed_params="""{"required":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}]}""", token=token, action=action)
        query_string = await create_query_string(token=token, action=action)
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateCartWithSharedItems"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/share-cart/{token}/{action}", token=token, action=action), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import SharedCartResponse
            schema = SharedCartResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCartWithSharedItems")
                print(e)

        

        return response
    
    async def getPromotionOffers(self, slug=None, page_size=None, promotion_group=None, body=""):
        """Use this API to get top 5 offers available for current product
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        :param page_size : Number of offers to be fetched to show : type integer
        :param promotion_group : Type of promotion groups : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if promotion_group is not None:
            payload["promotion_group"] = promotion_group
        
        # Parameter validation
        schema = CartValidator.getPromotionOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPromotionOffers"], proccessed_params="""{"required":[],"optional":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show","in":"query","schema":{"type":"integer"}},{"name":"promotion_group","description":"Type of promotion groups","in":"query","schema":{"type":"string"}}],"query":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show","in":"query","schema":{"type":"integer"}},{"name":"promotion_group","description":"Type of promotion groups","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", slug=slug, page_size=page_size, promotion_group=promotion_group)
        query_string = await create_query_string(slug=slug, page_size=page_size, promotion_group=promotion_group)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPromotionOffers"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/available-promotions", slug=slug, page_size=page_size, promotion_group=promotion_group), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import PromotionOffersResponse
            schema = PromotionOffersResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPromotionOffers")
                print(e)

        

        return response
    
    async def getLadderOffers(self, slug=None, store_id=None, promotion_id=None, page_size=None, body=""):
        """Use this API to get applicable ladder price promotion for current product
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        :param store_id : Store uid of assigned store on PDP page. If not passed default first created ladder will be returned : type string
        :param promotion_id : Get ladder information of given promotion id explicitely : type string
        :param page_size : Number of offers to be fetched to show : type integer
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        
        if store_id is not None:
            payload["store_id"] = store_id
        
        if promotion_id is not None:
            payload["promotion_id"] = promotion_id
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = CartValidator.getLadderOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLadderOffers"], proccessed_params="""{"required":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","required":true,"schema":{"type":"string"}}],"optional":[{"name":"store_id","description":"Store uid of assigned store on PDP page. If not passed default first created ladder will be returned","in":"query","schema":{"type":"string"}},{"name":"promotion_id","description":"Get ladder information of given promotion id explicitely","in":"query","required":false,"schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show","in":"query","schema":{"type":"integer"}}],"query":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","required":true,"schema":{"type":"string"}},{"name":"store_id","description":"Store uid of assigned store on PDP page. If not passed default first created ladder will be returned","in":"query","schema":{"type":"string"}},{"name":"promotion_id","description":"Get ladder information of given promotion id explicitely","in":"query","required":false,"schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show","in":"query","schema":{"type":"integer"}}],"headers":[],"path":[]}""", slug=slug, store_id=store_id, promotion_id=promotion_id, page_size=page_size)
        query_string = await create_query_string(slug=slug, store_id=store_id, promotion_id=promotion_id, page_size=page_size)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLadderOffers"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/available-ladder-prices", slug=slug, store_id=store_id, promotion_id=promotion_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        
        if 200 <= int(response['status_code']) < 300:
            from .models import LadderPriceOffers
            schema = LadderPriceOffers()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLadderOffers")
                print(e)

        

        return response
    

