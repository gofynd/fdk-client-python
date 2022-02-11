"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class CustomerOnboardingRequest(BaseSchema):
    # Payment swagger.json

    
    business_info = fields.Dict(required=False)
    
    personal_info = fields.Dict(required=False)
    
    marketplace_info = fields.Dict(required=False)
    
    device = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    

