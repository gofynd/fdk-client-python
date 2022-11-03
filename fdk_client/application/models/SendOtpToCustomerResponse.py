"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class SendOtpToCustomerResponse(BaseSchema):
    # Order swagger.json

    
    resend_timer = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    

