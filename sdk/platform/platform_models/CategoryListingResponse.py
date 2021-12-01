"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .DepartmentIdentifier import DepartmentIdentifier

from .DepartmentCategoryTree import DepartmentCategoryTree


class CategoryListingResponse(BaseSchema):

    
    departments = fields.List(fields.Nested(DepartmentIdentifier, required=False), required=False)
    
    data = fields.List(fields.Nested(DepartmentCategoryTree, required=False), required=False)
    

