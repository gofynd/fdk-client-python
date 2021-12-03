"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema
















class PlatformOrderTrack(BaseSchema):

    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    
    resend_token = fields.Str(required=False)
    

