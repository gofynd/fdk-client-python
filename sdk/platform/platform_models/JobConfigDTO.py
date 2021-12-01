"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema









from .TaskDTO import TaskDTO

from .DataTresholdDTO import DataTresholdDTO






class JobConfigDTO(BaseSchema):

    
    integration = fields.Str(required=False)
    
    integration_data = fields.Dict(required=False)
    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    task_details = fields.Nested(TaskDTO, required=False)
    
    threshold_details = fields.Nested(DataTresholdDTO, required=False)
    
    job_code = fields.Str(required=False)
    
    alias = fields.Str(required=False)
    

