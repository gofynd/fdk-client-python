"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class ErrorResponse(BaseSchema):
    #  swagger.json

    
    status = fields.Int(required=False)
    
    stack_trace = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
