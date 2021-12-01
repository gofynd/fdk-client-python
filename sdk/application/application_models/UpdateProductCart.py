"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema











from .CartProductIdentifer import CartProductIdentifer




class UpdateProductCart(BaseSchema):

    
    item_index = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    article_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    item_id = fields.Int(required=False)
    

