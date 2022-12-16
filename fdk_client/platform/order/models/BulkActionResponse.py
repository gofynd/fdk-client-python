"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class BulkActionResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    