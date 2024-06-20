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


class EventNotifier(BaseSchema):
    pass


class EventSchema(BaseSchema):
    pass


class InternalTransformEvent(BaseSchema):
    pass


class TransformEventData(BaseSchema):
    pass


class TransformEventServiceMeta(BaseSchema):
    pass


class TransformEventAssociation(BaseSchema):
    pass


class TransformEventRequest(BaseSchema):
    pass


class ValidateSchemaRequest(BaseSchema):
    pass


class ValidateSchemaResponse(BaseSchema):
    pass


class TransformEventResponse(BaseSchema):
    pass





class EventConfig(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    event_schema = fields.Dict(required=False, allow_none=True)
    
    version = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    description = fields.Str(required=False, allow_none=True)
    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    group = fields.Str(required=False, allow_none=True)
    


class EventConfigResponse(BaseSchema):
    # Webhook swagger.json

    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    


class EventConfigBase(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


class EventNotifier(BaseSchema):
    # Webhook swagger.json

    
    message = fields.Str(required=False)
    
    emails = fields.List(fields.Str(required=False), required=False)
    


class EventSchema(BaseSchema):
    # Webhook swagger.json

    
    payload = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    


class InternalTransformEvent(BaseSchema):
    # Webhook swagger.json

    
    trace_id = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    created_timestamp = fields.Float(required=False)
    


class TransformEventData(BaseSchema):
    # Webhook swagger.json

    
    event = fields.Nested(InternalTransformEvent, required=False)
    
    company_id = fields.Float(required=False)
    
    contains = fields.List(fields.Str(required=False), required=False)
    
    payload = fields.Dict(required=False)
    


class TransformEventServiceMeta(BaseSchema):
    # Webhook swagger.json

    
    name = fields.Str(required=False)
    


class TransformEventAssociation(BaseSchema):
    # Webhook swagger.json

    
    company_id = fields.Float(required=False)
    


class TransformEventRequest(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    event_version = fields.Str(required=False)
    
    event = fields.Nested(EventSchema, required=False)
    


class ValidateSchemaRequest(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    event_version = fields.Str(required=False)
    
    event = fields.Nested(EventSchema, required=False)
    
    event_schema = fields.Dict(required=False)
    


class ValidateSchemaResponse(BaseSchema):
    # Webhook swagger.json

    
    status = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class TransformEventResponse(BaseSchema):
    # Webhook swagger.json

    
    event_trace_id = fields.List(fields.Str(required=False), required=False)
    
    data = fields.Nested(TransformEventData, required=False)
    
    event_name = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    
    event_type = fields.Str(required=False)
    
    service_meta = fields.Nested(TransformEventServiceMeta, required=False)
    
    association = fields.Nested(TransformEventAssociation, required=False)
    


