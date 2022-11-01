"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PlanRecurring(BaseSchema):
    #  swagger.json

    
    interval = fields.Str(required=False)
    
    interval_count = fields.Float(required=False)
    
