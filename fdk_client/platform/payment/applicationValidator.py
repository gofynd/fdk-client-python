

"""Payment Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        

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
         
        
    
    class addBeneficiaryDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
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
         
        
    
    

