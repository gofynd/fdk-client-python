"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class TokenRequestBodySchema(BaseSchema):
    #  swagger.json

    
    token = fields.Str(required=False)
    
