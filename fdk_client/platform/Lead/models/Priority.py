"""Lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PriorityEnum import PriorityEnum







class Priority(BaseSchema):
    #  swagger.json

    
    key = fields.Nested(PriorityEnum, required=False)
    
    display = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
