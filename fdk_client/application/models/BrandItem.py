"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ImageUrls import ImageUrls

from .ProductListingAction import ProductListingAction









from .Media import Media


class BrandItem(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    name = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    

