"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class BankDetailsForOTP(BaseSchema):
    #  swagger.json

    
    branch_name = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
