"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class LogoutSuccess(BaseSchema):
    #  swagger.json

    
    logout = fields.Boolean(required=False)
    
