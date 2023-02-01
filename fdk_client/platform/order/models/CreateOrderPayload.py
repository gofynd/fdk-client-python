"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .OrderConfig import OrderConfig



from .OrderInfo import OrderInfo





class CreateOrderPayload(BaseSchema):
    #  swagger.json

    
    order_config = fields.Nested(OrderConfig, required=False)
    
    order_info = fields.Nested(OrderInfo, required=False)
    
    affiliate_id = fields.Str(required=False)
    
