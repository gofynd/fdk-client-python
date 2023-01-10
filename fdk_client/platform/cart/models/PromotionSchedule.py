"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class PromotionSchedule(BaseSchema):
    #  swagger.json

    
    end = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    cron = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    start = fields.Str(required=False)
    
