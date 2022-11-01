"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CategorySchema import CategorySchema



class GetFaqCategoriesSchema(BaseSchema):
    #  swagger.json

    
    categories = fields.List(fields.Nested(CategorySchema, required=False), required=False)
    
