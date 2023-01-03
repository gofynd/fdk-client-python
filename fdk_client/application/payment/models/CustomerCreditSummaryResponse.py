"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CreditSummary import CreditSummary





class CustomerCreditSummaryResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(CreditSummary, required=False)
    
    success = fields.Boolean(required=False)
    
