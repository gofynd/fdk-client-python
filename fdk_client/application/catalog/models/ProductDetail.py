"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductBrand import ProductBrand













from .ProductListingAction import ProductListingAction



from .ProductBrand import ProductBrand



from .Media import Media



















from .NetQuantity import NetQuantity



from .ApplicationItemSEO import ApplicationItemSEO





from .ProductCategoryMap import ProductCategoryMap



from .ApplicationItemMOQ import ApplicationItemMOQ













from .ProductListingPrice import ProductListingPrice



from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute









from .CustomMetaFields import CustomMetaFields



class ProductDetail(BaseSchema):
    #  swagger.json

    
    item_code = fields.Str(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    image_nature = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    short_description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    rating = fields.Float(required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    color = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    rating_count = fields.Int(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    product_online_date = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
