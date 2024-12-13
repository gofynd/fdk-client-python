"""Billing Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import BillingValidator

class Billing:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getChargeDetails(self, extension_id=None, charge_id=None, request_headers:Dict={}):
        """Retrieve comprehensive details about a specific billing charge.
        :param extension_id : Extension _id : type string
        :param charge_id : Standalone charge _id : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if charge_id is not None:
            payload["charge_id"] = charge_id

        # Parameter validation
        schema = BillingValidator.getChargeDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/charge/{charge_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string"}},{"in":"path","name":"charge_id","description":"Standalone charge _id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string"}},{"in":"path","name":"charge_id","description":"Standalone charge _id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", extension_id=extension_id, charge_id=charge_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/charge/{charge_id}", extension_id=extension_id, charge_id=charge_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ChargeDetails
            schema = ChargeDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getChargeDetails")
                print(e)

        return response
    
    async def getSubscriptionCharge(self, extension_id=None, subscription_id=None, request_headers:Dict={}):
        """Retrieve detailed information about subscription charges using this API.
        :param extension_id : Extension _id : type string
        :param subscription_id : Subscription charge _id : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if subscription_id is not None:
            payload["subscription_id"] = subscription_id

        # Parameter validation
        schema = BillingValidator.getSubscriptionCharge()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", extension_id=extension_id, subscription_id=subscription_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}", extension_id=extension_id, subscription_id=subscription_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionChargeRes
            schema = SubscriptionChargeRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSubscriptionCharge")
                print(e)

        return response
    
    async def cancelSubscriptionCharge(self, extension_id=None, subscription_id=None, request_headers:Dict={}):
        """Cancel an ongoing subscription charge for a customer.
        :param extension_id : Extension _id : type string
        :param subscription_id : Subscription charge _id : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if subscription_id is not None:
            payload["subscription_id"] = subscription_id

        # Parameter validation
        schema = BillingValidator.cancelSubscriptionCharge()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}/cancel", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", extension_id=extension_id, subscription_id=subscription_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}/cancel", extension_id=extension_id, subscription_id=subscription_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionChargeRes
            schema = SubscriptionChargeRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelSubscriptionCharge")
                print(e)

        return response
    
    async def createOneTimeCharge(self, extension_id=None, body="", request_headers:Dict={}):
        """Generate a one-time charge for specific services or products.
        :param extension_id : Extension _id : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id

        # Parameter validation
        schema = BillingValidator.createOneTimeCharge()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateOneTimeCharge
        schema = CreateOneTimeCharge()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/one_time_charge", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", extension_id=extension_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/one_time_charge", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateOneTimeChargeResponse
            schema = CreateOneTimeChargeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createOneTimeCharge")
                print(e)

        return response
    
    async def createSubscriptionCharge(self, extension_id=None, body="", request_headers:Dict={}):
        """Register a subscription charge for a seller using your extension.
        :param extension_id : Extension Id for which we need to crete new subscription : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id

        # Parameter validation
        schema = BillingValidator.createSubscriptionCharge()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateSubscriptionCharge
        schema = CreateSubscriptionCharge()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"integer"}},{"in":"path","name":"extension_id","description":"Extension Id for which we need to crete new subscription","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"integer"}},{"in":"path","name":"extension_id","description":"Extension Id for which we need to crete new subscription","required":true,"schema":{"type":"string"}}]}""", serverType="platform", extension_id=extension_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateSubscriptionResponse
            schema = CreateSubscriptionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSubscriptionCharge")
                print(e)

        return response
    