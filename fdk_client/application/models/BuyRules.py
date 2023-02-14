"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class BuyRules(BaseSchema):
    # Cart swagger.json

    
    item_criteria = fields.Dict(required=False)
    
    cart_conditions = fields.Dict(required=False)
    

