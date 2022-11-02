"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Meta(BaseSchema):
    #  swagger.json

    
    values = fields.List(fields.Dict(required=False), required=False)
    
    unit = fields.Str(required=False)
    
    headers = fields.Dict(required=False)
    
