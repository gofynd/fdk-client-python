"""Billing Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import BillingValidator

class Billing:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getCustomerDetail(self, request_headers:Dict={}):
        """Obtain customer-related billing information.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getCustomerDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Allows you to modify or insert customer information in the billing system.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.upsertCustomerDetail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionCustomerCreate
        schema = SubscriptionCustomerCreate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        """Retrieve details of a customer's subscription information.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getSubscription()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionStatus
            schema = SubscriptionStatus()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSubscription")
                print(e)

        return response
    
    async def currentAppLimit(self, product_suite=None, type=None, request_headers:Dict={}):
        """Retrieve configuration settings for feature limits in subscription plans.
        :param product_suite :  : type string
        :param type :  : type string
        """
        payload = {}
        
        if product_suite is not None:
            payload["product_suite"] = product_suite
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = BillingValidator.currentAppLimit()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current-app-limit", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"product_suite","schema":{"type":"string"}},{"in":"query","name":"type","schema":{"type":"string"}}],"query":[{"in":"query","name":"product_suite","schema":{"type":"string"}},{"in":"query","name":"type","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", product_suite=product_suite, type=type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current-app-limit", product_suite=product_suite, type=type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionLimit
            schema = SubscriptionLimit()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for currentAppLimit")
                print(e)

        return response
    
    async def currentLimit(self, product_suite=None, type=None, request_headers:Dict={}):
        """Retrieve configuration settings for feature limits in subscription plans.
        :param product_suite :  : type string
        :param type :  : type string
        """
        payload = {}
        
        if product_suite is not None:
            payload["product_suite"] = product_suite
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = BillingValidator.currentLimit()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current-limit", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"product_suite","schema":{"type":"string"}},{"in":"query","name":"type","schema":{"type":"string"}}],"query":[{"in":"query","name":"product_suite","schema":{"type":"string"}},{"in":"query","name":"type","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", product_suite=product_suite, type=type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current-limit", product_suite=product_suite, type=type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionLimit
            schema = SubscriptionLimit()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for currentLimit")
                print(e)

        return response
    
    async def getInvoices(self, request_headers:Dict={}):
        """Retrieve invoices for billing and payment tracking.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getInvoices()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/list", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/list", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Invoices
            schema = Invoices()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInvoices")
                print(e)

        return response
    
    async def globalSettings(self, page_no=None, page_size=None, query=None, request_headers:Dict={}):
        """API to get global settings details.
        :param page_no : number of pages needed : type integer
        :param page_size : number of items to be there in page : type integer
        :param query : field which will be used in db query : type object
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = BillingValidator.globalSettings()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/global-settings", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"query","name":"page_no","description":"number of pages needed","required":true,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"number of items to be there in page","required":true,"schema":{"type":"integer"}},{"in":"query","name":"query","description":"field which will be used in db query","required":true,"schema":{"type":"object"}}],"optional":[],"query":[{"in":"query","name":"page_no","description":"number of pages needed","required":true,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"number of items to be there in page","required":true,"schema":{"type":"integer"}},{"in":"query","name":"query","description":"field which will be used in db query","required":true,"schema":{"type":"object"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, query=query)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/global-settings", page_no=page_no, page_size=page_size, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GlobalSettings
            schema = GlobalSettings()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for globalSettings")
                print(e)

        return response
    
    async def checkCouponValidity(self, plan=None, coupon_code=None, request_headers:Dict={}):
        """Checks whether a coupon code is valid for discounts while billing.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/coupon/check-validity", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"query","name":"plan","description":"ID of the plan.","required":true,"schema":{"type":"string"}},{"in":"query","name":"coupon_code","description":"Coupon code.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"plan","description":"ID of the plan.","required":true,"schema":{"type":"string"}},{"in":"query","name":"coupon_code","description":"Coupon code.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", plan=plan, coupon_code=coupon_code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/coupon/check-validity", plan=plan, coupon_code=coupon_code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CheckValidityResponse
            schema = CheckValidityResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkCouponValidity")
                print(e)

        return response
    
    async def paymentStatus(self, order_id=None, request_headers:Dict={}):
        """Credit Transaction
        :param order_id : Unique ID of the company : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id

        # Parameter validation
        schema = BillingValidator.paymentStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/payment-status", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"query","required":true,"schema":{"type":"string"},"description":"Unique ID of the company"}],"optional":[],"query":[{"name":"order_id","in":"query","required":true,"schema":{"type":"string"},"description":"Unique ID of the company"}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/payment-status", order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentStatusResponse
            schema = PaymentStatusResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for paymentStatus")
                print(e)

        return response
    
    async def creditTransaction(self, unique_id=None, product_suite=None, type=None, page_size=None, page_no=None, start_date=None, end_date=None, search_type=None, search_value=None, request_headers:Dict={}):
        """Credit Transaction
        :param unique_id : Unique ID of the company : type integer
        :param product_suite : Product suite : type string
        :param type : Type of the company : type string
        :param page_size : Number of items per page : type integer
        :param page_no : Page number : type integer
        :param start_date : Start date : type string
        :param end_date : End date : type string
        :param search_type : Search Type : type string
        :param search_value : Search Value : type string
        """
        payload = {}
        
        if unique_id is not None:
            payload["unique_id"] = unique_id
        if product_suite is not None:
            payload["product_suite"] = product_suite
        if type is not None:
            payload["type"] = type
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date
        if search_type is not None:
            payload["search_type"] = search_type
        if search_value is not None:
            payload["search_value"] = search_value

        # Parameter validation
        schema = BillingValidator.creditTransaction()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/credit-transaction", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"name":"unique_id","in":"query","required":true,"schema":{"type":"integer"},"description":"Unique ID of the company"},{"name":"product_suite","in":"query","required":true,"schema":{"type":"string"},"description":"Product suite"},{"name":"type","in":"query","required":true,"schema":{"type":"string"},"description":"Type of the company"}],"optional":[{"name":"page_size","in":"query","required":false,"schema":{"type":"integer"},"description":"Number of items per page"},{"name":"page_no","in":"query","required":false,"schema":{"type":"integer"},"description":"Page number"},{"name":"start_date","in":"query","required":false,"schema":{"type":"string"},"description":"Start date"},{"name":"end_date","in":"query","required":false,"schema":{"type":"string"},"description":"End date"},{"name":"search_type","in":"query","required":false,"schema":{"type":"string"},"description":"Search Type"},{"name":"search_value","in":"query","required":false,"schema":{"type":"string"},"description":"Search Value"}],"query":[{"name":"unique_id","in":"query","required":true,"schema":{"type":"integer"},"description":"Unique ID of the company"},{"name":"product_suite","in":"query","required":true,"schema":{"type":"string"},"description":"Product suite"},{"name":"type","in":"query","required":true,"schema":{"type":"string"},"description":"Type of the company"},{"name":"page_size","in":"query","required":false,"schema":{"type":"integer"},"description":"Number of items per page"},{"name":"page_no","in":"query","required":false,"schema":{"type":"integer"},"description":"Page number"},{"name":"start_date","in":"query","required":false,"schema":{"type":"string"},"description":"Start date"},{"name":"end_date","in":"query","required":false,"schema":{"type":"string"},"description":"End date"},{"name":"search_type","in":"query","required":false,"schema":{"type":"string"},"description":"Search Type"},{"name":"search_value","in":"query","required":false,"schema":{"type":"string"},"description":"Search Value"}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", unique_id=unique_id, product_suite=product_suite, type=type, page_size=page_size, page_no=page_no, start_date=start_date, end_date=end_date, search_type=search_type, search_value=search_value)
        query_string = await create_query_string(unique_id=unique_id, product_suite=product_suite, type=type, page_size=page_size, page_no=page_no, start_date=start_date, end_date=end_date, search_type=search_type, search_value=search_value)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/credit-transaction", unique_id=unique_id, product_suite=product_suite, type=type, page_size=page_size, page_no=page_no, start_date=start_date, end_date=end_date, search_type=search_type, search_value=search_value), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreditTransactionResponse
            schema = CreditTransactionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for creditTransaction")
                print(e)

        return response
    
    async def updateConsent(self, subscriber_id=None, request_headers:Dict={}):
        """Update Consent
        :param subscriber_id : Customer unique id. In case of company it will be company id. : type string
        """
        payload = {}
        
        if subscriber_id is not None:
            payload["subscriber_id"] = subscriber_id

        # Parameter validation
        schema = BillingValidator.updateConsent()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/consent", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"query","name":"subscriber_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"subscriber_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", subscriber_id=subscriber_id)
        query_string = await create_query_string(subscriber_id=subscriber_id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/consent", subscriber_id=subscriber_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StatusMessage
            schema = StatusMessage()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateConsent")
                print(e)

        return response
    
    async def getEnterprisePlans(self, request_headers:Dict={}):
        """Retrieve available enterprise-level subscription plans.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getEnterprisePlans()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/plans", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/plans", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def subscriptionConfigs(self, request_headers:Dict={}):
        """API to get subscription config details.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.subscriptionConfigs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/configs", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/configs", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigRes
            schema = ConfigRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for subscriptionConfigs")
                print(e)

        return response
    
    async def getBankList(self, request_headers:Dict={}):
        """Get Bank List
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getBankList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/bank/list", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/bank/list", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getPaymentTransaction(self, transaction_id=None, request_headers:Dict={}):
        """API to get payment transaction details.
        :param transaction_id : Payment Transaction unique id. : type string
        """
        payload = {}
        
        if transaction_id is not None:
            payload["transaction_id"] = transaction_id

        # Parameter validation
        schema = BillingValidator.getPaymentTransaction()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/transaction/{transaction_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"transaction_id","description":"Payment Transaction unique id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"transaction_id","description":"Payment Transaction unique id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", transaction_id=transaction_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/transaction/{transaction_id}", transaction_id=transaction_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentTransactionDetails
            schema = PaymentTransactionDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentTransaction")
                print(e)

        return response
    
    async def getPaymentOptions(self, transaction_id=None, request_headers:Dict={}):
        """API to get payment options.
        :param transaction_id : ID of the payment transaction. : type string
        """
        payload = {}
        
        if transaction_id is not None:
            payload["transaction_id"] = transaction_id

        # Parameter validation
        schema = BillingValidator.getPaymentOptions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/options", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"query","name":"transaction_id","description":"ID of the payment transaction.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"transaction_id","description":"ID of the payment transaction.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", transaction_id=transaction_id)
        query_string = await create_query_string(transaction_id=transaction_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/options", transaction_id=transaction_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetPaymentOptions
            schema = GetPaymentOptions()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPaymentOptions")
                print(e)

        return response
    
    async def paymentInitiate(self, body="", request_headers:Dict={}):
        """Initiate Payment.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.paymentInitiate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscribePlan
        schema = SubscribePlan()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/initiate", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/initiate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscribePlanRes
            schema = SubscribePlanRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for paymentInitiate")
                print(e)

        return response
    
    async def planStatusUpdate(self, body="", request_headers:Dict={}):
        """Modify the status of a subscription plan.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.planStatusUpdate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlanStatusUpdateReq
        schema = PlanStatusUpdateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/plan/status", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/plan/status", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Plan
            schema = Plan()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for planStatusUpdate")
                print(e)

        return response
    
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
    
    async def upgradePlan(self, body="", request_headers:Dict={}):
        """Admin user can modify the subscription plan for an seller account.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.upgradePlan()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionMethodsReq
        schema = SubscriptionMethodsReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/methods", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/methods", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResourceNotFound
            schema = ResourceNotFound()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for upgradePlan")
                print(e)

        return response
    
    async def subscriptionMethods(self, unique_external_id=None, request_headers:Dict={}):
        """API to get subscription methods.
        :param unique_external_id : unique id for external company : type string
        """
        payload = {}
        
        if unique_external_id is not None:
            payload["unique_external_id"] = unique_external_id

        # Parameter validation
        schema = BillingValidator.subscriptionMethods()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/methods", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"query","name":"unique_external_id","description":"unique id for external company","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"unique_external_id","description":"unique id for external company","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", unique_external_id=unique_external_id)
        query_string = await create_query_string(unique_external_id=unique_external_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/methods", unique_external_id=unique_external_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionMethods
            schema = SubscriptionMethods()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for subscriptionMethods")
                print(e)

        return response
    
    async def subscriptionMethodsDelete(self, unique_external_id=None, payment_method_id=None, request_headers:Dict={}):
        """API to get subscription methods.
        :param unique_external_id : unique id for external company : type string
        :param payment_method_id : payment method id : type string
        """
        payload = {}
        
        if unique_external_id is not None:
            payload["unique_external_id"] = unique_external_id
        if payment_method_id is not None:
            payload["payment_method_id"] = payment_method_id

        # Parameter validation
        schema = BillingValidator.subscriptionMethodsDelete()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/methods", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"query","name":"unique_external_id","description":"unique id for external company","required":true,"schema":{"type":"string"}},{"in":"query","name":"payment_method_id","description":"payment method id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"unique_external_id","description":"unique id for external company","required":true,"schema":{"type":"string"}},{"in":"query","name":"payment_method_id","description":"payment method id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", unique_external_id=unique_external_id, payment_method_id=payment_method_id)
        query_string = await create_query_string(unique_external_id=unique_external_id, payment_method_id=payment_method_id)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/methods", unique_external_id=unique_external_id, payment_method_id=payment_method_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResourceNotFound
            schema = ResourceNotFound()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for subscriptionMethodsDelete")
                print(e)

        return response
    
    async def planDowngradeGet(self, request_headers:Dict={}):
        """Get plan change downgrade
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.planDowngradeGet()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/plan-change/downgrade", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/plan-change/downgrade", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DowngradeRes
            schema = DowngradeRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for planDowngradeGet")
                print(e)

        return response
    
    async def planDowngrade(self, body="", request_headers:Dict={}):
        """Plan change downgrade
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.planDowngrade()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DowngradePlanReq
        schema = DowngradePlanReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/plan-change/downgrade", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/plan-change/downgrade", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PostDowngradeRes
            schema = PostDowngradeRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for planDowngrade")
                print(e)

        return response
    
    async def subscriptionPlanChange(self, product_suite=None, coupon=None, unique_id=None, platform=None, plan_id=None, request_headers:Dict={}):
        """API to get plan change details of subscription.
        :param product_suite :  : type string
        :param coupon :  : type string
        :param unique_id :  : type integer
        :param platform :  : type string
        :param plan_id :  : type string
        """
        payload = {}
        
        if product_suite is not None:
            payload["product_suite"] = product_suite
        if coupon is not None:
            payload["coupon"] = coupon
        if unique_id is not None:
            payload["unique_id"] = unique_id
        if platform is not None:
            payload["platform"] = platform
        if plan_id is not None:
            payload["plan_id"] = plan_id

        # Parameter validation
        schema = BillingValidator.subscriptionPlanChange()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/plan-change", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"product_suite","schema":{"type":"string"}},{"in":"query","name":"coupon","required":false,"schema":{"type":"string"}},{"in":"query","name":"unique_id","schema":{"type":"integer"}},{"in":"query","name":"platform","schema":{"type":"string"}},{"in":"query","name":"plan_id","schema":{"type":"string"}}],"query":[{"in":"query","name":"product_suite","schema":{"type":"string"}},{"in":"query","name":"coupon","required":false,"schema":{"type":"string"}},{"in":"query","name":"unique_id","schema":{"type":"integer"}},{"in":"query","name":"platform","schema":{"type":"string"}},{"in":"query","name":"plan_id","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", product_suite=product_suite, coupon=coupon, unique_id=unique_id, platform=platform, plan_id=plan_id)
        query_string = await create_query_string(product_suite=product_suite, coupon=coupon, unique_id=unique_id, platform=platform, plan_id=plan_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/plan-change", product_suite=product_suite, coupon=coupon, unique_id=unique_id, platform=platform, plan_id=plan_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlanChangeDetails
            schema = PlanChangeDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for subscriptionPlanChange")
                print(e)

        return response
    
    async def changePlan(self, body="", request_headers:Dict={}):
        """Admin user can modify the subscription plan for an seller account.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.changePlan()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionActivateReq
        schema = SubscriptionActivateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/plan-change", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/plan-change", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionActivateRes
            schema = SubscriptionActivateRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for changePlan")
                print(e)

        return response
    
    async def activateSubscriptionPlan(self, body="", request_headers:Dict={}):
        """Activate a specific subscription plan for a customer.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.activateSubscriptionPlan()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionActivateReq
        schema = SubscriptionActivateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/activate", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/activate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionActivateRes
            schema = SubscriptionActivateRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for activateSubscriptionPlan")
                print(e)

        return response
    
    async def methodDefault(self, body="", request_headers:Dict={}):
        """Method Default
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.methodDefault()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DefaultReq
        schema = DefaultReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/method/default", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/method/default", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Message
            schema = Message()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for methodDefault")
                print(e)

        return response
    
    async def topupCredit(self, body="", request_headers:Dict={}):
        """Topup
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.topupCredit()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TopupReq
        schema = TopupReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/topup", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/topup", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TopupRes
            schema = TopupRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for topupCredit")
                print(e)

        return response
    
    async def topupCancelCredit(self, body="", request_headers:Dict={}):
        """Cancel Topup
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.topupCancelCredit()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CancelTopupReq
        schema = CancelTopupReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/topup/cancel", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/topup/cancel", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CancelTopupRes
            schema = CancelTopupRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for topupCancelCredit")
                print(e)

        return response
    
    async def setupPayment(self, body="", request_headers:Dict={}):
        """Setup Payment
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.setupPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SetupPaymentReq
        schema = SetupPaymentReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/setup/payment", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/setup/payment", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SetupPayment
            schema = SetupPayment()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setupPayment")
                print(e)

        return response
    
    async def setupMandate(self, body="", request_headers:Dict={}):
        """Setup Mandate
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.setupMandate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SetupMandateReq
        schema = SetupMandateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/setup/mandate", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/setup/mandate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Message
            schema = Message()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setupMandate")
                print(e)

        return response
    
    async def setupIntent(self, body="", request_headers:Dict={}):
        """Setup Intent
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.setupIntent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import IntentReq
        schema = IntentReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/setup/intent", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/setup/intent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SetupIntentRes
            schema = SetupIntentRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setupIntent")
                print(e)

        return response
    
    async def updateSetupIntent(self, body="", request_headers:Dict={}):
        """Setup Intent
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.updateSetupIntent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PutIntentReq
        schema = PutIntentReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/setup/intent", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/setup/intent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StatusMessage
            schema = StatusMessage()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSetupIntent")
                print(e)

        return response
    
    async def subscriptionRenew(self, body="", request_headers:Dict={}):
        """Subscription Renew
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.subscriptionRenew()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionRenewReq
        schema = SubscriptionRenewReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/renew", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/renew", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriptionRenewRes
            schema = SubscriptionRenewRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for subscriptionRenew")
                print(e)

        return response
    
    async def paymentCollect(self, body="", request_headers:Dict={}):
        """Payment Collect
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.paymentCollect()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PaymentCollectReq
        schema = PaymentCollectReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/collect", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/payment/collect", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentCollectRes
            schema = PaymentCollectRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for paymentCollect")
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/entity/detail", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"query","name":"entity_name","description":"Entity name.","required":true,"schema":{"type":"string"}},{"in":"query","name":"channel","description":"Ordering channel.","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"entity_id","description":"Entity unique id.","required":false,"schema":{"type":"string"}},{"in":"query","name":"component","description":"The coponents the user would like to know.","required":false,"schema":{"type":"string"}},{"in":"query","name":"component_name","description":"The name of component the preferred to be fetched.","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"entity_name","description":"Entity name.","required":true,"schema":{"type":"string"}},{"in":"query","name":"entity_id","description":"Entity unique id.","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel","description":"Ordering channel.","required":true,"schema":{"type":"string"}},{"in":"query","name":"component","description":"The coponents the user would like to know.","required":false,"schema":{"type":"string"}},{"in":"query","name":"component_name","description":"The name of component the preferred to be fetched.","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", entity_name=entity_name, entity_id=entity_id, channel=channel, component=component, component_name=component_name)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/entity/detail", entity_name=entity_name, entity_id=entity_id, channel=channel, component=component, component_name=component_name), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def cancelSubscriptionPlan(self, body="", request_headers:Dict={}):
        """Cancel an active subscription plan for a customer
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.cancelSubscriptionPlan()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CancelSubscriptionReq
        schema = CancelSubscriptionReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/cancel", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/cancel", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CancelSubscriptionRes
            schema = CancelSubscriptionRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelSubscriptionPlan")
                print(e)

        return response
    
    async def paymentOptions(self, code=None, request_headers:Dict={}):
        """API to get payment details of requested payment options.
        :param code : Payment options unique code. : type string
        """
        payload = {}
        
        if code is not None:
            payload["code"] = code

        # Parameter validation
        schema = BillingValidator.paymentOptions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/payment-options", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"query","name":"code","description":"Payment options unique code.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"code","description":"Payment options unique code.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", code=code)
        query_string = await create_query_string(code=code)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/payment-options", code=code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentOptions
            schema = PaymentOptions()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for paymentOptions")
                print(e)

        return response
    
    async def verifyPayment(self, body="", request_headers:Dict={}):
        """API to verify subscription payment.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.verifyPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyPaymentReq
        schema = VerifyPaymentReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/verify-payment", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/verify-payment", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyPaymentRes
            schema = VerifyPaymentRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyPayment")
                print(e)

        return response
    
    async def getInvoiceById(self, invoice_id=None, request_headers:Dict={}):
        """Retrieve a particular invoice's details by providing its unique ID.
        :param invoice_id : Invoice id : type string
        """
        payload = {}
        
        if invoice_id is not None:
            payload["invoice_id"] = invoice_id

        # Parameter validation
        schema = BillingValidator.getInvoiceById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/{invoice_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"invoice_id","description":"Invoice id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string"}},{"in":"path","name":"invoice_id","description":"Invoice id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", invoice_id=invoice_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/{invoice_id}", invoice_id=invoice_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InvoiceData
            schema = InvoiceData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInvoiceById")
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
    