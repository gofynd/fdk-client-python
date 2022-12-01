"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CategoryRequestSchema import CategoryRequestSchema



class CreateFaqCategoryRequestSchema(BaseSchema):
    #  swagger.json

    
    category = fields.Nested(CategoryRequestSchema, required=False)
    
