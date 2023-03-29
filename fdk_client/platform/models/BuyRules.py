"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ItemCriterias import ItemCriterias


class BuyRules(BaseSchema):
    # Order swagger.json

    
    cart_conditions = fields.Dict(required=False)
    
    item_criteria = fields.Nested(ItemCriterias, required=False)
    

