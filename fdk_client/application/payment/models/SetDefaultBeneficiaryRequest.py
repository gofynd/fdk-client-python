"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class SetDefaultBeneficiaryRequest(BaseSchema):
    #  swagger.json

    
    beneficiary_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
