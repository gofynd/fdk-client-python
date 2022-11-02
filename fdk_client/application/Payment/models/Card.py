"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






































class Card(BaseSchema):
    #  swagger.json

    
    card_reference = fields.Str(required=False)
    
    card_token = fields.Str(required=False)
    
    card_brand = fields.Str(required=False)
    
    card_name = fields.Str(required=False)
    
    expired = fields.Boolean(required=False)
    
    compliant_with_tokenisation_guidelines = fields.Boolean(required=False)
    
    card_type = fields.Str(required=False)
    
    card_number = fields.Str(required=False)
    
    exp_month = fields.Int(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    card_fingerprint = fields.Str(required=False)
    
    nickname = fields.Str(required=False)
    
    exp_year = fields.Int(required=False)
    
    card_isin = fields.Str(required=False)
    
    card_brand_image = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    
    card_issuer = fields.Str(required=False)
    