"""Payment Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import PaymentValidator

class Payment:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def getBrandPaymentGatewayConfig(self, aggregator=None, config_type=None, request_headers:Dict={}):
        """Retrieve configuration settings like key, secret, webhook url, merchant salt for brand payment gateways.
        :param aggregator : aggregator slug : type string
        :param config_type :  : type string
        """
        payload = {}
        
        if aggregator is not None:
            payload["aggregator"] = aggregator
        if config_type is not None:
            payload["config_type"] = config_type

        # Parameter validation
        schema = PaymentValidator.getBrandPaymentGatewayConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator","in":"query","description":"aggregator slug","schema":{"type":"string"},"required":true}],"optional":[{"name":"config_type","in":"query","schema":{"type":"string","enum":["self","partner","fynd"]}}],"query":[{"name":"aggregator","in":"query","description":"aggregator slug","schema":{"type":"string"},"required":true},{"name":"config_type","in":"query","schema":{"type":"string","enum":["self","partner","fynd"]}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", aggregator=aggregator, config_type=config_type)
        query_string = await create_query_string(aggregator=aggregator, config_type=config_type)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", aggregator=aggregator, config_type=config_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentGatewayConfigResponse
            schema = PaymentGatewayConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBrandPaymentGatewayConfig")
                print(e)

        return response
    
    async def saveBrandPaymentGatewayConfig(self, body="", request_headers:Dict={}):
        """Store and update configuration settings for brand payment gateways i.e required for payment for a payment gateway like key, secret, merchant salt. - Payment
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.saveBrandPaymentGatewayConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentGatewayConfigRequest
        schema = PaymentGatewayConfigRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentGatewayToBeReviewed
            schema = PaymentGatewayToBeReviewed()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for saveBrandPaymentGatewayConfig")
                print(e)

        return response
    
    async def getPaymentModeRoutes(self, refresh=None, request_type=None, order_id=None, shipment_id=None, amount=None, request_headers:Dict={}):
        """Get available payment methods on the payment page, specifying the aggregator for each option, such as 'Netbanking powered by Juspay' and 'Card powered by Razorpay'.
        :param refresh : Flag to refresh the cache and retrieve the updated payment option : type boolean
        :param request_type : type of payment request, i.e. self : type string
        :param order_id : order id for the payment : type string
        :param shipment_id : shipment id for the payment : type string
        :param amount : amount for the payment : type integer
        """
        payload = {}
        
        if refresh is not None:
            payload["refresh"] = refresh
        if request_type is not None:
            payload["request_type"] = request_type
        if order_id is not None:
            payload["order_id"] = order_id
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if amount is not None:
            payload["amount"] = amount

        # Parameter validation
        schema = PaymentValidator.getPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[{"name":"refresh","in":"query","description":"Flag to refresh the cache and retrieve the updated payment option","required":false,"schema":{"type":"boolean"}},{"name":"request_type","in":"query","required":false,"description":"type of payment request, i.e. self","schema":{"type":"string"}},{"name":"order_id","in":"query","required":false,"description":"order id for the payment","schema":{"type":"string"}},{"name":"shipment_id","in":"query","required":false,"description":"shipment id for the payment","schema":{"type":"string"}},{"name":"amount","in":"query","required":false,"description":"amount for the payment","schema":{"type":"integer"}}],"query":[{"name":"refresh","in":"query","description":"Flag to refresh the cache and retrieve the updated payment option","required":false,"schema":{"type":"boolean"}},{"name":"request_type","in":"query","required":false,"description":"type of payment request, i.e. self","schema":{"type":"string"}},{"name":"order_id","in":"query","required":false,"description":"order id for the payment","schema":{"type":"string"}},{"name":"shipment_id","in":"query","required":false,"description":"shipment id for the payment","schema":{"type":"string"}},{"name":"amount","in":"query","required":false,"description":"amount for the payment","schema":{"type":"integer"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", refresh=refresh, request_type=request_type, order_id=order_id, shipment_id=shipment_id, amount=amount)
        query_string = await create_query_string(refresh=refresh, request_type=request_type, order_id=order_id, shipment_id=shipment_id, amount=amount)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options", refresh=refresh, request_type=request_type, order_id=order_id, shipment_id=shipment_id, amount=amount), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentOptionsResponse
            schema = PaymentOptionsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentModeRoutes")
                print(e)

        return response
    
    async def getBankAccountDetailsOpenAPI(self, order_id=None, request_hash=None, request_headers:Dict={}):
        """Retrieve bank account information
        :param order_id :  : type string
        :param request_hash :  : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id
        if request_hash is not None:
            payload["request_hash"] = request_hash

        # Parameter validation
        schema = PaymentValidator.getBankAccountDetailsOpenAPI()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account", """{"required":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"request_hash","schema":{"type":"string"}}],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"request_hash","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", order_id=order_id, request_hash=request_hash, )
        query_string = await create_query_string(order_id=order_id, request_hash=request_hash, )
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account", order_id=order_id, request_hash=request_hash), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetRefundAccountResponse
            schema = GetRefundAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBankAccountDetailsOpenAPI")
                print(e)

        return response
    
    async def addRefundBankAccountUsingOTP(self, body="", request_headers:Dict={}):
        """The addition of a bank account specifically for refunds, employing OTP verification for security - Payment
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.addRefundBankAccountUsingOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddBeneficiaryDetailsOTPRequest
        schema = AddBeneficiaryDetailsOTPRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundAccountResponse
            schema = RefundAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addRefundBankAccountUsingOTP")
                print(e)

        return response
    
    async def getUserOrderBeneficiaries(self, order_id=None, request_headers:Dict={}):
        """Retrieve beneficiary details like bank name , ifsc code , branch name associated with a specific order for refund processing
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id

        # Parameter validation
        schema = PaymentValidator.getUserOrderBeneficiaries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/order", """{"required":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", order_id=order_id, )
        query_string = await create_query_string(order_id=order_id, )
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/order", order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderBeneficiaryResponse
            schema = OrderBeneficiaryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserOrderBeneficiaries")
                print(e)

        return response
    
    async def getUserBeneficiaries(self, order_id=None, request_headers:Dict={}):
        """Retrieves information about beneficiaries associated with the user for processing refunds, based on the provided order ID
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id

        # Parameter validation
        schema = PaymentValidator.getUserBeneficiaries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/user", """{"required":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", order_id=order_id, )
        query_string = await create_query_string(order_id=order_id, )
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/user", order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderBeneficiaryResponse
            schema = OrderBeneficiaryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserBeneficiaries")
                print(e)

        return response
    
    async def confirmPayment(self, body="", request_headers:Dict={}):
        """Authentication and confirmation of a payment.It requires details such as the order ID and payment methods in the request body to authenticate and confirm the payment.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.confirmPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentConfirmationRequest
        schema = PaymentConfirmationRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/confirm", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/confirm", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentConfirmationResponse
            schema = PaymentConfirmationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for confirmPayment")
                print(e)

        return response
    
    async def getUserCODlimitRoutes(self, merchant_user_id=None, mobile_no=None, request_headers:Dict={}):
        """Retrieve user cod limt data of user i.e cod is active or not for user and remaining limit
        :param merchant_user_id :  : type string
        :param mobile_no :  : type string
        """
        payload = {}
        
        if merchant_user_id is not None:
            payload["merchant_user_id"] = merchant_user_id
        if mobile_no is not None:
            payload["mobile_no"] = mobile_no

        # Parameter validation
        schema = PaymentValidator.getUserCODlimitRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/user-cod", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"merchant_user_id","in":"query","required":true,"schema":{"type":"string"}},{"name":"mobile_no","in":"query","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"merchant_user_id","in":"query","required":true,"schema":{"type":"string"}},{"name":"mobile_no","in":"query","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", merchant_user_id=merchant_user_id, mobile_no=mobile_no)
        query_string = await create_query_string(merchant_user_id=merchant_user_id, mobile_no=mobile_no)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/user-cod", merchant_user_id=merchant_user_id, mobile_no=mobile_no), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetUserCODLimitResponse
            schema = GetUserCODLimitResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserCODlimitRoutes")
                print(e)

        return response
    
    async def setUserCODlimitRoutes(self, body="", request_headers:Dict={}):
        """This allows access to seller to enable disable cod of specific user
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.setUserCODlimitRoutes()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SetCODForUserRequest
        schema = SetCODForUserRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/user-cod", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/user-cod", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetUserCODLimitResponse
            schema = GetUserCODLimitResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setUserCODlimitRoutes")
                print(e)

        return response
    
    async def edcAggregatorsAndModelList(self, request_headers:Dict={}):
        """Retrieve a list of EDC (Electronic Data Capture) aggregators and models.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.edcAggregatorsAndModelList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-aggregator-list", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-aggregator-list", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EdcAggregatorAndModelListResponse
            schema = EdcAggregatorAndModelListResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for edcAggregatorsAndModelList")
                print(e)

        return response
    
    async def edcDeviceStats(self, request_headers:Dict={}):
        """Information about EDC (Electronic Data Capture) devices linked to a specific application within a company. It provides statistics such as the count of active and inactive devices.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.edcDeviceStats()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-stats", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-stats", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EdcDeviceStatsResponse
            schema = EdcDeviceStatsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for edcDeviceStats")
                print(e)

        return response
    
    async def updateEdcDevice(self, body="", request_headers:Dict={}):
        """Enables the modification of settings and details associated with an Electronic Data Capture (EDC) device linked to a specific application within a company. Upon success, it returns the updated information of the EDC device.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.updateEdcDevice()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EdcAddRequest
        schema = EdcAddRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EdcDeviceAddResponse
            schema = EdcDeviceAddResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateEdcDevice")
                print(e)

        return response
    
    async def getEdcDevice(self, terminal_unique_identifier=None, request_headers:Dict={}):
        """Retrieve comprehensive details regarding an Electronic Data Capture (EDC) device associated with a particular terminal unique identifier within a company's application.Upon success, it returns the detailed information of the EDC device, including terminal serial number, EDC device serial number, merchant store POS code, store ID, aggregator ID and name, device tag, activation status, and EDC model.
        :param terminal_unique_identifier : Terminal unique identifier : type string
        """
        payload = {}
        
        if terminal_unique_identifier is not None:
            payload["terminal_unique_identifier"] = terminal_unique_identifier

        # Parameter validation
        schema = PaymentValidator.getEdcDevice()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}]}""", serverType="platform", terminal_unique_identifier=terminal_unique_identifier)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", terminal_unique_identifier=terminal_unique_identifier), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EdcDeviceDetailsResponse
            schema = EdcDeviceDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEdcDevice")
                print(e)

        return response
    
    async def addEdcDevice(self, terminal_unique_identifier=None, body="", request_headers:Dict={}):
        """Registration and addition of a new EDC device to the system
        :param terminal_unique_identifier : Terminal unique identifier : type string
        """
        payload = {}
        
        if terminal_unique_identifier is not None:
            payload["terminal_unique_identifier"] = terminal_unique_identifier

        # Parameter validation
        schema = PaymentValidator.addEdcDevice()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EdcUpdateRequest
        schema = EdcUpdateRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}]}""", serverType="platform", terminal_unique_identifier=terminal_unique_identifier)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", terminal_unique_identifier=terminal_unique_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EdcDeviceUpdateResponse
            schema = EdcDeviceUpdateResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addEdcDevice")
                print(e)

        return response
    
    async def edcDeviceList(self, page_no=None, page_size=None, is_active=None, store_id=None, device_tag=None, request_headers:Dict={}):
        """Retrieves a list of available Electronic Data Capture (EDC) devices.
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param is_active :  : type boolean
        :param store_id :  : type integer
        :param device_tag :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if is_active is not None:
            payload["is_active"] = is_active
        if store_id is not None:
            payload["store_id"] = store_id
        if device_tag is not None:
            payload["device_tag"] = device_tag

        # Parameter validation
        schema = PaymentValidator.edcDeviceList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-list", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"in":"query","name":"page_size","schema":{"type":"integer"}},{"in":"query","name":"is_active","schema":{"type":"boolean"}},{"in":"query","name":"store_id","schema":{"type":"integer"}},{"in":"query","name":"device_tag","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"in":"query","name":"page_size","schema":{"type":"integer"}},{"in":"query","name":"is_active","schema":{"type":"boolean"}},{"in":"query","name":"store_id","schema":{"type":"integer"}},{"in":"query","name":"device_tag","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, is_active=is_active, store_id=store_id, device_tag=device_tag, )
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_active=is_active, store_id=store_id, device_tag=device_tag, )
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-list", page_no=page_no, page_size=page_size, is_active=is_active, store_id=store_id, device_tag=device_tag), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EdcDeviceListResponse
            schema = EdcDeviceListResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for edcDeviceList")
                print(e)

        return response
    
    async def getPosPaymentModeRoutes(self, amount=None, cart_id=None, pincode=None, checkout_mode=None, refresh=None, order_id=None, card_reference=None, order_type=None, user_details=None, display_split=None, advance_payment=None, shipment_id=None, request_headers:Dict={}):
        """Retrieve payment options and aggregator for point-of-sale (POS).
        :param amount : Payable amount. : type integer
        :param cart_id : Identifier of the cart. : type string
        :param pincode : The PIN Code of the destination address, e.g. 400059 : type string
        :param checkout_mode : Option to checkout for self or for others. : type string
        :param refresh : This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one. : type boolean
        :param order_id :  : type string
        :param card_reference : Card reference id of user's debit or credit card. : type string
        :param order_type : The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        :param user_details : URIencoded JSON containing details of an anonymous user. : type string
        :param display_split : Display Split Payment Option or not : type boolean
        :param advance_payment : Display Advance Payment Options or Normal : type boolean
        :param shipment_id :  : type string
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
        if order_id is not None:
            payload["order_id"] = order_id
        if card_reference is not None:
            payload["card_reference"] = card_reference
        if order_type is not None:
            payload["order_type"] = order_type
        if user_details is not None:
            payload["user_details"] = user_details
        if display_split is not None:
            payload["display_split"] = display_split
        if advance_payment is not None:
            payload["advance_payment"] = advance_payment
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = PaymentValidator.getPosPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/pos", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string"}}],"optional":[{"name":"cart_id","in":"query","description":"Identifier of the cart.","schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","schema":{"type":"string"}},{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"order_id","in":"query","schema":{"type":"string"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","schema":{"type":"string"}},{"name":"display_split","in":"query","description":"Display Split Payment Option or not","schema":{"type":"boolean"}},{"name":"advance_payment","in":"query","description":"Display Advance Payment Options or Normal","schema":{"type":"boolean"}},{"name":"shipment_id","in":"query","schema":{"type":"string"}}],"query":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","schema":{"type":"string"}},{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"order_id","in":"query","schema":{"type":"string"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","schema":{"type":"string"}},{"name":"display_split","in":"query","description":"Display Split Payment Option or not","schema":{"type":"boolean"}},{"name":"advance_payment","in":"query","description":"Display Advance Payment Options or Normal","schema":{"type":"boolean"}},{"name":"shipment_id","in":"query","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, order_id=order_id, card_reference=card_reference, order_type=order_type, user_details=user_details, display_split=display_split, advance_payment=advance_payment, shipment_id=shipment_id)
        query_string = await create_query_string(amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, order_id=order_id, card_reference=card_reference, order_type=order_type, user_details=user_details, display_split=display_split, advance_payment=advance_payment, shipment_id=shipment_id)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/pos", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, order_id=order_id, card_reference=card_reference, order_type=order_type, user_details=user_details, display_split=display_split, advance_payment=advance_payment, shipment_id=shipment_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentModeRouteResponse
            schema = PaymentModeRouteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPosPaymentModeRoutes")
                print(e)

        return response
    
    async def initialisePayment(self, body="", request_headers:Dict={}):
        """Initiates the payment procedure for an order.Upon successful initiation, it returns a  details including the success status, aggregator information, payment method, status, merchant order ID aggregator order , polling URL, timeout, virtual ID, Razorpay payment ID, customer ID, and device ID.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.initialisePayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentInitializationRequest
        schema = PaymentInitializationRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/request", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentInitializationResponse
            schema = PaymentInitializationResponse()
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
        from .models import PaymentStatusUpdateRequest
        schema = PaymentStatusUpdateRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/confirm/polling", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/confirm/polling", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentStatusUpdateResponse
            schema = PaymentStatusUpdateResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkAndUpdatePaymentStatus")
                print(e)

        return response
    
    async def resendOrCancelPayment(self, body="", request_headers:Dict={}):
        """Enable you to perform actions related to the resending and cancellation of payment links through SMS or EMAIL. resend or cancel payment link that have been initiated but may require modification or cancellation for various reasons, ensuring flexibility and control in payment processing.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.resendOrCancelPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ResendOrCancelPaymentRequest
        schema = ResendOrCancelPaymentRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/cancel", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/cancel", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResendOrCancelPaymentResponse
            schema = ResendOrCancelPaymentResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for resendOrCancelPayment")
                print(e)

        return response
    
    async def paymentStatusBulk(self, body="", request_headers:Dict={}):
        """Retrieve status of multiple payments in bulk and returns the status of each payment along with associated details such as payment ID, amount, currency, status, payment mode, and payment gateway in the response
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.paymentStatusBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentStatusBulkHandlerRequest
        schema = PaymentStatusBulkHandlerRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/payment-status-bulk", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/payment-status-bulk", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentStatusBulkHandlerResponse
            schema = PaymentStatusBulkHandlerResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for paymentStatusBulk")
                print(e)

        return response
    
    async def oauthGetUrl(self, aggregator=None, success_redirect_url=None, failure_redirect_url=None, request_headers:Dict={}):
        """This has been used when merchant is setup their razorpay payment gateway, they will redirect to razorpay site after submitting all their secrets for authetication.
        :param aggregator : aggregator : type string
        :param success_redirect_url :  : type string
        :param failure_redirect_url :  : type string
        """
        payload = {}
        
        if aggregator is not None:
            payload["aggregator"] = aggregator
        if success_redirect_url is not None:
            payload["success_redirect_url"] = success_redirect_url
        if failure_redirect_url is not None:
            payload["failure_redirect_url"] = failure_redirect_url

        # Parameter validation
        schema = PaymentValidator.oauthGetUrl()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/onboard/{aggregator}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator","in":"path","description":"aggregator","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"success_redirect_url","schema":{"type":"string","description":"This is the url which will come back to after success authorization complete"}},{"in":"query","name":"failure_redirect_url","schema":{"type":"string","description":"This is the url which will come back to after failure authorization"}}],"query":[{"in":"query","name":"success_redirect_url","schema":{"type":"string","description":"This is the url which will come back to after success authorization complete"}},{"in":"query","name":"failure_redirect_url","schema":{"type":"string","description":"This is the url which will come back to after failure authorization"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator","in":"path","description":"aggregator","schema":{"type":"string"},"required":true}]}""", serverType="platform", aggregator=aggregator, success_redirect_url=success_redirect_url, failure_redirect_url=failure_redirect_url)
        query_string = await create_query_string(success_redirect_url=success_redirect_url, failure_redirect_url=failure_redirect_url)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/onboard/{aggregator}", aggregator=aggregator, success_redirect_url=success_redirect_url, failure_redirect_url=failure_redirect_url), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetOauthUrlResponse
            schema = GetOauthUrlResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for oauthGetUrl")
                print(e)

        return response
    
    async def revokeOauthToken(self, aggregator=None, request_headers:Dict={}):
        """Revoke the creds  for payment aggregator
        :param aggregator : aggregator_slug : type string
        """
        payload = {}
        
        if aggregator is not None:
            payload["aggregator"] = aggregator

        # Parameter validation
        schema = PaymentValidator.revokeOauthToken()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/revoke/{aggregator}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator","in":"path","description":"aggregator_slug","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator","in":"path","description":"aggregator_slug","schema":{"type":"string"},"required":true}]}""", serverType="platform", aggregator=aggregator)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/revoke/{aggregator}", aggregator=aggregator), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RevokeOAuthToken
            schema = RevokeOAuthToken()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for revokeOauthToken")
                print(e)

        return response
    
    async def repaymentDetails(self, body="", request_headers:Dict={}):
        """Retrieve repayment details for Buy Now Pay Later (BNPL) payment
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.repaymentDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RepaymentDetailsSerialiserPayAll
        schema = RepaymentDetailsSerialiserPayAll()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/repayment-details", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/repayment-details", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RepaymentResponse
            schema = RepaymentResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for repaymentDetails")
                print(e)

        return response
    
    async def merchantOnBoarding(self, body="", request_headers:Dict={}):
        """Initiate the merchant onboarding process for Buy Now Pay Later (BNPL).
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.merchantOnBoarding()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MerchantOnBoardingRequest
        schema = MerchantOnBoardingRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchant-onboarding", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchant-onboarding", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MerchantOnBoardingResponse
            schema = MerchantOnBoardingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for merchantOnBoarding")
                print(e)

        return response
    
    async def verifyCustomerForPayment(self, body="", request_headers:Dict={}):
        """Verify whether the user is eligible for pay-later payment from the payment aggregator's side using the customer's phone number
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.verifyCustomerForPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateCustomerRequest
        schema = ValidateCustomerRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/customer/validation", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/customer/validation", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ValidateCustomerResponse
            schema = ValidateCustomerResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyCustomerForPayment")
                print(e)

        return response
    
    async def getPaymentLink(self, payment_link_id=None, request_headers:Dict={}):
        """Retrieve a payment link for making payments - Payment
        :param payment_link_id :  : type string
        """
        payload = {}
        
        if payment_link_id is not None:
            payload["payment_link_id"] = payment_link_id

        # Parameter validation
        schema = PaymentValidator.getPaymentLink()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/create-payment-link", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"in":"query","name":"payment_link_id","required":true,"schema":{"type":"string","description":"Unique payment link id"}}],"optional":[],"query":[{"in":"query","name":"payment_link_id","required":true,"schema":{"type":"string","description":"Unique payment link id"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", payment_link_id=payment_link_id)
        query_string = await create_query_string(payment_link_id=payment_link_id)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/create-payment-link", payment_link_id=payment_link_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetPaymentLinkResponse
            schema = GetPaymentLinkResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentLink")
                print(e)

        return response
    
    async def createPaymentLink(self, body="", request_headers:Dict={}):
        """Generate a payment link for accepting payments.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.createPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreatePaymentLinkRequest
        schema = CreatePaymentLinkRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/create-payment-link", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/create-payment-link", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreatePaymentLinkResponse
            schema = CreatePaymentLinkResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPaymentLink")
                print(e)

        return response
    
    async def getPaymentLinkId(self, id=None, payment_link_id=None, request_headers:Dict={}):
        """get a payment link
        :param id :  : type string
        :param payment_link_id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if payment_link_id is not None:
            payload["payment_link_id"] = payment_link_id

        # Parameter validation
        schema = PaymentValidator.getPaymentLinkId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/create-payment-link/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","schema":{"type":"string","description":"Unique payment link id"},"required":true},{"in":"query","name":"payment_link_id","required":true,"schema":{"type":"string","description":"Unique payment link id"}}],"optional":[],"query":[{"in":"query","name":"payment_link_id","required":true,"schema":{"type":"string","description":"Unique payment link id"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","schema":{"type":"string","description":"Unique payment link id"},"required":true}]}""", serverType="platform", id=id, payment_link_id=payment_link_id)
        query_string = await create_query_string(payment_link_id=payment_link_id)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/create-payment-link/{id}", id=id, payment_link_id=payment_link_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetPaymentLinkResponse
            schema = GetPaymentLinkResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentLinkId")
                print(e)

        return response
    
    async def pollingPaymentLink(self, payment_link_id=None, request_headers:Dict={}):
        """Periodically checks the status of a payment link to monitor for any updates or changes.retrieve real-time information about the payment link's current status, such as whether it has been processed, cancelled, or expired
        :param payment_link_id :  : type string
        """
        payload = {}
        
        if payment_link_id is not None:
            payload["payment_link_id"] = payment_link_id

        # Parameter validation
        schema = PaymentValidator.pollingPaymentLink()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/polling-payment-link", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"in":"query","name":"payment_link_id","schema":{"type":"string","description":"Unique payment link id"},"required":true}],"optional":[],"query":[{"in":"query","name":"payment_link_id","schema":{"type":"string","description":"Unique payment link id"},"required":true}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", payment_link_id=payment_link_id)
        query_string = await create_query_string(payment_link_id=payment_link_id)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/polling-payment-link", payment_link_id=payment_link_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PollingPaymentLinkResponse
            schema = PollingPaymentLinkResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for pollingPaymentLink")
                print(e)

        return response
    
    async def resendPaymentLink(self, body="", request_headers:Dict={}):
        """Resends an existing payment link to the user to complete the payment
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.resendPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CancelOrResendPaymentLinkRequest
        schema = CancelOrResendPaymentLinkRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/resend-payment-link", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/resend-payment-link", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResendPaymentLinkResponse
            schema = ResendPaymentLinkResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for resendPaymentLink")
                print(e)

        return response
    
    async def cancelPaymentLink(self, body="", request_headers:Dict={}):
        """Deactivate and cancel a payment link.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.cancelPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CancelOrResendPaymentLinkRequest
        schema = CancelOrResendPaymentLinkRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cancel-payment-link", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cancel-payment-link", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CancelPaymentLinkResponse
            schema = CancelPaymentLinkResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelPaymentLink")
                print(e)

        return response
    
    async def getPaymentModeSequencing(self, business_unit=None, device=None, request_headers:Dict={}):
        """get details for the given payment modes and its sequencingfor merchant
        :param business_unit :  : type string
        :param device :  : type string
        """
        payload = {}
        
        if business_unit is not None:
            payload["business_unit"] = business_unit
        if device is not None:
            payload["device"] = device

        # Parameter validation
        schema = PaymentValidator.getPaymentModeSequencing()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment_modes/sequencing", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"business_unit","in":"query","required":true,"schema":{"type":"string"}},{"name":"device","in":"query","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"business_unit","in":"query","required":true,"schema":{"type":"string"}},{"name":"device","in":"query","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", business_unit=business_unit, device=device)
        query_string = await create_query_string(business_unit=business_unit, device=device)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment_modes/sequencing", business_unit=business_unit, device=device), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentModeResponse
            schema = PaymentModeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentModeSequencing")
                print(e)

        return response
    
    async def patchPaymentModeSequencing(self, body="", request_headers:Dict={}):
        """Update sequencing of payment modes for the merchant
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.patchPaymentModeSequencing()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformPaymentModeRequest
        schema = PlatformPaymentModeRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment_modes/sequencing", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment_modes/sequencing", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AggregatorConfigResponse
            schema = AggregatorConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for patchPaymentModeSequencing")
                print(e)

        return response
    
    async def getPaymentModeControlRoutes(self, mode=None, request_headers:Dict={}):
        """Get details of offline / advance payment mode like for cod  offline payment mode get user level cod limit, order level cod limit, cod charge.
        :param mode : offline / advance  modes to get the payment modes : type string
        """
        payload = {}
        
        if mode is not None:
            payload["mode"] = mode

        # Parameter validation
        schema = PaymentValidator.getPaymentModeControlRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance  modes to get the payment modes","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance  modes to get the payment modes","schema":{"type":"string"},"required":true}]}""", serverType="platform", mode=mode)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}", mode=mode), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformOfflineAdvanceResponse
            schema = PlatformOfflineAdvanceResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentModeControlRoutes")
                print(e)

        return response
    
    async def setMerchantModeControlRoutes(self, mode=None, body="", request_headers:Dict={}):
        """Update details of offline / advance payment mode like for cod  offline payment mode get user level cod limit, order level cod limit, cod charge.
        :param mode : offline / advance  modes to get the payment modes : type string
        """
        payload = {}
        
        if mode is not None:
            payload["mode"] = mode

        # Parameter validation
        schema = PaymentValidator.setMerchantModeControlRoutes()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformOfflineAdvanceRequest
        schema = PlatformOfflineAdvanceRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance  modes to get the payment modes","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance  modes to get the payment modes","schema":{"type":"string"},"required":true}]}""", serverType="platform", mode=mode)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}", mode=mode), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformOfflineAdvanceResponse
            schema = PlatformOfflineAdvanceResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setMerchantModeControlRoutes")
                print(e)

        return response
    
    async def getPaymentModeCustomConfig(self, mode=None, request_headers:Dict={}):
        """Merchants to fetch detailed information regarding advance payment custom configurations tailored to their specific business needs. merchants can access settings such as customer restrictions, available payment modes for both pre-order and post-order transactions
        :param mode : offline / advance  mode : type string
        """
        payload = {}
        
        if mode is not None:
            payload["mode"] = mode

        # Parameter validation
        schema = PaymentValidator.getPaymentModeCustomConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}/custom-config", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance  mode","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance  mode","schema":{"type":"string"},"required":true}]}""", serverType="platform", mode=mode)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}/custom-config", mode=mode), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentCustomConfigResponseSchema
            schema = PaymentCustomConfigResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentModeCustomConfig")
                print(e)

        return response
    
    async def setPaymentModeCustomConfig(self, mode=None, body="", request_headers:Dict={}):
        """Allows merchants to modify specific details of advance payment custom configurations tailored to their business requirements. By providing the company ID, application ID, and payment mode, merchants can update settings such as minimum order value, customer restrictions, and available payment modes for both pre-order and post-order transactions
        :param mode : offline / advance payment mode : type string
        """
        payload = {}
        
        if mode is not None:
            payload["mode"] = mode

        # Parameter validation
        schema = PaymentValidator.setPaymentModeCustomConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentCustomConfigRequestSchema
        schema = PaymentCustomConfigRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}/custom-config", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance payment mode","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance payment mode","schema":{"type":"string"},"required":true}]}""", serverType="platform", mode=mode)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}/custom-config", mode=mode), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentCustomConfigResponseSchema
            schema = PaymentCustomConfigResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setPaymentModeCustomConfig")
                print(e)

        return response
    
    async def getPaymentCodeOption(self, request_headers:Dict={}):
        """Enables users to retrieve options for payment codes.users can access information such as payment method names, networks, and associated codes, facilitating seamless integration and management of payment modes
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getPaymentCodeOption()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/codes", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/codes", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetPaymentCodeResponse
            schema = GetPaymentCodeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentCodeOption")
                print(e)

        return response
    
    async def getPaymentSession(self, gid=None, line_item=None, request_headers:Dict={}):
        """Allows users to fetch the payment session details associated with a given order ID or transaction ID
        :param gid : transaction id : type string
        :param line-item : A boolean flag to include detailed cart and line item information in the response. When set to true, the response will contain comprehensive details about the cart, including each line item's product or service descriptions, quantities, unit prices, applicable taxes, discounts, total cart value, and total quantity. This provides a clear breakdown of charges to the customer, helping to understand the total amount billed in a more granular way. : type boolean
        """
        payload = {}
        
        if gid is not None:
            payload["gid"] = gid
        if line_item is not None:
            payload["line_item"] = line_item

        # Parameter validation
        schema = PaymentValidator.getPaymentSession()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/session/{gid}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"gid","in":"path","description":"transaction id","schema":{"type":"string"},"required":true}],"optional":[{"name":"line-item","in":"query","description":"A boolean flag to include detailed cart and line item information in the response. When set to true, the response will contain comprehensive details about the cart, including each line item's product or service descriptions, quantities, unit prices, applicable taxes, discounts, total cart value, and total quantity. This provides a clear breakdown of charges to the customer, helping to understand the total amount billed in a more granular way.","schema":{"type":"boolean"}}],"query":[{"name":"line-item","in":"query","description":"A boolean flag to include detailed cart and line item information in the response. When set to true, the response will contain comprehensive details about the cart, including each line item's product or service descriptions, quantities, unit prices, applicable taxes, discounts, total cart value, and total quantity. This provides a clear breakdown of charges to the customer, helping to understand the total amount billed in a more granular way.","schema":{"type":"boolean"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"gid","in":"path","description":"transaction id","schema":{"type":"string"},"required":true}]}""", serverType="platform", gid=gid, line_item=line_item)
        query_string = await create_query_string(line_item=line_item)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/session/{gid}", gid=gid, line_item=line_item), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetPaymentSessionResponse
            schema = GetPaymentSessionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentSession")
                print(e)

        return response
    
    async def updatePaymentSession(self, gid=None, body="", request_headers:Dict={}):
        """Update the details of a payment session associated with a given order ID or transaction ID.
        :param gid : global identifier of the entity (e.g. order, cart etc.) against which payment_session was initiated. This is generated by Fynd payments platform and is unique. : type string
        """
        payload = {}
        
        if gid is not None:
            payload["gid"] = gid

        # Parameter validation
        schema = PaymentValidator.updatePaymentSession()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentSessionRequestSerializer
        schema = PaymentSessionRequestSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/session/{gid}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"gid","in":"path","description":"global identifier of the entity (e.g. order, cart etc.) against which payment_session was initiated. This is generated by Fynd payments platform and is unique.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"gid","in":"path","description":"global identifier of the entity (e.g. order, cart etc.) against which payment_session was initiated. This is generated by Fynd payments platform and is unique.","schema":{"type":"string"},"required":true}]}""", serverType="platform", gid=gid)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/session/{gid}", gid=gid), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentSessionResponseSerializer
            schema = PaymentSessionResponseSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePaymentSession")
                print(e)

        return response
    
    async def updateRefundSession(self, gid=None, request_id=None, body="", request_headers:Dict={}):
        """Allows users to update the details of a refund session associated with a specific global identifier (GID) and request ID.
        :param gid : global identifier of the entity (e.g. order, cart etc.) against which payment_session was initiated. This is generated by Fynd payments platform and is unique. : type string
        :param request_id : A unique id that was used to initiate a refund session. This is generated by Fynd platform and is usually shipment_id. : type string
        """
        payload = {}
        
        if gid is not None:
            payload["gid"] = gid
        if request_id is not None:
            payload["request_id"] = request_id

        # Parameter validation
        schema = PaymentValidator.updateRefundSession()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RefundSessionRequestSerializer
        schema = RefundSessionRequestSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/{gid}/refund/session/{request_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"gid","in":"path","description":"global identifier of the entity (e.g. order, cart etc.) against which payment_session was initiated. This is generated by Fynd payments platform and is unique.","schema":{"type":"string"},"required":true},{"name":"request_id","in":"path","description":"A unique id that was used to initiate a refund session. This is generated by Fynd platform and is usually shipment_id.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"gid","in":"path","description":"global identifier of the entity (e.g. order, cart etc.) against which payment_session was initiated. This is generated by Fynd payments platform and is unique.","schema":{"type":"string"},"required":true},{"name":"request_id","in":"path","description":"A unique id that was used to initiate a refund session. This is generated by Fynd platform and is usually shipment_id.","schema":{"type":"string"},"required":true}]}""", serverType="platform", gid=gid, request_id=request_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/{gid}/refund/session/{request_id}", gid=gid, request_id=request_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundSessionResponseSerializer
            schema = RefundSessionResponseSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateRefundSession")
                print(e)

        return response
    
    async def getMerchantPaymentOption(self, payment_option_type=None, request_headers:Dict={}):
        """Retrieve available payment gateways and offline payment mode details for a merchant by providing company ID and application ID, returning a list of active payment gateways and their configurations, including online and offline options.
        :param payment_option_type : Payment Option Type, Expected value - advance (Optional) : type string
        """
        payload = {}
        
        if payment_option_type is not None:
            payload["payment_option_type"] = payment_option_type

        # Parameter validation
        schema = PaymentValidator.getMerchantPaymentOption()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[{"name":"payment_option_type","in":"query","description":"Payment Option Type, Expected value - advance (Optional)","schema":{"type":"string"}}],"query":[{"name":"payment_option_type","in":"query","description":"Payment Option Type, Expected value - advance (Optional)","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", payment_option_type=payment_option_type)
        query_string = await create_query_string(payment_option_type=payment_option_type)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration", payment_option_type=payment_option_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformOnlineOfflinePaymentResponse
            schema = PlatformOnlineOfflinePaymentResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchantPaymentOption")
                print(e)

        return response
    
    async def patchMerchantPaymentOption(self, body="", request_headers:Dict={}):
        """Updated online/offline payment as active/inactive like disable offline payment mode will disable offline payment modes on checkout page on merchant's website
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.patchMerchantPaymentOption()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MerchantPaymentModeRequest
        schema = MerchantPaymentModeRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PatchPlatformOnlineOfflinePaymentResponse
            schema = PatchPlatformOnlineOfflinePaymentResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for patchMerchantPaymentOption")
                print(e)

        return response
    
    async def getDevices(self, request_headers:Dict={}):
        """Get all business units and it's devices.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getDevices()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/all-devices", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/all-devices", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetDeviceResponse
            schema = GetDeviceResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDevices")
                print(e)

        return response
    
    async def getMerchantAggregatorPaymentModeDetails(self, aggregator_id=None, business_unit=None, device=None, request_headers:Dict={}):
        """swagger not found. so operationId not found
        :param aggregator_id : Aggregators Id : type integer
        :param business_unit :  : type string
        :param device :  : type string
        """
        payload = {}
        
        if aggregator_id is not None:
            payload["aggregator_id"] = aggregator_id
        if business_unit is not None:
            payload["business_unit"] = business_unit
        if device is not None:
            payload["device"] = device

        # Parameter validation
        schema = PaymentValidator.getMerchantAggregatorPaymentModeDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true},{"name":"business_unit","in":"query","required":true,"schema":{"type":"string"}},{"name":"device","in":"query","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"business_unit","in":"query","required":true,"schema":{"type":"string"}},{"name":"device","in":"query","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", aggregator_id=aggregator_id, business_unit=business_unit, device=device)
        query_string = await create_query_string(business_unit=business_unit, device=device)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}", aggregator_id=aggregator_id, business_unit=business_unit, device=device), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AggregatorPlatformPaymentModeResponse
            schema = AggregatorPlatformPaymentModeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchantAggregatorPaymentModeDetails")
                print(e)

        return response
    
    async def patchMerchantAggregatorPaymentModeDetails(self, aggregator_id=None, body="", request_headers:Dict={}):
        """update payment gateway and it's payment mode and it's sub payment mode details like for razorpay update active/inactive payment modes.
        :param aggregator_id : Aggregators Id : type integer
        """
        payload = {}
        
        if aggregator_id is not None:
            payload["aggregator_id"] = aggregator_id

        # Parameter validation
        schema = PaymentValidator.patchMerchantAggregatorPaymentModeDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformPaymentModeRequest
        schema = PlatformPaymentModeRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", aggregator_id=aggregator_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}", aggregator_id=aggregator_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformPaymentModeResponse
            schema = PlatformPaymentModeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for patchMerchantAggregatorPaymentModeDetails")
                print(e)

        return response
    
    async def getPGConfigAggregators(self, request_headers:Dict={}):
        """Get payment gateway and it's payment mode and it's sub payment mode details like for razorpay update active/inactive payment modes.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getPGConfigAggregators()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration/aggregator", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration/aggregator", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AggregatorConfigResponse
            schema = AggregatorConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPGConfigAggregators")
                print(e)

        return response
    
    async def getAggregatorCredentialHistory(self, aggregator=None, config_type=None, request_headers:Dict={}):
        """Get merchant refund priority.
        :param aggregator : The aggregator for which credentials are requested : type string
        :param config_type : The configuration type for which credentials are requested : type string
        """
        payload = {}
        
        if aggregator is not None:
            payload["aggregator"] = aggregator
        if config_type is not None:
            payload["config_type"] = config_type

        # Parameter validation
        schema = PaymentValidator.getAggregatorCredentialHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration/aggregator/credential/history", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator","in":"query","required":true,"schema":{"type":"string"},"description":"The aggregator for which credentials are requested"},{"name":"config_type","in":"query","required":true,"schema":{"type":"string"},"description":"The configuration type for which credentials are requested"}],"optional":[],"query":[{"name":"aggregator","in":"query","required":true,"schema":{"type":"string"},"description":"The aggregator for which credentials are requested"},{"name":"config_type","in":"query","required":true,"schema":{"type":"string"},"description":"The configuration type for which credentials are requested"}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", aggregator=aggregator, config_type=config_type)
        query_string = await create_query_string(aggregator=aggregator, config_type=config_type)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration/aggregator/credential/history", aggregator=aggregator, config_type=config_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AggregatorHistoryResponse
            schema = AggregatorHistoryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAggregatorCredentialHistory")
                print(e)

        return response
    
    async def getAggregatorCredential(self, aggregator=None, config_type=None, request_headers:Dict={}):
        """API to get merchant refund priority
        :param aggregator : The aggregator for which credentials are requested : type string
        :param config_type : The configuration type for which credentials are requested : type string
        """
        payload = {}
        
        if aggregator is not None:
            payload["aggregator"] = aggregator
        if config_type is not None:
            payload["config_type"] = config_type

        # Parameter validation
        schema = PaymentValidator.getAggregatorCredential()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration/aggregator/credential", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator","in":"query","required":true,"schema":{"type":"string"},"description":"The aggregator for which credentials are requested"},{"name":"config_type","in":"query","required":true,"schema":{"type":"string"},"description":"The configuration type for which credentials are requested"}],"optional":[],"query":[{"name":"aggregator","in":"query","required":true,"schema":{"type":"string"},"description":"The aggregator for which credentials are requested"},{"name":"config_type","in":"query","required":true,"schema":{"type":"string"},"description":"The configuration type for which credentials are requested"}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", aggregator=aggregator, config_type=config_type)
        query_string = await create_query_string(aggregator=aggregator, config_type=config_type)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration/aggregator/credential", aggregator=aggregator, config_type=config_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AggregatorCredentialResponse
            schema = AggregatorCredentialResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAggregatorCredential")
                print(e)

        return response
    
    async def updateAggregatorCredential(self, body="", request_headers:Dict={}):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.updateAggregatorCredential()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AggregatorCredentialRequest
        schema = AggregatorCredentialRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration/aggregator/credential", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration/aggregator/credential", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PatchAggregatorCredentialResponse
            schema = PatchAggregatorCredentialResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAggregatorCredential")
                print(e)

        return response
    
    async def getMerchantRefundPriority(self, config_type=None, business_unit=None, request_headers:Dict={}):
        """Retrieve merchant refund priority configurations, returning the status of the update and the refund sources priority with their descriptions and priorities.
        :param config_type : configuration for merchant or customer : type string
        :param business_unit : Business unit storefront or pos : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        if business_unit is not None:
            payload["business_unit"] = business_unit

        # Parameter validation
        schema = PaymentValidator.getMerchantRefundPriority()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}/{business_unit}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"required":true},{"name":"business_unit","in":"path","description":"Business unit storefront or pos","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"required":true},{"name":"business_unit","in":"path","description":"Business unit storefront or pos","schema":{"type":"string"},"required":true}]}""", serverType="platform", config_type=config_type, business_unit=business_unit)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}/{business_unit}", config_type=config_type, business_unit=business_unit), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundPriorityResponseSerializer
            schema = RefundPriorityResponseSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchantRefundPriority")
                print(e)

        return response
    
    async def createMerchantRefundPriority(self, config_type=None, business_unit=None, body="", request_headers:Dict={}):
        """Create merchant refund priority configurations, with the provided refund sources priority details, and return the status of the operation.
        :param config_type : configuration for merchant or customer : type string
        :param business_unit : Business unit storefront or pos : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        if business_unit is not None:
            payload["business_unit"] = business_unit

        # Parameter validation
        schema = PaymentValidator.createMerchantRefundPriority()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RefundPriorityRequestSerializer
        schema = RefundPriorityRequestSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}/{business_unit}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"required":true},{"name":"business_unit","in":"path","description":"Business unit storefront or pos","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"required":true},{"name":"business_unit","in":"path","description":"Business unit storefront or pos","schema":{"type":"string"},"required":true}]}""", serverType="platform", config_type=config_type, business_unit=business_unit)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}/{business_unit}", config_type=config_type, business_unit=business_unit), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundPriorityResponseSerializer
            schema = RefundPriorityResponseSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createMerchantRefundPriority")
                print(e)

        return response
    
    async def updateMerchantRefundPriority(self, config_type=None, business_unit=None, body="", request_headers:Dict={}):
        """Update merchant refund priority configurations, with the provided refund sources priority details, and return the status of the operation.
        :param config_type : configuration for merchant or customer : type string
        :param business_unit : Business unit storefront or pos : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type
        if business_unit is not None:
            payload["business_unit"] = business_unit

        # Parameter validation
        schema = PaymentValidator.updateMerchantRefundPriority()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RefundPriorityRequestSerializer
        schema = RefundPriorityRequestSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}/{business_unit}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"required":true},{"name":"business_unit","in":"path","description":"Business unit storefront or pos","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"required":true},{"name":"business_unit","in":"path","description":"Business unit storefront or pos","schema":{"type":"string"},"required":true}]}""", serverType="platform", config_type=config_type, business_unit=business_unit)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}/{business_unit}", config_type=config_type, business_unit=business_unit), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundPriorityResponseSerializer
            schema = RefundPriorityResponseSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateMerchantRefundPriority")
                print(e)

        return response
    
    async def createPaymentOrder(self, body="", request_headers:Dict={}):
        """Create an order and payment on the aggregator side
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.createPaymentOrder()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentOrderRequest
        schema = PaymentOrderRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment-orders", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment-orders", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentOrderResponse
            schema = PaymentOrderResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPaymentOrder")
                print(e)

        return response
    
    async def copyConfigPaymentModes(self, body="", request_headers:Dict={}):
        """Copy aggregator config like Wallet, NB, paylater from one device of an aggregator like razorpay to another device.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.copyConfigPaymentModes()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformPaymentModeCopyConfigRequest
        schema = PlatformPaymentModeCopyConfigRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment_modes/sequencing/copy-config", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment_modes/sequencing/copy-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AggregatorConfigResponse
            schema = AggregatorConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for copyConfigPaymentModes")
                print(e)

        return response
    
    async def copyConfigAggPaymentModes(self, aggregator_id=None, body="", request_headers:Dict={}):
        """Copy aggregator config like Wallet, NB, paylater from one device of an aggregator like razorpay to another device.
        :param aggregator_id : Aggregator Id : type string
        """
        payload = {}
        
        if aggregator_id is not None:
            payload["aggregator_id"] = aggregator_id

        # Parameter validation
        schema = PaymentValidator.copyConfigAggPaymentModes()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformPaymentModeCopyConfigRequest
        schema = PlatformPaymentModeCopyConfigRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}/copy-config", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregator Id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregator Id","schema":{"type":"string"},"required":true}]}""", serverType="platform", aggregator_id=aggregator_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}/copy-config", aggregator_id=aggregator_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AggregatorConfigResponse
            schema = AggregatorConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for copyConfigAggPaymentModes")
                print(e)

        return response
    
    async def getMerchantAggregatorAppVersion(self, aggregator_id=None, business_unit=None, device=None, payment_mode_id=None, sub_payment_mode=None, request_headers:Dict={}):
        """Get app version required for Payment Mode or sub payment mode for an Aggregator.if merchant required any PG payment mode after certain version for mobile app.
        :param aggregator_id : Aggregators Id : type integer
        :param business_unit :  : type string
        :param device :  : type string
        :param payment_mode_id :  : type integer
        :param sub_payment_mode :  : type string
        """
        payload = {}
        
        if aggregator_id is not None:
            payload["aggregator_id"] = aggregator_id
        if business_unit is not None:
            payload["business_unit"] = business_unit
        if device is not None:
            payload["device"] = device
        if payment_mode_id is not None:
            payload["payment_mode_id"] = payment_mode_id
        if sub_payment_mode is not None:
            payload["sub_payment_mode"] = sub_payment_mode

        # Parameter validation
        schema = PaymentValidator.getMerchantAggregatorAppVersion()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}/version", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true},{"name":"business_unit","in":"query","required":true,"schema":{"type":"string"}},{"name":"device","in":"query","required":true,"schema":{"type":"string"}}],"optional":[{"name":"payment_mode_id","in":"query","schema":{"type":"integer"}},{"name":"sub_payment_mode","in":"query","schema":{"type":"string"}}],"query":[{"name":"business_unit","in":"query","required":true,"schema":{"type":"string"}},{"name":"device","in":"query","required":true,"schema":{"type":"string"}},{"name":"payment_mode_id","in":"query","schema":{"type":"integer"}},{"name":"sub_payment_mode","in":"query","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", aggregator_id=aggregator_id, business_unit=business_unit, device=device, payment_mode_id=payment_mode_id, sub_payment_mode=sub_payment_mode)
        query_string = await create_query_string(business_unit=business_unit, device=device, payment_mode_id=payment_mode_id, sub_payment_mode=sub_payment_mode)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}/version", aggregator_id=aggregator_id, business_unit=business_unit, device=device, payment_mode_id=payment_mode_id, sub_payment_mode=sub_payment_mode), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AggregatorVersionResponse
            schema = AggregatorVersionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchantAggregatorAppVersion")
                print(e)

        return response
    
    async def patchMerchantPaymentOptionVersion(self, aggregator_id=None, body="", request_headers:Dict={}):
        """Update app version required for Payment Mode or sub payment mode for an Aggregator.if merchant required any PG payment mode after certain version for mobile app.
        :param aggregator_id : Aggregators Id : type integer
        """
        payload = {}
        
        if aggregator_id is not None:
            payload["aggregator_id"] = aggregator_id

        # Parameter validation
        schema = PaymentValidator.patchMerchantPaymentOptionVersion()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AggregatorControlRequest
        schema = AggregatorControlRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}/version", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", aggregator_id=aggregator_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}/version", aggregator_id=aggregator_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AggregatorConfigResponse
            schema = AggregatorConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for patchMerchantPaymentOptionVersion")
                print(e)

        return response
    
    async def addRefundBankAccount(self, body="", request_headers:Dict={}):
        """save bank details for returned/cancelled order to refund amount in his account.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.addRefundBankAccount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddBeneficiaryDetailsOTPRequest
        schema = AddBeneficiaryDetailsOTPRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account_create", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account_create", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundAccountResponse
            schema = RefundAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addRefundBankAccount")
                print(e)

        return response
    
    async def deleteBeneficiaryDetails(self, body="", request_headers:Dict={}):
        """Delete the saved beneficiary details provided beneficiary Id.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.deleteBeneficiaryDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DeleteBeneficiaryRequest
        schema = DeleteBeneficiaryRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account_create", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account_create", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteRefundAccountResponse
            schema = DeleteRefundAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteBeneficiaryDetails")
                print(e)

        return response
    
    async def setRefundOptionforShipment(self, body="", request_headers:Dict={}):
        """Save refund source against shipment and order
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.setRefundOptionforShipment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ShipmentRefundRequest
        schema = ShipmentRefundRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/refundoptions", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/refundoptions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentRefundResponse
            schema = ShipmentRefundResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setRefundOptionforShipment")
                print(e)

        return response
    
    async def getSelectedRefundOption(self, shipment_id=None, order_id=None, request_headers:Dict={}):
        """get the selected refund options for shipment id
        :param shipment_id : shipment Id : type string
        :param order_id : Order Id : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if order_id is not None:
            payload["order_id"] = order_id

        # Parameter validation
        schema = PaymentValidator.getSelectedRefundOption()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/selected_refund_options", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"shipment_id","in":"query","description":"shipment Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"shipment_id","in":"query","description":"shipment Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", shipment_id=shipment_id, order_id=order_id)
        query_string = await create_query_string(shipment_id=shipment_id, order_id=order_id)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/selected_refund_options", shipment_id=shipment_id, order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SelectedRefundOptionResponse
            schema = SelectedRefundOptionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSelectedRefundOption")
                print(e)

        return response
    
    async def getUserBeneficiariesDetailV2(self, order_id=None, shipment_id=None, mop=None, request_headers:Dict={}):
        """get the details of all active beneficiary added by a user for refund.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        :param shipment_id : A unique number used for identifying and tracking your orders. : type string
        :param mop : Mode of payment for which beneficiary data required : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if mop is not None:
            payload["mop"] = mop

        # Parameter validation
        schema = PaymentValidator.getUserBeneficiariesDetailV2()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/user/beneficiary", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","schema":{"type":"string"}},{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"shipment_id","schema":{"type":"string"}},{"in":"query","description":"Mode of payment for which beneficiary data required","name":"mop","schema":{"type":"string"}}],"query":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","schema":{"type":"string"}},{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"shipment_id","schema":{"type":"string"}},{"in":"query","description":"Mode of payment for which beneficiary data required","name":"mop","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", order_id=order_id, shipment_id=shipment_id, mop=mop)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id, mop=mop)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/user/beneficiary", order_id=order_id, shipment_id=shipment_id, mop=mop), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderBeneficiaryResponseSchemaV2
            schema = OrderBeneficiaryResponseSchemaV2()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserBeneficiariesDetailV2")
                print(e)

        return response
    
    async def validateBeneficiaryAddress(self, body="", request_headers:Dict={}):
        """Validate UPI ID and IFSC code
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.validateBeneficiaryAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateValidateAddressRequest
        schema = ValidateValidateAddressRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/validate/beneficiary-address", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/validate/beneficiary-address", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ValidateValidateAddressResponse
            schema = ValidateValidateAddressResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateBeneficiaryAddress")
                print(e)

        return response
    
    async def updateDefaultBeneficiary(self, body="", request_headers:Dict={}):
        """set a default beneficiary for getting a refund.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.updateDefaultBeneficiary()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SetDefaultBeneficiaryRequest
        schema = SetDefaultBeneficiaryRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/beneficiary/default", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/beneficiary/default", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SetDefaultBeneficiaryResponse
            schema = SetDefaultBeneficiaryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateDefaultBeneficiary")
                print(e)

        return response
    
    async def getPennyDropValidation(self, request_headers:Dict={}):
        """get pennydrop validation for bank account
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getPennyDropValidation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pennydrop/validation", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pennydrop/validation", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PennyDropValidationResponse
            schema = PennyDropValidationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPennyDropValidation")
                print(e)

        return response
    
    async def updatePennyDropValidation(self, body="", request_headers:Dict={}):
        """update penny drop validation for application ID
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.updatePennyDropValidation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdatePennyDropValidationRequest
        schema = UpdatePennyDropValidationRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pennydrop/validation", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pennydrop/validation", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PennyDropValidationResponse
            schema = PennyDropValidationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePennyDropValidation")
                print(e)

        return response
    
    async def getShipmentBeneficiary(self, shipment_id=None, request_headers:Dict={}):
        """get beneficiary details
        :param shipment_id : Shipment id : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = PaymentValidator.getShipmentBeneficiary()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refunds/beneficiary-details/{shipment_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"shipment_id","in":"path","description":"Shipment id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"shipment_id","in":"path","description":"Shipment id","schema":{"type":"string"},"required":true}]}""", serverType="platform", shipment_id=shipment_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refunds/beneficiary-details/{shipment_id}", shipment_id=shipment_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentBeneficiaryDetailsResponse
            schema = ShipmentBeneficiaryDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentBeneficiary")
                print(e)

        return response
    