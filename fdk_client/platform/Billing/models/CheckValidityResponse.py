"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CheckValidityResponse(BaseSchema):
    #  swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    discount_amount = fields.Float(required=False)
    
