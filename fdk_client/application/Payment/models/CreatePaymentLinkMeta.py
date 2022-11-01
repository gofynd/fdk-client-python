"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class CreatePaymentLinkMeta(BaseSchema):
    #  swagger.json

    
    assign_card_id = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
