"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .BankDetailsForOTP import BankDetailsForOTP



class AddBeneficiaryDetailsOTPRequest(BaseSchema):
    #  swagger.json

    
    order_id = fields.Str(required=False)
    
    details = fields.Nested(BankDetailsForOTP, required=False)
    
