"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute



from .ProductListingAction import ProductListingAction



from .NetQuantity import NetQuantity





from .ProductListingPrice import ProductListingPrice













from .ApplicationItemSEO import ApplicationItemSEO



from .ProductBrand import ProductBrand























from .ProductBrand import ProductBrand









from .CustomMetaFields import CustomMetaFields





from .ApplicationItemMOQ import ApplicationItemMOQ



from .ProductCategoryMap import ProductCategoryMap





from .Media import Media



class ProductDetail(BaseSchema):
    #  swagger.json

    
    color = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    short_description = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    item_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    rating = fields.Float(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    product_online_date = fields.Str(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    discount = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    item_code = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
