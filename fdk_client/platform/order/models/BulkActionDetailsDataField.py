"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class BulkActionDetailsDataField(BaseSchema):
    #  swagger.json

    
    failed_shipments_count = fields.Int(required=False)
    
    successful_shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    total_shipments_count = fields.Int(required=False)
    
    successful_shipments_count = fields.Int(required=False)
    
    processing_shipments_count = fields.Int(required=False)
    
    company_id = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    