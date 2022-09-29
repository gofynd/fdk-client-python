"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DeviceDetails import DeviceDetails

from .MarketplaceInfo import MarketplaceInfo



from .UserPersonalInfoInDetails import UserPersonalInfoInDetails

from .BusinessDetails import BusinessDetails




class CustomerOnboardingRequest(BaseSchema):
    # Payment swagger.json

    
    device = fields.Nested(DeviceDetails, required=False)
    
    marketplace_info = fields.Nested(MarketplaceInfo, required=False)
    
    source = fields.Str(required=False)
    
    personal_info = fields.Nested(UserPersonalInfoInDetails, required=False)
    
    business_info = fields.Nested(BusinessDetails, required=False)
    
    aggregator = fields.Str(required=False)
    

