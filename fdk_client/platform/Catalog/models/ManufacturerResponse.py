"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ManufacturerResponse(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
