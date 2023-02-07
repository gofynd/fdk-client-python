"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Phone import Phone



from .SubscriptionBillingAddress import SubscriptionBillingAddress











class SubscriptionCustomerCreate(BaseSchema):
    #  swagger.json

    
    phone = fields.Nested(Phone, required=False)
    
    billing_address = fields.Nested(SubscriptionBillingAddress, required=False)
    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
