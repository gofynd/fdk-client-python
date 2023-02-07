"""audittrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CreateLogResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    internal_message = fields.Str(required=False)
    
