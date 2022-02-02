"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OnboardSummary import OnboardSummary




class CustomerOnboardingResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(OnboardSummary, required=False), required=False)
    
    success = fields.Boolean(required=False)
    

