"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .EntityConfiguration import EntityConfiguration



class GetAppCatalogEntityConfiguration(BaseSchema):
    #  swagger.json

    
    is_default = fields.Boolean(required=False)
    
    data = fields.Nested(EntityConfiguration, required=False)
    
