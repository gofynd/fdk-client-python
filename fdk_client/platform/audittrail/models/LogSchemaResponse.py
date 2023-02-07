"""audittrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LogDocs import LogDocs



class LogSchemaResponse(BaseSchema):
    #  swagger.json

    
    docs = fields.List(fields.Nested(LogDocs, required=False), required=False)
    
