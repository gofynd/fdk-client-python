"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema


















class ChargeCustomerResponse(BaseSchema):
    #  swagger.json

    
    aggregator = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    cart_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    delivery_address_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
