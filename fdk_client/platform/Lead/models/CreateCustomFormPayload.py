"""Lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .PriorityEnum import PriorityEnum







from .PollForAssignment import PollForAssignment



class CreateCustomFormPayload(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    inputs = fields.List(fields.Dict(required=False), required=False)
    
    description = fields.Str(required=False)
    
    header_image = fields.Str(required=False)
    
    priority = fields.Nested(PriorityEnum, required=False)
    
    should_notify = fields.Boolean(required=False)
    
    success_message = fields.Str(required=False)
    
    poll_for_assignment = fields.Nested(PollForAssignment, required=False)
    