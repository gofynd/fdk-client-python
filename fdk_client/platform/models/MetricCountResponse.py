"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .MetricsCount import MetricsCount




class MetricCountResponse(BaseSchema):
    # Orders swagger.json

    
    result = fields.List(fields.Nested(MetricsCount, required=False), required=False)
    
    success = fields.Boolean(required=False)
    

