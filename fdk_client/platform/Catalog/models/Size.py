"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class Size(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    is_available = fields.Boolean(required=False)
    
