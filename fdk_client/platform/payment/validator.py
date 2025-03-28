

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
         
        
    
    class updatePayouts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class activateAndDectivatePayouts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class deletePayouts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
        
    
    class getAllPayout(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
        
        unique_external_id = fields.Str(required=False)
         
        
    
    class savePayouts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
        
    
    class updatePayout(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
        
    
    class activateAndDectivatePayout(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
        
    
    class deletePayout(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
        
    
    class verifyIfscCode(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        ifsc_code = fields.Str(required=False)
         
        
    
    class getPaymentMethodConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    

