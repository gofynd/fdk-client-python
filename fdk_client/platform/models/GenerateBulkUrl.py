"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class GenerateBulkUrl(BaseSchema):
    # DocumentEngine swagger.json

    
    expires_in = fields.Float(required=False)
    
    document_type = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    

