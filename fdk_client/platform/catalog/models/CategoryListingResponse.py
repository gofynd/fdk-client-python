"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DepartmentCategoryTree import DepartmentCategoryTree



from .DepartmentIdentifier import DepartmentIdentifier



class CategoryListingResponse(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(DepartmentCategoryTree, required=False), required=False)
    
    departments = fields.List(fields.Nested(DepartmentIdentifier, required=False), required=False)
    
