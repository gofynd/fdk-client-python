"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class DepartmentErrorResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    errors = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
