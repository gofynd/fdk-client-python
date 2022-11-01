"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class StoreMeta(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
