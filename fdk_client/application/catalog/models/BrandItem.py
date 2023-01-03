"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Media import Media









from .ImageUrls import ImageUrls





from .ProductListingAction import ProductListingAction







class BrandItem(BaseSchema):
    #  swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    uid = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
