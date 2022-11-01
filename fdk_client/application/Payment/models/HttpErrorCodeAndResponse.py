"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ErrorCodeAndDescription import ErrorCodeAndDescription





class HttpErrorCodeAndResponse(BaseSchema):
    #  swagger.json

    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    
    success = fields.Boolean(required=False)
    
