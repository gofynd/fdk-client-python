"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CurrentPeriod(BaseSchema):
    #  swagger.json

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
