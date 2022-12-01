"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .LinkStatus import LinkStatus





class ResendOrCancelPaymentResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(LinkStatus, required=False)
    
    success = fields.Boolean(required=False)
    
