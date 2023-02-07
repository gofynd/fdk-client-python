"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .CategoryBanner import CategoryBanner





from .ProductListingAction import ProductListingAction



from .Child import Child



class CategoryItems(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(CategoryBanner, required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
