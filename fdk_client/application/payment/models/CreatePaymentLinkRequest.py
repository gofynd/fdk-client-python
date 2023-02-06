"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .CreatePaymentLinkMeta import CreatePaymentLinkMeta









class CreatePaymentLinkRequest(BaseSchema):
    #  swagger.json

    
    mobile_number = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    meta = fields.Nested(CreatePaymentLinkMeta, required=False)
    
    external_order_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
