"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductBrand import ProductBrand

from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute





















from .Media1 import Media1


















class ProductDetail(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    rating = fields.Float(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    color = fields.Str(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    item_type = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    medias = fields.List(fields.Nested(Media1, required=False), required=False)
    
    promo_meta = fields.Dict(required=False)
    
    short_description = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    image_nature = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    

