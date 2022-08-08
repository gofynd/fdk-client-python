"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



























from .EntityChargePrice import EntityChargePrice


class OneTimeChargeEntity(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    activated_on = fields.Str(required=False)
    
    cancelled_on = fields.Str(required=False)
    
    metadata = fields.Dict(required=False)
    
    return_url = fields.Str(required=False)
    
    is_test = fields.Boolean(required=False)
    
    pricing_type = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    price = fields.Nested(EntityChargePrice, required=False)
    

