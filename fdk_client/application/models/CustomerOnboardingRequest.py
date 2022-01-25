"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BusinessDetails import BusinessDetails

from .UserPersonalInfoInDetails import UserPersonalInfoInDetails

from .DeviceDetails import DeviceDetails


class CustomerOnboardingRequest(BaseSchema):
    # Payment swagger.json

    
    business_info = fields.List(fields.Nested(BusinessDetails, required=False), required=False)
    
    personal_info = fields.List(fields.Nested(UserPersonalInfoInDetails, required=False), required=False)
    
    device = fields.List(fields.Nested(DeviceDetails, required=False), required=False)
    

