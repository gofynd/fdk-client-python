"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












from .OfferPrice import OfferPrice







class OfferItem(BaseSchema):
    #  swagger.json

    
    margin = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    best = fields.Boolean(required=False)
    
    total = fields.Float(required=False)
    
    price = fields.Nested(OfferPrice, required=False)
    
    auto_applied = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
