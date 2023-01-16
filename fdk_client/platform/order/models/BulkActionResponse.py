"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class BulkActionResponse(BaseSchema):
    #  swagger.json

    
    status = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    