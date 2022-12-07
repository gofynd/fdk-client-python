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

    
    seller = fields.Nested(BaseInfo, required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    identifier = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    

