"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Meta(BaseSchema):
    #  swagger.json

    
    headers = fields.Dict(required=False)
    
    unit = fields.Str(required=False)
    
    values = fields.List(fields.Dict(required=False), required=False)
    
