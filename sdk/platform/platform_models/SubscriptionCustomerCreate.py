"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Phone import Phone

from .SubscriptionBillingAddress import SubscriptionBillingAddress










class SubscriptionCustomerCreate(BaseSchema):

    
    phone = fields.Nested(Phone, required=False)
    
    billing_address = fields.Nested(SubscriptionBillingAddress, required=False)
    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    

