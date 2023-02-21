"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class PaymentValidator:
    
    class getBrandPaymentGatewayConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class saveBrandPaymentGatewayConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateBrandPaymentGatewayConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getPaymentModeRoutes(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        request_type = fields.Str(required=False)
         
    
    class getAllPayouts(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_external_id = fields.Str(required=False)
         
    
    class savePayout(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class updatePayout(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
    
    class activateAndDectivatePayout(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
    
    class deletePayout(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
    
    class getSubscriptionPaymentMethod(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_external_id = fields.Str(required=False)
         
    
    class deleteSubscriptionPaymentMethod(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_external_id = fields.Str(required=False)
        
        payment_method_id = fields.Str(required=False)
         
    
    class getSubscriptionConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class saveSubscriptionSetupIntent(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getBankAccountDetailsOpenAPI(BaseSchema):
        
        order_id = fields.Str(required=False)
        
        request_hash = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class addRefundBankAccountUsingOTP(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class verifyIfscCode(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        ifsc_code = fields.Str(required=False)
         
    
    class getUserOrderBeneficiaries(BaseSchema):
        
        order_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getUserBeneficiaries(BaseSchema):
        
        order_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class confirmPayment(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getPlatformPaymentConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updatePlatformPaymentConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getUserCODlimitRoutes(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        merchant_user_id = fields.Str(required=False)
        
        mobile_no = fields.Str(required=False)
         
    
    class setUserCODlimitRoutes(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class edcDevice(BaseSchema):
        
        terminal_serial_no = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class edcDevice(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class edcDevice(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class edcDeviceList(BaseSchema):
        
        page_number = fields.Int(required=False)
        
        is_active = fields.Boolean(required=False)
        
        store_id = fields.Int(required=False)
        
        device_tag = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getPosPaymentModeRoutes(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        amount = fields.Int(required=False)
        
        cart_id = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        card_reference = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
        
        user_details = fields.Str(required=False)
         
    
    class initialisePayment(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class checkAndUpdatePaymentStatus(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class resendOrCancelPayment(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    