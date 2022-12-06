"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CategoryMappingValues import CategoryMappingValues



from .CategoryMappingValues import CategoryMappingValues



from .CategoryMappingValues import CategoryMappingValues



class CategoryMapping(BaseSchema):
    #  swagger.json

    
    google = fields.Nested(CategoryMappingValues, required=False)
    
    ajio = fields.Nested(CategoryMappingValues, required=False)
    
    facebook = fields.Nested(CategoryMappingValues, required=False)
    
