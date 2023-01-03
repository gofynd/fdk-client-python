"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class BuyRules(BaseSchema):
    #  swagger.json

    
    item_criteria = fields.Dict(required=False)
    
    cart_conditions = fields.Dict(required=False)
    
