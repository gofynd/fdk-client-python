"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class StatsProcessedSms(BaseSchema):
    #  swagger.json

    
    success = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    suppressed = fields.Int(required=False)
    
