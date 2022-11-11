"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
























class PayoutResponse(BaseSchema):
    #  swagger.json

    
    payouts = fields.Dict(required=False)
    
    payment_status = fields.Str(required=False)
    
    unique_transfer_no = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    transfer_type = fields.Str(required=False)
    
    users = fields.Dict(required=False)
    
    created = fields.Boolean(required=False)
    
    bank_details = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
