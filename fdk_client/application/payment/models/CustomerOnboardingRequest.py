"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .UserPersonalInfoInDetails import UserPersonalInfoInDetails





from .MarketplaceInfo import MarketplaceInfo



from .DeviceDetails import DeviceDetails



from .BusinessDetails import BusinessDetails



class CustomerOnboardingRequest(BaseSchema):
    #  swagger.json

    
    source = fields.Str(required=False)
    
    mcc = fields.Str(required=False)
    
    personal_info = fields.Nested(UserPersonalInfoInDetails, required=False)
    
    aggregator = fields.Str(required=False)
    
    marketplace_info = fields.Nested(MarketplaceInfo, required=False)
    
    device = fields.Nested(DeviceDetails, required=False)
    
    business_info = fields.Nested(BusinessDetails, required=False)
    
