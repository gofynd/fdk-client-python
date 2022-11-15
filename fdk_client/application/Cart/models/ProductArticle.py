"""Cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .BaseInfo import BaseInfo



from .BaseInfo import BaseInfo







from .ArticlePriceInfo import ArticlePriceInfo











class ProductArticle(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    uid = fields.Str(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    extra_meta = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
