"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class SetDefaultBeneficiaryResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    is_beneficiary_set = fields.Boolean(required=False)
    
