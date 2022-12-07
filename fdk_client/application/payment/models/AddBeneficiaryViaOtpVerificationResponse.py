"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class AddBeneficiaryViaOtpVerificationResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    