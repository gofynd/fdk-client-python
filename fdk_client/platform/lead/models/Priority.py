"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PriorityEnum import PriorityEnum







class Priority(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False, validate=OneOf([val.value for val in PriorityEnum.__members__.values()]))
    
    display = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
