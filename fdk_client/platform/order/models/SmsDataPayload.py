"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















class SmsDataPayload(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    customer_name = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    amount_paid = fields.Int(required=False)
    
    payment_mode = fields.Str(required=False)
    
    shipment_id = fields.Int(required=False)
    
    phone_number = fields.Int(required=False)
    
    country_code = fields.Str(required=False)
    
