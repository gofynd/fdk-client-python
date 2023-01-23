"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class GetCatalogConfigurationDetailsSchemaListing(BaseSchema):
    #  swagger.json

    
    sort = fields.Dict(required=False)
    
    filter = fields.Dict(required=False)
    
