"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .Association import Association





from .AuthMeta import AuthMeta





from .EventConfig import EventConfig


class SubscriberResponse(BaseSchema):

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    email_id = fields.Str(required=False)
    
    status = fields.Str(required=False, validate=OneOf(SubscriberStatus.__members__.keys()))
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    

