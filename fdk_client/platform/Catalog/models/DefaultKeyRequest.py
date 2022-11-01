"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class DefaultKeyRequest(BaseSchema):
    #  swagger.json

    
    default_key = fields.Str(required=False)
    
