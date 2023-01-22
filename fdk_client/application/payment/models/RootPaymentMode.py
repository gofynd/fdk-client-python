"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .PaymentModeList import PaymentModeList















class RootPaymentMode(BaseSchema):
    #  swagger.json

    
    anonymous_enable = fields.Boolean(required=False)
    
    save_card = fields.Boolean(required=False)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    
    name = fields.Str(required=False)
    
    display_priority = fields.Int(required=False)
    
    is_pay_by_card_pl = fields.Boolean(required=False)
    
    add_card_enabled = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    