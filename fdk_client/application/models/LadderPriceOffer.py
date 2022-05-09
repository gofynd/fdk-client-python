"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .LadderOfferItem import LadderOfferItem








class LadderPriceOffer(BaseSchema):
    # Cart swagger.json

    
    promotion_group = fields.Str(required=False)
    
    valid_till = fields.Str(required=False)
    
    offer_prices = fields.List(fields.Nested(LadderOfferItem, required=False), required=False)
    
    description = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
