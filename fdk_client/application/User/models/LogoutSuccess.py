"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class LogoutSuccess(BaseSchema):
    #  swagger.json

    
    logout = fields.Boolean(required=False)
    