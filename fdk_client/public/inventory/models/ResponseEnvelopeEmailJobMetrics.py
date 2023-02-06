"""inventory Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema


















from .EmailJobMetrics import EmailJobMetrics



from .EmailJobMetrics import EmailJobMetrics





from .Page import Page



class ResponseEnvelopeEmailJobMetrics(BaseSchema):
    #  swagger.json

    
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
    
