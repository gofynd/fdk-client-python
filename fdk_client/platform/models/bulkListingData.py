"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








































class bulkListingData(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    batch_id = fields.Str(required=False)
    
    user_name = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    uploaded_on = fields.Str(required=False)
    
    successful_shipments = fields.List(fields.Dict(required=False), required=False)
    
    successful = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    excel_url = fields.Str(required=False)
    
    processing_shipments = fields.List(fields.Str(required=False), required=False)
    
    failed = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    failed_shipments = fields.List(fields.Dict(required=False), required=False)
    
    processing = fields.Int(required=False)
    
    store_name = fields.Str(required=False)
    

