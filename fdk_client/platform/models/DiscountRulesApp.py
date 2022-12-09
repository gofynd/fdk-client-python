"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class DiscountRulesApp(BaseSchema):
    # Cart swagger.json

    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    
    item_criteria = fields.Dict(required=False)
    
    raw_offer = fields.Dict(required=False)
    
    offer = fields.Dict(required=False)
    

