"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class DomainSuggestion(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    unsupported = fields.Boolean(required=False)
    
    is_available = fields.Boolean(required=False)
    
    price = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
