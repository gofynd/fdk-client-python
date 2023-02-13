"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .BulkActionDetailsDataField import BulkActionDetailsDataField






class BulkActionDetailsResponse(BaseSchema):
    # Orders swagger.json

    
    status = fields.Boolean(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    error = fields.List(fields.Str(required=False), required=False)
    
    user_id = fields.Str(required=False)
    
    uploaded_on = fields.Str(required=False)
    
    success = fields.Str(required=False)
    
    data = fields.List(fields.Nested(BulkActionDetailsDataField, required=False), required=False)
    
    uploaded_by = fields.Str(required=False)
    
    message = fields.Str(required=False)
    

