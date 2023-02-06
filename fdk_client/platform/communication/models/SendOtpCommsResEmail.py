"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class SendOtpCommsResEmail(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    to = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    
