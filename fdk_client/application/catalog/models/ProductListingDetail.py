"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Media import Media









from .ProductBrand import ProductBrand



from .ProductCategoryMap import ProductCategoryMap













from .CustomMetaFields import CustomMetaFields





from .ProductListingPrice import ProductListingPrice





from .ApplicationItemSEO import ApplicationItemSEO



from .ProductBrand import ProductBrand







from .NetQuantity import NetQuantity



from .ApplicationItemMOQ import ApplicationItemMOQ









from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute











from .ProductListingAction import ProductListingAction





from .ProductVariantListingResponse import ProductVariantListingResponse















class ProductListingDetail(BaseSchema):
    #  swagger.json

    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    product_online_date = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    sellable = fields.Boolean(required=False)
    
    item_type = fields.Str(required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    teaser_tag = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    rating_count = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    rating = fields.Float(required=False)
    
    description = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    discount = fields.Str(required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    short_description = fields.Str(required=False)
    
