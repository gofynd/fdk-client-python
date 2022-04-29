"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .BaseInfo import BaseInfo

from .BaseInfo import BaseInfo







from .ArticlePriceInfo import ArticlePriceInfo






class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    size = fields.Str(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Str(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    parent_item_size = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    extra_meta = fields.Dict(required=False)
    
    parent_item_id = fields.Str(required=False)
    

