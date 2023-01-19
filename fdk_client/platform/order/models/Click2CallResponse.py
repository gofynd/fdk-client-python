"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Click2CallResponse(BaseSchema):
    #  swagger.json

    
    status = fields.Boolean(required=False)
    
    call_id = fields.Str(required=False)
    
