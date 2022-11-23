"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class CouponSchedule(BaseSchema):
    #  swagger.json

    
    duration = fields.Int(required=False)
    
    cron = fields.Str(required=False)
    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
