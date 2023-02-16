"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















from .BulkActionDetailsDataField import BulkActionDetailsDataField



class BulkActionDetailsResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Str(required=False)
    
    error = fields.List(fields.Str(required=False), required=False)
    
    uploaded_on = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    
    uploaded_by = fields.Str(required=False)
    
    data = fields.List(fields.Nested(BulkActionDetailsDataField, required=False), required=False)
    
