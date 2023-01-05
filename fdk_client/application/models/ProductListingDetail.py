"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ApplicationItemMOQ import ApplicationItemMOQ







from .ProductBrand import ProductBrand





from .ApplicationItemSEO import ApplicationItemSEO











from .ProductBrand import ProductBrand

from .ProductVariantListingResponse import ProductVariantListingResponse



from .NetQuantity import NetQuantity























from .Media import Media

from .ProductListingPrice import ProductListingPrice

from .CustomMetaFields import CustomMetaFields



from .ProductListingAction import ProductListingAction



from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute




class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    teaser_tag = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    product_online_date = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    sellable = fields.Boolean(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    item_type = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    has_variant = fields.Boolean(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    rating_count = fields.Int(required=False)
    
    image_nature = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    rating = fields.Float(required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    color = fields.Str(required=False)
    

