"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class UnauthenticatedSchema(BaseSchema):
    #  swagger.json

    
    authenticated = fields.Boolean(required=False)
    
