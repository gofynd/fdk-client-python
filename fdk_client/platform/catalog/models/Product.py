"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Brand import Brand





from .ProductPublished import ProductPublished











from .Image import Image

















































from .Media1 import Media1















class Product(BaseSchema):
    #  swagger.json

    
    brand = fields.Nested(Brand, required=False)
    
    slug = fields.Str(required=False)
    
    product_publish = fields.Nested(ProductPublished, required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    item_type = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    images = fields.List(fields.Nested(Image, required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    item_code = fields.Str(required=False)
    
    l3_mapping = fields.List(fields.Str(required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    sizes = fields.List(fields.Dict(required=False), required=False)
    
    variants = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    category_uid = fields.Int(required=False)
    
    size_guide = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    category_slug = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    short_description = fields.Str(required=False)
    
    primary_color = fields.Str(required=False)
    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    all_sizes = fields.List(fields.Dict(required=False), required=False)
    
    name = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    custom_order = fields.Dict(required=False)
    