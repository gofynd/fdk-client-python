"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class SendResetPasswordEmailRequestSchema(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    

