"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class LoyaltyPoints(BaseSchema):
    #  swagger.json

    
    applicable = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    