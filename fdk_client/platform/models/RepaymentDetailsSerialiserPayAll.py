"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .RepaymentRequestDetails import RepaymentRequestDetails




class RepaymentDetailsSerialiserPayAll(BaseSchema):
    # Payment swagger.json

    
    aggregator_transaction_id = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    extension_order_id = fields.Str(required=False)
    
    shipment_details = fields.List(fields.Nested(RepaymentRequestDetails, required=False), required=False)
    
    total_amount = fields.Float(required=False)
    

