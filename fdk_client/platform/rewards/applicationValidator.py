

"""Rewards Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
        

class RewardsValidator:
    
    
    class getOfferByName(BaseSchema):
        
        
        name = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        cookie = fields.Str(required=False)
         
        
    
    

