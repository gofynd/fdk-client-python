"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class CustomerOnboardingRequest(BaseSchema):
    # Payment swagger.json

    
    personal_info = fields.Dict(required=False)
    
    business_info = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    device = fields.Dict(required=False)
    
    marketplace_info = fields.Dict(required=False)
    

