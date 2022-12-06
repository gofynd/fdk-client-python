"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CategorySchema import CategorySchema



class CategoryData(BaseSchema):
    #  swagger.json

    
    list = fields.Nested(CategorySchema, required=False)
    
