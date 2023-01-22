"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .UserPersonalInfoInDetails import UserPersonalInfoInDetails





from .BusinessDetails import BusinessDetails





from .DeviceDetails import DeviceDetails



from .MarketplaceInfo import MarketplaceInfo



class CustomerOnboardingRequest(BaseSchema):
    #  swagger.json

    
    aggregator = fields.Str(required=False)
    
    personal_info = fields.Nested(UserPersonalInfoInDetails, required=False)
    
    mcc = fields.Str(required=False)
    
    business_info = fields.Nested(BusinessDetails, required=False)
    
    source = fields.Str(required=False)
    
    device = fields.Nested(DeviceDetails, required=False)
    
    marketplace_info = fields.Nested(MarketplaceInfo, required=False)
    