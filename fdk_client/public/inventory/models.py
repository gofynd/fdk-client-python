"""Inventory Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema




class DataTresholdDTO(BaseSchema):
    pass


class GenericDTO(BaseSchema):
    pass


class JobConfigDTO(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class ResponseEnvelopeListJobConfigDTO(BaseSchema):
    pass


class TaskDTO(BaseSchema):
    pass


class EmailJobMetrics(BaseSchema):
    pass


class ResponseEnvelopeEmailJobMetrics(BaseSchema):
    pass


class ResponseEnvelopeObject(BaseSchema):
    pass





class DataTresholdDTO(BaseSchema):
    # Inventory swagger.json

    
    min_price = fields.Float(required=False)
    
    safe_stock = fields.Int(required=False)
    
    period_threshold = fields.Int(required=False)
    
    period_threshold_type = fields.Str(required=False)
    
    period_type_list = fields.List(fields.Nested(GenericDTO, required=False), required=False)
    


class GenericDTO(BaseSchema):
    # Inventory swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    


class JobConfigDTO(BaseSchema):
    # Inventory swagger.json

    
    integration = fields.Str(required=False)
    
    integration_data = fields.Dict(required=False)
    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    task_details = fields.Nested(TaskDTO, required=False)
    
    threshold_details = fields.Nested(DataTresholdDTO, required=False)
    
    job_code = fields.Str(required=False)
    
    alias = fields.Str(required=False)
    


class Page(BaseSchema):
    # Inventory swagger.json

    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    


class ResponseEnvelopeListJobConfigDTO(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.List(fields.Nested(JobConfigDTO, required=False), required=False)
    
    payload = fields.List(fields.Nested(JobConfigDTO, required=False), required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


class TaskDTO(BaseSchema):
    # Inventory swagger.json

    
    type = fields.Int(required=False)
    
    group_list = fields.List(fields.Nested(GenericDTO, required=False), required=False)
    


class EmailJobMetrics(BaseSchema):
    # Inventory swagger.json

    
    executed = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    job_code = fields.Str(required=False)
    
    daily_job = fields.Boolean(required=False)
    
    last_executed_on = fields.Str(required=False)
    


class ResponseEnvelopeEmailJobMetrics(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.Nested(EmailJobMetrics, required=False)
    
    payload = fields.Nested(EmailJobMetrics, required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


class ResponseEnvelopeObject(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.Dict(required=False)
    
    payload = fields.Dict(required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


