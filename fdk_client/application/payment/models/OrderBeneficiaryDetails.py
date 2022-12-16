"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










































class OrderBeneficiaryDetails(BaseSchema):
    #  swagger.json

    
    display_name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    branch_name = fields.Str(required=False)
    
    delights_user_name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    