"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class NestedTrackingDetails(BaseSchema):
    #  swagger.json

    
    time = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    is_current = fields.Boolean(required=False)
    
