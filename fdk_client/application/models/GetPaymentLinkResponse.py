"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class GetPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    payment_link_url = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    external_order_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    payment_link_current_status = fields.Str(required=False)
    

