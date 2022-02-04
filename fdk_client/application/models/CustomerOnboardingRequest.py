"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DeviceDetails import DeviceDetails

from .MarketplaceInfo import MarketplaceInfo

from .BusinessDetails import BusinessDetails

from .UserPersonalInfoInDetails import UserPersonalInfoInDetails


class CustomerOnboardingRequest(BaseSchema):
    # Payment swagger.json

    
    device = fields.List(fields.Nested(DeviceDetails, required=False), required=False)
    
    marketplace_info = fields.List(fields.Nested(MarketplaceInfo, required=False), required=False)
    
    business_info = fields.List(fields.Nested(BusinessDetails, required=False), required=False)
    
    personal_info = fields.List(fields.Nested(UserPersonalInfoInDetails, required=False), required=False)
    

