"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class GetPingResponse(BaseSchema):
    #  swagger.json

    
    ping = fields.Str(required=False)
    
