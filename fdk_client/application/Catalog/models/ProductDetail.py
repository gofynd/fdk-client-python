"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














from .ProductListingAction import ProductListingAction











from .Media import Media









from .ProductBrand import ProductBrand





from .CustomMetaFields import CustomMetaFields









from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute





from .ProductListingPrice import ProductListingPrice





from .ProductBrand import ProductBrand











class ProductDetail(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    color = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    item_code = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    product_online_date = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    short_description = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    teaser_tag = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    name = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    attributes = fields.Dict(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    item_type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
