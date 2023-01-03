"""rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class Error(BaseSchema):
    #  swagger.json

    
    code = fields.Int(required=False)
    
    exception = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
