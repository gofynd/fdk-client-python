"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema














class SubscriptionBillingAddress(BaseSchema):

    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    line1 = fields.Str(required=False)
    
    line2 = fields.Str(required=False)
    
    postal_code = fields.Str(required=False)
    

