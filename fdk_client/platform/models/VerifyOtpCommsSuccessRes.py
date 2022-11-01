"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class VerifyOtpCommsSuccessRes(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    

