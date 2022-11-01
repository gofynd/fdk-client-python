"""Inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .TaskParam import TaskParam



class TaskConfig(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    task_config_id = fields.Int(required=False)
    
    task_params = fields.List(fields.Nested(TaskParam, required=False), required=False)
    
