"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .TATCategoryRequest import TATCategoryRequest





class TATArticlesRequest(BaseSchema):
    #  swagger.json

    
    manufacturing_time = fields.Int(required=False)
    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
