"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .AppCatalogConfiguration import AppCatalogConfiguration



class GetAppCatalogConfiguration(BaseSchema):
    #  swagger.json

    
    is_default = fields.Boolean(required=False)
    
    data = fields.Nested(AppCatalogConfiguration, required=False)
    