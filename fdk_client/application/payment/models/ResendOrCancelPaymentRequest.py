"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ResendOrCancelPaymentRequest(BaseSchema):
    #  swagger.json

    
    request_type = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
