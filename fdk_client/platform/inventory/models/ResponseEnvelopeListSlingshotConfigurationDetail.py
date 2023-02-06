"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















from .SlingshotConfigurationDetail import SlingshotConfigurationDetail



from .SlingshotConfigurationDetail import SlingshotConfigurationDetail





from .Page import Page



class ResponseEnvelopeListSlingshotConfigurationDetail(BaseSchema):
    #  swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.List(fields.Nested(SlingshotConfigurationDetail, required=False), required=False)
    
    payload = fields.List(fields.Nested(SlingshotConfigurationDetail, required=False), required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    
