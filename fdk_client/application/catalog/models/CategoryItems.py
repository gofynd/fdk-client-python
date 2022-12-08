"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ImageUrls import ImageUrls





from .ProductListingAction import ProductListingAction







from .Child import Child



class CategoryItems(BaseSchema):
    #  swagger.json

    
    banners = fields.Nested(ImageUrls, required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
