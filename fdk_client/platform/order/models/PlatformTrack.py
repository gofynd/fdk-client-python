"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
























class PlatformTrack(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
    account_name = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    updated_time = fields.Str(required=False)
    
    raw_status = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    awb = fields.Str(required=False)
    
    last_location_recieved_at = fields.Str(required=False)
    
