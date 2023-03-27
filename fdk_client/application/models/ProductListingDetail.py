"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ApplicationItemMOQ import ApplicationItemMOQ











from .Media import Media

from .ApplicationItemSEO import ApplicationItemSEO





from .CustomMetaFields import CustomMetaFields





from .ProductBrand import ProductBrand









from .NetQuantity import NetQuantity











from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute

from .ProductVariantListingResponse import ProductVariantListingResponse

from .ProductListingAction import ProductListingAction

from .ProductCategoryMap import ProductCategoryMap







from .ProductBrand import ProductBrand



from .ProductListingPrice import ProductListingPrice








class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    rating = fields.Float(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    sellable = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    attributes = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    item_code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    short_description = fields.Str(required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    product_online_date = fields.Str(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    color = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    

