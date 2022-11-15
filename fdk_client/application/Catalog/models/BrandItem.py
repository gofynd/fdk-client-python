"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ImageUrls import ImageUrls



from .ProductListingAction import ProductListingAction











from .Media import Media







class BrandItem(BaseSchema):
    #  swagger.json

    
    banners = fields.Nested(ImageUrls, required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    description = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
