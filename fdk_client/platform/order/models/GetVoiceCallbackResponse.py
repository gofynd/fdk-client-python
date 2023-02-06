"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class GetVoiceCallbackResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
