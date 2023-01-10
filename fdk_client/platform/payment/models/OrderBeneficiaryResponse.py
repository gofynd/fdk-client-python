"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .OrderBeneficiaryDetails import OrderBeneficiaryDetails



class OrderBeneficiaryResponse(BaseSchema):
    #  swagger.json

    
    show_beneficiary_details = fields.Boolean(required=False)
    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    
