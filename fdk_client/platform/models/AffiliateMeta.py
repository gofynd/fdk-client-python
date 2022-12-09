"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class AffiliateMeta(BaseSchema):
    # Order swagger.json

    
    employee_discount = fields.Float(required=False)
    
    channel_shipment_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    channel_order_id = fields.Str(required=False)
    
    order_item_id = fields.Str(required=False)
    
    due_date = fields.Str(required=False)
    
    box_type = fields.Str(required=False)
    
    is_priority = fields.Boolean(required=False)
    
    coupon_code = fields.Str(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    size_level_total_qty = fields.Int(required=False)
    

