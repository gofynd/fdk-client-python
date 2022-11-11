"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class VerifiedBy(BaseSchema):
    #  swagger.json

    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
