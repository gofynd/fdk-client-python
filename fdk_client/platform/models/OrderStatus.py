"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .FyndOrderIdList import FyndOrderIdList






class OrderStatus(BaseSchema):
    # Order swagger.json

    
    end_date = fields.Str(required=False)
    
    order_details = fields.List(fields.Nested(FyndOrderIdList, required=False), required=False)
    
    start_date = fields.Str(required=False)
    
    mobile = fields.Int(required=False)
    

