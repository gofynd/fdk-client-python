"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .FyndOrderIdList import FyndOrderIdList







class OrderStatus(BaseSchema):
    #  swagger.json

    
    mobile = fields.Int(required=False)
    
    order_details = fields.List(fields.Nested(FyndOrderIdList, required=False), required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
