"""AuditTrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class RequestBodyAuditLog(BaseSchema):
    pass


class CreateLogResponse(BaseSchema):
    pass


class LogMetaObj(BaseSchema):
    pass


class EntityObject(BaseSchema):
    pass


class LogSchemaResponse(BaseSchema):
    pass


class LogDocs(BaseSchema):
    pass


class EntityObj(BaseSchema):
    pass


class Modifier(BaseSchema):
    pass


class DeviceInfo(BaseSchema):
    pass


class Location(BaseSchema):
    pass


class BadRequest(BaseSchema):
    pass


class ResourceNotFound(BaseSchema):
    pass


class InternalServerError(BaseSchema):
    pass


class EntityTypesResponse(BaseSchema):
    pass


class EntityTypeObj(BaseSchema):
    pass





class RequestBodyAuditLog(BaseSchema):
    # AuditTrail swagger.json

    
    log_meta = fields.Nested(LogMetaObj, required=False)
    
    log_payload = fields.Dict(required=False)
    


class CreateLogResponse(BaseSchema):
    # AuditTrail swagger.json

    
    message = fields.Str(required=False)
    
    internal_message = fields.Str(required=False)
    


class LogMetaObj(BaseSchema):
    # AuditTrail swagger.json

    
    modifier = fields.Dict(required=False)
    
    application = fields.Str(required=False)
    
    entity = fields.Nested(EntityObject, required=False)
    
    device_info = fields.Dict(required=False)
    
    location = fields.Dict(required=False)
    


class EntityObject(BaseSchema):
    # AuditTrail swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    


class LogSchemaResponse(BaseSchema):
    # AuditTrail swagger.json

    
    docs = fields.List(fields.Nested(LogDocs, required=False), required=False)
    


class LogDocs(BaseSchema):
    # AuditTrail swagger.json

    
    entity = fields.Nested(EntityObj, required=False)
    
    modifier = fields.Nested(Modifier, required=False)
    
    device_info = fields.Nested(DeviceInfo, required=False)
    
    location = fields.Nested(Location, required=False)
    
    _id = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    sessions = fields.Str(required=False)
    
    date = fields.Str(required=False)
    
    logs = fields.Dict(required=False)
    


class EntityObj(BaseSchema):
    # AuditTrail swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    entity_details = fields.Dict(required=False)
    


class Modifier(BaseSchema):
    # AuditTrail swagger.json

    
    user_id = fields.Str(required=False)
    
    as_administrator = fields.Boolean(required=False)
    
    user_details = fields.Dict(required=False)
    


class DeviceInfo(BaseSchema):
    # AuditTrail swagger.json

    
    user_agent = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    


class Location(BaseSchema):
    # AuditTrail swagger.json

    
    extra_meta = fields.Dict(required=False)
    


class BadRequest(BaseSchema):
    # AuditTrail swagger.json

    
    message = fields.Str(required=False)
    


class ResourceNotFound(BaseSchema):
    # AuditTrail swagger.json

    
    message = fields.Str(required=False)
    


class InternalServerError(BaseSchema):
    # AuditTrail swagger.json

    
    message = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class EntityTypesResponse(BaseSchema):
    # AuditTrail swagger.json

    
    items = fields.List(fields.Nested(EntityTypeObj, required=False), required=False)
    


class EntityTypeObj(BaseSchema):
    # AuditTrail swagger.json

    
    entity_value = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


