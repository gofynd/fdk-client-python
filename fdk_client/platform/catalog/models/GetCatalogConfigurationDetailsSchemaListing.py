"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class GetCatalogConfigurationDetailsSchemaListing(BaseSchema):
    #  swagger.json

    
    filter = fields.Dict(required=False)
    
    sort = fields.Dict(required=False)
    
