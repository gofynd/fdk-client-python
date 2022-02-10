"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Currency import Currency

from .LadderPriceOffer import LadderPriceOffer


class LadderPriceOffers(BaseSchema):
    # Cart swagger.json

    
    currency = fields.Nested(Currency, required=False)
    
    available_offers = fields.List(fields.Nested(LadderPriceOffer, required=False), required=False)
    

