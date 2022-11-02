"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class TrackingDetails(BaseSchema):
    #  swagger.json

    
    is_current = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    time = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    