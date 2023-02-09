"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class LogisticValidator:
    
    class getPincodeCity(BaseSchema):
        
        pincode = fields.Str(required=False)
        
        country_code = fields.Str(required=False)
         
    
    class getTatProduct(BaseSchema):
        
        pass 
    
    class getEntityList(BaseSchema):
        
        page = fields.Str(required=False)
        
        limit = fields.Str(required=False)
         
    
    class getPincodeZones(BaseSchema):
        
        pass 
    