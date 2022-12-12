"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





















from .BagStateMapper import BagStateMapper














class BagStatusHistory(BaseSchema):
    # Order swagger.json

    
    created_at = fields.Str(required=False)
    
    delivery_partner_id = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    display_name = fields.Boolean(required=False)
    
    bag_id = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    state_type = fields.Str(required=False)
    
    kafka_sync = fields.Boolean(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    app_display_name = fields.Boolean(required=False)
    
    state_id = fields.Int(required=False)
    
    delivery_awb_number = fields.Str(required=False)
    
    forward = fields.Boolean(required=False)
    
    bsh_id = fields.Int(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    

