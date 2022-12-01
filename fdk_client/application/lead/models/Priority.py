"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PriorityEnum import PriorityEnum







class Priority(BaseSchema):
    #  swagger.json

    
    key = fields.Nested(PriorityEnum, required=False)
    
    display = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
