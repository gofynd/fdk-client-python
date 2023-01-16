"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .HSNData import HSNData



class HSNCodesResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(HSNData, required=False)
    