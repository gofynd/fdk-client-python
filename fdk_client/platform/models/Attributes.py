"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class Attributes(BaseSchema):
    # Order swagger.json

    
    essential = fields.Str(required=False)
    
    marketer_address = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    primary_color = fields.Str(required=False)
    
    primary_material = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    marketer_name = fields.Str(required=False)
    
    gender = fields.List(fields.Str(required=False), required=False)
    
    primary_color_hex = fields.Str(required=False)
    

