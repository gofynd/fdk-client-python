"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















class Attributes(BaseSchema):
    #  swagger.json

    
    brand_name = fields.Str(required=False)
    
    primary_color_hex = fields.Str(required=False)
    
    gender = fields.List(fields.Str(required=False), required=False)
    
    marketer_address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    essential = fields.Str(required=False)
    
    marketer_name = fields.Str(required=False)
    
    primary_color = fields.Str(required=False)
    
    primary_material = fields.Str(required=False)
    
