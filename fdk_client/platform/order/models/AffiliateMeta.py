"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


























class AffiliateMeta(BaseSchema):
    #  swagger.json

    
    box_type = fields.Str(required=False)
    
    is_priority = fields.Boolean(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    employee_discount = fields.Float(required=False)
    
    size_level_total_qty = fields.Int(required=False)
    
    channel_shipment_id = fields.Str(required=False)
    
    due_date = fields.Str(required=False)
    
    order_item_id = fields.Str(required=False)
    
    channel_order_id = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
