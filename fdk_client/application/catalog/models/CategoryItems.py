"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CategoryBanner import CategoryBanner



from .Child import Child









from .ProductListingAction import ProductListingAction



class CategoryItems(BaseSchema):
    #  swagger.json

    
    banners = fields.Nested(CategoryBanner, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
