"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SendResetPasswordEmailRequestSchema(BaseSchema):
    #  swagger.json

    
    email = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    
