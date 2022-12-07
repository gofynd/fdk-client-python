"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Options1 import Options1



class MetricsCount(BaseSchema):
    #  swagger.json

    
    value = fields.Int(required=False)
    
    text = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    options = fields.List(fields.Nested(Options1, required=False), required=False)
    
