"""Inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .JobHistoryDto import JobHistoryDto













class JobMetricsDto(BaseSchema):
    #  swagger.json

    
    job_code = fields.Str(required=False)
    
    is_run_more_than_usual = fields.Str(required=False)
    
    job_history = fields.List(fields.Nested(JobHistoryDto, required=False), required=False)
    
    total_success_count = fields.Int(required=False)
    
    total_failure_count = fields.Int(required=False)
    
    total_warning_count = fields.Int(required=False)
    
    total_suppressed_count = fields.Int(required=False)
    
    total_job_runs = fields.Int(required=False)
    
