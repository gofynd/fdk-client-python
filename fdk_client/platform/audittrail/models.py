"""AuditTrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class RequestBodyAuditLog(BaseSchema):
    pass


class CreateLogResp(BaseSchema):
    pass


class LogMetaObj(BaseSchema):
    pass


class EntityObject(BaseSchema):
    pass





class RequestBodyAuditLog(BaseSchema):
    # AuditTrail swagger.json

    
    log_meta = fields.Nested(LogMetaObj, required=False)
    
    log_payload = fields.Dict(required=False)
    


class CreateLogResp(BaseSchema):
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
    
    sessions = fields.Str(required=False)
    


class EntityObject(BaseSchema):
    # AuditTrail swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    


