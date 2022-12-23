"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Schedule(BaseSchema):
    # Rewards swagger.json

    
    cron = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
