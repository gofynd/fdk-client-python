"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ErrorCodeAndDescription(BaseSchema):
    #  swagger.json

    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
