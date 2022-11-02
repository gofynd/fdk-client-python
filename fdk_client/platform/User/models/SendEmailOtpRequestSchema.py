"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class SendEmailOtpRequestSchema(BaseSchema):
    #  swagger.json

    
    email = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    