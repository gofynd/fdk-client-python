"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class SendOtpRequestSchema(BaseSchema):
    #  swagger.json

    
    country_code = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    android_hash = fields.Str(required=False)
    
