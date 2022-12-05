"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .ArticlePriceInfo import ArticlePriceInfo



from .BaseInfo import BaseInfo





from .BaseInfo import BaseInfo









class ProductArticle(BaseSchema):
    #  swagger.json

    
    uid = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    size = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
