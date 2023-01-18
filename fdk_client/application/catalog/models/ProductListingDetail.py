"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ApplicationItemSEO import ApplicationItemSEO



from .ProductBrand import ProductBrand











from .ApplicationItemMOQ import ApplicationItemMOQ







from .ProductListingPrice import ProductListingPrice







from .CustomMetaFields import CustomMetaFields

















from .NetQuantity import NetQuantity









from .ProductVariantListingResponse import ProductVariantListingResponse



from .ProductListingAction import ProductListingAction













from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute





from .ProductBrand import ProductBrand



from .ProductCategoryMap import ProductCategoryMap





from .Media import Media



class ProductListingDetail(BaseSchema):
    #  swagger.json

    
    discount = fields.Str(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    rating = fields.Float(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    teaser_tag = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    color = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    sellable = fields.Boolean(required=False)
    
    rating_count = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    has_variant = fields.Boolean(required=False)
    
    item_code = fields.Str(required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    product_online_date = fields.Str(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
