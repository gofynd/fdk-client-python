"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class EdcUpdateRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator_id = fields.Int(required=False)
    
    edc_model = fields.Str(required=False)
    
    device_tag = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    edc_device_serial_no = fields.Str(required=False)
    
    is_active = fields.Str(required=False)
    
    merchant_store_pos_code = fields.Str(required=False)
    

