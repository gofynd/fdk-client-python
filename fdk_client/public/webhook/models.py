"""Webhook Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema




class EventConfig(BaseSchema):
    pass


class EventConfigResponse(BaseSchema):
    pass


class EventConfigBase(BaseSchema):
    pass





class EventConfig(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    


class EventConfigResponse(BaseSchema):
    # Webhook swagger.json

    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    


class EventConfigBase(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


