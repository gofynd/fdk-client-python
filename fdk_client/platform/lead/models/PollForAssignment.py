"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class PollForAssignment(BaseSchema):
    #  swagger.json

    
    duration = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    success_message = fields.Str(required=False)
    
    failure_message = fields.Str(required=False)
    
