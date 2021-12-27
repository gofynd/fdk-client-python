"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class WalletOtpResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    is_verified_flag = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    

