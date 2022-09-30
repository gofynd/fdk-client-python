"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductListingPrice import ProductListingPrice





from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute



from .CustomMetaFields import CustomMetaFields







from .ProductListingAction import ProductListingAction







from .Media import Media



from .ProductBrand import ProductBrand

from .ProductBrand import ProductBrand











from .ProductVariantListingResponse import ProductVariantListingResponse
















class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    teaser_tag = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    rating = fields.Float(required=False)
    
    item_type = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    has_variant = fields.Boolean(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    short_description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    rating_count = fields.Int(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    sellable = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    product_online_date = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    color = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    

