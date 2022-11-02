"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SuperLane import SuperLane


class LaneConfigResponse(BaseSchema):
    # Orders swagger.json

    
    super_lanes = fields.List(fields.Nested(SuperLane, required=False), required=False)
    

