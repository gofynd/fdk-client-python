"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class PTErrorResponse(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    
