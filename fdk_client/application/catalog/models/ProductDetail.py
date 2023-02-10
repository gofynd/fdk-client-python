"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .ProductListingPrice import ProductListingPrice



from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute









from .ApplicationItemMOQ import ApplicationItemMOQ



from .NetQuantity import NetQuantity

















from .ProductListingAction import ProductListingAction







from .Media import Media



from .ProductBrand import ProductBrand









from .ProductCategoryMap import ProductCategoryMap





from .ProductBrand import ProductBrand









from .ApplicationItemSEO import ApplicationItemSEO





from .CustomMetaFields import CustomMetaFields



class ProductDetail(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    has_variant = fields.Boolean(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    product_online_date = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    short_description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    item_type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_code = fields.Str(required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    rating_count = fields.Int(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    teaser_tag = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    attributes = fields.Dict(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
