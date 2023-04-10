"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class CartList(BaseSchema):
    # Cart swagger.json

    
    user_id = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    cart_value = fields.Float(required=False)
    
    item_counts = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    

