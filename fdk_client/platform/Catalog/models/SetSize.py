"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SetSize(BaseSchema):
    #  swagger.json

    
    pieces = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
