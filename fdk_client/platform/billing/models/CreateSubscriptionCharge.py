"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ChargeLineItem import ChargeLineItem







class CreateSubscriptionCharge(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    trial_days = fields.Int(required=False)
    
    line_items = fields.List(fields.Nested(ChargeLineItem, required=False), required=False)
    
    is_test = fields.Boolean(required=False)
    
    return_url = fields.Str(required=False)
    
