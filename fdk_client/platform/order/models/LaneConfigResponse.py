"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SuperLane import SuperLane



class LaneConfigResponse(BaseSchema):
    #  swagger.json

    
    super_lanes = fields.List(fields.Nested(SuperLane, required=False), required=False)
    
