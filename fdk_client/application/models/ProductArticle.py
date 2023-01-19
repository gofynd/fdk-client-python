"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ArticlePriceInfo import ArticlePriceInfo





from .BaseInfo import BaseInfo





from .BaseInfo import BaseInfo










class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    identifier = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    uid = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    extra_meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    

