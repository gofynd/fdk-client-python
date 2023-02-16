"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class CatalogMasterConfig(BaseSchema):
    #  swagger.json

    
    source_slug = fields.Str(required=False)
    
