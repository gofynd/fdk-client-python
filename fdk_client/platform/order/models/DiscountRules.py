"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DiscountRules(BaseSchema):
    #  swagger.json

    
    value = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
