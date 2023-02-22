

""" Billing Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import BillingValidator

class Billing:
    def __init__(self, config):
        self._conf = config
    
    async def checkCouponValidity(self, plan=None, coupon_code=None):
        """Check coupon validity.
        :param plan : ID of the plan. : type string
        :param coupon_code : Coupon code. : type string
        """
        payload = {}
        
        if plan:
            payload["plan"] = plan
        
        if coupon_code:
            payload["coupon_code"] = coupon_code
        

        # Parameter validation
        schema = BillingValidator.checkCouponValidity()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/coupon/check-validity", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"query","name":"plan","description":"ID of the plan.","required":true,"schema":{"type":"string","example":"61a5d6ea3e8c230f3aa2c507"}},{"in":"query","name":"coupon_code","description":"Coupon code.","required":true,"schema":{"type":"string","example":"FYND1"}}],"optional":[],"query":[{"in":"query","name":"plan","description":"ID of the plan.","required":true,"schema":{"type":"string","example":"61a5d6ea3e8c230f3aa2c507"}},{"in":"query","name":"coupon_code","description":"Coupon code.","required":true,"schema":{"type":"string","example":"FYND1"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", plan=plan, coupon_code=coupon_code)
        query_string = await create_query_string(plan=plan, coupon_code=coupon_code)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/coupon/check-validity", plan=plan, coupon_code=coupon_code), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createSubscriptionCharge(self, extension_id=None, body=""):
        """Register subscription charge for a seller of your extension.
        :param extension_id : Extension _id : type string
        """
        payload = {}
        
        if extension_id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSubscriptionCharge(self, extension_id=None, subscription_id=None):
        """Get created subscription charge details
        :param extension_id : Extension _id : type string
        :param subscription_id : Subscription charge _id : type string
        """
        payload = {}
        
        if extension_id:
            payload["extension_id"] = extension_id
        
        if subscription_id:
            payload["subscription_id"] = subscription_id
        

        # Parameter validation
        schema = BillingValidator.getSubscriptionCharge()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", extension_id=extension_id, subscription_id=subscription_id)
        query_string = await create_query_string(extension_id=extension_id, subscription_id=subscription_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}", extension_id=extension_id, subscription_id=subscription_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def cancelSubscriptionCharge(self, extension_id=None, subscription_id=None):
        """Cancel subscription and attached charges.
        :param extension_id : Extension _id : type string
        :param subscription_id : Subscription charge _id : type string
        """
        payload = {}
        
        if extension_id:
            payload["extension_id"] = extension_id
        
        if subscription_id:
            payload["subscription_id"] = subscription_id
        

        # Parameter validation
        schema = BillingValidator.cancelSubscriptionCharge()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}/cancel", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", extension_id=extension_id, subscription_id=subscription_id)
        query_string = await create_query_string(extension_id=extension_id, subscription_id=subscription_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}/cancel", extension_id=extension_id, subscription_id=subscription_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createOneTimeCharge(self, extension_id=None, body=""):
        """Register one time subscription charge for a seller of your extension.
        :param extension_id : Extension _id : type string
        """
        payload = {}
        
        if extension_id:
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/one_time_charge", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getChargeDetails(self, extension_id=None, charge_id=None):
        """Get created subscription charge details
        :param extension_id : Extension _id : type string
        :param charge_id : Standalone charge _id : type string
        """
        payload = {}
        
        if extension_id:
            payload["extension_id"] = extension_id
        
        if charge_id:
            payload["charge_id"] = charge_id
        

        # Parameter validation
        schema = BillingValidator.getChargeDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/charge/{charge_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"charge_id","description":"Standalone charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"charge_id","description":"Standalone charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", extension_id=extension_id, charge_id=charge_id)
        query_string = await create_query_string(extension_id=extension_id, charge_id=charge_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/charge/{charge_id}", extension_id=extension_id, charge_id=charge_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getInvoices(self, ):
        """Get invoices.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getInvoices()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/list", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/list", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getInvoiceById(self, invoice_id=None):
        """Get invoice by id.
        :param invoice_id : Invoice id : type string
        """
        payload = {}
        
        if invoice_id:
            payload["invoice_id"] = invoice_id
        

        # Parameter validation
        schema = BillingValidator.getInvoiceById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/{invoice_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"invoice_id","description":"Invoice id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"invoice_id","description":"Invoice id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", invoice_id=invoice_id)
        query_string = await create_query_string(invoice_id=invoice_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/{invoice_id}", invoice_id=invoice_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCustomerDetail(self, ):
        """Get subscription customer detail.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getCustomerDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def upsertCustomerDetail(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSubscription(self, ):
        """If subscription is active then it will return is_enabled true and return subscription object. If subscription is not active then is_enabled false and message.

        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getSubscription()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getFeatureLimitConfig(self, ):
        """Get subscription subscription limits.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getFeatureLimitConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current-limit", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current-limit", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def activateSubscriptionPlan(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/activate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def cancelSubscriptionPlan(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/cancel", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

