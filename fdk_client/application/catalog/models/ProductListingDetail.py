"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .ProductBrand import ProductBrand









from .ProductListingAction import ProductListingAction











from .Media import Media









from .ProductListingPrice import ProductListingPrice





from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute





from .CustomMetaFields import CustomMetaFields



from .NetQuantity import NetQuantity









from .ProductBrand import ProductBrand





from .ApplicationItemMOQ import ApplicationItemMOQ





from .ProductVariantListingResponse import ProductVariantListingResponse





from .ApplicationItemSEO import ApplicationItemSEO









class ProductListingDetail(BaseSchema):
    #  swagger.json

    
    short_description = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    rating_count = fields.Int(required=False)
    
    sellable = fields.Boolean(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    teaser_tag = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    discount = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    color = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    item_code = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    has_variant = fields.Boolean(required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    uid = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
