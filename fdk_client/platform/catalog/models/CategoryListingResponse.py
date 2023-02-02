"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DepartmentIdentifier import DepartmentIdentifier



from .DepartmentCategoryTree import DepartmentCategoryTree



class CategoryListingResponse(BaseSchema):
    #  swagger.json

    
    departments = fields.List(fields.Nested(DepartmentIdentifier, required=False), required=False)
    
    data = fields.List(fields.Nested(DepartmentCategoryTree, required=False), required=False)
    
