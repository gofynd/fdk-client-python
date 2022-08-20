"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .NestedErrorSchemaDataSet import NestedErrorSchemaDataSet








class JioCodeUpsertResponse(BaseSchema):
    # Orders swagger.json

    
    data = fields.List(fields.Dict(required=False), required=False)
    
    error = fields.List(fields.Nested(NestedErrorSchemaDataSet, required=False), required=False)
    
    identifier = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    trace_id = fields.Str(required=False)
    
