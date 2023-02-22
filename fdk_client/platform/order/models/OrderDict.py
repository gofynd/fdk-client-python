"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Prices import Prices



from .OrderMeta import OrderMeta









class OrderDict(BaseSchema):
    #  swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    meta = fields.Nested(OrderMeta, required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    order_date = fields.Str(required=False)
    
