"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .LadderOfferItem import LadderOfferItem







class LadderPriceOffer(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    valid_till = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    offer_prices = fields.List(fields.Nested(LadderOfferItem, required=False), required=False)
    
    promotion_group = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
