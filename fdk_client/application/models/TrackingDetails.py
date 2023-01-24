"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .NestedTrackingDetails import NestedTrackingDetails








class TrackingDetails(BaseSchema):
    # Order swagger.json

    
    is_current = fields.Boolean(required=False)
    
    tracking_details = fields.List(fields.Nested(NestedTrackingDetails, required=False), required=False)
    
    is_passed = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    time = fields.Str(required=False)
    

