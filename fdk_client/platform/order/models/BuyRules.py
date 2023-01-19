"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ItemCriterias import ItemCriterias





class BuyRules(BaseSchema):
    #  swagger.json

    
    item_criteria = fields.Nested(ItemCriterias, required=False)
    
    cart_conditions = fields.Dict(required=False)
    
