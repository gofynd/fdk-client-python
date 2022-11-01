"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .BeneficiaryModeDetails import BeneficiaryModeDetails







class AddBeneficiaryDetailsRequest(BaseSchema):
    #  swagger.json

    
    shipment_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    
    delights = fields.Boolean(required=False)
    
    details = fields.Nested(BeneficiaryModeDetails, required=False)
    
    transfer_mode = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
