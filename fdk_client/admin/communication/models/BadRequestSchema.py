"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class BadRequestSchema(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
