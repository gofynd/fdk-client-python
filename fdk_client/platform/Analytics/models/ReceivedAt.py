"""Analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ReceivedAt(BaseSchema):
    #  swagger.json

    
    value = fields.Str(required=False)
    
