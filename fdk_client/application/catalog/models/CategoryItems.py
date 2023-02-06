"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductListingAction import ProductListingAction





from .Child import Child





from .CategoryBanner import CategoryBanner





class CategoryItems(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(ProductListingAction, required=False)
    
    slug = fields.Str(required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(CategoryBanner, required=False)
    
    uid = fields.Int(required=False)
    
