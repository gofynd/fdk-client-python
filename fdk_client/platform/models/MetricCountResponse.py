"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .MetricsCount import MetricsCount


class MetricCountResponse(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(MetricsCount, required=False), required=False)
    

