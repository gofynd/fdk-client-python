"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .OrderMeta import OrderMeta







from .Prices import Prices





class OrderDict(BaseSchema):
    #  swagger.json

    
    meta = fields.Nested(OrderMeta, required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    order_date = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    payment_methods = fields.Dict(required=False)
    
