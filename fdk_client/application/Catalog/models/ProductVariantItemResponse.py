"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .Media import Media





from .ProductListingAction import ProductListingAction













class ProductVariantItemResponse(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    color_name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    is_available = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
