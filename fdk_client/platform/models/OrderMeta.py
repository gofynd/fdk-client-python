"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class OrderMeta(BaseSchema):
    # Order swagger.json

    
    order_platform = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False)
    
    order_type = fields.Str(required=False)
    
    employee_id = fields.Str(required=False)
    
    payment_type = fields.Str(required=False)
    
    staff = fields.Dict(required=False)
    
    order_child_entities = fields.List(fields.Str(required=False), required=False)
    
    extra_meta = fields.Dict(required=False)
    
    mongo_cart_id = fields.Raw(required=False)
    
    files = fields.List(fields.Str(required=False), required=False)
    
    comment = fields.Str(required=False)
    

