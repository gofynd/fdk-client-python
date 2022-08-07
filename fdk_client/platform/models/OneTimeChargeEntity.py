"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .OneTimeCharge import OneTimeCharge


class OneTimeChargeEntity(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    activated_on = fields.Str(required=False)
    
    cancelled_on = fields.Str(required=False)
    
    metadata = fields.Dict(required=False)
    
    line_items = fields.List(fields.Nested(OneTimeCharge, required=False), required=False)
    

