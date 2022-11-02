"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .MarketplaceInfo import MarketplaceInfo





from .UserPersonalInfoInDetails import UserPersonalInfoInDetails





from .BusinessDetails import BusinessDetails



from .DeviceDetails import DeviceDetails



class CustomerOnboardingRequest(BaseSchema):
    #  swagger.json

    
    source = fields.Str(required=False)
    
    marketplace_info = fields.Nested(MarketplaceInfo, required=False)
    
    mcc = fields.Str(required=False)
    
    personal_info = fields.Nested(UserPersonalInfoInDetails, required=False)
    
    aggregator = fields.Str(required=False)
    
    business_info = fields.Nested(BusinessDetails, required=False)
    
    device = fields.Nested(DeviceDetails, required=False)
    