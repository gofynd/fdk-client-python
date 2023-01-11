"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .NestedTrackingDetails import NestedTrackingDetails









class TrackingDetails(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
    tracking_details = fields.List(fields.Nested(NestedTrackingDetails, required=False), required=False)
    
    time = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    is_current = fields.Boolean(required=False)
    
