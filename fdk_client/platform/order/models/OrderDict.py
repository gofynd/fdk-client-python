"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .OrderMeta import OrderMeta





class OrderDict(BaseSchema):
    #  swagger.json

    
    fynd_order_id = fields.Str(required=False)
    
    order_date = fields.Str(required=False)
    
    shipment_count = fields.Int(required=False)
    
    meta = fields.Nested(OrderMeta, required=False)
    
    payment_methods = fields.Dict(required=False)
    
