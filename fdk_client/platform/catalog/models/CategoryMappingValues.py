"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CategoryMappingValues(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    catalog_id = fields.Int(required=False)
    
