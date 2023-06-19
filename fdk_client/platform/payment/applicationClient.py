

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

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentGatewayToBeReviewed
            schema = PaymentGatewayToBeReviewed()
            try:
                schema.load(response["json"])
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
    
    async def addBeneficiaryDetails(self, body=""):
        """Use this API to save bank details for returned/cancelled order to refund amount in his account.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.addBeneficiaryDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddBeneficiaryDetailsRequest
        schema = AddBeneficiaryDetailsRequest()
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
                print("Response Validation failed for addBeneficiaryDetails")
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
    

