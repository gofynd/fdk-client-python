"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Options import Options



class MetricsCount(BaseSchema):
    #  swagger.json

    
    text = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    options = fields.List(fields.Nested(Options, required=False), required=False)
    
