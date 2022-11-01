"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class AuthSuccessUserDebug(BaseSchema):
    #  swagger.json

    
    platform = fields.Str(required=False)
    
