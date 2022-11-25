"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class BulkPresignedSuccessResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    presigned_type = fields.Str(required=False)
    
    presigned_url = fields.Str(required=False)
    
    expires_in = fields.Float(required=False)
    

