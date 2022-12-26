"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Media import Media











from .CustomMetaFields import CustomMetaFields

from .ProductListingAction import ProductListingAction


class ProductVariantItemResponse(BaseSchema):
    # Catalog swagger.json

    
    is_available = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    color = fields.Str(required=False)
    
    color_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    

