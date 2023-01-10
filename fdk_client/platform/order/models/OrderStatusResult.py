"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .OrderStatusData import OrderStatusData



class OrderStatusResult(BaseSchema):
    #  swagger.json

    
    success = fields.Str(required=False)
    
    result = fields.List(fields.Nested(OrderStatusData, required=False), required=False)
    
