"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class ErrorResponse(BaseSchema):
    #  swagger.json

    
    meta = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Int(required=False)
    