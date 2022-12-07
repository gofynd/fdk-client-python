"""webhook Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema










from .Association import Association







from .SubscriberStatus import SubscriberStatus



from .AuthMeta import AuthMeta







from .EventConfig import EventConfig



class SubscriberResponse(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    email_id = fields.Str(required=False)
    
    status = fields.Nested(SubscriberStatus, required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    