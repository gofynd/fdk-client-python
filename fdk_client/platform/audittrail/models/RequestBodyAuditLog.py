"""audittrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LogMetaObj import LogMetaObj





class RequestBodyAuditLog(BaseSchema):
    #  swagger.json

    
    log_meta = fields.Nested(LogMetaObj, required=False)
    
    log_payload = fields.Dict(required=False)
    
