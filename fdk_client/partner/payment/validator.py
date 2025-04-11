

"""Payment Partner Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema



    
    
        
    
    
        
        
    
    
        
    
    
        
    
    
        
    
    
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        

class PaymentValidator:
    
    
    class getPaymentconfig(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class getPayout(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        unique_external_id = fields.Int(required=False)
         
        
    
    class postPayout(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class updatePayout(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class putPayout(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class deletePayout(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        unique_external_id = fields.Int(required=False)
         
        
    
    class getPayouts(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        unique_transfer_no = fields.Str(required=False)
        
        unique_external_id = fields.Int(required=False)
         
        
    
    class postPayouts(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
        
    
    class updatePayouts(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
        
    
    class putPayouts(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
        
    
    class deletePayouts(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        unique_transfer_no = fields.Int(required=False)
         
        
    
    

