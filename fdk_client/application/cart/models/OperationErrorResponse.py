"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class OperationErrorResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    