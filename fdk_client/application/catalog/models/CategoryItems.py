"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Child import Child



from .CategoryBanner import CategoryBanner







from .ProductListingAction import ProductListingAction





class CategoryItems(BaseSchema):
    #  swagger.json

    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    banners = fields.Nested(CategoryBanner, required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    name = fields.Str(required=False)
    
