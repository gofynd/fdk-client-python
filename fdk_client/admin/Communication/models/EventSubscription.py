"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EventSubscriptionTemplate import EventSubscriptionTemplate



















class EventSubscription(BaseSchema):
    #  swagger.json

    
    template = fields.Nested(EventSubscriptionTemplate, required=False)
    
    is_default = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    event = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
