"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductBrand import ProductBrand















from .CustomMetaFields import CustomMetaFields



from .ApplicationItemSEO import ApplicationItemSEO











from .ProductListingPrice import ProductListingPrice



from .ProductBrand import ProductBrand







from .Media import Media







from .ApplicationItemMOQ import ApplicationItemMOQ









from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute



from .ProductListingAction import ProductListingAction











class ProductDetail(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    product_online_date = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    uid = fields.Int(required=False)
    
    attributes = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    item_type = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    short_description = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    has_variant = fields.Boolean(required=False)
    
    image_nature = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
