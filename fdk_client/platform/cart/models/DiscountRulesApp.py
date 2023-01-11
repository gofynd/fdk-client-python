"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class DiscountRulesApp(BaseSchema):
    #  swagger.json

    
    item_criteria = fields.Dict(required=False)
    
    raw_offer = fields.Dict(required=False)
    
    offer = fields.Dict(required=False)
    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    
