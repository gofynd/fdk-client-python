"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .BaseInfo import BaseInfo

from .ArticlePriceInfo import ArticlePriceInfo



from .BaseInfo import BaseInfo








class ProductArticle(BaseSchema):

    
    type = fields.Str(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    uid = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    

