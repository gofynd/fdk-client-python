"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class GenerateBulkUrlSuccessResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    url = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    expires_in = fields.Float(required=False)
    
    presigned_type = fields.Str(required=False)
    

