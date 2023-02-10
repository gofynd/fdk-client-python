"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DepartmentCreateResponse(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
