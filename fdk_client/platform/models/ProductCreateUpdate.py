"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .TaxIdentifier import TaxIdentifier

from .Trader import Trader













from .NetQuantity import NetQuantity

















from .ProductPublish import ProductPublish









from .CustomOrder import CustomOrder













from .ReturnConfig import ReturnConfig

from .TeaserTag import TeaserTag





from .Media1 import Media1








class ProductCreateUpdate(BaseSchema):
    # Catalog swagger.json

    
    category_slug = fields.Str(required=False)
    
    change_request_id = fields.Raw(required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier, required=False)
    
    trader = fields.List(fields.Nested(Trader, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    short_description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    size_guide = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    variants = fields.Dict(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    item_code = fields.Raw(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    product_publish = fields.Nested(ProductPublish, required=False)
    
    name = fields.Raw(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    multi_size = fields.Boolean(required=False)
    
    brand_uid = fields.Int(required=False)
    
    custom_order = fields.Nested(CustomOrder, required=False)
    
    uid = fields.Int(required=False)
    
    variant_media = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    bulk_job_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    teaser_tag = fields.Nested(TeaserTag, required=False)
    
    item_type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    requester = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    

