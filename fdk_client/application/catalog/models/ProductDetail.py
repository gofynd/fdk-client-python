"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














from .CustomMetaFields import CustomMetaFields



from .Media import Media



from .ProductListingPrice import ProductListingPrice



from .ApplicationItemMOQ import ApplicationItemMOQ



from .ApplicationItemSEO import ApplicationItemSEO







from .NetQuantity import NetQuantity













from .ProductCategoryMap import ProductCategoryMap



from .ProductBrand import ProductBrand









from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute



from .ProductListingAction import ProductListingAction





from .ProductBrand import ProductBrand

















class ProductDetail(BaseSchema):
    #  swagger.json

    
    rating_count = fields.Int(required=False)
    
    color = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    item_type = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    rating = fields.Float(required=False)
    
    attributes = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    short_description = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    discount = fields.Str(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    description = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
