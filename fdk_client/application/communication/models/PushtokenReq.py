"""communication Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class PushtokenReq(BaseSchema):
    #  swagger.json

    
    action = fields.Str(required=False)
    
    bundle_identifier = fields.Str(required=False)
    
    push_token = fields.Str(required=False)
    
    unique_device_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
