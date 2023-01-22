"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class DiscountRulesApp(BaseSchema):
    #  swagger.json

    
    raw_offer = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    
    offer = fields.Dict(required=False)
    