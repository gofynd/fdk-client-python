"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute

















from .ProductListingAction import ProductListingAction











from .NetQuantity import NetQuantity



from .CustomMetaFields import CustomMetaFields

from .ApplicationItemSEO import ApplicationItemSEO

from .ProductBrand import ProductBrand



from .Media import Media



from .ProductBrand import ProductBrand







from .ProductListingPrice import ProductListingPrice





from .ApplicationItemMOQ import ApplicationItemMOQ



from .ProductCategoryMap import ProductCategoryMap




class ProductDetail(BaseSchema):
    # Catalog swagger.json

    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    rating = fields.Float(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    short_description = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    teaser_tag = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    rating_count = fields.Int(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    item_code = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    has_variant = fields.Boolean(required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    item_type = fields.Str(required=False)
    

