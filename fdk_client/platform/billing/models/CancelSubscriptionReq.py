"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class CancelSubscriptionReq(BaseSchema):
    #  swagger.json

    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product_suite = fields.Str(required=False)
    
    subscription_id = fields.Str(required=False)
    
