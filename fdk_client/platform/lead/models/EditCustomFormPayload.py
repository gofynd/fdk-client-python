"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .PriorityEnum import PriorityEnum











from .PollForAssignment import PollForAssignment



class EditCustomFormPayload(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    inputs = fields.List(fields.Dict(required=False), required=False)
    
    description = fields.Str(required=False)
    
    priority = fields.Str(required=False, validate=OneOf([val.value for val in PriorityEnum.__members__.values()]))
    
    header_image = fields.Str(required=False)
    
    should_notify = fields.Boolean(required=False)
    
    login_required = fields.Boolean(required=False)
    
    success_message = fields.Str(required=False)
    
    poll_for_assignment = fields.Nested(PollForAssignment, required=False)
    
