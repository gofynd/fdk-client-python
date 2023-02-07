"""analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class StatsGroupComponent(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    filters = fields.Dict(required=False)
    
