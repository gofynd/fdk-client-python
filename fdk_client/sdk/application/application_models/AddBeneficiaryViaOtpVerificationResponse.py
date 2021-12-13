"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class AddBeneficiaryViaOtpVerificationResponse(BaseSchema):

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    

