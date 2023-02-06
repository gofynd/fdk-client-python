"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class TrackingList(BaseSchema):
    #  swagger.json

    
    is_current = fields.Boolean(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    time = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
