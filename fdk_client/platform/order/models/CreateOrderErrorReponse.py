"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















class CreateOrderErrorReponse(BaseSchema):
    #  swagger.json

    
    status = fields.Int(required=False)
    
    stack_trace = fields.Str(required=False)
    
    meta = fields.Str(required=False)
    
    info = fields.Raw(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
