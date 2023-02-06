"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ErrorDescription import ErrorDescription







class ErrorResponse(BaseSchema):
    #  swagger.json

    
    status_code = fields.Int(required=False)
    
    error = fields.Nested(ErrorDescription, required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
