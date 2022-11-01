"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .UserSchema import UserSchema





class VerifyMobileOTPSuccess(BaseSchema):
    #  swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    verify_mobile_link = fields.Boolean(required=False)
    
