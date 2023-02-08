"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
























class BagStateMapper(BaseSchema):
    #  swagger.json

    
    app_facing = fields.Boolean(required=False)
    
    notify_customer = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    app_state_name = fields.Str(required=False)
    
    bs_id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    journey_type = fields.Str(required=False)
    
    app_display_name = fields.Str(required=False)
    
    state_type = fields.Str(required=False)
    
