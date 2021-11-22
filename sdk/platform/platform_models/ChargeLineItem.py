"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *







from .EntityChargePrice import EntityChargePrice

from .EntityChargeRecurring import EntityChargeRecurring










class ChargeLineItem(Schema):

    
    name = fields.Str(required=False)
    
    term = fields.Str(required=False)
    
    pricing_type = fields.Str(required=False)
    
    price = fields.Nested(EntityChargePrice, required=False)
    
    recurring = fields.Nested(EntityChargeRecurring, required=False)
    
    capped_amount = fields.Float(required=False)
    
    trial_days = fields.Int(required=False)
    
    is_test = fields.Boolean(required=False)
    
    metadata = fields.Dict(required=False)
    

