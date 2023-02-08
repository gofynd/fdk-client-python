"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DiscountRules(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
