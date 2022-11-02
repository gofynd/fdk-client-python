"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .PayoutBankDetails import PayoutBankDetails









class PayoutRequest(BaseSchema):
    #  swagger.json

    
    unique_external_id = fields.Str(required=False)
    
    transfer_type = fields.Str(required=False)
    
    bank_details = fields.Nested(PayoutBankDetails, required=False)
    
    users = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    