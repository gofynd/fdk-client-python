"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute



from .ProductListingPrice import ProductListingPrice



from .ProductVariantListingResponse import ProductVariantListingResponse







from .CustomMetaFields import CustomMetaFields





from .ApplicationItemMOQ import ApplicationItemMOQ































from .ProductCategoryMap import ProductCategoryMap



from .NetQuantity import NetQuantity



from .ProductBrand import ProductBrand





from .ApplicationItemSEO import ApplicationItemSEO





from .ProductBrand import ProductBrand







from .Media import Media







from .ProductListingAction import ProductListingAction







class ProductListingDetail(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    rating = fields.Float(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    color = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    short_description = fields.Str(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    attributes = fields.Dict(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    image_nature = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    sellable = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    item_code = fields.Str(required=False)
    
