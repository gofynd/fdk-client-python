"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
























from .BagStateMapper1 import BagStateMapper1















class BagStatusHistory(BaseSchema):
    #  swagger.json

    
    store_id = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    app_display_name = fields.Boolean(required=False)
    
    state_id = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    display_name = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    bsh_id = fields.Int(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper1, required=False)
    
    state_type = fields.Str(required=False)
    
    delivery_partner_id = fields.Int(required=False)
    
    kafka_sync = fields.Boolean(required=False)
    
    delivery_awb_number = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    forward = fields.Boolean(required=False)
    
