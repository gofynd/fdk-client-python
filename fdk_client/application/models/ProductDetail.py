"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



































from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute





from .CustomMetaFields import CustomMetaFields





from .ProductListingAction import ProductListingAction

from .ProductBrand import ProductBrand

from .ProductListingPrice import ProductListingPrice

from .ProductBrand import ProductBrand

from .Media import Media




class ProductDetail(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    teaser_tag = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    item_type = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    rating_count = fields.Int(required=False)
    
    short_description = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    product_online_date = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    description = fields.Str(required=False)
    

