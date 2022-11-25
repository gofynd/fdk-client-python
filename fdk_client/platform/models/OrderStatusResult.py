"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OrderStatusData import OrderStatusData


class OrderStatusResult(BaseSchema):
    # OrderManage swagger.json

    
    success = fields.Str(required=False)
    
    result = fields.List(fields.Nested(OrderStatusData, required=False), required=False)
    

