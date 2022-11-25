"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class GetConfigMetadataResponse(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Dict(required=False), required=False)
    
    values = fields.List(fields.Dict(required=False), required=False)
    
    condition = fields.List(fields.Dict(required=False), required=False)
    
