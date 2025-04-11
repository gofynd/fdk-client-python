"""Payment Partner Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PartnerConfig import PartnerConfig

from .validator import PaymentValidator

class Payment:
    def __init__(self, config: PartnerConfig):
        self._conf = config

    
    async def getPaymentconfig(self, request_headers:Dict={}):
        """Get partner Payout details
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getPaymentconfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payment/methods/configs", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true}]}""", serverType="partner", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payment/methods/configs", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentConfigDetails
            schema = PaymentConfigDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentconfig")
                print(e)

        return response
    
    async def getPayout(self, unique_external_id=None, request_headers:Dict={}):
        """Get partner Payout details
        :param unique_external_id : unique_external_id. : type integer
        """
        payload = {}
        
        if unique_external_id is not None:
            payload["unique_external_id"] = unique_external_id

        # Parameter validation
        schema = PaymentValidator.getPayout()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_external_id","in":"query","description":"unique_external_id.","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[{"name":"unique_external_id","in":"query","description":"unique_external_id.","required":true,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true}]}""", serverType="partner", unique_external_id=unique_external_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts", unique_external_id=unique_external_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PayoutDetails
            schema = PayoutDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPayout")
                print(e)

        return response
    
    async def postPayout(self, body="", request_headers:Dict={}):
        """save payout details
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.postPayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostPayout
        schema = PostPayout()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true}]}""", serverType="partner", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PostPayoutDetails
            schema = PostPayoutDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for postPayout")
                print(e)

        return response
    
    async def updatePayout(self, body="", request_headers:Dict={}):
        """save payout details
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.updatePayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostPayout
        schema = PostPayout()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true}]}""", serverType="partner", )
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PostPayoutDetails
            schema = PostPayoutDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePayout")
                print(e)

        return response
    
    async def putPayout(self, body="", request_headers:Dict={}):
        """update payout details
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.putPayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostPayout
        schema = PostPayout()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true}]}""", serverType="partner", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PostPayoutDetails
            schema = PostPayoutDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for putPayout")
                print(e)

        return response
    
    async def deletePayout(self, unique_external_id=None, request_headers:Dict={}):
        """Get partner Payout details
        :param unique_external_id : unique_external_id. : type integer
        """
        payload = {}
        
        if unique_external_id is not None:
            payload["unique_external_id"] = unique_external_id

        # Parameter validation
        schema = PaymentValidator.deletePayout()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_external_id","in":"query","description":"unique_external_id.","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[{"name":"unique_external_id","in":"query","description":"unique_external_id.","required":true,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true}]}""", serverType="partner", unique_external_id=unique_external_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts", unique_external_id=unique_external_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PayoutDetails
            schema = PayoutDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deletePayout")
                print(e)

        return response
    
    async def getPayouts(self, unique_transfer_no=None, unique_external_id=None, request_headers:Dict={}):
        """Get partner Payout details
        :param unique_transfer_no : unique_transfer_no : type string
        :param unique_external_id : unique_external_id. : type integer
        """
        payload = {}
        
        if unique_transfer_no is not None:
            payload["unique_transfer_no"] = unique_transfer_no
        if unique_external_id is not None:
            payload["unique_external_id"] = unique_external_id

        # Parameter validation
        schema = PaymentValidator.getPayouts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts/{unique_transfer_no}", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_transfer_no","in":"path","description":"unique_transfer_no","schema":{"type":"string"},"required":true},{"name":"unique_external_id","in":"query","description":"unique_external_id.","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[{"name":"unique_external_id","in":"query","description":"unique_external_id.","required":true,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_transfer_no","in":"path","description":"unique_transfer_no","schema":{"type":"string"},"required":true}]}""", serverType="partner", unique_transfer_no=unique_transfer_no, unique_external_id=unique_external_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no, unique_external_id=unique_external_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PayoutDetails
            schema = PayoutDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPayouts")
                print(e)

        return response
    
    async def postPayouts(self, unique_transfer_no=None, body="", request_headers:Dict={}):
        """save payout details
        :param unique_transfer_no : unique_transfer_no : type string
        """
        payload = {}
        
        if unique_transfer_no is not None:
            payload["unique_transfer_no"] = unique_transfer_no

        # Parameter validation
        schema = PaymentValidator.postPayouts()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostPayout
        schema = PostPayout()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts/{unique_transfer_no}", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_transfer_no","in":"path","description":"unique_transfer_no","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_transfer_no","in":"path","description":"unique_transfer_no","schema":{"type":"string"},"required":true}]}""", serverType="partner", unique_transfer_no=unique_transfer_no)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PostPayoutDetails
            schema = PostPayoutDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for postPayouts")
                print(e)

        return response
    
    async def updatePayouts(self, unique_transfer_no=None, body="", request_headers:Dict={}):
        """save payout details
        :param unique_transfer_no : unique_transfer_no : type string
        """
        payload = {}
        
        if unique_transfer_no is not None:
            payload["unique_transfer_no"] = unique_transfer_no

        # Parameter validation
        schema = PaymentValidator.updatePayouts()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostPayout
        schema = PostPayout()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts/{unique_transfer_no}", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_transfer_no","in":"path","description":"unique_transfer_no","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_transfer_no","in":"path","description":"unique_transfer_no","schema":{"type":"string"},"required":true}]}""", serverType="partner", unique_transfer_no=unique_transfer_no)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PostPayoutDetails
            schema = PostPayoutDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePayouts")
                print(e)

        return response
    
    async def putPayouts(self, unique_transfer_no=None, body="", request_headers:Dict={}):
        """update payout details
        :param unique_transfer_no : unique_transfer_no : type string
        """
        payload = {}
        
        if unique_transfer_no is not None:
            payload["unique_transfer_no"] = unique_transfer_no

        # Parameter validation
        schema = PaymentValidator.putPayouts()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostPayout
        schema = PostPayout()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts/{unique_transfer_no}", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_transfer_no","in":"path","description":"unique_transfer_no","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_transfer_no","in":"path","description":"unique_transfer_no","schema":{"type":"string"},"required":true}]}""", serverType="partner", unique_transfer_no=unique_transfer_no)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PostPayoutDetails
            schema = PostPayoutDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for putPayouts")
                print(e)

        return response
    
    async def deletePayouts(self, unique_transfer_no=None, request_headers:Dict={}):
        """Get partner Payout details
        :param unique_transfer_no : unique_transfer_no. : type integer
        """
        payload = {}
        
        if unique_transfer_no is not None:
            payload["unique_transfer_no"] = unique_transfer_no

        # Parameter validation
        schema = PaymentValidator.deletePayouts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts/{unique_transfer_no}", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_transfer_no","in":"path","description":"unique_transfer_no.","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","schema":{"type":"string"},"required":true},{"name":"unique_transfer_no","in":"path","description":"unique_transfer_no.","required":true,"schema":{"type":"integer"}}]}""", serverType="partner", unique_transfer_no=unique_transfer_no)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/partner/payment/v1.0/organization/{self._conf.organizationId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PayoutDetails
            schema = PayoutDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deletePayouts")
                print(e)

        return response
    