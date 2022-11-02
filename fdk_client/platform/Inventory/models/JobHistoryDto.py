"""Inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


























class JobHistoryDto(BaseSchema):
    #  swagger.json

    
    total_added_count = fields.Int(required=False)
    
    total_updated_count = fields.Int(required=False)
    
    total_suppressed_count = fields.Int(required=False)
    
    total_initial_count = fields.Int(required=False)
    
    job_id = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    job_code = fields.Str(required=False)
    
    processed_on = fields.Str(required=False)
    
    filename = fields.List(fields.Str(required=False), required=False)
    
    error_type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    