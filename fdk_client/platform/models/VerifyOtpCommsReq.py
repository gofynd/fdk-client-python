"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class VerifyOtpCommsReq(BaseSchema):
    # Communication swagger.json

    
    request_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    
