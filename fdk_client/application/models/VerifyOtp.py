"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class VerifyOtp(BaseSchema):
    # Order swagger.json

    
    otp_code = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    

