"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SegmentCredentials import SegmentCredentials





class Segment(BaseSchema):
    #  swagger.json

    
    credentials = fields.Nested(SegmentCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    
