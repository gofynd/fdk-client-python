"""Communication Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class BadRequestSchema(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
