"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CategorySchema import CategorySchema



class CreateFaqCategorySchema(BaseSchema):
    #  swagger.json

    
    category = fields.Nested(CategorySchema, required=False)
    