"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .ImageUrls import ImageUrls



from .ProductListingAction import ProductListingAction







from .Media import Media







class BrandItem(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    uid = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    discount = fields.Str(required=False)
    
