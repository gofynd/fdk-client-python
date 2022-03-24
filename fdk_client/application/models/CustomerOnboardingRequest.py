"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BusinessDetails import BusinessDetails

from .UserPersonalInfoInDetails import UserPersonalInfoInDetails





from .MarketplaceInfo import MarketplaceInfo

from .DeviceDetails import DeviceDetails


class CustomerOnboardingRequest(BaseSchema):
    # Payment swagger.json

    
    business_info = fields.Nested(BusinessDetails, required=False)
    
    personal_info = fields.Nested(UserPersonalInfoInDetails, required=False)
    
    aggregator = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    marketplace_info = fields.Nested(MarketplaceInfo, required=False)
    
    device = fields.Nested(DeviceDetails, required=False)
    

