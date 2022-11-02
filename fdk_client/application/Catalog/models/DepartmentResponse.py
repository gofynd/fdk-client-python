"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Department import Department



class DepartmentResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(Department, required=False), required=False)
    