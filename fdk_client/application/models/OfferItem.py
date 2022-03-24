"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .OfferPrice import OfferPrice


class OfferItem(BaseSchema):
    # Cart swagger.json

    
    auto_applied = fields.Boolean(required=False)
    
    total = fields.Float(required=False)
    
    best = fields.Boolean(required=False)
    
    margin = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Nested(OfferPrice, required=False)
    

