"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class ErrorCodeDescription(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
