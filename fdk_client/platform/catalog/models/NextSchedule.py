"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class NextSchedule(BaseSchema):
    #  swagger.json

    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
