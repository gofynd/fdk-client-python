"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .NetQuantity import NetQuantity



from .ProductBrand import ProductBrand



from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute







from .ProductVariantListingResponse import ProductVariantListingResponse













from .ApplicationItemMOQ import ApplicationItemMOQ



from .ApplicationItemSEO import ApplicationItemSEO



from .ProductListingAction import ProductListingAction

















from .CustomMetaFields import CustomMetaFields





from .ProductBrand import ProductBrand



from .Media import Media









from .ProductListingPrice import ProductListingPrice







from .ProductCategoryMap import ProductCategoryMap















class ProductListingDetail(BaseSchema):
    #  swagger.json

    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    description = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    teaser_tag = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    short_description = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    uid = fields.Int(required=False)
    
    color = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    rating_count = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    sellable = fields.Boolean(required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    attributes = fields.Dict(required=False)
    
    item_code = fields.Str(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rating = fields.Float(required=False)
    
