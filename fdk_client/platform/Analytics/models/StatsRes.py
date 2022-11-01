"""Analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class StatsRes(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
