"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PaymentModeLogo import PaymentModeLogo













from .PaymentModeList import PaymentModeList


class RootPaymentMode(BaseSchema):
    # Payment swagger.json

    
    aggregator_name = fields.Str(required=False)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    display_name = fields.Str(required=False)
    
    anonymous_enable = fields.Boolean(required=False)
    
    add_card_enabled = fields.Boolean(required=False)
    
    display_priority = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    

