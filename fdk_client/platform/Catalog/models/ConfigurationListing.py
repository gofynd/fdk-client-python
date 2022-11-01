"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ConfigurationListingFilter import ConfigurationListingFilter



from .ConfigurationListingSort import ConfigurationListingSort



class ConfigurationListing(BaseSchema):
    #  swagger.json

    
    filter = fields.Nested(ConfigurationListingFilter, required=False)
    
    sort = fields.Nested(ConfigurationListingSort, required=False)
    
