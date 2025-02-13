"""Payment Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import PaymentValidator

class Payment:
    def __init__(self, config: ApplicationConfig):
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
            "walletLinkInitiate": "/service/application/payment/v1.0/payment/options/wallet/link",
            "linkWallet": "/service/application/payment/v1.0/payment/options/wallet/verify",
            "delinkWallet": "/service/application/payment/v1.0/payment/options/wallet/delink",
            "getRupifiBannerDetails": "/service/application/payment/v1.0/rupifi/banner",
            "getEpaylaterBannerDetails": "/service/application/payment/v1.0/epaylater/banner",
            "resendOrCancelPayment": "/service/application/payment/v1.0/payment/resend_or_cancel",
            "renderHTML": "/service/application/payment/v1.0/payment/html/render/",
            "validateVPA": "/service/application/payment/v1.0/validate-vpa",
            "cardDetails": "/service/application/payment/v1.0/cards/info/{card_info}",
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
            "getPaymentLink": "/service/application/payment/v1.0/create-payment-link/",
            "createPaymentLink": "/service/application/payment/v1.0/create-payment-link/",
            "resendPaymentLink": "/service/application/payment/v1.0/resend-payment-link/",
            "cancelPaymentLink": "/service/application/payment/v1.0/cancel-payment-link/",
            "getPaymentModeRoutesPaymentLink": "/service/application/payment/v1.0/payment/options/link/",
            "pollingPaymentLink": "/service/application/payment/v1.0/polling-payment-link/",
            "createOrderHandlerPaymentLink": "/service/application/payment/v1.0/create-order/link/",
            "initialisePaymentPaymentLink": "/service/application/payment/v1.0/payment/request/link/",
            "checkAndUpdatePaymentStatusPaymentLink": "/service/application/payment/v1.0/payment/confirm/polling/link/",
            "customerCreditSummary": "/service/application/payment/v1.0/payment/credit-summary/",
            "redirectToAggregator": "/service/application/payment/v1.0/payment/redirect-to-aggregator/",
            "checkCredit": "/service/application/payment/v1.0/check-credits/",
            "customerOnboard": "/service/application/payment/v1.0/credit-onboard/",
            "outstandingOrderDetails": "/service/application/payment/v1.0/payment/outstanding-orders/",
            "paidOrderDetails": "/service/application/payment/v1.0/payment/paid-orders/",
            "createPaymentOrder": "/service/application/payment/v1.0/payment-orders/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getAggregatorsConfig(self, x_api_token=None, refresh=None, body="", request_headers:Dict={}):
        """Get aggregator secret key of all payment gateways utilized for payments when using the SDK for the payment gateway.
        :param x-api-token : Basic auth token. : type string
        :param refresh : Select `true` to remove temporary cache files on payment gateway and replace with the latest one. : type boolean
        """
        payload = {}
        
        if x_api_token is not None:
            payload["x_api_token"] = x_api_token
        if refresh is not None:
            payload["refresh"] = refresh

        # Parameter validation
        schema = PaymentValidator.getAggregatorsConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAggregatorsConfig"], proccessed_params="""{"required":[],"optional":[{"name":"x-api-token","in":"header","description":"Basic auth token.","required":false,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}}],"query":[{"name":"refresh","in":"query","description":"Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}}],"headers":[{"name":"x-api-token","in":"header","description":"Basic auth token.","required":false,"schema":{"type":"string"}}],"path":[]}""", serverType="application", x_api_token=x_api_token, refresh=refresh)
        query_string = await create_query_string(refresh=refresh)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAggregatorsConfig"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/config/aggregators/key", x_api_token=x_api_token, refresh=refresh), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AggregatorsConfigDetail
            schema = AggregatorsConfigDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAggregatorsConfig")
                print(e)

        return response
    
    async def attachCardToCustomer(self, body="", request_headers:Dict={}):
        """Link payment card to a user account for seamless transactions. Upon successful linking, the card becomes associated with the user's profile, enabling secure and convenient payments.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.attachCardToCustomer()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AttachCard
        schema = AttachCard()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["attachCardToCustomer"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["attachCardToCustomer"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/card/attach", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AttachCardsDetails
            schema = AttachCardsDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for attachCardToCustomer")
                print(e)

        return response
    
    async def getActiveCardAggregator(self, refresh=None, body="", request_headers:Dict={}):
        """Get details about the active card aggregator used by the user, including the aggregator name.You can refresh the data by setting the 'refresh' parameter to true if needed.
        :param refresh : Select `true` to remove temporary cache files on payment gateway and replace with the latest one. : type boolean
        """
        payload = {}
        
        if refresh is not None:
            payload["refresh"] = refresh

        # Parameter validation
        schema = PaymentValidator.getActiveCardAggregator()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getActiveCardAggregator"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"refresh","schema":{"type":"boolean","default":false},"description":"Select `true` to remove temporary cache files on payment gateway and replace with the latest one."}],"query":[{"in":"query","name":"refresh","schema":{"type":"boolean","default":false},"description":"Select `true` to remove temporary cache files on payment gateway and replace with the latest one."}],"headers":[],"path":[]}""", serverType="application", refresh=refresh)
        query_string = await create_query_string(refresh=refresh)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getActiveCardAggregator"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/card/aggregator", refresh=refresh), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ActiveCardPaymentGatewayDetails
            schema = ActiveCardPaymentGatewayDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getActiveCardAggregator")
                print(e)

        return response
    
    async def getActiveUserCards(self, force_refresh=None, body="", request_headers:Dict={}):
        """List all active cards saved by the user.Includes details such as the card's aggregator name, card ID, token, reference, number, expiration date, type, issuer, brand, nickname, and whether it has expired.
        :param force_refresh : Select `true` to clear the cache. : type boolean
        """
        payload = {}
        
        if force_refresh is not None:
            payload["force_refresh"] = force_refresh

        # Parameter validation
        schema = PaymentValidator.getActiveUserCards()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getActiveUserCards"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"force_refresh","schema":{"type":"boolean","default":false},"description":"Select `true` to clear the cache."}],"query":[{"in":"query","name":"force_refresh","schema":{"type":"boolean","default":false},"description":"Select `true` to clear the cache."}],"headers":[],"path":[]}""", serverType="application", force_refresh=force_refresh)
        query_string = await create_query_string(force_refresh=force_refresh)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getActiveUserCards"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/cards", force_refresh=force_refresh), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ListCardsDetails
            schema = ListCardsDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getActiveUserCards")
                print(e)

        return response
    
    async def deleteUserCard(self, body="", request_headers:Dict={}):
        """Delete payment card from the user's account.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.deleteUserCard()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DeleteCard
        schema = DeleteCard()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["deleteUserCard"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deleteUserCard"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/card/remove", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteCardsDetails
            schema = DeleteCardsDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteUserCard")
                print(e)

        return response
    
    async def verifyCustomerForPayment(self, body="", request_headers:Dict={}):
        """Verify if the user is eligible for pay-later payment from the payment aggregator side using the customer's phone number.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.verifyCustomerForPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateCustomer
        schema = ValidateCustomer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["verifyCustomerForPayment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyCustomerForPayment"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/customer/validation", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ValidateCustomerDetails
            schema = ValidateCustomerDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyCustomerForPayment")
                print(e)

        return response
    
    async def verifyAndChargePayment(self, body="", request_headers:Dict={}):
        """Verify the payment status and charge from the customer's BNPL (Buy Now, Pay Later) account after order confirmation.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.verifyAndChargePayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ChargeCustomer
        schema = ChargeCustomer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["verifyAndChargePayment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyAndChargePayment"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/confirm/charge", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ChargeCustomerDetails
            schema = ChargeCustomerDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyAndChargePayment")
                print(e)

        return response
    
    async def initialisePayment(self, body="", request_headers:Dict={}):
        """Initiate the payment procedure for an order. Upon successful initiation, it returns a  details including the success status, aggregator information, payment method, status, merchant order ID aggregator order , polling URL, timeout, virtual ID, Razorpay payment ID, customer ID, and device ID.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.initialisePayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentInitialization
        schema = PaymentInitialization()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["initialisePayment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["initialisePayment"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/request", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentInitializationDetails
            schema = PaymentInitializationDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for initialisePayment")
                print(e)

        return response
    
    async def checkAndUpdatePaymentStatus(self, body="", request_headers:Dict={}):
        """Polling process to confirm the payment status. It periodically checks and updates the current status of a payment, ensuring timely and accurate confirmation of payment transactions.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.checkAndUpdatePaymentStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentStatusUpdate
        schema = PaymentStatusUpdate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["checkAndUpdatePaymentStatus"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["checkAndUpdatePaymentStatus"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/confirm/polling", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentStatusUpdateDetails
            schema = PaymentStatusUpdateDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkAndUpdatePaymentStatus")
                print(e)

        return response
    
    async def getPaymentModeRoutes(self, amount=None, cart_id=None, checkout_mode=None, refresh=None, order_id=None, card_reference=None, user_details=None, display_split=None, advance_payment=None, shipment_id=None, body="", request_headers:Dict={}):
        """Get available payment methods on the payment page, specifying the aggregator for each option, such as 'Netbanking powered by Juspay' and 'Card powered by Razorpay'.
        :param amount : Payable amount. : type integer
        :param cart_id : Identifier of the cart. : type string
        :param checkout_mode : Option to checkout for self or for others. : type string
        :param refresh : Select `true` to remove temporary cache files on payment gateway and replace with the latest one. : type boolean
        :param order_id : Identifier of the order, order_id. : type string
        :param card_reference : Card reference id of user's debit or credit card. : type string
        :param user_details : URLencoded JSON containing details of an anonymous user. : type string
        :param display_split : Display Split Payment Option or not. : type boolean
        :param advance_payment : Display Advance Payment Options or Normal. : type boolean
        :param shipment_id : Identifier of the shipment, shipment_id. : type string
        """
        payload = {}
        
        if amount is not None:
            payload["amount"] = amount
        if cart_id is not None:
            payload["cart_id"] = cart_id
        if checkout_mode is not None:
            payload["checkout_mode"] = checkout_mode
        if refresh is not None:
            payload["refresh"] = refresh
        if order_id is not None:
            payload["order_id"] = order_id
        if card_reference is not None:
            payload["card_reference"] = card_reference
        if user_details is not None:
            payload["user_details"] = user_details
        if display_split is not None:
            payload["display_split"] = display_split
        if advance_payment is not None:
            payload["advance_payment"] = advance_payment
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = PaymentValidator.getPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPaymentModeRoutes"], proccessed_params="""{"required":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":false,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"order_id","in":"query","required":false,"schema":{"type":"string"},"description":"Identifier of the order, order_id."},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URLencoded JSON containing details of an anonymous user.","schema":{"type":"string"}},{"name":"display_split","in":"query","description":"Display Split Payment Option or not.","schema":{"type":"boolean"}},{"name":"advance_payment","in":"query","description":"Display Advance Payment Options or Normal.","schema":{"type":"boolean"}},{"name":"shipment_id","in":"query","required":false,"schema":{"type":"string"},"description":"Identifier of the shipment, shipment_id."}],"query":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":false,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"order_id","in":"query","required":false,"schema":{"type":"string"},"description":"Identifier of the order, order_id."},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URLencoded JSON containing details of an anonymous user.","schema":{"type":"string"}},{"name":"display_split","in":"query","description":"Display Split Payment Option or not.","schema":{"type":"boolean"}},{"name":"advance_payment","in":"query","description":"Display Advance Payment Options or Normal.","schema":{"type":"boolean"}},{"name":"shipment_id","in":"query","required":false,"schema":{"type":"string"},"description":"Identifier of the shipment, shipment_id."}],"headers":[],"path":[]}""", serverType="application", amount=amount, cart_id=cart_id, checkout_mode=checkout_mode, refresh=refresh, order_id=order_id, card_reference=card_reference, user_details=user_details, display_split=display_split, advance_payment=advance_payment, shipment_id=shipment_id)
        query_string = await create_query_string(amount=amount, cart_id=cart_id, checkout_mode=checkout_mode, refresh=refresh, order_id=order_id, card_reference=card_reference, user_details=user_details, display_split=display_split, advance_payment=advance_payment, shipment_id=shipment_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPaymentModeRoutes"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/options", amount=amount, cart_id=cart_id, checkout_mode=checkout_mode, refresh=refresh, order_id=order_id, card_reference=card_reference, user_details=user_details, display_split=display_split, advance_payment=advance_payment, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentModeRouteDetails
            schema = PaymentModeRouteDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentModeRoutes")
                print(e)

        return response
    
    async def getPosPaymentModeRoutes(self, amount=None, cart_id=None, pincode=None, checkout_mode=None, refresh=None, card_reference=None, order_type=None, user_details=None, body="", request_headers:Dict={}):
        """Get available payment methods on the payment page for POS, specifying the aggregator for each option, such as 'CARD powered by Juspay' and 'QR powered by Razorpay'.
        :param amount : Payable amount. : type integer
        :param cart_id : Identifier of the cart. : type string
        :param pincode : The PIN Code of the destination address, e.g. 400059. : type string
        :param checkout_mode : Option to checkout for self or for others. : type string
        :param refresh : Select `true` to remove temporary cache files on payment gateway and replace with the latest one. : type boolean
        :param card_reference : Card reference id of user's debit or credit card. : type string
        :param order_type : The order type of shipment  HomeDelivery - If the customer wants the order home-delivered  PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        :param user_details : URLencoded JSON containing details of an anonymous user. : type string
        """
        payload = {}
        
        if amount is not None:
            payload["amount"] = amount
        if cart_id is not None:
            payload["cart_id"] = cart_id
        if pincode is not None:
            payload["pincode"] = pincode
        if checkout_mode is not None:
            payload["checkout_mode"] = checkout_mode
        if refresh is not None:
            payload["refresh"] = refresh
        if card_reference is not None:
            payload["card_reference"] = card_reference
        if order_type is not None:
            payload["order_type"] = order_type
        if user_details is not None:
            payload["user_details"] = user_details

        # Parameter validation
        schema = PaymentValidator.getPosPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPosPaymentModeRoutes"], proccessed_params="""{"required":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059.","required":true,"schema":{"type":"string"}},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment  HomeDelivery - If the customer wants the order home-delivered  PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"x-not-enum":true,"type":"string"}}],"optional":[{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":false,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"},"required":false},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"},"required":false},{"name":"user_details","in":"query","description":"URLencoded JSON containing details of an anonymous user.","schema":{"type":"string"},"required":false}],"query":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059.","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":false,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"},"required":false},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"},"required":false},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment  HomeDelivery - If the customer wants the order home-delivered  PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"x-not-enum":true,"type":"string"}},{"name":"user_details","in":"query","description":"URLencoded JSON containing details of an anonymous user.","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", serverType="application", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details)
        query_string = await create_query_string(amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPosPaymentModeRoutes"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/options/pos", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentModeRouteDetails
            schema = PaymentModeRouteDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPosPaymentModeRoutes")
                print(e)

        return response
    
    async def walletLinkInitiate(self, body="", request_headers:Dict={}):
        """Link wallet for the aggregator for processing of payment.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.walletLinkInitiate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import WalletLinkRequestSchema
        schema = WalletLinkRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["walletLinkInitiate"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["walletLinkInitiate"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/options/wallet/link", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import WalletResponseSchema
            schema = WalletResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for walletLinkInitiate")
                print(e)

        return response
    
    async def linkWallet(self, body="", request_headers:Dict={}):
        """Verify the linking of wallet using OTP for further processing of payment.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.linkWallet()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import WalletVerifyRequestSchema
        schema = WalletVerifyRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["linkWallet"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["linkWallet"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/options/wallet/verify", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import WalletResponseSchema
            schema = WalletResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for linkWallet")
                print(e)

        return response
    
    async def delinkWallet(self, body="", request_headers:Dict={}):
        """Delink the wallet.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.delinkWallet()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import WalletDelinkRequestSchema
        schema = WalletDelinkRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["delinkWallet"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["delinkWallet"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/options/wallet/delink", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import WalletResponseSchema
            schema = WalletResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for delinkWallet")
                print(e)

        return response
    
    async def getRupifiBannerDetails(self, body="", request_headers:Dict={}):
        """Get Rupifi payment banner details. It provides information such as the KYC URL and the current status of the Rupifi payment banner.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getRupifiBannerDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getRupifiBannerDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getRupifiBannerDetails"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/rupifi/banner", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RupifiBannerDetails
            schema = RupifiBannerDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRupifiBannerDetails")
                print(e)

        return response
    
    async def getEpaylaterBannerDetails(self, body="", request_headers:Dict={}):
        """Get Epaylater payment banner details. It provides information about the banner's display status, along with relevant messages and the user's registration status.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getEpaylaterBannerDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getEpaylaterBannerDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getEpaylaterBannerDetails"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/epaylater/banner", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EpaylaterBannerDetails
            schema = EpaylaterBannerDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEpaylaterBannerDetails")
                print(e)

        return response
    
    async def resendOrCancelPayment(self, body="", request_headers:Dict={}):
        """Resend or cancel payment link that have been initiated but may require modification or cancellation for various reasons, ensuring flexibility and control in payment processing.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.resendOrCancelPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ResendOrCancelPayment
        schema = ResendOrCancelPayment()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["resendOrCancelPayment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["resendOrCancelPayment"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/resend_or_cancel", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResendOrCancelPaymentDetails
            schema = ResendOrCancelPaymentDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for resendOrCancelPayment")
                print(e)

        return response
    
    async def renderHTML(self, body="", request_headers:Dict={}):
        """Render HTML for a payment aggregator page.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.renderHTML()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RenderHTML
        schema = RenderHTML()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["renderHTML"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["renderHTML"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/html/render/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RenderHTMLDetails
            schema = RenderHTMLDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for renderHTML")
                print(e)

        return response
    
    async def validateVPA(self, body="", request_headers:Dict={}):
        """Validate if a Virtual Payment Address (VPA) is valid for processing payments and returns the validation result.is_valid boolean value indicating whether the VPA is valid for payments.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.validateVPA()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateVPA
        schema = ValidateVPA()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["validateVPA"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["validateVPA"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/validate-vpa", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ValidateVPADetails
            schema = ValidateVPADetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateVPA")
                print(e)

        return response
    
    async def cardDetails(self, card_info=None, aggregator=None, body="", request_headers:Dict={}):
        """Get details of a specified payment card, including information such as the card type, brand, country, and expiration date.
        :param card_info : Card first 6 digit IIN(prefix) number. : type string
        :param aggregator : This is a string value describing the aggregator name. : type string
        """
        payload = {}
        
        if card_info is not None:
            payload["card_info"] = card_info
        if aggregator is not None:
            payload["aggregator"] = aggregator

        # Parameter validation
        schema = PaymentValidator.cardDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["cardDetails"], proccessed_params="""{"required":[{"name":"card_info","in":"path","description":"Card first 6 digit IIN(prefix) number.","schema":{"type":"string"},"required":true}],"optional":[{"name":"aggregator","in":"query","schema":{"type":"string","default":"juspay"},"description":"This is a string value describing the aggregator name."}],"query":[{"name":"aggregator","in":"query","schema":{"type":"string","default":"juspay"},"description":"This is a string value describing the aggregator name."}],"headers":[],"path":[{"name":"card_info","in":"path","description":"Card first 6 digit IIN(prefix) number.","schema":{"type":"string"},"required":true}]}""", serverType="application", card_info=card_info, aggregator=aggregator)
        query_string = await create_query_string(aggregator=aggregator)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["cardDetails"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/cards/info/{card_info}", card_info=card_info, aggregator=aggregator), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CardDetailsFetchedDetails
            schema = CardDetailsFetchedDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cardDetails")
                print(e)

        return response
    
    async def getActiveRefundTransferModes(self, body="", request_headers:Dict={}):
        """Lists available refund modes, such as UPI, providing details like display name, logo, and ID for each mode.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getActiveRefundTransferModes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getActiveRefundTransferModes"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getActiveRefundTransferModes"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/refund/transfer-mode", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TransferModeFetchDetails
            schema = TransferModeFetchDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getActiveRefundTransferModes")
                print(e)

        return response
    
    async def enableOrDisableRefundTransferMode(self, body="", request_headers:Dict={}):
        """Enable/Disable a particular refund transfer mode based on the request body parameters, indicating whether the mode should be enabled or disabled.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.enableOrDisableRefundTransferMode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateRefundTransferMode
        schema = UpdateRefundTransferMode()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["enableOrDisableRefundTransferMode"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["enableOrDisableRefundTransferMode"]).netloc, "put", await create_url_without_domain("/service/application/payment/v1.0/refund/transfer-mode", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundTransferModeUpdateDetails
            schema = RefundTransferModeUpdateDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for enableOrDisableRefundTransferMode")
                print(e)

        return response
    
    async def getUserBeneficiariesDetail(self, order_id=None, body="", request_headers:Dict={}):
        """Get beneficiaries associated with the user for processing refunds, based on the provided order ID.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id

        # Parameter validation
        schema = PaymentValidator.getUserBeneficiariesDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserBeneficiariesDetail"], proccessed_params="""{"required":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", serverType="application", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getUserBeneficiariesDetail"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/refund/user/beneficiary", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderBeneficiaryFetchDetails
            schema = OrderBeneficiaryFetchDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserBeneficiariesDetail")
                print(e)

        return response
    
    async def verifyIfscCode(self, ifsc_code=None, body="", request_headers:Dict={}):
        """Validate IFSC code and returns bank details if valid.
        :param ifsc_code : A 11-digit alphanumeric code that uniquely identifies a bank branch. : type string
        """
        payload = {}
        
        if ifsc_code is not None:
            payload["ifsc_code"] = ifsc_code

        # Parameter validation
        schema = PaymentValidator.verifyIfscCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyIfscCode"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"ifsc_code","schema":{"x-not-enum":true,"type":"string"},"description":"A 11-digit alphanumeric code that uniquely identifies a bank branch."}],"query":[{"in":"query","name":"ifsc_code","schema":{"x-not-enum":true,"type":"string"},"description":"A 11-digit alphanumeric code that uniquely identifies a bank branch."}],"headers":[],"path":[]}""", serverType="application", ifsc_code=ifsc_code)
        query_string = await create_query_string(ifsc_code=ifsc_code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyIfscCode"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/ifsc-code/verify", ifsc_code=ifsc_code), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import IfscCodeDetails
            schema = IfscCodeDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyIfscCode")
                print(e)

        return response
    
    async def getOrderBeneficiariesDetail(self, order_id=None, body="", request_headers:Dict={}):
        """Get beneficiary details like bank name , ifsc code , branch name associated with a specific order for refund processing.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id

        # Parameter validation
        schema = PaymentValidator.getOrderBeneficiariesDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderBeneficiariesDetail"], proccessed_params="""{"required":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", serverType="application", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrderBeneficiariesDetail"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/refund/order/beneficiaries", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderBeneficiaryFetchDetails
            schema = OrderBeneficiaryFetchDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrderBeneficiariesDetail")
                print(e)

        return response
    
    async def verifyOtpAndAddBeneficiaryForBank(self, body="", request_headers:Dict={}):
        """Verify the OTP provided by the user and adds a bank beneficiary for refund processing.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.verifyOtpAndAddBeneficiaryForBank()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddBeneficiaryViaOtpVerification
        schema = AddBeneficiaryViaOtpVerification()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["verifyOtpAndAddBeneficiaryForBank"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyOtpAndAddBeneficiaryForBank"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/verification/bank", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AddBeneficiaryViaOtpVerificationDetails
            schema = AddBeneficiaryViaOtpVerificationDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyOtpAndAddBeneficiaryForBank")
                print(e)

        return response
    
    async def addBeneficiaryDetails(self, body="", request_headers:Dict={}):
        """Add beneficiary details specifically for refund transactions, including account holder name, account number and bank details.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.addBeneficiaryDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddBeneficiaryDetails
        schema = AddBeneficiaryDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["addBeneficiaryDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addBeneficiaryDetails"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/account", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundAccountDetails
            schema = RefundAccountDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addBeneficiaryDetails")
                print(e)

        return response
    
    async def addRefundBankAccountUsingOTP(self, body="", request_headers:Dict={}):
        """Add bank account specifically for refunds, employing OTP verification for security.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.addRefundBankAccountUsingOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddBeneficiaryDetailsOTP
        schema = AddBeneficiaryDetailsOTP()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["addRefundBankAccountUsingOTP"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addRefundBankAccountUsingOTP"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/account/otp", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundAccountDetails
            schema = RefundAccountDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addRefundBankAccountUsingOTP")
                print(e)

        return response
    
    async def verifyOtpAndAddBeneficiaryForWallet(self, body="", request_headers:Dict={}):
        """Verify OTP provided by the user and adds a wallet beneficiary.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.verifyOtpAndAddBeneficiaryForWallet()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import WalletOtp
        schema = WalletOtp()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["verifyOtpAndAddBeneficiaryForWallet"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyOtpAndAddBeneficiaryForWallet"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/verification/wallet", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import WalletOtpDetails
            schema = WalletOtpDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyOtpAndAddBeneficiaryForWallet")
                print(e)

        return response
    
    async def updateDefaultBeneficiary(self, body="", request_headers:Dict={}):
        """Update default beneficiary for the order refund of the user.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.updateDefaultBeneficiary()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SetDefaultBeneficiary
        schema = SetDefaultBeneficiary()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["updateDefaultBeneficiary"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateDefaultBeneficiary"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/beneficiary/default", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SetDefaultBeneficiaryDetails
            schema = SetDefaultBeneficiaryDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateDefaultBeneficiary")
                print(e)

        return response
    
    async def getPaymentLink(self, payment_link_id=None, body="", request_headers:Dict={}):
        """Get a generated payment link.
        :param payment_link_id : Unique payment link id. : type string
        """
        payload = {}
        
        if payment_link_id is not None:
            payload["payment_link_id"] = payment_link_id

        # Parameter validation
        schema = PaymentValidator.getPaymentLink()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPaymentLink"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"payment_link_id","schema":{"type":"string"},"description":"Unique payment link id."}],"query":[{"in":"query","name":"payment_link_id","schema":{"type":"string"},"description":"Unique payment link id."}],"headers":[],"path":[]}""", serverType="application", payment_link_id=payment_link_id)
        query_string = await create_query_string(payment_link_id=payment_link_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPaymentLink"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/create-payment-link/", payment_link_id=payment_link_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetPaymentLinkDetails
            schema = GetPaymentLinkDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentLink")
                print(e)

        return response
    
    async def createPaymentLink(self, body="", request_headers:Dict={}):
        """Create new payment link for transactions.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.createPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreatePaymentLink
        schema = CreatePaymentLink()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["createPaymentLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["createPaymentLink"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/create-payment-link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreatePaymentLinkDetails
            schema = CreatePaymentLinkDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPaymentLink")
                print(e)

        return response
    
    async def resendPaymentLink(self, body="", request_headers:Dict={}):
        """Resend an existing payment link to the user to complete the payment.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.resendPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CancelOrResendPaymentLink
        schema = CancelOrResendPaymentLink()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["resendPaymentLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["resendPaymentLink"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/resend-payment-link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResendPaymentLinkDetails
            schema = ResendPaymentLinkDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for resendPaymentLink")
                print(e)

        return response
    
    async def cancelPaymentLink(self, body="", request_headers:Dict={}):
        """Cancel previously generated payment link.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.cancelPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CancelOrResendPaymentLink
        schema = CancelOrResendPaymentLink()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["cancelPaymentLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["cancelPaymentLink"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/cancel-payment-link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CancelPaymentLinkDetails
            schema = CancelPaymentLinkDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelPaymentLink")
                print(e)

        return response
    
    async def getPaymentModeRoutesPaymentLink(self, payment_link_id=None, body="", request_headers:Dict={}):
        """List payment modes available for a given payment link.
        :param payment_link_id : Payment link id. : type string
        """
        payload = {}
        
        if payment_link_id is not None:
            payload["payment_link_id"] = payment_link_id

        # Parameter validation
        schema = PaymentValidator.getPaymentModeRoutesPaymentLink()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPaymentModeRoutesPaymentLink"], proccessed_params="""{"required":[{"name":"payment_link_id","in":"query","description":"Payment link id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"payment_link_id","in":"query","description":"Payment link id.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", serverType="application", payment_link_id=payment_link_id)
        query_string = await create_query_string(payment_link_id=payment_link_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPaymentModeRoutesPaymentLink"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/options/link/", payment_link_id=payment_link_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentModeRouteDetails
            schema = PaymentModeRouteDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentModeRoutesPaymentLink")
                print(e)

        return response
    
    async def pollingPaymentLink(self, payment_link_id=None, body="", request_headers:Dict={}):
        """Get real-time information about the payment link's current status, such as whether it has been processed, cancelled, or expired.
        :param payment_link_id : Unique payment link id. : type string
        """
        payload = {}
        
        if payment_link_id is not None:
            payload["payment_link_id"] = payment_link_id

        # Parameter validation
        schema = PaymentValidator.pollingPaymentLink()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["pollingPaymentLink"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"payment_link_id","schema":{"type":"string"},"description":"Unique payment link id."}],"query":[{"in":"query","name":"payment_link_id","schema":{"type":"string"},"description":"Unique payment link id."}],"headers":[],"path":[]}""", serverType="application", payment_link_id=payment_link_id)
        query_string = await create_query_string(payment_link_id=payment_link_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["pollingPaymentLink"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/polling-payment-link/", payment_link_id=payment_link_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PollingPaymentLinkDetails
            schema = PollingPaymentLinkDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for pollingPaymentLink")
                print(e)

        return response
    
    async def createOrderHandlerPaymentLink(self, body="", request_headers:Dict={}):
        """Initiate the creation of an order handler for processing payments through a link.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.createOrderHandlerPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateOrderUser
        schema = CreateOrderUser()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["createOrderHandlerPaymentLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["createOrderHandlerPaymentLink"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/create-order/link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateOrderUserDetails
            schema = CreateOrderUserDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createOrderHandlerPaymentLink")
                print(e)

        return response
    
    async def initialisePaymentPaymentLink(self, body="", request_headers:Dict={}):
        """Begin payment process for an order by initializing it through a payment link.Upon successful initialization, the response includes details about the payment status, aggregator details, order IDs, polling URL for status updates, and other relevant information.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.initialisePaymentPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentInitialization
        schema = PaymentInitialization()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["initialisePaymentPaymentLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["initialisePaymentPaymentLink"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/request/link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentInitializationDetails
            schema = PaymentInitializationDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for initialisePaymentPaymentLink")
                print(e)

        return response
    
    async def checkAndUpdatePaymentStatusPaymentLink(self, body="", request_headers:Dict={}):
        """Verify and update status of a payment made through a link.Upon successful verification and update, the response includes details about the aggregator name, payment status, and whether retrying the process is required.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.checkAndUpdatePaymentStatusPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentStatusUpdate
        schema = PaymentStatusUpdate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["checkAndUpdatePaymentStatusPaymentLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["checkAndUpdatePaymentStatusPaymentLink"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/confirm/polling/link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentStatusUpdateDetails
            schema = PaymentStatusUpdateDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkAndUpdatePaymentStatusPaymentLink")
                print(e)

        return response
    
    async def customerCreditSummary(self, aggregator=None, body="", request_headers:Dict={}):
        """Get summary of the customer's credit information, including details such as merchant customer reference ID, status, balance, limit, due amount, used amount, due date, days overdue, total due amount, and a repayment URL.
        :param aggregator : Aggregator name. : type string
        """
        payload = {}
        
        if aggregator is not None:
            payload["aggregator"] = aggregator

        # Parameter validation
        schema = PaymentValidator.customerCreditSummary()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["customerCreditSummary"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"aggregator","schema":{"type":"string"},"description":"Aggregator name."}],"query":[{"in":"query","name":"aggregator","schema":{"type":"string"},"description":"Aggregator name."}],"headers":[],"path":[]}""", serverType="application", aggregator=aggregator)
        query_string = await create_query_string(aggregator=aggregator)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["customerCreditSummary"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/credit-summary/", aggregator=aggregator), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomerCreditSummaryDetails
            schema = CustomerCreditSummaryDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for customerCreditSummary")
                print(e)

        return response
    
    async def redirectToAggregator(self, source=None, aggregator=None, body="", request_headers:Dict={}):
        """This endpoint is used to redirect users to the payment aggregator's platform where they can complete the payment process. The request may include necessary details for initiating the payment on the aggregator’s side, and the user is transferred seamlessly to their interface.
        :param source : Callback URL to get callback from aggregator. : type string
        :param aggregator : Aggregator name. : type string
        """
        payload = {}
        
        if source is not None:
            payload["source"] = source
        if aggregator is not None:
            payload["aggregator"] = aggregator

        # Parameter validation
        schema = PaymentValidator.redirectToAggregator()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["redirectToAggregator"], proccessed_params="""{"required":[{"name":"aggregator","in":"query","description":"Aggregator name.","schema":{"type":"string"},"required":true}],"optional":[{"name":"source","in":"query","description":"Callback URL to get callback from aggregator.","schema":{"type":"string"}}],"query":[{"name":"source","in":"query","description":"Callback URL to get callback from aggregator.","schema":{"type":"string"}},{"name":"aggregator","in":"query","description":"Aggregator name.","schema":{"type":"string"},"required":true}],"headers":[],"path":[]}""", serverType="application", source=source, aggregator=aggregator)
        query_string = await create_query_string(source=source, aggregator=aggregator)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["redirectToAggregator"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/redirect-to-aggregator/", source=source, aggregator=aggregator), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RedirectToAggregatorDetails
            schema = RedirectToAggregatorDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for redirectToAggregator")
                print(e)

        return response
    
    async def checkCredit(self, aggregator=None, body="", request_headers:Dict={}):
        """Check the availability and status of customer credit, providing the status of payment along with registration information and signup URL if the customer is not registered.
        :param aggregator : Aggregator name. : type string
        """
        payload = {}
        
        if aggregator is not None:
            payload["aggregator"] = aggregator

        # Parameter validation
        schema = PaymentValidator.checkCredit()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["checkCredit"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"aggregator","schema":{"type":"string"},"description":"Aggregator name."}],"query":[{"in":"query","name":"aggregator","schema":{"type":"string"},"description":"Aggregator name."}],"headers":[],"path":[]}""", serverType="application", aggregator=aggregator)
        query_string = await create_query_string(aggregator=aggregator)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["checkCredit"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/check-credits/", aggregator=aggregator), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CheckCreditDetails
            schema = CheckCreditDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkCredit")
                print(e)

        return response
    
    async def customerOnboard(self, body="", request_headers:Dict={}):
        """Initiate the onboarding process for payment services, providing personal, business, and device information, along with marketplace details, to enable customer registration and credit availability.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.customerOnboard()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CustomerOnboarding
        schema = CustomerOnboarding()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["customerOnboard"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["customerOnboard"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/credit-onboard/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomerOnboardingDetails
            schema = CustomerOnboardingDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for customerOnboard")
                print(e)

        return response
    
    async def outstandingOrderDetails(self, aggregator=None, body="", request_headers:Dict={}):
        """Get details of orders with outstanding payments.
        :param aggregator : Merchant user ID as value. : type string
        """
        payload = {}
        
        if aggregator is not None:
            payload["aggregator"] = aggregator

        # Parameter validation
        schema = PaymentValidator.outstandingOrderDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["outstandingOrderDetails"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"aggregator","schema":{"type":"string"},"description":"Merchant user ID as value."}],"query":[{"in":"query","name":"aggregator","schema":{"type":"string"},"description":"Merchant user ID as value."}],"headers":[],"path":[]}""", serverType="application", aggregator=aggregator)
        query_string = await create_query_string(aggregator=aggregator)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["outstandingOrderDetails"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/outstanding-orders/", aggregator=aggregator), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OutstandingOrderDetails
            schema = OutstandingOrderDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for outstandingOrderDetails")
                print(e)

        return response
    
    async def paidOrderDetails(self, aggregator=None, body="", request_headers:Dict={}):
        """Get details of orders that have been paid for, including shipment ID, order ID, due date, payment date, amount, and transaction ID, based on the aggregator merchant user ID.
        :param aggregator : Merchant user ID as value. : type string
        """
        payload = {}
        
        if aggregator is not None:
            payload["aggregator"] = aggregator

        # Parameter validation
        schema = PaymentValidator.paidOrderDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["paidOrderDetails"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"aggregator","schema":{"type":"string"},"description":"Merchant user ID as value."}],"query":[{"in":"query","name":"aggregator","schema":{"type":"string"},"description":"Merchant user ID as value."}],"headers":[],"path":[]}""", serverType="application", aggregator=aggregator)
        query_string = await create_query_string(aggregator=aggregator)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["paidOrderDetails"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/paid-orders/", aggregator=aggregator), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaidOrderDetails
            schema = PaidOrderDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for paidOrderDetails")
                print(e)

        return response
    
    async def createPaymentOrder(self, body="", request_headers:Dict={}):
        """Create an order and payment on the aggregator side.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.createPaymentOrder()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentOrder
        schema = PaymentOrder()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["createPaymentOrder"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["createPaymentOrder"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment-orders/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentOrderDetails
            schema = PaymentOrderDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPaymentOrder")
                print(e)

        return response
    