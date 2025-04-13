"""Payment Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import PaymentValidator

class Payment:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getAllPayouts(self, unique_external_id=None, request_headers:Dict={}):
        """Retrieve a list of all payout transactions.
        :param unique_external_id : Fetch payouts using unique external id : type string
        """
        payload = {}
        
        if unique_external_id is not None:
            payload["unique_external_id"] = unique_external_id

        # Parameter validation
        schema = PaymentValidator.getAllPayouts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[{"name":"unique_external_id","in":"query","description":"Fetch payouts using unique external id","schema":{"type":"string"}}],"query":[{"name":"unique_external_id","in":"query","description":"Fetch payouts using unique external id","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", unique_external_id=unique_external_id)
        query_string = await create_query_string(unique_external_id=unique_external_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", unique_external_id=unique_external_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PayoutsResponse
            schema = PayoutsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllPayouts")
                print(e)

        return response
    
    async def savePayout(self, body="", request_headers:Dict={}):
        """Store and process a payout transaction.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.savePayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PayoutRequest
        schema = PayoutRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PayoutResponse
            schema = PayoutResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for savePayout")
                print(e)

        return response
    
    async def updatePayouts(self, body="", request_headers:Dict={}):
        """Modify the details of a payout transaction.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.updatePayouts()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PayoutRequest
        schema = PayoutRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdatePayoutResponse
            schema = UpdatePayoutResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePayouts")
                print(e)

        return response
    
    async def activateAndDectivatePayouts(self, body="", request_headers:Dict={}):
        """Enable or disable payout functionality.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.activateAndDectivatePayouts()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdatePayoutRequest
        schema = UpdatePayoutRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdatePayoutResponse
            schema = UpdatePayoutResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for activateAndDectivatePayouts")
                print(e)

        return response
    
    async def deletePayouts(self, unique_transfer_no=None, request_headers:Dict={}):
        """Remove a payout transaction from the system.
        :param unique_transfer_no : Unique transfer id : type string
        """
        payload = {}
        
        if unique_transfer_no is not None:
            payload["unique_transfer_no"] = unique_transfer_no

        # Parameter validation
        schema = PaymentValidator.deletePayouts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"query","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"name":"unique_transfer_no","in":"query","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", unique_transfer_no=unique_transfer_no)
        query_string = await create_query_string(unique_transfer_no=unique_transfer_no)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", unique_transfer_no=unique_transfer_no), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeletePayoutResponse
            schema = DeletePayoutResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deletePayouts")
                print(e)

        return response
    
    async def getAllPayout(self, unique_transfer_no=None, unique_external_id=None, request_headers:Dict={}):
        """Get All Payouts
        :param unique_transfer_no : Unique transfer id : type string
        :param unique_external_id : Fetch payouts using unique external id : type string
        """
        payload = {}
        
        if unique_transfer_no is not None:
            payload["unique_transfer_no"] = unique_transfer_no
        if unique_external_id is not None:
            payload["unique_external_id"] = unique_external_id

        # Parameter validation
        schema = PaymentValidator.getAllPayout()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[{"name":"unique_external_id","in":"query","description":"Fetch payouts using unique external id","schema":{"type":"string"}}],"query":[{"name":"unique_external_id","in":"query","description":"Fetch payouts using unique external id","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}]}""", serverType="platform", unique_transfer_no=unique_transfer_no, unique_external_id=unique_external_id)
        query_string = await create_query_string(unique_external_id=unique_external_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no, unique_external_id=unique_external_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PayoutsResponse
            schema = PayoutsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllPayout")
                print(e)

        return response
    
    async def savePayouts(self, unique_transfer_no=None, body="", request_headers:Dict={}):
        """Save Payout
        :param unique_transfer_no : Unique transfer id : type string
        """
        payload = {}
        
        if unique_transfer_no is not None:
            payload["unique_transfer_no"] = unique_transfer_no

        # Parameter validation
        schema = PaymentValidator.savePayouts()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PayoutRequest
        schema = PayoutRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}]}""", serverType="platform", unique_transfer_no=unique_transfer_no)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PayoutResponse
            schema = PayoutResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for savePayouts")
                print(e)

        return response
    
    async def updatePayout(self, unique_transfer_no=None, body="", request_headers:Dict={}):
        """Update Payout
        :param unique_transfer_no : Unique transfer id : type string
        """
        payload = {}
        
        if unique_transfer_no is not None:
            payload["unique_transfer_no"] = unique_transfer_no

        # Parameter validation
        schema = PaymentValidator.updatePayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PayoutRequest
        schema = PayoutRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}]}""", serverType="platform", unique_transfer_no=unique_transfer_no)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdatePayoutResponse
            schema = UpdatePayoutResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePayout")
                print(e)

        return response
    
    async def activateAndDectivatePayout(self, unique_transfer_no=None, body="", request_headers:Dict={}):
        """Enable or disable payout functionality.
        :param unique_transfer_no : Unique transfer id : type string
        """
        payload = {}
        
        if unique_transfer_no is not None:
            payload["unique_transfer_no"] = unique_transfer_no

        # Parameter validation
        schema = PaymentValidator.activateAndDectivatePayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdatePayoutRequest
        schema = UpdatePayoutRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}]}""", serverType="platform", unique_transfer_no=unique_transfer_no)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdatePayoutResponse
            schema = UpdatePayoutResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for activateAndDectivatePayout")
                print(e)

        return response
    
    async def deletePayout(self, unique_transfer_no=None, request_headers:Dict={}):
        """Delete Payout
        :param unique_transfer_no : Unique transfer id : type string
        """
        payload = {}
        
        if unique_transfer_no is not None:
            payload["unique_transfer_no"] = unique_transfer_no

        # Parameter validation
        schema = PaymentValidator.deletePayout()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}]}""", serverType="platform", unique_transfer_no=unique_transfer_no)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeletePayoutResponse
            schema = DeletePayoutResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deletePayout")
                print(e)

        return response
    
    async def verifyIfscCode(self, ifsc_code=None, request_headers:Dict={}):
        """Checks the validity of the provided IFSC code and returns bank details if valid.
        :param ifsc_code :  : type string
        """
        payload = {}
        
        if ifsc_code is not None:
            payload["ifsc_code"] = ifsc_code

        # Parameter validation
        schema = PaymentValidator.verifyIfscCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/ifsc-code/verify", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"ifsc_code","in":"query","schema":{"type":"string","description":"Fetch bank details for correct ifsc code"},"required":true}],"optional":[],"query":[{"name":"ifsc_code","in":"query","schema":{"type":"string","description":"Fetch bank details for correct ifsc code"},"required":true}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", ifsc_code=ifsc_code)
        query_string = await create_query_string(ifsc_code=ifsc_code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/ifsc-code/verify", ifsc_code=ifsc_code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import IfscCodeResponse
            schema = IfscCodeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyIfscCode")
                print(e)

        return response
    
    async def getPaymentMethodConfig(self, request_headers:Dict={}):
        """Get all active List Payment  Method Configs
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getPaymentMethodConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payment/methods/configs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payment/methods/configs", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentMethodConfigResponse
            schema = PaymentMethodConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentMethodConfig")
                print(e)

        return response
    