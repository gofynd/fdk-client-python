"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Category import Category



class SingleCategoryResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(Category, required=False)
    
