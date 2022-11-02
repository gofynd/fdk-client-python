"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















from .ConfigurationProduct import ConfigurationProduct







from .ConfigurationListing import ConfigurationListing





class AppCatalogConfiguration(BaseSchema):
    #  swagger.json

    
    config_type = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    created_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    modified_by = fields.Dict(required=False)
    