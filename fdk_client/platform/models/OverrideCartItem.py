"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .OverrideCartItemPromo import OverrideCartItemPromo




class OverrideCartItem(BaseSchema):
    # Cart swagger.json

    
    amount_paid = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    item_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    price_marked = fields.Float(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    price_effective = fields.Float(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    promo_list = fields.List(fields.Nested(OverrideCartItemPromo, required=False), required=False)
    
    size = fields.Str(required=False)
    

