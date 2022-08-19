"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderConfig import OrderConfig



from .OrderInfo import OrderInfo


class CreateOrderPayload(BaseSchema):
    # Order swagger.json

    
    order_config = fields.Nested(OrderConfig, required=False)
    
    affiliate_id = fields.Str(required=False)
    
    order_info = fields.Nested(OrderInfo, required=False)
    

