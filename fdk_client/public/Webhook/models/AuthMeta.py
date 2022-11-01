"""Webhook Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema








class AuthMeta(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
