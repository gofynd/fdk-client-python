"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class TokenRequestBodySchema(BaseSchema):
    #  swagger.json

    
    token = fields.Str(required=False)
    
