"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderMeta import OrderMeta

from .Prices import Prices










class OrderDict(BaseSchema):
    # Order swagger.json

    
    meta = fields.Nested(OrderMeta, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    tax_details = fields.Dict(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    order_date = fields.Str(required=False)
    

