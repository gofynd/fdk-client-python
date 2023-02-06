"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Media import Media











from .ProductListingPrice import ProductListingPrice

from .NetQuantity import NetQuantity

from .CustomMetaFields import CustomMetaFields

from .ProductBrand import ProductBrand







from .ApplicationItemMOQ import ApplicationItemMOQ











from .ProductVariantListingResponse import ProductVariantListingResponse







from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute

from .ProductCategoryMap import ProductCategoryMap







from .ProductListingAction import ProductListingAction







from .ApplicationItemSEO import ApplicationItemSEO



from .ProductBrand import ProductBrand








class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    sellable = fields.Boolean(required=False)
    
    item_code = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    rating_count = fields.Int(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    rating = fields.Float(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    product_online_date = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    short_description = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    image_nature = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    

