"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class ErrorResponse(BaseSchema):
    #  swagger.json

    
    stack_trace = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
