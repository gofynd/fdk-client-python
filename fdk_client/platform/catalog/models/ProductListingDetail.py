"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .ProductListingPrice import ProductListingPrice





from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute

















from .ProductBrand import ProductBrand



from .Media1 import Media1

























class ProductListingDetail(BaseSchema):
    #  swagger.json

    
    product_online_date = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    rating_count = fields.Int(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    description = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    color = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    sellable = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    medias = fields.List(fields.Nested(Media1, required=False), required=False)
    
    promo_meta = fields.Dict(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    rating = fields.Float(required=False)
    
    short_description = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
