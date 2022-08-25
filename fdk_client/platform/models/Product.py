"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .Image import Image











from .Brand import Brand













from .Media1 import Media1













from .ProductPublished import ProductPublished






















class Product(BaseSchema):
    # Catalog swagger.json

    
    size_guide = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    primary_color = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    images = fields.List(fields.Nested(Image, required=False), required=False)
    
    is_physical = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    brand_uid = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    template_tag = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    image_nature = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    all_sizes = fields.List(fields.Dict(required=False), required=False)
    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    multi_size = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    l3_mapping = fields.List(fields.Str(required=False), required=False)
    
    product_publish = fields.Nested(ProductPublished, required=False)
    
    custom_order = fields.Dict(required=False)
    
    moq = fields.Dict(required=False)
    
    variants = fields.Dict(required=False)
    
    category_slug = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    sizes = fields.List(fields.Dict(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    category_uid = fields.Int(required=False)
    
    color = fields.Str(required=False)
    

