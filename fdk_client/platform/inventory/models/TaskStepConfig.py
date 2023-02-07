"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TaskConfig import TaskConfig







class TaskStepConfig(BaseSchema):
    #  swagger.json

    
    task_configs = fields.List(fields.Nested(TaskConfig, required=False), required=False)
    
    task_config_ids = fields.List(fields.Int(required=False), required=False)
    
    task_config_group_ids = fields.List(fields.Int(required=False), required=False)
    
