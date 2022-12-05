"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
























class PayoutBankDetails(BaseSchema):
    #  swagger.json

    
    ifsc_code = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    account_type = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
