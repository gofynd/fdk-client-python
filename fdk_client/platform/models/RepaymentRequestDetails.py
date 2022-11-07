"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class RepaymentRequestDetails(BaseSchema):
    # Payment swagger.json

    
    outstanding_details_id = fields.Int(required=False)
    
    amount = fields.Float(required=False)
    
    aggregator = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    fwd_shipment_id = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    aggregator_transaction_id = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    payment_mode_identifier = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    

