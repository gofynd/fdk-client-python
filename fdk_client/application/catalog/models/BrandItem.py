"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductListingAction import ProductListingAction





from .Media import Media







from .ImageUrls import ImageUrls









class BrandItem(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(ProductListingAction, required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
