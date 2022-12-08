"""webhook Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema










from .Association import Association





from .SubscriberStatus import SubscriberStatus





from .AuthMeta import AuthMeta





class SubscriberConfig(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    status = fields.Str(required=False, validate=OneOf([val.value for val in SubscriberStatus.__members__.values()]))
    
    email_id = fields.Str(required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    event_id = fields.List(fields.Int(required=False), required=False)
    
