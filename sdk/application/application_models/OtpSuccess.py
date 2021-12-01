"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema


















class OtpSuccess(BaseSchema):

    
    resend_timer = fields.Int(required=False)
    
    resend_token = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    

