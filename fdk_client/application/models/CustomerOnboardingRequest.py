"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DeviceDetails import DeviceDetails

from .UserPersonalInfoInDetails import UserPersonalInfoInDetails



from .MarketplaceInfo import MarketplaceInfo

from .BusinessDetails import BusinessDetails




class CustomerOnboardingRequest(BaseSchema):
    # Payment swagger.json

    
    device = fields.Nested(DeviceDetails, required=False)
    
    personal_info = fields.Nested(UserPersonalInfoInDetails, required=False)
    
    source = fields.Str(required=False)
    
    marketplace_info = fields.Nested(MarketplaceInfo, required=False)
    
    business_info = fields.Nested(BusinessDetails, required=False)
    
    aggregator = fields.Str(required=False)
    

