"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















class JobStepsDTO(BaseSchema):
    #  swagger.json

    
    step_name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    step_execution_time = fields.Int(required=False)
    
    start_count = fields.Int(required=False)
    
    end_count = fields.Int(required=False)
    
    deleted_count = fields.Int(required=False)
    
    processed_start_time = fields.Str(required=False)
    
    processed_at = fields.Str(required=False)
    
