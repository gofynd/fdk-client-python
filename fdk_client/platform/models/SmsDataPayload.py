"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class SmsDataPayload(BaseSchema):
    # OrderManage swagger.json

    
    customer_name = fields.Str(required=False)
    
    phone_number = fields.Int(required=False)
    
    payment_mode = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    shipment_id = fields.Int(required=False)
    
    order_id = fields.Str(required=False)
    
    amount_paid = fields.Int(required=False)
    
    brand_name = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
