"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class OrderBrandName(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
