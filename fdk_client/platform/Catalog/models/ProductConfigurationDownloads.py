"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ProductConfigurationDownloads(BaseSchema):
    #  swagger.json

    
    multivalue = fields.Boolean(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
