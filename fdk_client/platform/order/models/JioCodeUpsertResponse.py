"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .NestedErrorSchemaDataSet import NestedErrorSchemaDataSet







class JioCodeUpsertResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    identifier = fields.Str(required=False)
    
    error = fields.List(fields.Nested(NestedErrorSchemaDataSet, required=False), required=False)
    
    trace_id = fields.Str(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
