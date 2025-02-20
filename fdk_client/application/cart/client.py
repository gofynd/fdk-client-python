"""Cart Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import CartValidator

class Cart:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "getCart": "/service/application/cart/v1.0/detail",
            "getCartLastModified": "/service/application/cart/v1.0/detail",
            "addItems": "/service/application/cart/v1.0/detail",
            "updateCart": "/service/application/cart/v1.0/detail",
            "deleteCart": "/service/application/cart/v1.0/cart_archive",
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
            "getLadderOffers": "/service/application/cart/v1.0/available-ladder-prices",
            "getPromotionPaymentOffers": "/service/application/cart/v1.0/available-payment-offers",
            "checkoutCartV2": "/service/application/cart/v2.0/checkout",
            "getPromotions": "/service/application/cart/v1.0/promotion"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getCart(self, id=None, i=None, b=None, c=None, assign_card_id=None, area_code=None, buy_now=None, order_type=None, body="", request_headers:Dict={}):
        """Get details of a cart linked to a specific customer using a unique cart ID. It offers an overview of the items, quantities, prices, and other relevant information associated with the cart.
        :param id : The unique identifier of the cart. : type string
        :param i : Select `true` to retrieve all the items added in the cart. : type boolean
        :param b : Select `true` to retrieve the price breakup of cart items. : type boolean
        :param c : Select `true` to retrieve the cod charges in breakup of cart items. : type boolean
        :param assign_card_id : Token of user's debit or credit card. : type integer
        :param area_code : Customer servicable area_code. : type string
        :param buy_now : Select `true` to set/initialize buy now cart. : type boolean
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
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
        if order_type is not None:
            payload["order_type"] = order_type

        # Parameter validation
        schema = CartValidator.getCart()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"c","schema":{"type":"boolean"},"description":"Select `true` to retrieve the cod charges in breakup of cart items."},{"in":"query","name":"assign_card_id","schema":{"type":"integer"},"description":"Token of user's debit or credit card."},{"in":"query","name":"area_code","schema":{"type":"string","x-not-enum":true},"description":"Customer servicable area_code."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Select `true` to set/initialize buy now cart."},{"in":"query","name":"order_type","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]},"description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself."}],"query":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"c","schema":{"type":"boolean"},"description":"Select `true` to retrieve the cod charges in breakup of cart items."},{"in":"query","name":"assign_card_id","schema":{"type":"integer"},"description":"Token of user's debit or credit card."},{"in":"query","name":"area_code","schema":{"type":"string","x-not-enum":true},"description":"Customer servicable area_code."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Select `true` to set/initialize buy now cart."},{"in":"query","name":"order_type","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]},"description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself."}],"headers":[],"path":[]}""", serverType="application", id=id, i=i, b=b, c=c, assign_card_id=assign_card_id, area_code=area_code, buy_now=buy_now, order_type=order_type)
        query_string = await create_query_string(id=id, i=i, b=b, c=c, assign_card_id=assign_card_id, area_code=area_code, buy_now=buy_now, order_type=order_type)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCart"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/detail", id=id, i=i, b=b, c=c, assign_card_id=assign_card_id, area_code=area_code, buy_now=buy_now, order_type=order_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResult
            schema = CartDetailResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCart")
                print(e)

        return response
    
    async def getCartLastModified(self, id=None, body="", request_headers:Dict={}):
        """Retrieve the last modified timestamp of the cart using unique cart ID. It indicates the most recent update made to the cart's content or properties.
        :param id : The unique identifier of the cart. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.getCartLastModified()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartLastModified"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."}],"query":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."}],"headers":[],"path":[]}""", serverType="application", id=id)
        query_string = await create_query_string(id=id)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("HEAD", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCartLastModified"]).netloc, "head", await create_url_without_domain("/service/application/cart/v1.0/detail", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def addItems(self, i=None, b=None, area_code=None, buy_now=None, id=None, order_type=None, body="", request_headers:Dict={}):
        """Add product items to the customer's existing shopping cart. If there is no existing cart associated with the customer, it creates a new one and adds the items to it.
        :param i : Select `true` to retrieve all the items added in the cart. : type boolean
        :param b : Select `true` to retrieve the price breakup of cart items. : type boolean
        :param area_code : Customer servicable area_code. : type string
        :param buy_now : Select `true` to set/initialize buy now cart. : type boolean
        :param id : The unique identifier of the cart. : type string
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
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
        if order_type is not None:
            payload["order_type"] = order_type

        # Parameter validation
        schema = CartValidator.addItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddCartCreation
        schema = AddCartCreation()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["addItems"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"area_code","schema":{"type":"string","x-not-enum":true},"description":"Customer servicable area_code."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Select `true` to set/initialize buy now cart."},{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"order_type","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]},"description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself."}],"query":[{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"area_code","schema":{"type":"string","x-not-enum":true},"description":"Customer servicable area_code."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Select `true` to set/initialize buy now cart."},{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"order_type","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]},"description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself."}],"headers":[],"path":[]}""", serverType="application", i=i, b=b, area_code=area_code, buy_now=buy_now, id=id, order_type=order_type)
        query_string = await create_query_string(i=i, b=b, area_code=area_code, buy_now=buy_now, id=id, order_type=order_type)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addItems"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/detail", i=i, b=b, area_code=area_code, buy_now=buy_now, id=id, order_type=order_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AddCartDetailResult
            schema = AddCartDetailResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addItems")
                print(e)

        return response
    
    async def updateCart(self, id=None, i=None, b=None, area_code=None, buy_now=None, cart_type=None, order_type=None, body="", request_headers:Dict={}):
        """Update cart. Customers can modify added product attributes such as quantity and size, as well as remove items from the cart.
        :param id : The unique identifier of the cart. : type string
        :param i : Select `true` to retrieve all the items added in the cart. : type boolean
        :param b : Select `true` to retrieve the price breakup of cart items. : type boolean
        :param area_code : Customer servicable area_code. : type string
        :param buy_now : Select `true` to set/initialize buy now cart. : type boolean
        :param cart_type : The type of cart. : type string
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
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
        if cart_type is not None:
            payload["cart_type"] = cart_type
        if order_type is not None:
            payload["order_type"] = order_type

        # Parameter validation
        schema = CartValidator.updateCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCartCreation
        schema = UpdateCartCreation()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["updateCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"area_code","schema":{"type":"string","x-not-enum":true},"description":"Customer servicable area_code."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Select `true` to set/initialize buy now cart."},{"name":"cart_type","in":"query","schema":{"type":"string","x-not-enum":true},"description":"The type of cart."},{"in":"query","name":"order_type","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]},"description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself."}],"query":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"area_code","schema":{"type":"string","x-not-enum":true},"description":"Customer servicable area_code."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Select `true` to set/initialize buy now cart."},{"name":"cart_type","in":"query","schema":{"type":"string","x-not-enum":true},"description":"The type of cart."},{"in":"query","name":"order_type","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]},"description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself."}],"headers":[],"path":[]}""", serverType="application", id=id, i=i, b=b, area_code=area_code, buy_now=buy_now, cart_type=cart_type, order_type=order_type)
        query_string = await create_query_string(id=id, i=i, b=b, area_code=area_code, buy_now=buy_now, cart_type=cart_type, order_type=order_type)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateCart"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/detail", id=id, i=i, b=b, area_code=area_code, buy_now=buy_now, cart_type=cart_type, order_type=order_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateCartDetailResult
            schema = UpdateCartDetailResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCart")
                print(e)

        return response
    
    async def deleteCart(self, id=None, body="", request_headers:Dict={}):
        """Delete all items from the user's cart and resets it to its initial state, providing a clean slate for new selections.
        :param id : The unique identifier of the cart. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.deleteCart()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteCart"], proccessed_params="""{"required":[],"optional":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}}],"query":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}}],"headers":[],"path":[]}""", serverType="application", id=id)
        query_string = await create_query_string(id=id)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deleteCart"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/cart_archive", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteCartDetailResult
            schema = DeleteCartDetailResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCart")
                print(e)

        return response
    
    async def getItemCount(self, id=None, buy_now=None, body="", request_headers:Dict={}):
        """Get total count of items currently present in the customer's cart.
        :param id : The unique identifier of the cart. : type string
        :param buy_now : Boolean value to get buy_now cart. : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = CartValidator.getItemCount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getItemCount"], proccessed_params="""{"required":[],"optional":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Boolean value to get buy_now cart."}],"query":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Boolean value to get buy_now cart."}],"headers":[],"path":[]}""", serverType="application", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getItemCount"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/basic", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartItemCountResult
            schema = CartItemCountResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getItemCount")
                print(e)

        return response
    
    async def getCoupons(self, id=None, buy_now=None, slug=None, store_id=None, body="", request_headers:Dict={}):
        """List all available coupons that customer can apply to their carts. It provides details about each coupon, including its code, discount amount, and applicable conditions.
        :param id : The unique identifier of the cart. : type string
        :param buy_now : Whether to get buy_now cart. : type boolean
        :param slug : Product slug to fetch the available coupons. : type string
        :param store_id : Unique identifier of a store. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if slug is not None:
            payload["slug"] = slug
        if store_id is not None:
            payload["store_id"] = store_id

        # Parameter validation
        schema = CartValidator.getCoupons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCoupons"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."},{"in":"query","name":"slug","schema":{"type":"string"},"description":"Product slug to fetch the available coupons."},{"in":"query","name":"store_id","schema":{"type":"string"},"description":"Unique identifier of a store."}],"query":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."},{"in":"query","name":"slug","schema":{"type":"string"},"description":"Product slug to fetch the available coupons."},{"in":"query","name":"store_id","schema":{"type":"string"},"description":"Unique identifier of a store."}],"headers":[],"path":[]}""", serverType="application", id=id, buy_now=buy_now, slug=slug, store_id=store_id)
        query_string = await create_query_string(id=id, buy_now=buy_now, slug=slug, store_id=store_id)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCoupons"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/coupon", id=id, buy_now=buy_now, slug=slug, store_id=store_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCouponResult
            schema = GetCouponResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCoupons")
                print(e)

        return response
    
    async def applyCoupon(self, i=None, b=None, p=None, id=None, buy_now=None, cart_type=None, body="", request_headers:Dict={}):
        """Apply a coupon code to the cart to trigger discounts on eligible items.
        :param i : Select `true` to retrieve all the items added in the cart. : type boolean
        :param b : Select `true` to retrieve the price breakup of cart items. : type boolean
        :param p : Select `true` for getting a payment option in response. : type boolean
        :param id : The unique identifier of the cart. : type string
        :param buy_now : This is boolean to get buy_now cart. : type boolean
        :param cart_type : The type of cart. : type string
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
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.applyCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplyCoupon
        schema = ApplyCoupon()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["applyCoupon"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"p","schema":{"type":"boolean"},"description":"Select `true` for getting a payment option in response."},{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is boolean to get buy_now cart."},{"in":"query","name":"cart_type","schema":{"type":"string","x-not-enum":true},"description":"The type of cart."}],"query":[{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"p","schema":{"type":"boolean"},"description":"Select `true` for getting a payment option in response."},{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is boolean to get buy_now cart."},{"in":"query","name":"cart_type","schema":{"type":"string","x-not-enum":true},"description":"The type of cart."}],"headers":[],"path":[]}""", serverType="application", i=i, b=b, p=p, id=id, buy_now=buy_now, cart_type=cart_type)
        query_string = await create_query_string(i=i, b=b, p=p, id=id, buy_now=buy_now, cart_type=cart_type)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["applyCoupon"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/coupon", i=i, b=b, p=p, id=id, buy_now=buy_now, cart_type=cart_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResult
            schema = CartDetailResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for applyCoupon")
                print(e)

        return response
    
    async def removeCoupon(self, id=None, buy_now=None, body="", request_headers:Dict={}):
        """Remove an applied coupon from the customer's cart, thereby removing the associated discount from the cart total.
        :param id : The unique identifier of the cart. : type string
        :param buy_now : Wheter to get buy_now cart. : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = CartValidator.removeCoupon()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeCoupon"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Wheter to get buy_now cart."}],"query":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Wheter to get buy_now cart."}],"headers":[],"path":[]}""", serverType="application", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["removeCoupon"]).netloc, "delete", await create_url_without_domain("/service/application/cart/v1.0/coupon", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResult
            schema = CartDetailResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeCoupon")
                print(e)

        return response
    
    async def getBulkDiscountOffers(self, item_id=None, article_id=None, uid=None, slug=None, body="", request_headers:Dict={}):
        """List offer discounts with information about quantity and seller. One offer is marked with a "best" flag, indicating it as the best offer among the list.
        :param item_id : The Item ID of the product. : type integer
        :param article_id : Article Mongo ID. : type string
        :param uid : UID of the product. : type integer
        :param slug : A short, human-readable, URL-friendly identifier of a product. : type string
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBulkDiscountOffers"], proccessed_params="""{"required":[],"optional":[{"name":"item_id","description":"The Item ID of the product.","in":"query","schema":{"type":"integer"}},{"name":"article_id","description":"Article Mongo ID.","in":"query","schema":{"type":"string"}},{"name":"uid","description":"UID of the product.","in":"query","schema":{"type":"integer"}},{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product.","in":"query","schema":{"type":"string"}}],"query":[{"name":"item_id","description":"The Item ID of the product.","in":"query","schema":{"type":"integer"}},{"name":"article_id","description":"Article Mongo ID.","in":"query","schema":{"type":"string"}},{"name":"uid","description":"UID of the product.","in":"query","schema":{"type":"integer"}},{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product.","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", serverType="application", item_id=item_id, article_id=article_id, uid=uid, slug=slug)
        query_string = await create_query_string(item_id=item_id, article_id=article_id, uid=uid, slug=slug)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getBulkDiscountOffers"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/bulk-price", item_id=item_id, article_id=article_id, uid=uid, slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkPriceResult
            schema = BulkPriceResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkDiscountOffers")
                print(e)

        return response
    
    async def applyRewardPoints(self, id=None, i=None, b=None, buy_now=None, body="", request_headers:Dict={}):
        """Users can redeem their accumulated reward points and apply them to the items in their cart, thereby availing discounts on their current purchases.
        :param id : The unique identifier of the cart. : type string
        :param i : Select `true` to retrieve all the items added in the cart. : type boolean
        :param b : Select `true` to retrieve the price breakup of cart items. : type boolean
        :param buy_now : This is boolean to get buy_now cart. : type boolean
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
        from .models import RewardPointCreation
        schema = RewardPointCreation()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["applyRewardPoints"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is boolean to get buy_now cart."}],"query":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is boolean to get buy_now cart."}],"headers":[],"path":[]}""", serverType="application", id=id, i=i, b=b, buy_now=buy_now)
        query_string = await create_query_string(id=id, i=i, b=b, buy_now=buy_now)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["applyRewardPoints"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/redeem/points/", id=id, i=i, b=b, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResult
            schema = CartDetailResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for applyRewardPoints")
                print(e)

        return response
    
    async def getAddresses(self, cart_id=None, buy_now=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, body="", request_headers:Dict={}):
        """List all addresses saved by the customer, simplifying the checkout process by offering pre-saved address options for delivery.
        :param cart_id : The unique identifier of the user cart. : type string
        :param buy_now : Whether to get buy_now cart. : type boolean
        :param mobile_no : Mobile number of the customer. : type string
        :param checkout_mode : Option to checkout for self or for others. : type string
        :param tags : Tag given to an address, e.g. work, home, office, shop. : type string
        :param is_default : Select `true` to fetch the default address. : type boolean
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAddresses"], proccessed_params="""{"required":[],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string"},"description":"The unique identifier of the user cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."},{"in":"query","name":"mobile_no","schema":{"type":"string"},"description":"Mobile number of the customer."},{"in":"query","name":"checkout_mode","schema":{"type":"string"},"description":"Option to checkout for self or for others."},{"in":"query","name":"tags","schema":{"type":"string"},"description":"Tag given to an address, e.g. work, home, office, shop."},{"in":"query","name":"is_default","schema":{"type":"boolean"},"description":"Select `true` to fetch the default address."}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string"},"description":"The unique identifier of the user cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."},{"in":"query","name":"mobile_no","schema":{"type":"string"},"description":"Mobile number of the customer."},{"in":"query","name":"checkout_mode","schema":{"type":"string"},"description":"Option to checkout for self or for others."},{"in":"query","name":"tags","schema":{"type":"string"},"description":"Tag given to an address, e.g. work, home, office, shop."},{"in":"query","name":"is_default","schema":{"type":"boolean"},"description":"Select `true` to fetch the default address."}],"headers":[],"path":[]}""", serverType="application", cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        query_string = await create_query_string(cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAddresses"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/address", cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetAddressesResult
            schema = GetAddressesResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAddresses")
                print(e)

        return response
    
    async def addAddress(self, body="", request_headers:Dict={}):
        """Add a new address to their cart to save details such as name, email, contact information, and address.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.addAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import Address
        schema = Address()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["addAddress"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addAddress"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/address", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SaveAddressResult
            schema = SaveAddressResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addAddress")
                print(e)

        return response
    
    async def getAddressById(self, id=None, cart_id=None, buy_now=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, body="", request_headers:Dict={}):
        """Get a specific customer address stored in the system by providing its unique identifier. This API provides detailed information about the address, including the recipient's name, address, city, postal code, and other relevant details.
        :param id : ID allotted to the selected address. : type string
        :param cart_id : The unique identifier of the cart. : type string
        :param buy_now : This is boolean to get buy_now cart. : type boolean
        :param mobile_no : Mobile number of the customer. : type string
        :param checkout_mode : Option to checkout for self or for others. : type string
        :param tags : Tag given to an address, e.g. work, home, office, shop. : type string
        :param is_default : This is a boolean value. Select `true` to fetch the default address. : type boolean
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAddressById"], proccessed_params="""{"required":[{"name":"id","in":"path","schema":{"type":"string"},"required":true,"description":"ID allotted to the selected address."}],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is boolean to get buy_now cart."},{"in":"query","name":"mobile_no","schema":{"type":"string"},"description":"Mobile number of the customer."},{"in":"query","name":"checkout_mode","schema":{"type":"string"},"description":"Option to checkout for self or for others."},{"in":"query","name":"tags","schema":{"type":"string"},"description":"Tag given to an address, e.g. work, home, office, shop."},{"in":"query","name":"is_default","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to fetch the default address."}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is boolean to get buy_now cart."},{"in":"query","name":"mobile_no","schema":{"type":"string"},"description":"Mobile number of the customer."},{"in":"query","name":"checkout_mode","schema":{"type":"string"},"description":"Option to checkout for self or for others."},{"in":"query","name":"tags","schema":{"type":"string"},"description":"Tag given to an address, e.g. work, home, office, shop."},{"in":"query","name":"is_default","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to fetch the default address."}],"headers":[],"path":[{"name":"id","in":"path","schema":{"type":"string"},"required":true,"description":"ID allotted to the selected address."}]}""", serverType="application", id=id, cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        query_string = await create_query_string(cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAddressById"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/address/{id}", id=id, cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

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
        """Customer can modify the details of a previously saved addresses.
        :param id : ID allotted to the selected address. : type string
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

        url_with_params = await create_url_with_params(api_url=self._urls["updateAddress"], proccessed_params="""{"required":[{"name":"id","description":"ID allotted to the selected address.","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","description":"ID allotted to the selected address.","schema":{"type":"string"},"in":"path","required":true}]}""", serverType="application", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateAddress"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/address/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateAddressResult
            schema = UpdateAddressResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAddress")
                print(e)

        return response
    
    async def removeAddress(self, id=None, body="", request_headers:Dict={}):
        """Delete an existing customer address from the system.
        :param id : ID allotted to the selected address. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.removeAddress()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeAddress"], proccessed_params="""{"required":[{"name":"id","description":"ID allotted to the selected address.","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","description":"ID allotted to the selected address.","schema":{"type":"string"},"in":"path","required":true}]}""", serverType="application", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["removeAddress"]).netloc, "delete", await create_url_without_domain("/service/application/cart/v1.0/address/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteAddressResult
            schema = DeleteAddressResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeAddress")
                print(e)

        return response
    
    async def selectAddress(self, cart_id=None, buy_now=None, i=None, b=None, body="", request_headers:Dict={}):
        """Select an address from the saved customer addresses and validates the availability of items in the cart. Additionally, it verifies and updates the delivery promise based on the selected address.
        :param cart_id : The unique identifier of the cart. : type string
        :param buy_now : Whether to get buy_now cart. : type boolean
        :param i : Select `true` to retrieve all the items added in the cart. : type boolean
        :param b : Select `true` to retrieve the price breakup of cart items. : type boolean
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
        from .models import SelectCartAddressCreation
        schema = SelectCartAddressCreation()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["selectAddress"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"cart_id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."}],"query":[{"in":"query","name":"cart_id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"Select `true` to retrieve the price breakup of cart items."}],"headers":[],"path":[]}""", serverType="application", cart_id=cart_id, buy_now=buy_now, i=i, b=b)
        query_string = await create_query_string(cart_id=cart_id, buy_now=buy_now, i=i, b=b)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["selectAddress"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/select-address", cart_id=cart_id, buy_now=buy_now, i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResult
            schema = CartDetailResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for selectAddress")
                print(e)

        return response
    
    async def selectPaymentMode(self, id=None, buy_now=None, body="", request_headers:Dict={}):
        """Select a preferred payment mode from available options during the cart checkout process to securely and efficiently complete their transaction.
        :param id : The unique identifier of the cart. : type string
        :param buy_now : Whether to get buy_now cart. : type boolean
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
        from .models import UpdateCartPaymentCreation
        schema = UpdateCartPaymentCreation()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["selectPaymentMode"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."}],"query":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."}],"headers":[],"path":[]}""", serverType="application", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["selectPaymentMode"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/payment", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResult
            schema = CartDetailResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for selectPaymentMode")
                print(e)

        return response
    
    async def validateCouponForPayment(self, id=None, buy_now=None, address_id=None, payment_mode=None, payment_identifier=None, aggregator_name=None, merchant_code=None, iin=None, network=None, type=None, card_id=None, cart_type=None, body="", request_headers:Dict={}):
        """Validate the applicability of a coupon code for the selected payment mode for the existing cart. This ensures the coupon's validity before proceeding with the payment process, enhancing user experience and preventing potential errors during transactions.
        :param id : The unique identifier of the cart. : type string
        :param buy_now : Whether to get buy_now cart. : type boolean
        :param address_id : ID allotted to an address. : type string
        :param payment_mode : Payment mode selected by the customer. : type string
        :param payment_identifier : Identifier of payment like ICIC, PAYTM. : type string
        :param aggregator_name : Payment gateway identifier. : type string
        :param merchant_code : Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM. : type string
        :param iin : Debit/Credit card prefix (first 6 digit). : type string
        :param network : Credit/Debit card issuer, e.g. VISA, MASTERCARD, RUPAY. : type string
        :param type : Card type, e.g. Credit, Debit. : type string
        :param card_id : Saved card token reference id. : type string
        :param cart_type : Type of the cart. : type string
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
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.validateCouponForPayment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["validateCouponForPayment"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."},{"in":"query","name":"address_id","schema":{"type":"string"},"description":"ID allotted to an address."},{"in":"query","name":"payment_mode","schema":{"type":"string"},"description":"Payment mode selected by the customer."},{"in":"query","name":"payment_identifier","schema":{"type":"string"},"description":"Identifier of payment like ICIC, PAYTM."},{"in":"query","name":"aggregator_name","schema":{"type":"string"},"description":"Payment gateway identifier."},{"in":"query","name":"merchant_code","schema":{"type":"string","x-not-enum":true},"description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM."},{"in":"query","name":"iin","schema":{"type":"string"},"description":"Debit/Credit card prefix (first 6 digit)."},{"in":"query","name":"network","schema":{"type":"string"},"description":"Credit/Debit card issuer, e.g. VISA, MASTERCARD, RUPAY."},{"in":"query","name":"type","schema":{"type":"string"},"description":"Card type, e.g. Credit, Debit."},{"in":"query","name":"card_id","schema":{"type":"string"},"description":"Saved card token reference id."},{"in":"query","name":"cart_type","schema":{"type":"string","x-not-enum":true},"description":"Type of the cart."}],"query":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."},{"in":"query","name":"address_id","schema":{"type":"string"},"description":"ID allotted to an address."},{"in":"query","name":"payment_mode","schema":{"type":"string"},"description":"Payment mode selected by the customer."},{"in":"query","name":"payment_identifier","schema":{"type":"string"},"description":"Identifier of payment like ICIC, PAYTM."},{"in":"query","name":"aggregator_name","schema":{"type":"string"},"description":"Payment gateway identifier."},{"in":"query","name":"merchant_code","schema":{"type":"string","x-not-enum":true},"description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM."},{"in":"query","name":"iin","schema":{"type":"string"},"description":"Debit/Credit card prefix (first 6 digit)."},{"in":"query","name":"network","schema":{"type":"string"},"description":"Credit/Debit card issuer, e.g. VISA, MASTERCARD, RUPAY."},{"in":"query","name":"type","schema":{"type":"string"},"description":"Card type, e.g. Credit, Debit."},{"in":"query","name":"card_id","schema":{"type":"string"},"description":"Saved card token reference id."},{"in":"query","name":"cart_type","schema":{"type":"string","x-not-enum":true},"description":"Type of the cart."}],"headers":[],"path":[]}""", serverType="application", id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id, cart_type=cart_type)
        query_string = await create_query_string(id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id, cart_type=cart_type)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["validateCouponForPayment"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/payment/validate/", id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id, cart_type=cart_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentCouponValidate
            schema = PaymentCouponValidate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateCouponForPayment")
                print(e)

        return response
    
    async def getShipments(self, p=None, id=None, buy_now=None, address_id=None, area_code=None, order_type=None, body="", request_headers:Dict={}):
        """Get shipment details for the items in a cart, specific to the selected address. Shipment details include delivery promises, seller information, item details, and other relevant information.
        :param p : Select `true` for getting a payment option in response. : type boolean
        :param id : The unique identifier of the cart. : type string
        :param buy_now : This is boolean to get buy_now cart. : type boolean
        :param address_id : ID allotted to the selected address. : type string
        :param area_code : The PIN Code of the destination address, e.g. 400059. : type string
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. Digital - If the customer wants to buy digital voucher ( for jiogames ). : type string
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
        if order_type is not None:
            payload["order_type"] = order_type

        # Parameter validation
        schema = CartValidator.getShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipments"], proccessed_params="""{"required":[],"optional":[{"name":"p","description":"Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart.","in":"query","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is boolean to get buy_now cart."},{"name":"address_id","description":"ID allotted to the selected address.","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059.","in":"query","schema":{"type":"string","x-not-enum":true}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. Digital - If the customer wants to buy digital voucher ( for jiogames ).","in":"query","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]}}],"query":[{"name":"p","description":"Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart.","in":"query","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is boolean to get buy_now cart."},{"name":"address_id","description":"ID allotted to the selected address.","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059.","in":"query","schema":{"type":"string","x-not-enum":true}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. Digital - If the customer wants to buy digital voucher ( for jiogames ).","in":"query","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]}}],"headers":[],"path":[]}""", serverType="application", p=p, id=id, buy_now=buy_now, address_id=address_id, area_code=area_code, order_type=order_type)
        query_string = await create_query_string(p=p, id=id, buy_now=buy_now, address_id=address_id, area_code=area_code, order_type=order_type)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getShipments"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/shipment", p=p, id=id, buy_now=buy_now, address_id=address_id, area_code=area_code, order_type=order_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartShipmentsResult
            schema = CartShipmentsResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipments")
                print(e)

        return response
    
    async def checkoutCart(self, buy_now=None, cart_type=None, body="", request_headers:Dict={}):
        """The checkout cart initiates the order creation process based on the selected address and payment method. It revalidates the cart details to ensure safe and seamless order placement.
        :param buy_now : This indicates the type of cart to checkout. : type boolean
        :param cart_type : The type of cart. : type string
        """
        payload = {}
        
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.checkoutCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CartCheckoutDetailCreation
        schema = CartCheckoutDetailCreation()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["checkoutCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"buy_now","description":"This indicates the type of cart to checkout.","schema":{"type":"boolean"}},{"name":"cart_type","in":"query","schema":{"type":"string","x-not-enum":true},"description":"The type of cart."}],"query":[{"in":"query","name":"buy_now","description":"This indicates the type of cart to checkout.","schema":{"type":"boolean"}},{"name":"cart_type","in":"query","schema":{"type":"string","x-not-enum":true},"description":"The type of cart."}],"headers":[],"path":[]}""", serverType="application", buy_now=buy_now, cart_type=cart_type)
        query_string = await create_query_string(buy_now=buy_now, cart_type=cart_type)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["checkoutCart"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/checkout", buy_now=buy_now, cart_type=cart_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartCheckoutResult
            schema = CartCheckoutResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkoutCart")
                print(e)

        return response
    
    async def updateCartMeta(self, id=None, buy_now=None, body="", request_headers:Dict={}):
        """Update metadata associated with a cart, which includes customer preferences, delivery instructions, or any special requirements related to the cart items.
        :param id : The unique identifier of the cart. : type string
        :param buy_now : Whether to get buy_now cart. : type boolean
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
        from .models import CartMetaCreation
        schema = CartMetaCreation()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["updateCartMeta"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."}],"query":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Whether to get buy_now cart."}],"headers":[],"path":[]}""", serverType="application", id=id, buy_now=buy_now)
        query_string = await create_query_string(id=id, buy_now=buy_now)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateCartMeta"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/meta", id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartMetaResult
            schema = CartMetaResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCartMeta")
                print(e)

        return response
    
    async def getCartShareLink(self, body="", request_headers:Dict={}):
        """Generate a unique shareable link for the customer's cart for a specific sales channel. This link enables easy sharing of the cart contents with other users, facilitating collaborative shopping experiences.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.getCartShareLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetShareCartLinkCreation
        schema = GetShareCartLinkCreation()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["getCartShareLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCartShareLink"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/share-cart", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetShareCartLinkResult
            schema = GetShareCartLinkResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCartShareLink")
                print(e)

        return response
    
    async def getCartSharedItems(self, token=None, body="", request_headers:Dict={}):
        """Get cart items from the shared cart link based on unique token.
        :param token : Token of the shared short link. : type string
        """
        payload = {}
        
        if token is not None:
            payload["token"] = token

        # Parameter validation
        schema = CartValidator.getCartSharedItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartSharedItems"], proccessed_params="""{"required":[{"name":"token","description":"Token of the shared short link.","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"token","description":"Token of the shared short link.","schema":{"type":"string"},"in":"path","required":true}]}""", serverType="application", token=token)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCartSharedItems"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/share-cart/{token}", token=token), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SharedCartResult
            schema = SharedCartResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCartSharedItems")
                print(e)

        return response
    
    async def updateCartWithSharedItems(self, token=None, action=None, body="", request_headers:Dict={}):
        """Merge or replace shared cart items with existing cart.
        :param token : Token of the shared short link. : type string
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateCartWithSharedItems"], proccessed_params="""{"required":[{"name":"token","description":"Token of the shared short link.","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"token","description":"Token of the shared short link.","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}]}""", serverType="application", token=token, action=action)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateCartWithSharedItems"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/share-cart/{token}/{action}", token=token, action=action), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SharedCartResult
            schema = SharedCartResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCartWithSharedItems")
                print(e)

        return response
    
    async def getPromotionOffers(self, slug=None, page_size=None, promotion_group=None, store_id=None, cart_type=None, sort_by=None, body="", request_headers:Dict={}):
        """List all promotional offers available for the items in the cart, including details such as offer text, unique promotion ID, and validity period.
        :param slug : A short, human-readable, URL-friendly identifier of a product. : type string
        :param page_size : Number of offers to be fetched to show. : type integer
        :param promotion_group : Type of promotion groups. : type string
        :param store_id : Unique identifier of a store. : type integer
        :param cart_type : The type of cart. : type string
        :param sort_by : Specifies the sorting criteria for the promotions. Sorts promotions in descending order by the value provided. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if page_size is not None:
            payload["page_size"] = page_size
        if promotion_group is not None:
            payload["promotion_group"] = promotion_group
        if store_id is not None:
            payload["store_id"] = store_id
        if cart_type is not None:
            payload["cart_type"] = cart_type
        if sort_by is not None:
            payload["sort_by"] = sort_by

        # Parameter validation
        schema = CartValidator.getPromotionOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPromotionOffers"], proccessed_params="""{"required":[],"optional":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product.","in":"query","schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show.","in":"query","schema":{"type":"integer"}},{"name":"promotion_group","description":"Type of promotion groups.","in":"query","schema":{"type":"string"}},{"name":"store_id","description":"Unique identifier of a store.","in":"query","schema":{"type":"integer"}},{"name":"cart_type","in":"query","schema":{"type":"string","x-not-enum":true},"description":"The type of cart."},{"name":"sort_by","in":"query","schema":{"type":"string","enum":["priority"]},"description":"Specifies the sorting criteria for the promotions. Sorts promotions in descending order by the value provided."}],"query":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product.","in":"query","schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show.","in":"query","schema":{"type":"integer"}},{"name":"promotion_group","description":"Type of promotion groups.","in":"query","schema":{"type":"string"}},{"name":"store_id","description":"Unique identifier of a store.","in":"query","schema":{"type":"integer"}},{"name":"cart_type","in":"query","schema":{"type":"string","x-not-enum":true},"description":"The type of cart."},{"name":"sort_by","in":"query","schema":{"type":"string","enum":["priority"]},"description":"Specifies the sorting criteria for the promotions. Sorts promotions in descending order by the value provided."}],"headers":[],"path":[]}""", serverType="application", slug=slug, page_size=page_size, promotion_group=promotion_group, store_id=store_id, cart_type=cart_type, sort_by=sort_by)
        query_string = await create_query_string(slug=slug, page_size=page_size, promotion_group=promotion_group, store_id=store_id, cart_type=cart_type, sort_by=sort_by)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPromotionOffers"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/available-promotions", slug=slug, page_size=page_size, promotion_group=promotion_group, store_id=store_id, cart_type=cart_type, sort_by=sort_by), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PromotionOffersResult
            schema = PromotionOffersResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPromotionOffers")
                print(e)

        return response
    
    async def getLadderOffers(self, slug=None, store_id=None, promotion_id=None, page_size=None, body="", request_headers:Dict={}):
        """Get ladder offers associated for the items in the cart. Ladder offers provide discounts or special pricing based on item quantity, allowing users to benefit from bulk purchases or promotional deals.
        :param slug : A short, human-readable, URL-friendly identifier of a product. : type string
        :param store_id : Store uid of assigned store on PDP page. If not passed default first created ladder will be returned. : type string
        :param promotion_id : Get ladder information of given promotion id explicitely. : type string
        :param page_size : Number of offers to be fetched to show. : type integer
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLadderOffers"], proccessed_params="""{"required":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product.","in":"query","required":true,"schema":{"type":"string"}}],"optional":[{"name":"store_id","description":"Store uid of assigned store on PDP page. If not passed default first created ladder will be returned.","in":"query","schema":{"type":"string"}},{"name":"promotion_id","description":"Get ladder information of given promotion id explicitely.","in":"query","required":false,"schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show.","in":"query","schema":{"type":"integer"}}],"query":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product.","in":"query","required":true,"schema":{"type":"string"}},{"name":"store_id","description":"Store uid of assigned store on PDP page. If not passed default first created ladder will be returned.","in":"query","schema":{"type":"string"}},{"name":"promotion_id","description":"Get ladder information of given promotion id explicitely.","in":"query","required":false,"schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show.","in":"query","schema":{"type":"integer"}}],"headers":[],"path":[]}""", serverType="application", slug=slug, store_id=store_id, promotion_id=promotion_id, page_size=page_size)
        query_string = await create_query_string(slug=slug, store_id=store_id, promotion_id=promotion_id, page_size=page_size)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLadderOffers"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/available-ladder-prices", slug=slug, store_id=store_id, promotion_id=promotion_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LadderPriceOffers
            schema = LadderPriceOffers()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLadderOffers")
                print(e)

        return response
    
    async def getPromotionPaymentOffers(self, id=None, uid=None, body="", request_headers:Dict={}):
        """Use this API to get top 5 payment offers available for current product.
        :param id : Cart id of the user cart . : type string
        :param uid : Cart uid of the user cart . : type integer
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if uid is not None:
            payload["uid"] = uid

        # Parameter validation
        schema = CartValidator.getPromotionPaymentOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPromotionPaymentOffers"], proccessed_params="""{"required":[],"optional":[{"name":"id","schema":{"type":"string"},"in":"query","description":"Cart id of the user cart ."},{"name":"uid","schema":{"type":"integer"},"in":"query","description":"Cart uid of the user cart ."}],"query":[{"name":"id","schema":{"type":"string"},"in":"query","description":"Cart id of the user cart ."},{"name":"uid","schema":{"type":"integer"},"in":"query","description":"Cart uid of the user cart ."}],"headers":[],"path":[]}""", serverType="application", id=id, uid=uid)
        query_string = await create_query_string(id=id, uid=uid)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPromotionPaymentOffers"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/available-payment-offers", id=id, uid=uid), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PromotionPaymentOffersResult
            schema = PromotionPaymentOffersResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPromotionPaymentOffers")
                print(e)

        return response
    
    async def checkoutCartV2(self, buy_now=None, cart_type=None, body="", request_headers:Dict={}):
        """The checkout cart initiates the order creation process based on the items in the user’s cart,  their selected address, and chosen payment methods. It also supports multiple payment method  options and revalidates the cart details to ensure a secure and seamless order placement.
        :param buy_now : This indicates the type of cart to checkout. : type boolean
        :param cart_type : The type of cart. : type string
        """
        payload = {}
        
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.checkoutCartV2()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CartCheckoutDetailV2Creation
        schema = CartCheckoutDetailV2Creation()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["checkoutCartV2"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"buy_now","description":"This indicates the type of cart to checkout.","schema":{"type":"boolean"}},{"name":"cart_type","in":"query","schema":{"type":"string","x-not-enum":true},"description":"The type of cart."}],"query":[{"in":"query","name":"buy_now","description":"This indicates the type of cart to checkout.","schema":{"type":"boolean"}},{"name":"cart_type","in":"query","schema":{"type":"string","x-not-enum":true},"description":"The type of cart."}],"headers":[],"path":[]}""", serverType="application", buy_now=buy_now, cart_type=cart_type)
        query_string = await create_query_string(buy_now=buy_now, cart_type=cart_type)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["checkoutCartV2"]).netloc, "post", await create_url_without_domain("/service/application/cart/v2.0/checkout", buy_now=buy_now, cart_type=cart_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartCheckoutResult
            schema = CartCheckoutResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkoutCartV2")
                print(e)

        return response
    
    async def getPromotions(self, page_size=None, page_no=None, promotion_type=None, body="", request_headers:Dict={}):
        """List all promotional offers available for the sales channel, including details such as offer text, unique promotion ID, and validity period.
        :param page_size : Number of offers to be fetched to show. : type integer
        :param page_no : Page number to be fetched to show : type integer
        :param promotion_type : Promotion type of promotions to be fetched : type string
        """
        payload = {}
        
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no
        if promotion_type is not None:
            payload["promotion_type"] = promotion_type

        # Parameter validation
        schema = CartValidator.getPromotions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPromotions"], proccessed_params="""{"required":[],"optional":[{"name":"page_size","description":"Number of offers to be fetched to show.","in":"query","schema":{"type":"integer"}},{"name":"page_no","description":"Page number to be fetched to show","in":"query","schema":{"type":"integer"}},{"name":"promotion_type","description":"Promotion type of promotions to be fetched","in":"query","schema":{"type":"string"}}],"query":[{"name":"page_size","description":"Number of offers to be fetched to show.","in":"query","schema":{"type":"integer"}},{"name":"page_no","description":"Page number to be fetched to show","in":"query","schema":{"type":"integer"}},{"name":"promotion_type","description":"Promotion type of promotions to be fetched","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", serverType="application", page_size=page_size, page_no=page_no, promotion_type=promotion_type)
        query_string = await create_query_string(page_size=page_size, page_no=page_no, promotion_type=promotion_type)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPromotions"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/promotion", page_size=page_size, page_no=page_no, promotion_type=promotion_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Promotions
            schema = Promotions()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPromotions")
                print(e)

        return response
    