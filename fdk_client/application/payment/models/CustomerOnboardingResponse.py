"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .OnboardSummary import OnboardSummary



class CustomerOnboardingResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(OnboardSummary, required=False)
    
