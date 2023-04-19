

"""Payment Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
    
    
        
    
    
        
        
    
    
        



class PaymentValidator:
    
    
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
         
        
    
    class verifyIfscCode(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        ifsc_code = fields.Str(required=False)
         
        
    
    class getPayoutPennyDropAndChequeConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    

