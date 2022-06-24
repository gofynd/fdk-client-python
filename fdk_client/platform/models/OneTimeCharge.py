"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .EntityChargePrice import EntityChargePrice
















class OneTimeCharge(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    term = fields.Str(required=False)
    
    pricing_type = fields.Str(required=False)
    
    price = fields.Nested(EntityChargePrice, required=False)
    
    capped_amount = fields.Float(required=False)
    
    activated_on = fields.Str(required=False)
    
    cancelled_on = fields.Str(required=False)
    
    billing_date = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    is_test = fields.Boolean(required=False)
    
    metadata = fields.Dict(required=False)
    

