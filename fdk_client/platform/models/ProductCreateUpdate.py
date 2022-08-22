"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Media1 import Media1



from .OrderQuantity import OrderQuantity













from .ReturnConfig import ReturnConfig







from .ProductPublish import ProductPublish





from .TeaserTag import TeaserTag























from .Trader import Trader

from .CustomOrder import CustomOrder










class ProductCreateUpdate(BaseSchema):
    # Catalog swagger.json

    
    is_set = fields.Boolean(required=False)
    
    hsn_code = fields.Str(required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    brand_uid = fields.Int(required=False)
    
    moq = fields.Nested(OrderQuantity, required=False)
    
    template_tag = fields.Str(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    requester = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    product_publish = fields.Nested(ProductPublish, required=False)
    
    name = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    teaser_tag = fields.Nested(TeaserTag, required=False)
    
    slug = fields.Str(required=False)
    
    bulk_job_id = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    size_guide = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    multi_size = fields.Boolean(required=False)
    
    short_description = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    category_slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader, required=False), required=False)
    
    custom_order = fields.Nested(CustomOrder, required=False)
    
    variants = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    change_request_id = fields.Str(required=False)
    

