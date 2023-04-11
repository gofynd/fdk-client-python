"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class PollingPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    http_status = fields.Int(required=False)
    
    amount = fields.Float(required=False)
    
    status = fields.Str(required=False)
    
    payment_link_id = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    redirect_url = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    

