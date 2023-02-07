"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .MetricsCount import MetricsCount



class MetricCountResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(MetricsCount, required=False), required=False)
    
