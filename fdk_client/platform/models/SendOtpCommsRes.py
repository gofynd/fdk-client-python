"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SendOtpCommsResSms import SendOtpCommsResSms

from .SendOtpCommsResEmail import SendOtpCommsResEmail


class SendOtpCommsRes(BaseSchema):
    # Communication swagger.json

    
    sms = fields.Nested(SendOtpCommsResSms, required=False)
    
    email = fields.Nested(SendOtpCommsResEmail, required=False)
    

