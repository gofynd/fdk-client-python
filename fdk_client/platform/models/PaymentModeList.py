"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .IntentAppErrorList import IntentAppErrorList









from .IntentApp import IntentApp















from .PaymentModeLogo import PaymentModeLogo






























class PaymentModeList(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    intent_app_error_dict_list = fields.List(fields.Nested(IntentAppErrorList, required=False), required=False)
    
    intent_app_error_list = fields.List(fields.Str(required=False), required=False)
    
    aggregator_name = fields.Str(required=False)
    
    card_type = fields.Str(required=False)
    
    card_issuer = fields.Str(required=False)
    
    intent_app = fields.List(fields.Nested(IntentApp, required=False), required=False)
    
    retry_count = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    card_reference = fields.Str(required=False)
    
    display_priority = fields.Int(required=False)
    
    intent_flow = fields.Boolean(required=False)
    
    timeout = fields.Int(required=False)
    
    expired = fields.Boolean(required=False)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    card_number = fields.Str(required=False)
    
    card_name = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    
    exp_year = fields.Int(required=False)
    
    nickname = fields.Str(required=False)
    
    exp_month = fields.Int(required=False)
    
    merchant_code = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    card_brand_image = fields.Str(required=False)
    
    card_brand = fields.Str(required=False)
    
    card_fingerprint = fields.Str(required=False)
    
    card_isin = fields.Str(required=False)
    
    fynd_vpa = fields.Str(required=False)
    
    card_token = fields.Str(required=False)
    

