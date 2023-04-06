"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CustomMetaFields import CustomMetaFields

from .ApplicationItemSEO import ApplicationItemSEO

from .NetQuantity import NetQuantity











from .Media import Media







from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute



from .ProductListingPrice import ProductListingPrice









from .ApplicationItemMOQ import ApplicationItemMOQ





from .ProductListingAction import ProductListingAction



from .ProductBrand import ProductBrand

from .ProductCategoryMap import ProductCategoryMap





from .ProductBrand import ProductBrand








class ProductDetail(BaseSchema):
    # Catalog swagger.json

    
    item_type = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    description = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    type = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    rating_count = fields.Int(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    discount = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    item_code = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    short_description = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    color = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    

