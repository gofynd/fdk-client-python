"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .PayoutBankDetails import PayoutBankDetails





class PayoutRequest(BaseSchema):
    #  swagger.json

    
    transfer_type = fields.Str(required=False)
    
    users = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    unique_external_id = fields.Str(required=False)
    
    bank_details = fields.Nested(PayoutBankDetails, required=False)
    
    aggregator = fields.Str(required=False)
    
