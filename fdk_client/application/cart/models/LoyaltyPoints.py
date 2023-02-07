"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class LoyaltyPoints(BaseSchema):
    #  swagger.json

    
    description = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    applicable = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
