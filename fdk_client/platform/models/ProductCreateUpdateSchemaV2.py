"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .TaxIdentifier import TaxIdentifier





from .NetQuantity import NetQuantity















from .ProductPublish import ProductPublish

from .Trader import Trader















from .CustomOrder import CustomOrder





from .ReturnConfig import ReturnConfig





from .TeaserTag import TeaserTag

from .Media1 import Media1


















class ProductCreateUpdateSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    variant_media = fields.Dict(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier, required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    uid = fields.Int(required=False)
    
    template_tag = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    requester = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    size_guide = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    product_publish = fields.Nested(ProductPublish, required=False)
    
    trader = fields.List(fields.Nested(Trader, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    item_code = fields.Str(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    category_slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    custom_order = fields.Nested(CustomOrder, required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    brand_uid = fields.Int(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    variants = fields.Dict(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    teaser_tag = fields.Nested(TeaserTag, required=False)
    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    description = fields.Str(required=False)
    
    sizes = fields.List(fields.Dict(required=False), required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    variant_group = fields.Dict(required=False)
    
    short_description = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    change_request_id = fields.Raw(required=False)
    
    bulk_job_id = fields.Str(required=False)
    

