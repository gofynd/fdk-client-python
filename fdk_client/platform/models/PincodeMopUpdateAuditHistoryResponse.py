"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class PincodeMopUpdateAuditHistoryResponse(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    error_file_s3_url = fields.Str(required=False)
    
    s3_url = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    

