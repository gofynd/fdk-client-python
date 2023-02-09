"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductBrand import ProductBrand



from .NetQuantity import NetQuantity





from .ProductListingPrice import ProductListingPrice



from .ProductBrand import ProductBrand







from .Media import Media



from .ApplicationItemMOQ import ApplicationItemMOQ









from .ProductListingAction import ProductListingAction

from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute













from .ApplicationItemSEO import ApplicationItemSEO

from .CustomMetaFields import CustomMetaFields



from .ProductVariantListingResponse import ProductVariantListingResponse












class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    has_variant = fields.Boolean(required=False)
    
    rating_count = fields.Int(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    product_online_date = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    color = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    teaser_tag = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    sellable = fields.Boolean(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    short_description = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

