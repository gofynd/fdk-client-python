"""Inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class TaskParam(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    
