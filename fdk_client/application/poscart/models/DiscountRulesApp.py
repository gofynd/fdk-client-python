"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class DiscountRulesApp(BaseSchema):
    #  swagger.json

    
    offer = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    
    raw_offer = fields.Dict(required=False)
    