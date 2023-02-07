"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductCategoryMap import ProductCategoryMap



from .ProductBrand import ProductBrand









from .NetQuantity import NetQuantity















from .CustomMetaFields import CustomMetaFields







from .ProductListingAction import ProductListingAction





from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute









from .ApplicationItemSEO import ApplicationItemSEO









from .ApplicationItemMOQ import ApplicationItemMOQ



from .ProductListingPrice import ProductListingPrice





from .ProductBrand import ProductBrand



from .Media import Media









class ProductDetail(BaseSchema):
    #  swagger.json

    
    teaser_tag = fields.Str(required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    type = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    slug = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    rating_count = fields.Int(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    rating = fields.Float(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    image_nature = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    has_variant = fields.Boolean(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    product_online_date = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    name = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    short_description = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
