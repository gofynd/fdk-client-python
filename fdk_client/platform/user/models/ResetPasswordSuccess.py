"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ResetPasswordSuccess(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
