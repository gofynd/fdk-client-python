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
        """Get All Brand Payment Gateway Config Secret
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[{"name":"aggregator","in":"query","description":"aggregator slug","schema":{"type":"string"},"required":false},{"name":"config_type","in":"query","required":false,"schema":{"type":"string","enum":["self","partner","fynd"]}}],"query":[{"name":"aggregator","in":"query","description":"aggregator slug","schema":{"type":"string"},"required":false},{"name":"config_type","in":"query","required":false,"schema":{"type":"string","enum":["self","partner","fynd"]}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", aggregator=aggregator, config_type=config_type)
        query_string = await create_query_string(aggregator=aggregator, config_type=config_type)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", aggregator=aggregator, config_type=config_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
    
    async def getPaymentModeRoutes(self, refresh=None, request_type=None, order_id=None, shipment_id=None, request_headers:Dict={}):
        """Use this API to get Get All Valid Payment Options for making payment
        :param refresh :  : type boolean
        :param request_type :  : type string
        :param order_id :  : type string
        :param shipment_id :  : type string
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

        # Parameter validation
        schema = PaymentValidator.getPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"refresh","in":"query","required":true,"schema":{"type":"boolean"}},{"name":"request_type","in":"query","required":true,"schema":{"type":"string"}}],"optional":[{"name":"order_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"shipment_id","in":"query","required":false,"schema":{"type":"string"}}],"query":[{"name":"refresh","in":"query","required":true,"schema":{"type":"boolean"}},{"name":"request_type","in":"query","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"shipment_id","in":"query","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", refresh=refresh, request_type=request_type, order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(refresh=refresh, request_type=request_type, order_id=order_id, shipment_id=shipment_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options", refresh=refresh, request_type=request_type, order_id=order_id, shipment_id=shipment_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account", order_id=order_id, request_hash=request_hash), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundAccountResponse
            schema = RefundAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBankAccountDetailsOpenAPI")
                print(e)

        return response
    
    async def addRefundBankAccountUsingOTP(self, body="", request_headers:Dict={}):
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
    
    async def getUserOrderBeneficiaries(self, order_id=None, request_headers:Dict={}):
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/order", order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/user", order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
    
    async def getUserCODlimitRoutes(self, merchant_user_id=None, mobile_no=None, request_headers:Dict={}):
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
    
    async def setUserCODlimitRoutes(self, body="", request_headers:Dict={}):
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
    
    async def edcAggregatorsAndModelList(self, request_headers:Dict={}):
        """Use this API to get info of devices linked to a particular app.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.edcAggregatorsAndModelList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-aggregator-list", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-aggregator-list", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to get info of devices linked to a particular app.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.edcDeviceStats()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-stats", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-stats", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to map new edc device to the terminal
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.updateEdcDevice()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EdcAddRequest
        schema = EdcAddRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to get details of a single edc device
        :param terminal_unique_identifier : Terminal unique identifier : type string
        """
        payload = {}
        
        if terminal_unique_identifier is not None:
            payload["terminal_unique_identifier"] = terminal_unique_identifier

        # Parameter validation
        schema = PaymentValidator.getEdcDevice()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}]}""", terminal_unique_identifier=terminal_unique_identifier)
        query_string = await create_query_string(terminal_unique_identifier=terminal_unique_identifier)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", terminal_unique_identifier=terminal_unique_identifier), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to Update store id and device tag of edc device
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"terminal_unique_identifier","in":"path","description":"Terminal unique identifier","schema":{"type":"string"},"required":true}]}""", terminal_unique_identifier=terminal_unique_identifier)
        query_string = await create_query_string(terminal_unique_identifier=terminal_unique_identifier)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device/{terminal_unique_identifier}", terminal_unique_identifier=terminal_unique_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to get all devices linked to a particular app.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-list", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"store_id","required":false,"schema":{"type":"integer"}},{"in":"query","name":"device_tag","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_active","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"store_id","required":false,"schema":{"type":"integer"}},{"in":"query","name":"device_tag","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", page_no=page_no, page_size=page_size, is_active=is_active, store_id=store_id, device_tag=device_tag, )
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_active=is_active, store_id=store_id, device_tag=device_tag, )

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/edc-device-list", page_no=page_no, page_size=page_size, is_active=is_active, store_id=store_id, device_tag=device_tag), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to get Get All Valid Payment Options for making payment
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/pos", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string"}}],"optional":[{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":false,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":false,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"order_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}},{"name":"display_split","in":"query","description":"Display Split Payment Option or not","schema":{"type":"boolean"}},{"name":"advance_payment","in":"query","description":"Display Advance Payment Options or Normal","schema":{"type":"boolean"}},{"name":"shipment_id","in":"query","required":false,"schema":{"type":"string"}}],"query":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":false,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":false,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"order_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}},{"name":"display_split","in":"query","description":"Display Split Payment Option or not","schema":{"type":"boolean"}},{"name":"advance_payment","in":"query","description":"Display Advance Payment Options or Normal","schema":{"type":"boolean"}},{"name":"shipment_id","in":"query","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, order_id=order_id, card_reference=card_reference, order_type=order_type, user_details=user_details, display_split=display_split, advance_payment=advance_payment, shipment_id=shipment_id)
        query_string = await create_query_string(amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, order_id=order_id, card_reference=card_reference, order_type=order_type, user_details=user_details, display_split=display_split, advance_payment=advance_payment, shipment_id=shipment_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/pos", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, order_id=order_id, card_reference=card_reference, order_type=order_type, user_details=user_details, display_split=display_split, advance_payment=advance_payment, shipment_id=shipment_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/request", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/confirm/polling", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/cancel", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to get Payment status and information for a list of order_ids
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.paymentStatusBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentStatusBulkHandlerRequest
        schema = PaymentStatusBulkHandlerRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/payment-status-bulk/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/payment-status-bulk/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
    
    async def revokeOauthToken(self, aggregator=None, request_headers:Dict={}):
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
    
    async def repaymentDetails(self, body="", request_headers:Dict={}):
        """Use this API to register any repayment record in the db and notify the aggrgator
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.repaymentDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RepaymentDetailsSerialiserPayAll
        schema = RepaymentDetailsSerialiserPayAll()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/repayment-details", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/repayment-details", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to push Ajiodhan merchant data to Gringotts system
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.merchantOnBoarding()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MerchantOnBoardingRequest
        schema = MerchantOnBoardingRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchant-onboarding", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/merchant-onboarding", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/customer/validation", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/customer/validation", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to get a payment link
        :param payment_link_id :  : type string
        """
        payload = {}
        
        if payment_link_id is not None:
            payload["payment_link_id"] = payment_link_id

        # Parameter validation
        schema = PaymentValidator.getPaymentLink()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/create-payment-link/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"payment_link_id","schema":{"type":"string","description":"Unique payment link id"}}],"query":[{"in":"query","name":"payment_link_id","schema":{"type":"string","description":"Unique payment link id"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", payment_link_id=payment_link_id)
        query_string = await create_query_string(payment_link_id=payment_link_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/create-payment-link/", payment_link_id=payment_link_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to create a payment link for the customer
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.createPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreatePaymentLinkRequest
        schema = CreatePaymentLinkRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/create-payment-link/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/create-payment-link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CreatePaymentLinkResponse
            schema = CreatePaymentLinkResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPaymentLink")
                print(e)

        return response
    
    async def pollingPaymentLink(self, payment_link_id=None, request_headers:Dict={}):
        """Use this API to poll if payment through payment was successful or not
        :param payment_link_id :  : type string
        """
        payload = {}
        
        if payment_link_id is not None:
            payload["payment_link_id"] = payment_link_id

        # Parameter validation
        schema = PaymentValidator.pollingPaymentLink()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/polling-payment-link/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"payment_link_id","schema":{"type":"string","description":"Unique payment link id"}}],"query":[{"in":"query","name":"payment_link_id","schema":{"type":"string","description":"Unique payment link id"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", payment_link_id=payment_link_id)
        query_string = await create_query_string(payment_link_id=payment_link_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/polling-payment-link/", payment_link_id=payment_link_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to resend a payment link for the customer
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.resendPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CancelOrResendPaymentLinkRequest
        schema = CancelOrResendPaymentLinkRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/resend-payment-link/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/resend-payment-link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to cancel a payment link for the customer
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.cancelPaymentLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CancelOrResendPaymentLinkRequest
        schema = CancelOrResendPaymentLinkRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cancel-payment-link/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cancel-payment-link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CancelPaymentLinkResponse
            schema = CancelPaymentLinkResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelPaymentLink")
                print(e)

        return response
    
    async def getPaymentModeControlRoutes(self, mode=None, request_headers:Dict={}):
        """Use this API to get details for the given offline / advance payment mode for merchant
        :param mode : offline / advance  modes to get the payment modes : type string
        """
        payload = {}
        
        if mode is not None:
            payload["mode"] = mode

        # Parameter validation
        schema = PaymentValidator.getPaymentModeControlRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance  modes to get the payment modes","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance  modes to get the payment modes","schema":{"type":"string"},"required":true}]}""", mode=mode)
        query_string = await create_query_string(mode=mode)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}", mode=mode), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformPaymentModeResponse
            schema = PlatformPaymentModeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentModeControlRoutes")
                print(e)

        return response
    
    async def setMerchantModeControlRoutes(self, mode=None, body="", request_headers:Dict={}):
        """Use this API to update given offline / advance payment mode details for the merchant
        :param mode : offline / advance payment mode : type string
        """
        payload = {}
        
        if mode is not None:
            payload["mode"] = mode

        # Parameter validation
        schema = PaymentValidator.setMerchantModeControlRoutes()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MerchantPaymentModeRequest
        schema = MerchantPaymentModeRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance payment mode","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance payment mode","schema":{"type":"string"},"required":true}]}""", mode=mode)
        query_string = await create_query_string(mode=mode)

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}", mode=mode), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformPaymentModeResponse
            schema = PlatformPaymentModeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setMerchantModeControlRoutes")
                print(e)

        return response
    
    async def getPaymentModeCustomConfig(self, mode=None, request_headers:Dict={}):
        """Use this API to Get details of advance payment custom configurations of merchant
        :param mode : offline / advance  mode : type string
        """
        payload = {}
        
        if mode is not None:
            payload["mode"] = mode

        # Parameter validation
        schema = PaymentValidator.getPaymentModeCustomConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}/custom-config", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance  mode","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance  mode","schema":{"type":"string"},"required":true}]}""", mode=mode)
        query_string = await create_query_string(mode=mode)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}/custom-config", mode=mode), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to update given details of advance payment custom configurations of merchant
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}/custom-config", """{"required":[{"name":"company_id","in":"path","description":"Company ID","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance payment mode","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"mode","in":"path","description":"offline / advance payment mode","schema":{"type":"string"},"required":true}]}""", mode=mode)
        query_string = await create_query_string(mode=mode)

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/modes/{mode}/custom-config", mode=mode), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Get all active List Payment Options Method Codes
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getPaymentCodeOption()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/codes", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/codes", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """Use this API to fetch the payment session details for given order ID or Transaction ID.
        :param gid : global identifier of the entity (e.g. order, cart etc.) against which payment session was initiated. This is generated by Fynd payments platform and is unique. : type string
        :param line-item : line-item to add extra data into response (e.g. cart details) : type boolean
        """
        payload = {}
        
        if gid is not None:
            payload["gid"] = gid
        if line_item is not None:
            payload["line_item"] = line_item

        # Parameter validation
        schema = PaymentValidator.getPaymentSession()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/session/{gid}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"status_update_success":{"summary":"valid company id","value":1},"status_update_failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"status_update_failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"gid","in":"path","description":"global identifier of the entity (e.g. order, cart etc.) against which payment session was initiated. This is generated by Fynd payments platform and is unique.","schema":{"type":"string"},"examples":{"transaction_details_success":{"summary":"valid global identifier","value":"TR9C4AF3A615DE251A23"},"order_details_success":{"summary":"valid Order ID","value":"FY615DE25839C4AF3A1A"},"payment_details_failed":{"summary":"invalid global identifier","value":"1"}},"required":true}],"optional":[{"name":"line-item","in":"query","description":"line-item to add extra data into response (e.g. cart details)","schema":{"type":"boolean"},"examples":{"line_item_success":{"summary":"Valid line-item options","value":true},"line_iteme_failed":{"summary":"invalid line-item options","value":false}}}],"query":[{"name":"line-item","in":"query","description":"line-item to add extra data into response (e.g. cart details)","schema":{"type":"boolean"},"examples":{"line_item_success":{"summary":"Valid line-item options","value":true},"line_iteme_failed":{"summary":"invalid line-item options","value":false}}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"status_update_success":{"summary":"valid company id","value":1},"status_update_failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"status_update_failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"gid","in":"path","description":"global identifier of the entity (e.g. order, cart etc.) against which payment session was initiated. This is generated by Fynd payments platform and is unique.","schema":{"type":"string"},"examples":{"transaction_details_success":{"summary":"valid global identifier","value":"TR9C4AF3A615DE251A23"},"order_details_success":{"summary":"valid Order ID","value":"FY615DE25839C4AF3A1A"},"payment_details_failed":{"summary":"invalid global identifier","value":"1"}},"required":true}]}""", gid=gid, line_item=line_item)
        query_string = await create_query_string(gid=gid, line_item=line_item)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/session/{gid}", gid=gid, line_item=line_item), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentSessionSerializer
            schema = PaymentSessionSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentSession")
                print(e)

        return response
    
    async def updatePaymentSession(self, gid=None, body="", request_headers:Dict={}):
        """A payment_session is initiated against a global identifier (gid) which is identifies the entity payment is initiated against. e.g. order_id, cart_id. This endpoint is to update the status of the said payment_session.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/session/{gid}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"status_update_success":{"summary":"valid company id","value":1},"status_update_failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"status_update_failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"gid","in":"path","description":"global identifier of the entity (e.g. order, cart etc.) against which payment_session was initiated. This is generated by Fynd payments platform and is unique.","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid global identifier","value":"FY615DE25839C4AF3A1A"},"status_update_failed":{"summary":"invalid global identifier","value":"1"}},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"status_update_success":{"summary":"valid company id","value":1},"status_update_failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"status_update_failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"gid","in":"path","description":"global identifier of the entity (e.g. order, cart etc.) against which payment_session was initiated. This is generated by Fynd payments platform and is unique.","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid global identifier","value":"FY615DE25839C4AF3A1A"},"status_update_failed":{"summary":"invalid global identifier","value":"1"}},"required":true}]}""", gid=gid)
        query_string = await create_query_string(gid=gid)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/session/{gid}", gid=gid), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """A refund_session is initiated against a refund request, and this endpoint is to update the status against the refund request_id. A gid is unique indentifier of the entity against which payment was received e.g. an order.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/{gid}/refund/session/{request_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"status_update_success":{"summary":"valid company id","value":1},"status_update_failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"status_update_failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"gid","in":"path","description":"global identifier of the entity (e.g. order, cart etc.) against which payment_session was initiated. This is generated by Fynd payments platform and is unique.","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid global identifier","value":"FY615DE25839C4AF3A1A"},"status_update_failed":{"summary":"invalid global identifier","value":"1"}},"required":true},{"name":"request_id","in":"path","description":"A unique id that was used to initiate a refund session. This is generated by Fynd platform and is usually shipment_id.","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid refund request id","value":"16100144824381402124"},"status_update_failed":{"summary":"invalid request id","value":"1"}},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"status_update_success":{"summary":"valid company id","value":1},"status_update_failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"status_update_failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"gid","in":"path","description":"global identifier of the entity (e.g. order, cart etc.) against which payment_session was initiated. This is generated by Fynd payments platform and is unique.","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid global identifier","value":"FY615DE25839C4AF3A1A"},"status_update_failed":{"summary":"invalid global identifier","value":"1"}},"required":true},{"name":"request_id","in":"path","description":"A unique id that was used to initiate a refund session. This is generated by Fynd platform and is usually shipment_id.","schema":{"type":"string"},"examples":{"status_update_success":{"summary":"valid refund request id","value":"16100144824381402124"},"status_update_failed":{"summary":"invalid request id","value":"1"}},"required":true}]}""", gid=gid, request_id=request_id)
        query_string = await create_query_string(gid=gid, request_id=request_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/{gid}/refund/session/{request_id}", gid=gid, request_id=request_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundSessionResponseSerializer
            schema = RefundSessionResponseSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateRefundSession")
                print(e)

        return response
    
    async def getMerchantPaymentOption(self, request_headers:Dict={}):
        """This api fetches all the available PGs for merchant and its offline payment mode details.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getMerchantPaymentOption()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid company id","value":1}}},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid app id","value":"000000000000000000000001"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid company id","value":1}}},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid app id","value":"000000000000000000000001"}}}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformPaymentModeResponse
            schema = PlatformPaymentModeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchantPaymentOption")
                print(e)

        return response
    
    async def patchMerchantPaymentOption(self, body="", request_headers:Dict={}):
        """To updated online payment as active/inactive or offline payment configuration like cod charges, anonymous cod allowed flags.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.patchMerchantPaymentOption()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import MerchnatPaymentModeRequest
        schema = MerchnatPaymentModeRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid company id","value":1}}},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid app id","value":"000000000000000000000001"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid company id","value":1}}},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid app id","value":"000000000000000000000001"}}}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformPaymentModeResponse
            schema = PlatformPaymentModeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for patchMerchantPaymentOption")
                print(e)

        return response
    
    async def getMerchantAggregatorPaymentModeDetails(self, aggregator_id=None, business_unit=None, device=None, request_headers:Dict={}):
        """Get Aggregator, payment mode and sub payment mode details.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true},{"name":"business_unit","in":"query","required":true,"schema":{"type":"string"}},{"name":"device","in":"query","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"business_unit","in":"query","required":true,"schema":{"type":"string"}},{"name":"device","in":"query","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true}]}""", aggregator_id=aggregator_id, business_unit=business_unit, device=device)
        query_string = await create_query_string(aggregator_id=aggregator_id, business_unit=business_unit, device=device)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}", aggregator_id=aggregator_id, business_unit=business_unit, device=device), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformPaymentModeResponse
            schema = PlatformPaymentModeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchantAggregatorPaymentModeDetails")
                print(e)

        return response
    
    async def patchMerchantAggregatorPaymentModeDetails(self, aggregator_id=None, body="", request_headers:Dict={}):
        """Update Aggregator, payment mode and sub payment mode details.
        :param aggregator_id : Aggregators Id : type integer
        """
        payload = {}
        
        if aggregator_id is not None:
            payload["aggregator_id"] = aggregator_id

        # Parameter validation
        schema = PaymentValidator.patchMerchantAggregatorPaymentModeDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformPaymentModeResponse
        schema = PlatformPaymentModeResponse()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true}]}""", aggregator_id=aggregator_id)
        query_string = await create_query_string(aggregator_id=aggregator_id)

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}", aggregator_id=aggregator_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Get Aggregators available to be added as PG.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getPGConfigAggregators()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration/aggregator", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/configuration/aggregator", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformPaymentModeResponse
            schema = PlatformPaymentModeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPGConfigAggregators")
                print(e)

        return response
    
    async def getMerchantRefundPriority(self, config_type=None, request_headers:Dict={}):
        """API to get merchant refund priority
        :param config_type : configuration for merchant or customer : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type

        # Parameter validation
        schema = PaymentValidator.getMerchantRefundPriority()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"success":{"summary":"valid company id","value":1},"failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"examples":{"success":{"summary":"config source valid","value":"merchant"}},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"success":{"summary":"valid company id","value":1},"failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"examples":{"success":{"summary":"config source valid","value":"merchant"}},"required":true}]}""", config_type=config_type)
        query_string = await create_query_string(config_type=config_type)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}", config_type=config_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundPriorityResponseSerializer
            schema = RefundPriorityResponseSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getMerchantRefundPriority")
                print(e)

        return response
    
    async def createMerchantRefundPriority(self, config_type=None, body="", request_headers:Dict={}):
        """API to update merchant refund priority
        :param config_type : configuration for merchant or customer : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type

        # Parameter validation
        schema = PaymentValidator.createMerchantRefundPriority()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RefundPriorityRequestSerializer
        schema = RefundPriorityRequestSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"success":{"summary":"valid company id","value":1},"failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"examples":{"success":{"summary":"config source valid","value":"merchant"}},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"success":{"summary":"valid company id","value":1},"failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"examples":{"success":{"summary":"config source valid","value":"merchant"}},"required":true}]}""", config_type=config_type)
        query_string = await create_query_string(config_type=config_type)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}", config_type=config_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundPriorityResponseSerializer
            schema = RefundPriorityResponseSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createMerchantRefundPriority")
                print(e)

        return response
    
    async def updateMerchantRefundPriority(self, config_type=None, body="", request_headers:Dict={}):
        """API to update merchant refund priority
        :param config_type : configuration for merchant or customer : type string
        """
        payload = {}
        
        if config_type is not None:
            payload["config_type"] = config_type

        # Parameter validation
        schema = PaymentValidator.updateMerchantRefundPriority()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RefundPriorityRequestSerializer
        schema = RefundPriorityRequestSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"success":{"summary":"valid company id","value":1},"failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"examples":{"success":{"summary":"config source valid","value":"merchant"}},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"examples":{"success":{"summary":"valid company id","value":1},"failed":{"summary":"invalid company id","value":0}},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"examples":{"success":{"summary":"valid app id","value":"64bf81dcc07acacc135733ea"},"failed":{"summary":"invalid app id","value":"123"}},"required":true},{"name":"config_type","in":"path","description":"configuration for merchant or customer","schema":{"type":"string","enum":["merchant","customer","default"]},"examples":{"success":{"summary":"config source valid","value":"merchant"}},"required":true}]}""", config_type=config_type)
        query_string = await create_query_string(config_type=config_type)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund_priority/config/{config_type}", config_type=config_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)

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
        """Use this API to create a order and payment on aggregator side
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.createPaymentOrder()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentOrderRequest
        schema = PaymentOrderRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment-orders/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment-orders/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentOrderResponse
            schema = PaymentOrderResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPaymentOrder")
                print(e)

        return response
    
    async def getMerchantAggregatorAppVersion(self, aggregator_id=None, business_unit=None, device=None, payment_mode_id=None, sub_payment_mode=None, request_headers:Dict={}):
        """This api provide read operations on the app version required for Payment Mode or sub payment mode for an Aggregator.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}/version", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid company id","value":1}}},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid app id","value":"000000000000000000000001"}}},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid aggregator id","value":1}}},{"name":"business_unit","in":"query","required":true,"schema":{"type":"string"},"examples":{"merchant_payment_response_success":{"summary":"valid business unit","value":"storefront"}}},{"name":"device","in":"query","required":true,"schema":{"type":"string"},"examples":{"merchant_payment_response_success":{"summary":"valid device","value":"desktop"}}}],"optional":[{"name":"payment_mode_id","in":"query","required":false,"schema":{"type":"integer"},"examples":{"merchant_payment_response_success":{"summary":"valid payment mode id","value":3}}},{"name":"sub_payment_mode","in":"query","required":false,"schema":{"type":"string"},"examples":{"merchant_payment_response_success":{"summary":"valid sub payment mode code.","value":"LAVB_R"}}}],"query":[{"name":"business_unit","in":"query","required":true,"schema":{"type":"string"},"examples":{"merchant_payment_response_success":{"summary":"valid business unit","value":"storefront"}}},{"name":"device","in":"query","required":true,"schema":{"type":"string"},"examples":{"merchant_payment_response_success":{"summary":"valid device","value":"desktop"}}},{"name":"payment_mode_id","in":"query","required":false,"schema":{"type":"integer"},"examples":{"merchant_payment_response_success":{"summary":"valid payment mode id","value":3}}},{"name":"sub_payment_mode","in":"query","required":false,"schema":{"type":"string"},"examples":{"merchant_payment_response_success":{"summary":"valid sub payment mode code.","value":"LAVB_R"}}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid company id","value":1}}},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid app id","value":"000000000000000000000001"}}},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid aggregator id","value":1}}}]}""", aggregator_id=aggregator_id, business_unit=business_unit, device=device, payment_mode_id=payment_mode_id, sub_payment_mode=sub_payment_mode)
        query_string = await create_query_string(aggregator_id=aggregator_id, business_unit=business_unit, device=device, payment_mode_id=payment_mode_id, sub_payment_mode=sub_payment_mode)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}/version", aggregator_id=aggregator_id, business_unit=business_unit, device=device, payment_mode_id=payment_mode_id, sub_payment_mode=sub_payment_mode), query_string, headers, "", exclude_headers=exclude_headers), data="")

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
        """This api provide wrote operations on the app version required for Payment Mode or sub payment mode for an Aggregator.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}/version", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid company id","value":1}}},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid app id","value":"000000000000000000000001"}}},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid aggregator id","value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid company id","value":1}}},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid app id","value":"000000000000000000000001"}}},{"name":"aggregator_id","in":"path","description":"Aggregators Id","schema":{"type":"integer"},"required":true,"examples":{"merchant_payment_response_success":{"summary":"valid aggregator id","value":1}}}]}""", aggregator_id=aggregator_id)
        query_string = await create_query_string(aggregator_id=aggregator_id)

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options/aggregators/{aggregator_id}/version", aggregator_id=aggregator_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformPaymentModeResponse
            schema = PlatformPaymentModeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for patchMerchantPaymentOptionVersion")
                print(e)

        return response
    