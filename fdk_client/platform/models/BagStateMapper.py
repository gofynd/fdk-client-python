"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class BagStateMapper(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    bs_id = fields.Int(required=False)
    
    state_type = fields.Str(required=False)
    
    app_state_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    app_facing = fields.Boolean(required=False)
    
    app_display_name = fields.Str(required=False)
    
    notify_customer = fields.Boolean(required=False)
    

