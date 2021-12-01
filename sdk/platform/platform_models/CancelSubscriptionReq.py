"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class CancelSubscriptionReq(BaseSchema):

    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product_suite = fields.Str(required=False)
    
    subscription_id = fields.Str(required=False)
    

