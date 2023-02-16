"""analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .StatsGroupComponent import StatsGroupComponent



class StatsGroupComponents(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    components = fields.List(fields.Nested(StatsGroupComponent, required=False), required=False)
    
