"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class DepartmentErrorResponse(BaseSchema):
    #  swagger.json

    
    errors = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
