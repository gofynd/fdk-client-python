"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .BagStateMapper import BagStateMapper



























class BagStatusHistory(BaseSchema):
    #  swagger.json

    
    updated_at = fields.Str(required=False)
    
    delivery_partner_id = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    store_id = fields.Int(required=False)
    
    bsh_id = fields.Int(required=False)
    
    app_display_name = fields.Boolean(required=False)
    
    state_type = fields.Str(required=False)
    
    forward = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    delivery_awb_number = fields.Str(required=False)
    
    kafka_sync = fields.Boolean(required=False)
    
    display_name = fields.Boolean(required=False)
    
    state_id = fields.Int(required=False)
    