"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class DepartmentCreateErrorResponse(BaseSchema):
    #  swagger.json

    
    error = fields.Str(required=False)
    
