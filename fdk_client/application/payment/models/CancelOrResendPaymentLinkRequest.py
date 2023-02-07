"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class CancelOrResendPaymentLinkRequest(BaseSchema):
    #  swagger.json

    
    payment_link_id = fields.Str(required=False)
    
