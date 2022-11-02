"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Login(BaseSchema):
    #  swagger.json

    
    password = fields.Boolean(required=False)
    
    otp = fields.Boolean(required=False)
    