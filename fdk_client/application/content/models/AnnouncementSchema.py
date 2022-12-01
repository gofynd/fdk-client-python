"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ScheduleStartSchema import ScheduleStartSchema



class AnnouncementSchema(BaseSchema):
    #  swagger.json

    
    announcement = fields.Str(required=False)
    
    schedule = fields.Nested(ScheduleStartSchema, required=False)
    
