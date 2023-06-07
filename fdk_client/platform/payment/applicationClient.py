

"""Payment Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import PaymentValidator

class Payment:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId

    
    async def getBrandPaymentGatewayConfig(self, ):
        """Get All Brand Payment Gateway Config Secret
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getBrandPaymentGatewayConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentGatewayConfigResponse
            schema = PaymentGatewayConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBrandPaymentGatewayConfig")
                print(e)

        

        return response
    
    async def saveBrandPaymentGatewayConfig(self, body=""):
        """Save Config Secret For Brand Payment Gateway
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.saveBrandPaymentGatewayConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentGatewayConfigRequest
        schema = PaymentGatewayConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentGatewayToBeReviewed
            schema = PaymentGatewayToBeReviewed()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for saveBrandPaymentGatewayConfig")
                print(e)

        

        return response
    
    async def getPaymentModeRoutes(self, refresh=None, request_type=None):
        """Use this API to get Get All Valid Payment Options for making payment
        :param refresh :  : type boolean
        :param request_type :  : type string
        """
        payload = {}
        
        if refresh is not None:
            payload["refresh"] = refresh
        
        if request_type is not None:
            payload["request_type"] = request_type
        

        # Parameter validation
        schema = PaymentValidator.getPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"refresh","in":"query","required":true,"schema":{"type":"boolean"}},{"name":"request_type","in":"query","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"refresh","in":"query","required":true,"schema":{"type":"boolean"}},{"name":"request_type","in":"query","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", refresh=refresh, request_type=request_type)
        query_string = await create_query_string(refresh=refresh, request_type=request_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options", refresh=refresh, request_type=request_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentOptionsResponse
            schema = PaymentOptionsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentModeRoutes")
                print(e)

        

        return response
    
    async def getBankAccountDetailsOpenAPI(self, order_id=None, request_hash=None):
        """Use this API to get saved bank details for returned/cancelled order using order id.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account", """{"required":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"request_hash","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"request_hash","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", order_id=order_id, request_hash=request_hash, )
        query_string = await create_query_string(order_id=order_id, request_hash=request_hash, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account", order_id=order_id, request_hash=request_hash, ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundAccountResponse
            schema = RefundAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBankAccountDetailsOpenAPI")
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundAccountResponse
            schema = RefundAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addRefundBankAccountUsingOTP")
                print(e)

        

        return response
    
    async def getUserOrderBeneficiaries(self, order_id=None):
        """Get all active  beneficiary details added by the user for refund
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = PaymentValidator.getUserOrderBeneficiaries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/order", """{"required":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", order_id=order_id, )
        query_string = await create_query_string(order_id=order_id, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/order", order_id=order_id, ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderBeneficiaryResponse
            schema = OrderBeneficiaryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserOrderBeneficiaries")
                print(e)

        

        return response
    
    async def getUserBeneficiaries(self, order_id=None):
        """Get all active  beneficiary details added by the user for refund
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = PaymentValidator.getUserBeneficiaries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/user", """{"required":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", order_id=order_id, )
        query_string = await create_query_string(order_id=order_id, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/user", order_id=order_id, ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderBeneficiaryResponse
            schema = OrderBeneficiaryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserBeneficiaries")
                print(e)

        

        return response
    
    async def confirmPayment(self, body=""):
        """Use this API to confirm payment after payment gateway accepted payment.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.confirmPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentConfirmationRequest
        schema = PaymentConfirmationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/confirm", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/confirm", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentConfirmationResponse
            schema = PaymentConfirmationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for confirmPayment")
                print(e)

        

        return response
    
    async def getUserCODlimitRoutes(self, merchant_user_id=None, mobile_no=None):
        """Use this API to get user cod limit and reamining limit for the payment
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/user-cod", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"merchant_user_id","in":"query","required":true,"schema":{"type":"string"}},{"name":"mobile_no","in":"query","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"merchant_user_id","in":"query","required":true,"schema":{"type":"string"}},{"name":"mobile_no","in":"query","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", merchant_user_id=merchant_user_id, mobile_no=mobile_no)
        query_string = await create_query_string(merchant_user_id=merchant_user_id, mobile_no=mobile_no)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/user-cod", merchant_user_id=merchant_user_id, mobile_no=mobile_no), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetUserCODLimitResponse
            schema = GetUserCODLimitResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserCODlimitRoutes")
                print(e)

        

        return response
    
    async def setUserCODlimitRoutes(self, body=""):
        """Use this API to set cod option as true or false for the payment
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.setUserCODlimitRoutes()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SetCODForUserRequest
        schema = SetCODForUserRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/user-cod", """{"required":[{"name":"company_id","in":"path","description":"Company ID","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/user-cod", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SetCODOptionResponse
            schema = SetCODOptionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setUserCODlimitRoutes")
                print(e)

        

        return response
    
    async def oauthGetUrl(self, aggregator=None, success_redirect_url=None, failure_redirect_url=None):
        """Use this API to Get the url to call for oauth.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/onboard/{aggregator}/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator","in":"path","description":"aggregator","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"success_redirect_url","schema":{"type":"string","description":"This is the url which will come back to after success authorization complete"}},{"in":"query","name":"failure_redirect_url","schema":{"type":"string","description":"This is the url which will come back to after failure authorization"}}],"query":[{"in":"query","name":"success_redirect_url","schema":{"type":"string","description":"This is the url which will come back to after success authorization complete"}},{"in":"query","name":"failure_redirect_url","schema":{"type":"string","description":"This is the url which will come back to after failure authorization"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator","in":"path","description":"aggregator","schema":{"type":"string"},"required":true}]}""", aggregator=aggregator, success_redirect_url=success_redirect_url, failure_redirect_url=failure_redirect_url)
        query_string = await create_query_string(aggregator=aggregator, success_redirect_url=success_redirect_url, failure_redirect_url=failure_redirect_url)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/onboard/{aggregator}/", aggregator=aggregator, success_redirect_url=success_redirect_url, failure_redirect_url=failure_redirect_url), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetOauthUrlResponse
            schema = GetOauthUrlResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for oauthGetUrl")
                print(e)

        

        return response
    
    async def revokeOauthToken(self, aggregator=None):
        """Use this API to Revoke oauth for razorpay partnership
        :param aggregator : aggregator_slug : type string
        """
        payload = {}
        
        if aggregator is not None:
            payload["aggregator"] = aggregator
        

        # Parameter validation
        schema = PaymentValidator.revokeOauthToken()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/revoke/{aggregator}/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator","in":"path","description":"aggregator_slug","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator","in":"path","description":"aggregator_slug","schema":{"type":"string"},"required":true}]}""", aggregator=aggregator)
        query_string = await create_query_string(aggregator=aggregator)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/revoke/{aggregator}/", aggregator=aggregator), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import RevokeOAuthToken
            schema = RevokeOAuthToken()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for revokeOauthToken")
                print(e)

        

        return response
    

