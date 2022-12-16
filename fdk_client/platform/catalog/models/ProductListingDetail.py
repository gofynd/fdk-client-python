"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductBrand import ProductBrand









from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute





















from .ProductListingPrice import ProductListingPrice

















from .Media1 import Media1









class ProductListingDetail(BaseSchema):
    #  swagger.json

    
    brand = fields.Nested(ProductBrand, required=False)
    
    slug = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    product_online_date = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    attributes = fields.Dict(required=False)
    
    promo_meta = fields.Dict(required=False)
    
    rating_count = fields.Int(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    short_description = fields.Str(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    sellable = fields.Boolean(required=False)
    
    medias = fields.List(fields.Nested(Media1, required=False), required=False)
    
    name = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    