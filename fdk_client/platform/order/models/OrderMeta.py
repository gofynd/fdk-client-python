"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


































class OrderMeta(BaseSchema):
    #  swagger.json

    
    order_platform = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    customer_note = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    mongo_cart_id = fields.Int(required=False)
    
    ordering_store = fields.Int(required=False)
    
    files = fields.List(fields.Dict(required=False), required=False)
    
    order_child_entities = fields.List(fields.Str(required=False), required=False)
    
    payment_type = fields.Str(required=False)
    
    order_tags = fields.List(fields.Dict(required=False), required=False)
    
    order_type = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    staff = fields.Dict(required=False)
    
    employee_id = fields.Int(required=False)
    
