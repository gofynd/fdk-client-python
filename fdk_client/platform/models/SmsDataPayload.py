"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class SmsDataPayload(BaseSchema):
    # Order swagger.json

    
    country_code = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    amount_paid = fields.Int(required=False)
    
    phone_number = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    shipment_id = fields.Int(required=False)
    
    customer_name = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    

