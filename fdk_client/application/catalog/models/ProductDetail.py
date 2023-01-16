"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute









from .NetQuantity import NetQuantity













from .ProductListingPrice import ProductListingPrice







from .ApplicationItemMOQ import ApplicationItemMOQ





from .CustomMetaFields import CustomMetaFields



from .ProductBrand import ProductBrand



from .ApplicationItemSEO import ApplicationItemSEO





from .Media import Media



from .ProductListingAction import ProductListingAction









from .ProductBrand import ProductBrand









from .ProductCategoryMap import ProductCategoryMap





class ProductDetail(BaseSchema):
    #  swagger.json

    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    rating = fields.Float(required=False)
    
    rating_count = fields.Int(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    item_code = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    item_type = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    attributes = fields.Dict(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    name = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    short_description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    color = fields.Str(required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    teaser_tag = fields.Str(required=False)
    
