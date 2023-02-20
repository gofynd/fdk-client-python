"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















from .ProductPublished import ProductPublished











from .Brand import Brand





from .Media1 import Media1



























from .ReturnConfigResponse import ReturnConfigResponse























from .Image import Image









from .VerifiedBy import VerifiedBy









from .NetQuantityResponse import NetQuantityResponse































class Product(BaseSchema):
    #  swagger.json

    
    image_nature = fields.Str(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    pending = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    category_slug = fields.Str(required=False)
    
    product_publish = fields.Nested(ProductPublished, required=False)
    
    category_uid = fields.Int(required=False)
    
    all_sizes = fields.List(fields.Dict(required=False), required=False)
    
    is_physical = fields.Boolean(required=False)
    
    modified_by = fields.Dict(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    is_active = fields.Boolean(required=False)
    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    description = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    sizes = fields.List(fields.Dict(required=False), required=False)
    
    all_company_ids = fields.List(fields.Int(required=False), required=False)
    
    custom_order = fields.Dict(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    all_identifiers = fields.List(fields.Str(required=False), required=False)
    
    return_config = fields.Nested(ReturnConfigResponse, required=False)
    
    short_description = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    l3_mapping = fields.List(fields.Str(required=False), required=False)
    
    hsn_code = fields.Str(required=False)
    
    moq = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    variant_group = fields.Dict(required=False)
    
    images = fields.List(fields.Nested(Image, required=False), required=False)
    
    variant_media = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    size_guide = fields.Str(required=False)
    
    verified_by = fields.Nested(VerifiedBy, required=False)
    
    verified_on = fields.Str(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    net_quantity = fields.Nested(NetQuantityResponse, required=False)
    
    name = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    trader = fields.List(fields.Dict(required=False), required=False)
    
    is_set = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    variants = fields.Dict(required=False)
    
    primary_color = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    category = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
