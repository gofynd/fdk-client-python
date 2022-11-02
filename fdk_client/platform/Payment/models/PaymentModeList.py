"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















from .IntentApp import IntentApp













from .PaymentModeLogo import PaymentModeLogo





























from .IntentAppErrorList import IntentAppErrorList



class PaymentModeList(BaseSchema):
    #  swagger.json

    
    display_name = fields.Str(required=False)
    
    card_reference = fields.Str(required=False)
    
    card_number = fields.Str(required=False)
    
    expired = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    card_token = fields.Str(required=False)
    
    card_fingerprint = fields.Str(required=False)
    
    exp_month = fields.Int(required=False)
    
    intent_app = fields.List(fields.Nested(IntentApp, required=False), required=False)
    
    exp_year = fields.Int(required=False)
    
    compliant_with_tokenisation_guidelines = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    card_brand_image = fields.Str(required=False)
    
    card_type = fields.Str(required=False)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    fynd_vpa = fields.Str(required=False)
    
    card_isin = fields.Str(required=False)
    
    card_issuer = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    
    card_name = fields.Str(required=False)
    
    nickname = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    intent_app_error_list = fields.List(fields.Str(required=False), required=False)
    
    timeout = fields.Int(required=False)
    
    intent_flow = fields.Boolean(required=False)
    
    display_priority = fields.Int(required=False)
    
    retry_count = fields.Int(required=False)
    
    card_brand = fields.Str(required=False)
    
    intent_app_error_dict_list = fields.List(fields.Nested(IntentAppErrorList, required=False), required=False)
    