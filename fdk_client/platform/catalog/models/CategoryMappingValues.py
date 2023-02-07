"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CategoryMappingValues(BaseSchema):
    #  swagger.json

    
    catalog_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
