"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema


















class ChargeCustomerResponse(BaseSchema):
    #  swagger.json

    
    cart_id = fields.Str(required=False)
    
    delivery_address_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
