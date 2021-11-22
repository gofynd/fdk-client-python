"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .OfferPrice import OfferPrice












class OfferItem(Schema):

    
    auto_applied = fields.Boolean(required=False)
    
    price = fields.Nested(OfferPrice, required=False)
    
    type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    total = fields.Float(required=False)
    
    best = fields.Boolean(required=False)
    
    margin = fields.Int(required=False)
    

