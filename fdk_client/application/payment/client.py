

"""Payment Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import PaymentValidator

class Payment:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getAggregatorsConfig": "/service/application/payment/v1.0/config/aggregators/key",
            "attachCardToCustomer": "/service/application/payment/v1.0/card/attach",
            "getActiveCardAggregator": "/service/application/payment/v1.0/card/aggregator",
            "getActiveUserCards": "/service/application/payment/v1.0/cards",
            "deleteUserCard": "/service/application/payment/v1.0/card/remove",
            "verifyCustomerForPayment": "/service/application/payment/v1.0/payment/customer/validation",
            "verifyAndChargePayment": "/service/application/payment/v1.0/payment/confirm/charge",
            "initialisePayment": "/service/application/payment/v1.0/payment/request",
            "checkAndUpdatePaymentStatus": "/service/application/payment/v1.0/payment/confirm/polling",
            "getPaymentModeRoutes": "/service/application/payment/v1.0/payment/options",
            "getPosPaymentModeRoutes": "/service/application/payment/v1.0/payment/options/pos",
            "getRupifiBannerDetails": "/service/application/payment/v1.0/rupifi/banner",
            "getEpaylaterBannerDetails": "/service/application/payment/v1.0/epaylater/banner",
            "resendOrCancelPayment": "/service/application/payment/v1.0/payment/resend_or_cancel",
            "getActiveRefundTransferModes": "/service/application/payment/v1.0/refund/transfer-mode",
            "enableOrDisableRefundTransferMode": "/service/application/payment/v1.0/refund/transfer-mode",
            "getUserBeneficiariesDetail": "/service/application/payment/v1.0/refund/user/beneficiary",
            "verifyIfscCode": "/service/application/payment/v1.0/ifsc-code/verify",
            "getOrderBeneficiariesDetail": "/service/application/payment/v1.0/refund/order/beneficiaries",
            "verifyOtpAndAddBeneficiaryForBank": "/service/application/payment/v1.0/refund/verification/bank",
            "addBeneficiaryDetails": "/service/application/payment/v1.0/refund/account",
            "addRefundBankAccountUsingOTP": "/service/application/payment/v1.0/refund/account/otp",
            "verifyOtpAndAddBeneficiaryForWallet": "/service/application/payment/v1.0/refund/verification/wallet",
            "updateDefaultBeneficiary": "/service/application/payment/v1.0/refund/beneficiary/default",
            "customerCreditSummary": "/service/application/payment/v1.0/payment/credit-summary/",
            "redirectToAggregator": "/service/application/payment/v1.0/payment/redirect-to-aggregator/",
            "checkCredit": "/service/application/payment/v1.0/check-credits/",
            "customerOnboard": "/service/application/payment/v1.0/credit-onboard/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getAggregatorsConfig(self, x_api_token=None, refresh=None, body=""):
        """Use this API to retrieve the payment gateway key, secrets, merchant, SDK/API details to complete a payment at front-end.
        :param x-api-token : Used for basic authentication. : type string
        :param refresh : This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one. : type boolean
        """
        payload = {}
        
        if x_api_token:
            payload["x_api_token"] = x_api_token
        
        if refresh:
            payload["refresh"] = refresh
        
        # Parameter validation
        schema = PaymentValidator.getAggregatorsConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAggregatorsConfig"], proccessed_params="""{"required":[],"optional":[{"name":"x-api-token","in":"header","description":"Used for basic authentication.","required":false,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}}],"query":[{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}}],"headers":[{"name":"x-api-token","in":"header","description":"Used for basic authentication.","required":false,"schema":{"type":"string"}}],"path":[]}""", x_api_token=x_api_token, refresh=refresh)
        query_string = await create_query_string(x_api_token=x_api_token, refresh=refresh)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAggregatorsConfig"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/config/aggregators/key", x_api_token=x_api_token, refresh=refresh), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import AggregatorsConfigDetailResponse
        schema = AggregatorsConfigDetailResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getAggregatorsConfig")
            print(e)

        

        return response
    
    async def attachCardToCustomer(self, body=""):
        """Use this API to attach a customer's saved card at the payment gateway, such as Stripe, Juspay.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.attachCardToCustomer()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AttachCardRequest
        schema = AttachCardRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["attachCardToCustomer"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["attachCardToCustomer"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/card/attach", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import AttachCardsResponse
        schema = AttachCardsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for attachCardToCustomer")
            print(e)

        

        return response
    
    async def getActiveCardAggregator(self, refresh=None, body=""):
        """Use this API to retrieve an active payment aggregator along with the Customer ID. This is applicable for cards payments only.
        :param refresh :  : type boolean
        """
        payload = {}
        
        if refresh:
            payload["refresh"] = refresh
        
        # Parameter validation
        schema = PaymentValidator.getActiveCardAggregator()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getActiveCardAggregator"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"refresh","schema":{"type":"boolean","default":false,"description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one."}}],"query":[{"in":"query","name":"refresh","schema":{"type":"boolean","default":false,"description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one."}}],"headers":[],"path":[]}""", refresh=refresh)
        query_string = await create_query_string(refresh=refresh)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getActiveCardAggregator"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/card/aggregator", refresh=refresh), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import ActiveCardPaymentGatewayResponse
        schema = ActiveCardPaymentGatewayResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getActiveCardAggregator")
            print(e)

        

        return response
    
    async def getActiveUserCards(self, force_refresh=None, body=""):
        """Use this API to retrieve a list of cards stored by user from an active payment gateway.
        :param force_refresh :  : type boolean
        """
        payload = {}
        
        if force_refresh:
            payload["force_refresh"] = force_refresh
        
        # Parameter validation
        schema = PaymentValidator.getActiveUserCards()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getActiveUserCards"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"force_refresh","schema":{"type":"boolean","default":false,"description":"This is a boolean value. Select `true` to clear the cache."}}],"query":[{"in":"query","name":"force_refresh","schema":{"type":"boolean","default":false,"description":"This is a boolean value. Select `true` to clear the cache."}}],"headers":[],"path":[]}""", force_refresh=force_refresh)
        query_string = await create_query_string(force_refresh=force_refresh)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getActiveUserCards"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/cards", force_refresh=force_refresh), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import ListCardsResponse
        schema = ListCardsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getActiveUserCards")
            print(e)

        

        return response
    
    async def deleteUserCard(self, body=""):
        """Use this API to delete a card added by a user on the payment gateway and clear the cache.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.deleteUserCard()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DeletehCardRequest
        schema = DeletehCardRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteUserCard"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deleteUserCard"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/card/remove", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import DeleteCardsResponse
        schema = DeleteCardsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for deleteUserCard")
            print(e)

        

        return response
    
    async def verifyCustomerForPayment(self, body=""):
        """Use this API to check if the customer is eligible to use credit-line facilities such as Simpl Pay Later and Rupifi.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.verifyCustomerForPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateCustomerRequest
        schema = ValidateCustomerRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyCustomerForPayment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyCustomerForPayment"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/customer/validation", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import ValidateCustomerResponse
        schema = ValidateCustomerResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for verifyCustomerForPayment")
            print(e)

        

        return response
    
    async def verifyAndChargePayment(self, body=""):
        """Use this API to verify and check the status of a payment transaction (server-to-server) made through aggregators like Simpl and Mswipe.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.verifyAndChargePayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ChargeCustomerRequest
        schema = ChargeCustomerRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyAndChargePayment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyAndChargePayment"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/confirm/charge", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import ChargeCustomerResponse
        schema = ChargeCustomerResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for verifyAndChargePayment")
            print(e)

        

        return response
    
    async def initialisePayment(self, body=""):
        """PUse this API to inititate payment using UPI, BharatQR, wherein the UPI requests are send to the app and QR code is displayed on the screen.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.initialisePayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentInitializationRequest
        schema = PaymentInitializationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["initialisePayment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["initialisePayment"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/request", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import PaymentInitializationResponse
        schema = PaymentInitializationResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for initialisePayment")
            print(e)

        

        return response
    
    async def checkAndUpdatePaymentStatus(self, body=""):
        """Use this API to perform continuous polling at intervals to check the status of payment until timeout.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.checkAndUpdatePaymentStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentStatusUpdateRequest
        schema = PaymentStatusUpdateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["checkAndUpdatePaymentStatus"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["checkAndUpdatePaymentStatus"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/confirm/polling", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import PaymentStatusUpdateResponse
        schema = PaymentStatusUpdateResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for checkAndUpdatePaymentStatus")
            print(e)

        

        return response
    
    async def getPaymentModeRoutes(self, amount=None, cart_id=None, pincode=None, checkout_mode=None, refresh=None, card_reference=None, user_details=None, body=""):
        """Use this API to get all valid payment options for doing a payment.
        :param amount : Payable amount. : type integer
        :param cart_id : Identifier of the cart. : type string
        :param pincode : The PIN Code of the destination address, e.g. 400059 : type string
        :param checkout_mode : Option to checkout for self or for others. : type string
        :param refresh : This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one. : type boolean
        :param card_reference : Card reference id of user's debit or credit card. : type string
        :param user_details : URIencoded JSON containing details of an anonymous user. : type string
        """
        payload = {}
        
        if amount:
            payload["amount"] = amount
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if pincode:
            payload["pincode"] = pincode
        
        if checkout_mode:
            payload["checkout_mode"] = checkout_mode
        
        if refresh:
            payload["refresh"] = refresh
        
        if card_reference:
            payload["card_reference"] = card_reference
        
        if user_details:
            payload["user_details"] = user_details
        
        # Parameter validation
        schema = PaymentValidator.getPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPaymentModeRoutes"], proccessed_params="""{"required":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}}],"query":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":true,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}}],"headers":[],"path":[]}""", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, user_details=user_details)
        query_string = await create_query_string(amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, user_details=user_details)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPaymentModeRoutes"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/options", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, user_details=user_details), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import PaymentModeRouteResponse
        schema = PaymentModeRouteResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getPaymentModeRoutes")
            print(e)

        

        return response
    
    async def getPosPaymentModeRoutes(self, amount=None, cart_id=None, pincode=None, checkout_mode=None, refresh=None, card_reference=None, order_type=None, user_details=None, body=""):
        """Use this API to get all valid payment options for doing a payment in POS.
        :param amount : Payable amount. : type integer
        :param cart_id : Identifier of the cart. : type string
        :param pincode : The PIN Code of the destination address, e.g. 400059 : type string
        :param checkout_mode : Option to checkout for self or for others. : type string
        :param refresh : This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one. : type boolean
        :param card_reference : Card reference id of user's debit or credit card. : type string
        :param order_type : The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        :param user_details : URIencoded JSON containing details of an anonymous user. : type string
        """
        payload = {}
        
        if amount:
            payload["amount"] = amount
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if pincode:
            payload["pincode"] = pincode
        
        if checkout_mode:
            payload["checkout_mode"] = checkout_mode
        
        if refresh:
            payload["refresh"] = refresh
        
        if card_reference:
            payload["card_reference"] = card_reference
        
        if order_type:
            payload["order_type"] = order_type
        
        if user_details:
            payload["user_details"] = user_details
        
        # Parameter validation
        schema = PaymentValidator.getPosPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPosPaymentModeRoutes"], proccessed_params="""{"required":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":true,"schema":{"type":"string"}},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string"}}],"optional":[{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}}],"query":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":true,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}}],"headers":[],"path":[]}""", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details)
        query_string = await create_query_string(amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPosPaymentModeRoutes"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/options/pos", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import PaymentModeRouteResponse
        schema = PaymentModeRouteResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getPosPaymentModeRoutes")
            print(e)

        

        return response
    
    async def getRupifiBannerDetails(self, body=""):
        """Get CreditLine Offer if user is tentatively approved by rupifi
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.getRupifiBannerDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getRupifiBannerDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getRupifiBannerDetails"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/rupifi/banner", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import RupifiBannerResponse
        schema = RupifiBannerResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getRupifiBannerDetails")
            print(e)

        

        return response
    
    async def getEpaylaterBannerDetails(self, body=""):
        """Get Epaylater Enabled if user is tentatively approved by epaylater
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.getEpaylaterBannerDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getEpaylaterBannerDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getEpaylaterBannerDetails"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/epaylater/banner", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import EpaylaterBannerResponse
        schema = EpaylaterBannerResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getEpaylaterBannerDetails")
            print(e)

        

        return response
    
    async def resendOrCancelPayment(self, body=""):
        """Use this API to perform resend or cancel a payment link based on request payload.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.resendOrCancelPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ResendOrCancelPaymentRequest
        schema = ResendOrCancelPaymentRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["resendOrCancelPayment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["resendOrCancelPayment"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/resend_or_cancel", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import ResendOrCancelPaymentResponse
        schema = ResendOrCancelPaymentResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for resendOrCancelPayment")
            print(e)

        

        return response
    
    async def getActiveRefundTransferModes(self, body=""):
        """Use this API to retrieve eligible refund modes (such as Netbanking) and add the beneficiary details.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.getActiveRefundTransferModes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getActiveRefundTransferModes"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getActiveRefundTransferModes"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/refund/transfer-mode", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import TransferModeResponse
        schema = TransferModeResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getActiveRefundTransferModes")
            print(e)

        

        return response
    
    async def enableOrDisableRefundTransferMode(self, body=""):
        """Activate or Deactivate Transfer Mode to collect Beneficiary Details for Refund
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.enableOrDisableRefundTransferMode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateRefundTransferModeRequest
        schema = UpdateRefundTransferModeRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["enableOrDisableRefundTransferMode"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["enableOrDisableRefundTransferMode"]).netloc, "put", await create_url_without_domain("/service/application/payment/v1.0/refund/transfer-mode", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import UpdateRefundTransferModeResponse
        schema = UpdateRefundTransferModeResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for enableOrDisableRefundTransferMode")
            print(e)

        

        return response
    
    async def getUserBeneficiariesDetail(self, order_id=None, body=""):
        """Use this API to get the details of all active beneficiary added by a user for refund.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        # Parameter validation
        schema = PaymentValidator.getUserBeneficiariesDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserBeneficiariesDetail"], proccessed_params="""{"required":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getUserBeneficiariesDetail"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/refund/user/beneficiary", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import OrderBeneficiaryResponse
        schema = OrderBeneficiaryResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getUserBeneficiariesDetail")
            print(e)

        

        return response
    
    async def verifyIfscCode(self, ifsc_code=None, body=""):
        """Use this API to check whether the 11-digit IFSC code is valid and to fetch the bank details for refund.
        :param ifsc_code : A 11-digit alphanumeric code that uniquely identifies a bank branch. : type string
        """
        payload = {}
        
        if ifsc_code:
            payload["ifsc_code"] = ifsc_code
        
        # Parameter validation
        schema = PaymentValidator.verifyIfscCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyIfscCode"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"ifsc_code","schema":{"type":"string"},"description":"A 11-digit alphanumeric code that uniquely identifies a bank branch."}],"query":[{"in":"query","name":"ifsc_code","schema":{"type":"string"},"description":"A 11-digit alphanumeric code that uniquely identifies a bank branch."}],"headers":[],"path":[]}""", ifsc_code=ifsc_code)
        query_string = await create_query_string(ifsc_code=ifsc_code)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyIfscCode"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/ifsc-code/verify", ifsc_code=ifsc_code), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import IfscCodeResponse
        schema = IfscCodeResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for verifyIfscCode")
            print(e)

        

        return response
    
    async def getOrderBeneficiariesDetail(self, order_id=None, body=""):
        """Use this API to get the details of all active beneficiary added by a user for refund.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        # Parameter validation
        schema = PaymentValidator.getOrderBeneficiariesDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderBeneficiariesDetail"], proccessed_params="""{"required":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrderBeneficiariesDetail"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/refund/order/beneficiaries", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import OrderBeneficiaryResponse
        schema = OrderBeneficiaryResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getOrderBeneficiariesDetail")
            print(e)

        

        return response
    
    async def verifyOtpAndAddBeneficiaryForBank(self, body=""):
        """Use this API to perform an OTP validation before saving the beneficiary details added for a refund.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.verifyOtpAndAddBeneficiaryForBank()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddBeneficiaryViaOtpVerificationRequest
        schema = AddBeneficiaryViaOtpVerificationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyOtpAndAddBeneficiaryForBank"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyOtpAndAddBeneficiaryForBank"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/verification/bank", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import AddBeneficiaryViaOtpVerificationResponse
        schema = AddBeneficiaryViaOtpVerificationResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for verifyOtpAndAddBeneficiaryForBank")
            print(e)

        

        return response
    
    async def addBeneficiaryDetails(self, body=""):
        """Use this API to save the bank details for a returned or cancelled order to refund the amount.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.addBeneficiaryDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddBeneficiaryDetailsRequest
        schema = AddBeneficiaryDetailsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addBeneficiaryDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addBeneficiaryDetails"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/account", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import RefundAccountResponse
        schema = RefundAccountResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for addBeneficiaryDetails")
            print(e)

        

        return response
    
    async def addRefundBankAccountUsingOTP(self, body=""):
        """Use this API to save bank details for returned/cancelled order to refund amount in his account.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.addRefundBankAccountUsingOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddBeneficiaryDetailsOTPRequest
        schema = AddBeneficiaryDetailsOTPRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addRefundBankAccountUsingOTP"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addRefundBankAccountUsingOTP"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/account/otp", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import RefundAccountResponse
        schema = RefundAccountResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for addRefundBankAccountUsingOTP")
            print(e)

        

        return response
    
    async def verifyOtpAndAddBeneficiaryForWallet(self, body=""):
        """Use this API to send an OTP while adding a wallet beneficiary by mobile no. verification.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.verifyOtpAndAddBeneficiaryForWallet()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import WalletOtpRequest
        schema = WalletOtpRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyOtpAndAddBeneficiaryForWallet"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyOtpAndAddBeneficiaryForWallet"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/verification/wallet", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import WalletOtpResponse
        schema = WalletOtpResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for verifyOtpAndAddBeneficiaryForWallet")
            print(e)

        

        return response
    
    async def updateDefaultBeneficiary(self, body=""):
        """Use this API to set a default beneficiary for getting a refund.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.updateDefaultBeneficiary()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SetDefaultBeneficiaryRequest
        schema = SetDefaultBeneficiaryRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateDefaultBeneficiary"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateDefaultBeneficiary"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/beneficiary/default", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import SetDefaultBeneficiaryResponse
        schema = SetDefaultBeneficiaryResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateDefaultBeneficiary")
            print(e)

        

        return response
    
    async def customerCreditSummary(self, aggregator=None, body=""):
        """Use this API to fetch the customer credit summary.
        :param aggregator :  : type string
        """
        payload = {}
        
        if aggregator:
            payload["aggregator"] = aggregator
        
        # Parameter validation
        schema = PaymentValidator.customerCreditSummary()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["customerCreditSummary"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"aggregator","schema":{"type":"string","description":"This is a String value that contains aggregator name as value."}}],"query":[{"in":"query","name":"aggregator","schema":{"type":"string","description":"This is a String value that contains aggregator name as value."}}],"headers":[],"path":[]}""", aggregator=aggregator)
        query_string = await create_query_string(aggregator=aggregator)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["customerCreditSummary"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/credit-summary/", aggregator=aggregator), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import CustomerCreditSummaryResponse
        schema = CustomerCreditSummaryResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for customerCreditSummary")
            print(e)

        

        return response
    
    async def redirectToAggregator(self, source=None, aggregator=None, body=""):
        """Use this API to get the redirect url to redirect the user to aggregator's page
        :param source : This is a String value that contains callback URL as value. : type string
        :param aggregator : This is a String value that contains aggregator name as value. : type string
        """
        payload = {}
        
        if source:
            payload["source"] = source
        
        if aggregator:
            payload["aggregator"] = aggregator
        
        # Parameter validation
        schema = PaymentValidator.redirectToAggregator()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["redirectToAggregator"], proccessed_params="""{"required":[],"optional":[{"name":"source","in":"query","description":"This is a String value that contains callback URL as value.","schema":{"type":"string"}},{"name":"aggregator","in":"query","description":"This is a String value that contains aggregator name as value.","schema":{"type":"string"}}],"query":[{"name":"source","in":"query","description":"This is a String value that contains callback URL as value.","schema":{"type":"string"}},{"name":"aggregator","in":"query","description":"This is a String value that contains aggregator name as value.","schema":{"type":"string"}}],"headers":[],"path":[]}""", source=source, aggregator=aggregator)
        query_string = await create_query_string(source=source, aggregator=aggregator)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["redirectToAggregator"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/redirect-to-aggregator/", source=source, aggregator=aggregator), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import RedirectToAggregatorResponse
        schema = RedirectToAggregatorResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for redirectToAggregator")
            print(e)

        

        return response
    
    async def checkCredit(self, aggregator=None, body=""):
        """Use this API to fetch the customer credit summary.
        :param aggregator :  : type string
        """
        payload = {}
        
        if aggregator:
            payload["aggregator"] = aggregator
        
        # Parameter validation
        schema = PaymentValidator.checkCredit()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["checkCredit"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"aggregator","schema":{"type":"string","description":"This is a String value that contains aggregator name as value."}}],"query":[{"in":"query","name":"aggregator","schema":{"type":"string","description":"This is a String value that contains aggregator name as value."}}],"headers":[],"path":[]}""", aggregator=aggregator)
        query_string = await create_query_string(aggregator=aggregator)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["checkCredit"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/check-credits/", aggregator=aggregator), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import CheckCreditResponse
        schema = CheckCreditResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for checkCredit")
            print(e)

        

        return response
    
    async def customerOnboard(self, body=""):
        """Use this API to fetch the customer credit summary.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.customerOnboard()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomerOnboardingRequest
        schema = CustomerOnboardingRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["customerOnboard"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["customerOnboard"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/credit-onboard/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
                
        

        from .models import CustomerOnboardingResponse
        schema = CustomerOnboardingResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for customerOnboard")
            print(e)

        

        return response
    

