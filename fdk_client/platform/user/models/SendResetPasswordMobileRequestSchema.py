"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class SendResetPasswordMobileRequestSchema(BaseSchema):
    #  swagger.json

    
    country_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    
