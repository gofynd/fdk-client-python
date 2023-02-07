"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class SubscriptionBillingAddress(BaseSchema):
    #  swagger.json

    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    line1 = fields.Str(required=False)
    
    line2 = fields.Str(required=False)
    
    postal_code = fields.Str(required=False)
    
