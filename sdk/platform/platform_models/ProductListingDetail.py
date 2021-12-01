"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema











from .ProductListingPrice import ProductListingPrice





from .ProductBrand import ProductBrand

from .Media1 import Media1



















from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute














class ProductListingDetail(BaseSchema):

    
    short_description = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    item_code = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    item_type = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    medias = fields.List(fields.Nested(Media1, required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    rating = fields.Float(required=False)
    
    product_online_date = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    sellable = fields.Boolean(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    color = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    promo_meta = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    

