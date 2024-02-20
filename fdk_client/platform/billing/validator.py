

"""Billing Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
    
    
        
        
    
    
        
    
    
        
    
    
        
    
    
        
        
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
        
        
        
        
        
    
    
        
        
    
    
        
    
    
        
        
        
        
    
    
        
        
    
    
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        



class BillingValidator:
    
    
    class checkCouponValidity(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        plan = fields.Str(required=False)
        
        coupon_code = fields.Str(required=False)
         
        
    
    class createSubscriptionCharge(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class getSubscriptionCharge(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        subscription_id = fields.Str(required=False)
         
        
    
    class cancelSubscriptionCharge(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        subscription_id = fields.Str(required=False)
         
        
    
    class createOneTimeCharge(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class getChargeDetails(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        charge_id = fields.Str(required=False)
         
        
    
    class getInvoices(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getInvoiceById(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        invoice_id = fields.Str(required=False)
         
        
    
    class getCustomerDetail(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class upsertCustomerDetail(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getSubscription(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getFeatureLimitConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        product_suite = fields.Str(required=False)
        
        type = fields.Str(required=False)
         
        
    
    class activateSubscriptionPlan(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class cancelSubscriptionPlan(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getEnterprisePlans(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class planStatusUpdate(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class subscripePlan(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getentityDetail(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        entity_name = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        channel = fields.Str(required=False)
        
        component = fields.Str(required=False)
        
        component_name = fields.Str(required=False)
         
        
    
    class paymentOptions(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        code = fields.Str(required=False)
         
        
    
    class verifyPayment(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class globalSettings(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        query = fields.Dict(required=False)
         
        
    
    class subscriptionMethods(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        unique_external_id = fields.Dict(required=False)
         
        
    
    class subscriptionConfigs(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class subscriptionPlanChange(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        product_suite = fields.Str(required=False)
        
        unique_id = fields.Int(required=False)
        
        platform = fields.Str(required=False)
         
        
    
    class getPaymentTransaction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        transactionId = fields.Str(required=False)
         
        
    
    class getPaymentOptions(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        transaction_id = fields.Str(required=False)
         
        
    
    

