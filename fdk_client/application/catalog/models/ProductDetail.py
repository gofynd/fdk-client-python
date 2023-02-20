"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Media import Media













from .CustomMetaFields import CustomMetaFields







from .ProductBrand import ProductBrand



from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute



from .ProductListingAction import ProductListingAction







from .ProductCategoryMap import ProductCategoryMap





from .ApplicationItemMOQ import ApplicationItemMOQ





from .ApplicationItemSEO import ApplicationItemSEO







from .ProductListingPrice import ProductListingPrice













from .NetQuantity import NetQuantity





from .ProductBrand import ProductBrand











class ProductDetail(BaseSchema):
    #  swagger.json

    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    short_description = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    item_code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    item_type = fields.Str(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    teaser_tag = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    slug = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    uid = fields.Int(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    rating_count = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
