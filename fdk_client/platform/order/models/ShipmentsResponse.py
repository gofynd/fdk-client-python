"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class ShipmentsResponse(BaseSchema):
    #  swagger.json

    
    exception = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    final_state = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
