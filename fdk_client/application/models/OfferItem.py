"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .OfferPrice import OfferPrice








class OfferItem(BaseSchema):
    # Cart swagger.json

    
    total = fields.Float(required=False)
    
    best = fields.Boolean(required=False)
    
    auto_applied = fields.Boolean(required=False)
    
    price = fields.Nested(OfferPrice, required=False)
    
    margin = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
