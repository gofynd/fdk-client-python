"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CategoryItems import CategoryItems





class DepartmentCategoryTree(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(CategoryItems, required=False), required=False)
    
    department = fields.Str(required=False)
    