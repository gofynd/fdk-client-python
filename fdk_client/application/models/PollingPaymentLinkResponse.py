"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class PollingPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    payment_link_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    http_status = fields.Int(required=False)
    
    order_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    status_code = fields.Int(required=False)
    
    redirect_url = fields.Str(required=False)
    
    message = fields.Str(required=False)
    

