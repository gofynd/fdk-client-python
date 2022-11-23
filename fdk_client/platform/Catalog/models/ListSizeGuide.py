"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ListSizeGuide(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Dict(required=False)
    
