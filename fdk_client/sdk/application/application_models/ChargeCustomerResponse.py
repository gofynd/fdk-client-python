"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema
















class ChargeCustomerResponse(BaseSchema):

    
    aggregator = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    delivery_address_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    

