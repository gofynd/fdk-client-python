"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute

from .ProductBrand import ProductBrand

from .MetaFields import MetaFields



from .ActionPage import ActionPage





from .ProductBrand import ProductBrand

























from .Media import Media

from .ProductListingPrice import ProductListingPrice










class ProductDetail(BaseSchema):
    # Catalog swagger.json

    
    attributes = fields.Dict(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    _custom_meta = fields.List(fields.Nested(MetaFields, required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    product_online_date = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    short_description = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    color = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    image_nature = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    rating = fields.Float(required=False)
    
    discount = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    

