"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BankDetailsForOTP import BankDetailsForOTP





class AddBeneficiaryDetailsOTPRequest(BaseSchema):
    #  swagger.json

    
    details = fields.Nested(BankDetailsForOTP, required=False)
    
    order_id = fields.Str(required=False)
    
