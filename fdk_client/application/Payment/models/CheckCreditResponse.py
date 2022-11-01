"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CreditDetail import CreditDetail





class CheckCreditResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(CreditDetail, required=False)
    
    success = fields.Boolean(required=False)
    
