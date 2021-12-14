"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema















from .JobConfigDTO import JobConfigDTO

from .JobConfigDTO import JobConfigDTO



from .Page import Page


class ResponseEnvelopeJobConfigDTO(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.Nested(JobConfigDTO, required=False)
    
    payload = fields.Nested(JobConfigDTO, required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    

