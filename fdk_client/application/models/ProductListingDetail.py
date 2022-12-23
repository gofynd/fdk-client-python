"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute

from .CustomMetaFields import CustomMetaFields







from .ProductListingAction import ProductListingAction













from .Media import Media

from .ApplicationItemMOQ import ApplicationItemMOQ





from .ProductVariantListingResponse import ProductVariantListingResponse







from .ProductListingPrice import ProductListingPrice







from .ProductBrand import ProductBrand



from .ProductBrand import ProductBrand

from .ApplicationItemSEO import ApplicationItemSEO







from .NetQuantity import NetQuantity










class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    product_online_date = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    rating = fields.Float(required=False)
    
    slug = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    color = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    discount = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    teaser_tag = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    uid = fields.Int(required=False)
    
    short_description = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    sellable = fields.Boolean(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    type = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    

