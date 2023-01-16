"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .ProductListingAction import ProductListingAction



from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute



from .ApplicationItemMOQ import ApplicationItemMOQ





from .Media import Media













from .NetQuantity import NetQuantity









from .ProductCategoryMap import ProductCategoryMap



from .ApplicationItemSEO import ApplicationItemSEO

















from .ProductListingPrice import ProductListingPrice





from .ProductBrand import ProductBrand



from .ProductBrand import ProductBrand





from .CustomMetaFields import CustomMetaFields







class ProductDetail(BaseSchema):
    #  swagger.json

    
    item_code = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    image_nature = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    has_variant = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    product_online_date = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    rating_count = fields.Int(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    discount = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    short_description = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    teaser_tag = fields.Str(required=False)
    