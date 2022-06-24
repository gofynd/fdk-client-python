"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .EntityChargePrice import EntityChargePrice








class OneTimeChargeItem(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    term = fields.Str(required=False)
    
    pricing_type = fields.Str(required=False)
    
    price = fields.Nested(EntityChargePrice, required=False)
    
    capped_amount = fields.Float(required=False)
    
    is_test = fields.Boolean(required=False)
    
    metadata = fields.Dict(required=False)
    

