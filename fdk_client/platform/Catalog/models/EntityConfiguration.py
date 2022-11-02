"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .GetCatalogConfigurationDetailsProduct import GetCatalogConfigurationDetailsProduct



from .GetCatalogConfigurationDetailsSchemaListing import GetCatalogConfigurationDetailsSchemaListing



class EntityConfiguration(BaseSchema):
    #  swagger.json

    
    config_type = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    
    listing = fields.Nested(GetCatalogConfigurationDetailsSchemaListing, required=False)
    