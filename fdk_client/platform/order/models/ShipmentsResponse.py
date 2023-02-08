"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















class ShipmentsResponse(BaseSchema):
    #  swagger.json

    
    status = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    
    final_state = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
