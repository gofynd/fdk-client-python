"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .BagStateMapper import BagStateMapper

















class CurrentStatus(BaseSchema):
    #  swagger.json

    
    kafka_sync = fields.Boolean(required=False)
    
    store_id = fields.Int(required=False)
    
    state_id = fields.Int(required=False)
    
    delivery_awb_number = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    state_type = fields.Str(required=False)
    
    current_status_id = fields.Int(required=False)
    
    bag_id = fields.Int(required=False)
    
    delivery_partner_id = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    updated_at = fields.Int(required=False)
    
