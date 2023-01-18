"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .NextSchedule import NextSchedule







class CollectionSchedule(BaseSchema):
    #  swagger.json

    
    start = fields.Str(required=False)
    
    cron = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Nested(NextSchedule, required=False), required=False)
    
    end = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    
