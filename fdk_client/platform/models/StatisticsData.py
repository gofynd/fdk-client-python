"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class StatisticsData(BaseSchema):
    # Payment swagger.json

    
    active_device_count = fields.Int(required=False)
    
    inactive_device_count = fields.Int(required=False)
    

