"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ResendOrCancelPaymentRequest(BaseSchema):
    #  swagger.json

    
    order_id = fields.Str(required=False)
    
    request_type = fields.Str(required=False)
    
