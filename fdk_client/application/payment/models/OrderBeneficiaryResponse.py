"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderBeneficiaryDetails import OrderBeneficiaryDetails





class OrderBeneficiaryResponse(BaseSchema):
    #  swagger.json

    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    
    show_beneficiary_details = fields.Boolean(required=False)
    
