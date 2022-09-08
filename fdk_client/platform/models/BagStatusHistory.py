"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



















from .BagStateMapper1 import BagStateMapper1










class BagStatusHistory(BaseSchema):
    # Order swagger.json

    
    state_type = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    state_id = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    delivery_partner_id = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    delivery_awb_number = fields.Str(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper1, required=False)
    
    kafka_sync = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    bsh_id = fields.Int(required=False)
    

