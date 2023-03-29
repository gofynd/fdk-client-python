"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .BaseInfo import BaseInfo

from .BaseInfo import BaseInfo

from .ArticlePriceInfo import ArticlePriceInfo
















class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    is_gift_visible = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    cart_item_meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    gift_card = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    

