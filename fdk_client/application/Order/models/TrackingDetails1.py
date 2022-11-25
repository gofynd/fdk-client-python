"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .NestedTrackingDetails import NestedTrackingDetails











class TrackingDetails1(BaseSchema):
    #  swagger.json

    
    tracking_details = fields.List(fields.Nested(NestedTrackingDetails, required=False), required=False)
    
    is_passed = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    is_current = fields.Boolean(required=False)
    
    time = fields.Str(required=False)
    
