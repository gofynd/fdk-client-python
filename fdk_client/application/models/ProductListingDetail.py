"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ProductBrand import ProductBrand

from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute





from .ProductVariantListingResponse import ProductVariantListingResponse

from .ProductListingPrice import ProductListingPrice

from .CustomMetaFields import CustomMetaFields











from .ProductBrand import ProductBrand





from .Media import Media

























from .ProductListingAction import ProductListingAction


class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    rating_count = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    rating = fields.Float(required=False)
    
    description = fields.Str(required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    product_online_date = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    image_nature = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    sellable = fields.Boolean(required=False)
    
    short_description = fields.Str(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    

