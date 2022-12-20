"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .ProductBrand import ProductBrand







from .Media import Media





from .CustomMetaFields import CustomMetaFields



from .NetQuantity import NetQuantity



from .ApplicationItemSEO import ApplicationItemSEO









from .ProductListingAction import ProductListingAction

from .ProductVariantListingResponse import ProductVariantListingResponse

from .ApplicationItemMOQ import ApplicationItemMOQ









from .ProductListingPrice import ProductListingPrice



from .ProductBrand import ProductBrand







from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute




class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    image_nature = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    rating_count = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    item_code = fields.Str(required=False)
    
    sellable = fields.Boolean(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    description = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    has_variant = fields.Boolean(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    color = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    rating = fields.Float(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    slug = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    item_type = fields.Str(required=False)
    

