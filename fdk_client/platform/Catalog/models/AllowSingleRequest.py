"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AllowSingleRequest(BaseSchema):
    #  swagger.json

    
    allow_single = fields.Boolean(required=False)
    
