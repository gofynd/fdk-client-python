"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute















from .ProductListingAction import ProductListingAction

from .MetaFields import MetaFields









from .ProductVariantListingResponse import ProductVariantListingResponse

from .ProductBrand import ProductBrand





from .ProductBrand import ProductBrand













from .ProductListingPrice import ProductListingPrice

from .Media import Media






class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    has_variant = fields.Boolean(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    rating = fields.Float(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    sellable = fields.Boolean(required=False)
    
    discount = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    _custom_meta = fields.List(fields.Nested(MetaFields, required=False), required=False)
    
    color = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    type = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    short_description = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    

