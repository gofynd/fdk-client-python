"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class TATCategoryRequest(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    level = fields.Str(required=False)
    
