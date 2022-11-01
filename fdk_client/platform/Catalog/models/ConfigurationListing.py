"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ConfigurationListingSort import ConfigurationListingSort



from .ConfigurationListingFilter import ConfigurationListingFilter



class ConfigurationListing(BaseSchema):
    #  swagger.json

    
    sort = fields.Nested(ConfigurationListingSort, required=False)
    
    filter = fields.Nested(ConfigurationListingFilter, required=False)
    
