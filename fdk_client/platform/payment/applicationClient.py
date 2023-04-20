

"""Payment Platform Client."""

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
        
        

        from .models import PaymentGatewayConfigResponse
        schema = PaymentGatewayConfigResponse()
        try:
            schema.dump(schema.load(response))
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
        
        

        from .models import PaymentGatewayToBeReviewed
        schema = PaymentGatewayToBeReviewed()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for saveBrandPaymentGatewayConfig")
            print(e)
            
        

        return response
    
    async def updateBrandPaymentGatewayConfig(self, body=""):
        """Save Config Secret For Brand Payment Gateway
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.updateBrandPaymentGatewayConfig()
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import PaymentGatewayToBeReviewed
        schema = PaymentGatewayToBeReviewed()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateBrandPaymentGatewayConfig")
            print(e)
            
        

        return response
    
    async def getPaymentModeRoutes(self, refresh=None, request_type=None):
        """Use this API to get Get All Valid Payment Options for making payment
        :param refresh :  : type boolean
        :param request_type :  : type string
        """
        payload = {}
        
        if refresh:
            payload["refresh"] = refresh
        
        if request_type:
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
        
        

        from .models import PaymentOptionsResponse
        schema = PaymentOptionsResponse()
        try:
            schema.dump(schema.load(response))
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
        
        if order_id:
            payload["order_id"] = order_id
        
        if request_hash:
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
        
        

        from .models import RefundAccountResponse
        schema = RefundAccountResponse()
        try:
            schema.dump(schema.load(response))
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
        
        

        from .models import RefundAccountResponse
        schema = RefundAccountResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for addRefundBankAccountUsingOTP")
            print(e)
            
        

        return response
    
    async def getUserOrderBeneficiaries(self, order_id=None):
        """Get all active  beneficiary details added by the user for refund
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id:
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
        
        

        from .models import OrderBeneficiaryResponse
        schema = OrderBeneficiaryResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getUserOrderBeneficiaries")
            print(e)
            
        

        return response
    
    async def getUserBeneficiaries(self, order_id=None):
        """Get all active  beneficiary details added by the user for refund
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id:
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
        
        

        from .models import OrderBeneficiaryResponse
        schema = OrderBeneficiaryResponse()
        try:
            schema.dump(schema.load(response))
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
        
        

        from .models import PaymentConfirmationResponse
        schema = PaymentConfirmationResponse()
        try:
            schema.dump(schema.load(response))
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
        
        if merchant_user_id:
            payload["merchant_user_id"] = merchant_user_id
        
        if mobile_no:
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
        
        

        from .models import GetUserCODLimitResponse
        schema = GetUserCODLimitResponse()
        try:
            schema.dump(schema.load(response))
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
        
        

        from .models import SetCODOptionResponse
        schema = SetCODOptionResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for setUserCODlimitRoutes")
            print(e)
            
        

        return response
    
    async def edcAggregatorsAndModelList(self, ):
        """Use this API to get info of devices linked to a particular app.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.edcAggregatorsAndModelList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-aggregator-list", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-aggregator-list", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import EdcAggregatorAndModelListResponse
        schema = EdcAggregatorAndModelListResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for edcAggregatorsAndModelList")
            print(e)
            
        

        return response
    
    async def edcDeviceStats(self, ):
        """Use this API to get info of devices linked to a particular app.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.edcDeviceStats()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-stats", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-stats", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import EdcDeviceStatsResponse
        schema = EdcDeviceStatsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for edcDeviceStats")
            print(e)
            
        

        return response
    
    async def updateEdcDevice(self, terminal_unique_identifier=None, body=""):
        """Use this API to map new edc device to the terminal
        :param terminal_unique_identifier : Terminal unique identifier : type string
        """
        payload = {}
        
        if terminal_unique_identifier:
            payload["terminal_unique_identifier"] = terminal_unique_identifier
        

        # Parameter validation
        schema = PaymentValidator.updateEdcDevice()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EdcAddRequest
        schema = EdcAddRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}]}""", terminal_unique_identifier=terminal_unique_identifier)
        query_string = await create_query_string(terminal_unique_identifier=terminal_unique_identifier)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device", terminal_unique_identifier=terminal_unique_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import EdcDeviceAddResponse
        schema = EdcDeviceAddResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateEdcDevice")
            print(e)
            
        

        return response
    
    async def getEdcDevice(self, terminal_unique_identifier=None):
        """Use this API to get details of a single edc device
        :param terminal_unique_identifier : Terminal unique identifier : type string
        """
        payload = {}
        
        if terminal_unique_identifier:
            payload["terminal_unique_identifier"] = terminal_unique_identifier
        

        # Parameter validation
        schema = PaymentValidator.getEdcDevice()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}]}""", terminal_unique_identifier=terminal_unique_identifier)
        query_string = await create_query_string(terminal_unique_identifier=terminal_unique_identifier)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", terminal_unique_identifier=terminal_unique_identifier), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import EdcDeviceDetailsResponse
        schema = EdcDeviceDetailsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getEdcDevice")
            print(e)
            
        

        return response
    
    async def addEdcDevice(self, terminal_unique_identifier=None, body=""):
        """Use this API to Update store id and device tag of edc device
        :param terminal_unique_identifier : Terminal unique identifier : type string
        """
        payload = {}
        
        if terminal_unique_identifier:
            payload["terminal_unique_identifier"] = terminal_unique_identifier
        

        # Parameter validation
        schema = PaymentValidator.addEdcDevice()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EdcUpdateRequest
        schema = EdcUpdateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}]}""", terminal_unique_identifier=terminal_unique_identifier)
        query_string = await create_query_string(terminal_unique_identifier=terminal_unique_identifier)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", terminal_unique_identifier=terminal_unique_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import EdcDeviceUpdateResponse
        schema = EdcDeviceUpdateResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for addEdcDevice")
            print(e)
            
        

        return response
    
    async def edcDeviceList(self, page_no=None, page_size=None, is_active=None, store_id=None, device_tag=None):
        """Use this API to get all devices linked to a particular app.
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param is_active :  : type boolean
        :param store_id :  : type integer
        :param device_tag :  : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if is_active:
            payload["is_active"] = is_active
        
        if store_id:
            payload["store_id"] = store_id
        
        if device_tag:
            payload["device_tag"] = device_tag
        

        # Parameter validation
        schema = PaymentValidator.edcDeviceList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-list", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"store_id","required":false,"schema":{"type":"integer"}},{"in":"query","name":"device_tag","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"store_id","required":false,"schema":{"type":"integer"}},{"in":"query","name":"device_tag","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", page_no=page_no, page_size=page_size, is_active=is_active, store_id=store_id, device_tag=device_tag, )
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_active=is_active, store_id=store_id, device_tag=device_tag, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-list", page_no=page_no, page_size=page_size, is_active=is_active, store_id=store_id, device_tag=device_tag, ), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import EdcDeviceListResponse
        schema = EdcDeviceListResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for edcDeviceList")
            print(e)
            
        

        return response
    
    async def getPosPaymentModeRoutes(self, amount=None, cart_id=None, pincode=None, checkout_mode=None, refresh=None, card_reference=None, order_type=None, user_details=None):
        """Use this API to get Get All Valid Payment Options for making payment
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/pos", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":true,"schema":{"type":"string"}},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string"}}],"optional":[{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}}],"query":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":true,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details)
        query_string = await create_query_string(amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/pos", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import PaymentOptionsResponse
        schema = PaymentOptionsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getPosPaymentModeRoutes")
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/request", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/confirm/polling", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/confirm/polling", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import PaymentStatusUpdateResponse
        schema = PaymentStatusUpdateResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for checkAndUpdatePaymentStatus")
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/cancel", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/cancel", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
        
        

        from .models import ResendOrCancelPaymentResponse
        schema = ResendOrCancelPaymentResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for resendOrCancelPayment")
            print(e)
            
        

        return response
    
    async def getPaymentCodeOption(self, ):
        """Get all active List Payment Options Method Codes
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getPaymentCodeOption()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/codes", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/codes", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
        
        

        from .models import GetPaymentCodeResponse
        schema = GetPaymentCodeResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getPaymentCodeOption")
            print(e)
            
        

        return response
    

