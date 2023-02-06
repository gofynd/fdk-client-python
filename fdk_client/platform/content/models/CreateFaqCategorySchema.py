"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CategorySchema import CategorySchema



class CreateFaqCategorySchema(BaseSchema):
    #  swagger.json

    
    category = fields.Nested(CategorySchema, required=False)
    
