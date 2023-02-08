"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Child import Child



from .ProductListingAction import ProductListingAction





from .CategoryBanner import CategoryBanner







class CategoryItems(BaseSchema):
    #  swagger.json

    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(CategoryBanner, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
