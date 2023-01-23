"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .CustomMetaFields import CustomMetaFields





from .ProductCategoryMap import ProductCategoryMap







from .ProductListingPrice import ProductListingPrice















from .ProductListingAction import ProductListingAction



from .ProductBrand import ProductBrand





from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute



from .ApplicationItemSEO import ApplicationItemSEO





from .Media import Media



















from .ApplicationItemMOQ import ApplicationItemMOQ



from .ProductBrand import ProductBrand





from .NetQuantity import NetQuantity





class ProductDetail(BaseSchema):
    #  swagger.json

    
    color = fields.Str(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    rating_count = fields.Int(required=False)
    
    short_description = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    image_nature = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    product_online_date = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    has_variant = fields.Boolean(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    uid = fields.Int(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    item_code = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    type = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    item_type = fields.Str(required=False)
    
