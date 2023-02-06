"""analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .StatGroup import StatGroup



class StatsGroups(BaseSchema):
    #  swagger.json

    
    groups = fields.List(fields.Nested(StatGroup, required=False), required=False)
    
