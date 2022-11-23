"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .ConfigurationListing import ConfigurationListing





from .ConfigurationProduct import ConfigurationProduct











class AppCatalogConfiguration(BaseSchema):
    #  swagger.json

    
    modified_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    app_id = fields.Str(required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    config_id = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    config_type = fields.Str(required=False)
    
