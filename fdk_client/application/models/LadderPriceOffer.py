"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LadderOfferItem import LadderOfferItem


















class LadderPriceOffer(BaseSchema):
    # Cart swagger.json

    
    offer_prices = fields.List(fields.Nested(LadderOfferItem, required=False), required=False)
    
    description = fields.Str(required=False)
    
    valid_till = fields.Str(required=False)
    
    calculate_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    promotion_group = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Dict(required=False), required=False)
    
    offer_text = fields.Str(required=False)
    

