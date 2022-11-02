"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .ProductListingAction import ProductListingAction







from .Media import Media







class ProductVariantItemResponse(BaseSchema):
    #  swagger.json

    
    is_available = fields.Boolean(required=False)
    
    color_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    color = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    value = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
