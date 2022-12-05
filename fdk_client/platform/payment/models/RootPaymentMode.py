"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















from .PaymentModeList import PaymentModeList





class RootPaymentMode(BaseSchema):
    #  swagger.json

    
    is_pay_by_card_pl = fields.Boolean(required=False)
    
    add_card_enabled = fields.Boolean(required=False)
    
    save_card = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    anonymous_enable = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    
    display_priority = fields.Int(required=False)
    
