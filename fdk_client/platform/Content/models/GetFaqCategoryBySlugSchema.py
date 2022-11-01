"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .FAQCategorySchema import FAQCategorySchema



class GetFaqCategoryBySlugSchema(BaseSchema):
    #  swagger.json

    
    category = fields.Nested(FAQCategorySchema, required=False)
    
