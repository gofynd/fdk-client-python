"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










































class bulkListingData(BaseSchema):
    #  swagger.json

    
    store_name = fields.Str(required=False)
    
    processing_shipments = fields.List(fields.Str(required=False), required=False)
    
    status = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    user_id = fields.Str(required=False)
    
    excel_url = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    uploaded_on = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    file_name = fields.Str(required=False)
    
    successful = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    processing = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    failed_shipments = fields.List(fields.Dict(required=False), required=False)
    
    successful_shipments = fields.List(fields.Dict(required=False), required=False)
    
    user_name = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
