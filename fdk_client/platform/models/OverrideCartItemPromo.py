"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class OverrideCartItemPromo(BaseSchema):
    # Cart swagger.json

    
    promo_id = fields.Str(required=False)
    
    item_list = fields.List(fields.Dict(required=False), required=False)
    
    promo_amount = fields.Str(required=False)
    
    rwrd_tndr = fields.Str(required=False)
    
    promo_desc = fields.Str(required=False)
    

