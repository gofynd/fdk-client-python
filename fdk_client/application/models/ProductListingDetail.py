"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductListingPrice import ProductListingPrice

from .ProductVariantListingResponse import ProductVariantListingResponse









from .ApplicationItemMOQ import ApplicationItemMOQ





from .ProductBrand import ProductBrand

from .ApplicationItemSEO import ApplicationItemSEO







from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute























from .CustomMetaFields import CustomMetaFields







from .NetQuantity import NetQuantity

from .Media import Media

from .ProductBrand import ProductBrand



from .ProductListingAction import ProductListingAction


class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    product_online_date = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    sellable = fields.Boolean(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    short_description = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    teaser_tag = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    rating = fields.Float(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    

