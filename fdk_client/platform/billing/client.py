"""Billing Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import BillingValidator

class Billing:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def checkCouponValidity(self, plan=None, coupon_code=None, request_headers:Dict={}):
        """Check coupon validity.
        :param plan : ID of the plan. : type string
        :param coupon_code : Coupon code. : type string
        """
        payload = {}
        
        if plan is not None:
            payload["plan"] = plan
        if coupon_code is not None:
            payload["coupon_code"] = coupon_code

        # Parameter validation
        schema = BillingValidator.checkCouponValidity()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/coupon/check-validity", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"query","name":"plan","description":"ID of the plan.","required":true,"schema":{"type":"string","example":"61a5d6ea3e8c230f3aa2c507"}},{"in":"query","name":"coupon_code","description":"Coupon code.","required":true,"schema":{"type":"string","example":"FYND1"}}],"optional":[],"query":[{"in":"query","name":"plan","description":"ID of the plan.","required":true,"schema":{"type":"string","example":"61a5d6ea3e8c230f3aa2c507"}},{"in":"query","name":"coupon_code","description":"Coupon code.","required":true,"schema":{"type":"string","example":"FYND1"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", plan=plan, coupon_code=coupon_code)
        query_string = await create_query_string(plan=plan, coupon_code=coupon_code)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/coupon/check-validity", plan=plan, coupon_code=coupon_code), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CheckValidityResponse
            schema = CheckValidityResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkCouponValidity")
                print(e)

        return response
    
    async def createSubscriptionCharge(self, extension_id=None, body="", request_headers:Dict={}):
        """Register subscription charge for a seller of your extension.
        :param extension_id : Extension _id : type string
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", extension_id=extension_id)
        query_string = await create_query_string(extension_id=extension_id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateSubscriptionResponse
            schema = CreateSubscriptionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSubscriptionCharge")
                print(e)

        return response
    
    async def getSubscriptionCharge(self, extension_id=None, subscription_id=None, request_headers:Dict={}):
        """Get created subscription charge details
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", extension_id=extension_id, subscription_id=subscription_id)
        query_string = await create_query_string(extension_id=extension_id, subscription_id=subscription_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}", extension_id=extension_id, subscription_id=subscription_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import EntitySubscription
            schema = EntitySubscription()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSubscriptionCharge")
                print(e)

        return response
    
    async def cancelSubscriptionCharge(self, extension_id=None, subscription_id=None, request_headers:Dict={}):
        """Cancel subscription and attached charges.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}/cancel", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", extension_id=extension_id, subscription_id=subscription_id)
        query_string = await create_query_string(extension_id=extension_id, subscription_id=subscription_id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}/cancel", extension_id=extension_id, subscription_id=subscription_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import EntitySubscription
            schema = EntitySubscription()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelSubscriptionCharge")
                print(e)

        return response
    
    async def createOneTimeCharge(self, extension_id=None, body="", request_headers:Dict={}):
        """Register one time subscription charge for a seller of your extension.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/one_time_charge", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", extension_id=extension_id)
        query_string = await create_query_string(extension_id=extension_id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/one_time_charge", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateOneTimeChargeResponse
            schema = CreateOneTimeChargeResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createOneTimeCharge")
                print(e)

        return response
    
    async def getChargeDetails(self, extension_id=None, charge_id=None, request_headers:Dict={}):
        """Get created subscription charge details
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/charge/{charge_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"charge_id","description":"Standalone charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"charge_id","description":"Standalone charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", extension_id=extension_id, charge_id=charge_id)
        query_string = await create_query_string(extension_id=extension_id, charge_id=charge_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/charge/{charge_id}", extension_id=extension_id, charge_id=charge_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import OneTimeChargeEntity
            schema = OneTimeChargeEntity()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getChargeDetails")
                print(e)

        return response
    
    async def getInvoices(self, request_headers:Dict={}):
        """Get invoices.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getInvoices()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/list", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/list", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import Invoices
            schema = Invoices()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInvoices")
                print(e)

        return response
    
    async def getInvoiceById(self, invoice_id=None, request_headers:Dict={}):
        """Get invoice by id.
        :param invoice_id : Invoice id : type string
        """
        payload = {}
        
        if invoice_id is not None:
            payload["invoice_id"] = invoice_id

        # Parameter validation
        schema = BillingValidator.getInvoiceById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/{invoice_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"invoice_id","description":"Invoice id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"invoice_id","description":"Invoice id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", invoice_id=invoice_id)
        query_string = await create_query_string(invoice_id=invoice_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/{invoice_id}", invoice_id=invoice_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import Invoice
            schema = Invoice()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInvoiceById")
                print(e)

        return response
    
    async def getCustomerDetail(self, request_headers:Dict={}):
        """Get subscription customer detail.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getCustomerDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionCustomer
            schema = SubscriptionCustomer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomerDetail")
                print(e)

        return response
    
    async def upsertCustomerDetail(self, body="", request_headers:Dict={}):
        """Upsert subscription customer detail.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.upsertCustomerDetail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionCustomerCreate
        schema = SubscriptionCustomerCreate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionCustomer
            schema = SubscriptionCustomer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for upsertCustomerDetail")
                print(e)

        return response
    
    async def getSubscription(self, request_headers:Dict={}):
        """If subscription is active then it will return is_enabled true and return subscription object. If subscription is not active then is_enabled false and message.

        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getSubscription()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionStatus
            schema = SubscriptionStatus()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSubscription")
                print(e)

        return response
    
    async def getFeatureLimitConfig(self, product_suite=None, type=None, request_headers:Dict={}):
        """Get subscription subscription limits.
        :param product_suite :  : type string
        :param type :  : type string
        """
        payload = {}
        
        if product_suite is not None:
            payload["product_suite"] = product_suite
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = BillingValidator.getFeatureLimitConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current-limit", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[{"in":"query","name":"product_suite","schema":{"type":"string"}},{"in":"query","name":"type","schema":{"type":"string"}}],"query":[{"in":"query","name":"product_suite","schema":{"type":"string"}},{"in":"query","name":"type","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", product_suite=product_suite, type=type)
        query_string = await create_query_string(product_suite=product_suite, type=type)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current-limit", product_suite=product_suite, type=type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionLimit
            schema = SubscriptionLimit()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFeatureLimitConfig")
                print(e)

        return response
    
    async def activateSubscriptionPlan(self, body="", request_headers:Dict={}):
        """It will activate subscription plan for customer
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.activateSubscriptionPlan()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionActivateReq
        schema = SubscriptionActivateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/activate", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/activate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionActivateRes
            schema = SubscriptionActivateRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for activateSubscriptionPlan")
                print(e)

        return response
    
    async def cancelSubscriptionPlan(self, body="", request_headers:Dict={}):
        """It will cancel current active subscription.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.cancelSubscriptionPlan()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CancelSubscriptionReq
        schema = CancelSubscriptionReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/cancel", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/cancel", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import CancelSubscriptionRes
            schema = CancelSubscriptionRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelSubscriptionPlan")
                print(e)

        return response
    
    async def getEnterprisePlans(self, request_headers:Dict={}):
        """Get Enterprise Plans.

        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getEnterprisePlans()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/plans", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/plans", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        return response
    
    async def planStatusUpdate(self, body="", request_headers:Dict={}):
        """It will update the status of the plan
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.planStatusUpdate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlanStatusUpdateReq
        schema = PlanStatusUpdateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/plan/status", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/plan/status", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import Plan
            schema = Plan()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for planStatusUpdate")
                print(e)

        return response
    
    async def subscripePlan(self, body="", request_headers:Dict={}):
        """It will subscribe a plan.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.subscripePlan()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SunscribePlan
        schema = SunscribePlan()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/initiate", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/initiate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscribePlanRes
            schema = SubscribePlanRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for subscripePlan")
                print(e)

        return response
    
    async def getentityDetail(self, entity_name=None, entity_id=None, channel=None, component=None, component_name=None, request_headers:Dict={}):
        """Generic api to get the entity detail
        :param entity_name : Entity name. : type string
        :param entity_id : Entity unique id. : type string
        :param channel : Ordering channel. : type string
        :param component : The coponents the user would like to know. : type string
        :param component_name : The name of component the preferred to be fetched. : type string
        """
        payload = {}
        
        if entity_name is not None:
            payload["entity_name"] = entity_name
        if entity_id is not None:
            payload["entity_id"] = entity_id
        if channel is not None:
            payload["channel"] = channel
        if component is not None:
            payload["component"] = component
        if component_name is not None:
            payload["component_name"] = component_name

        # Parameter validation
        schema = BillingValidator.getentityDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/entity/detail", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"query","name":"entity_name","description":"Entity name.","required":true,"schema":{"type":"string","example":"plan/subscription"}},{"in":"query","name":"channel","description":"Ordering channel.","required":true,"schema":{"type":"string","example":"ecomm"}}],"optional":[{"in":"query","name":"entity_id","description":"Entity unique id.","required":false,"schema":{"type":"string","example":"1"}},{"in":"query","name":"component","description":"The coponents the user would like to know.","required":false,"schema":{"type":"string","example":"fee/feature"}},{"in":"query","name":"component_name","description":"The name of component the preferred to be fetched.","required":false,"schema":{"type":"string","example":"logistic_fee"}}],"query":[{"in":"query","name":"entity_name","description":"Entity name.","required":true,"schema":{"type":"string","example":"plan/subscription"}},{"in":"query","name":"entity_id","description":"Entity unique id.","required":false,"schema":{"type":"string","example":"1"}},{"in":"query","name":"channel","description":"Ordering channel.","required":true,"schema":{"type":"string","example":"ecomm"}},{"in":"query","name":"component","description":"The coponents the user would like to know.","required":false,"schema":{"type":"string","example":"fee/feature"}},{"in":"query","name":"component_name","description":"The name of component the preferred to be fetched.","required":false,"schema":{"type":"string","example":"logistic_fee"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", entity_name=entity_name, entity_id=entity_id, channel=channel, component=component, component_name=component_name)
        query_string = await create_query_string(entity_name=entity_name, entity_id=entity_id, channel=channel, component=component, component_name=component_name)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/entity/detail", entity_name=entity_name, entity_id=entity_id, channel=channel, component=component, component_name=component_name), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import EntityResponse
            schema = EntityResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getentityDetail")
                print(e)

        return response
    