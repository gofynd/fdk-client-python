"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class NotFoundResourceError(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
