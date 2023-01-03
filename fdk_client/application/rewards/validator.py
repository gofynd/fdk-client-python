

"""Rewards Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
        

class RewardsValidator:
    
    
    class getOfferByName(BaseSchema):
        
        
        name = fields.Str(required=False)
         
        
    
    


