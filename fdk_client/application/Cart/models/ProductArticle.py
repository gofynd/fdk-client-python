"""Cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .BaseInfo import BaseInfo











from .ArticlePriceInfo import ArticlePriceInfo



from .BaseInfo import BaseInfo









class ProductArticle(BaseSchema):
    #  swagger.json

    
    seller = fields.Nested(BaseInfo, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    extra_meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    size = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
