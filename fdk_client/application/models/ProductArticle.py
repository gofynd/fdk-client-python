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

    
    identifier = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    size = fields.Str(required=False)
    

