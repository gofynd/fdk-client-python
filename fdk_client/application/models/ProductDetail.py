"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .ProductListingAction import ProductListingAction













from .ProductListingPrice import ProductListingPrice

from .Media import Media

from .CustomMetaFields import CustomMetaFields





from .ProductBrand import ProductBrand



from .ApplicationItemMOQ import ApplicationItemMOQ





from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute



from .ProductBrand import ProductBrand









from .ApplicationItemSEO import ApplicationItemSEO


class ProductDetail(BaseSchema):
    # Catalog swagger.json

    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    rating = fields.Float(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    has_variant = fields.Boolean(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    rating_count = fields.Int(required=False)
    
    attributes = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    description = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    discount = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    teaser_tag = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    

