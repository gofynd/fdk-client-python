"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class SubscriptionActivateReq(BaseSchema):
    #  swagger.json

    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product_suite = fields.Str(required=False)
    
    plan_id = fields.Str(required=False)
    
    payment_method = fields.Str(required=False)
    
