"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SendOtpSmsCommsProvider(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
