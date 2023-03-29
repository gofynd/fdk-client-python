"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Prices import Prices

from .OrderMeta import OrderMeta




class OrderDict(BaseSchema):
    # Order swagger.json

    
    fynd_order_id = fields.Str(required=False)
    
    tax_details = fields.Dict(required=False)
    
    order_date = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    meta = fields.Nested(OrderMeta, required=False)
    
    payment_methods = fields.Dict(required=False)
    

