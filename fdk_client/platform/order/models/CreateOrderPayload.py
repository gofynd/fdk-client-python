"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .OrderInfo import OrderInfo



from .OrderConfig import OrderConfig



class CreateOrderPayload(BaseSchema):
    #  swagger.json

    
    affiliate_id = fields.Str(required=False)
    
    order_info = fields.Nested(OrderInfo, required=False)
    
    order_config = fields.Nested(OrderConfig, required=False)
    
