"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .MarketplaceInfo import MarketplaceInfo

from .UserPersonalInfoInDetails import UserPersonalInfoInDetails

from .DeviceDetails import DeviceDetails

from .BusinessDetails import BusinessDetails


class CustomerOnboardingRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    marketplace_info = fields.Nested(MarketplaceInfo, required=False)
    
    personal_info = fields.Nested(UserPersonalInfoInDetails, required=False)
    
    device = fields.Nested(DeviceDetails, required=False)
    
    business_info = fields.Nested(BusinessDetails, required=False)
    

