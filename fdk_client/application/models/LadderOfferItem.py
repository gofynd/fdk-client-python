"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .LadderPrice import LadderPrice




class LadderOfferItem(BaseSchema):
    # Cart swagger.json

    
    total = fields.Float(required=False)
    
    type = fields.Str(required=False)
    
    margin = fields.Int(required=False)
    
    price = fields.Nested(LadderPrice, required=False)
    
    quantity = fields.Int(required=False)
    

