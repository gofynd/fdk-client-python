"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class BulkActionDetailsDataField(BaseSchema):
    # Orders swagger.json

    
    processing_shipments_count = fields.Int(required=False)
    
    batch_id = fields.Str(required=False)
    
    successful_shipments_count = fields.Int(required=False)
    
    failed_shipments_count = fields.Int(required=False)
    
    company_id = fields.Str(required=False)
    
    total_shipments_count = fields.Int(required=False)
    
    successful_shipment_ids = fields.List(fields.Str(required=False), required=False)
    

