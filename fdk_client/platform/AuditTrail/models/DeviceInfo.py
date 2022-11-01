"""AuditTrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DeviceInfo(BaseSchema):
    #  swagger.json

    
    user_agent = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
