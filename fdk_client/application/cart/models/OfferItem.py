"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












from .OfferPrice import OfferPrice







class OfferItem(BaseSchema):
    #  swagger.json

    
    auto_applied = fields.Boolean(required=False)
    
    total = fields.Float(required=False)
    
    type = fields.Str(required=False)
    
    best = fields.Boolean(required=False)
    
    price = fields.Nested(OfferPrice, required=False)
    
    quantity = fields.Int(required=False)
    
    margin = fields.Int(required=False)
    
