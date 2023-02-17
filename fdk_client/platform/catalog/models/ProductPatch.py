"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .TaxIdentifier1 import TaxIdentifier1









from .ProductPublish1 import ProductPublish1













from .Trader1 import Trader1







from .NetQuantity import NetQuantity





from .Media3 import Media3

































from .CustomOrder1 import CustomOrder1







from .ReturnConfig1 import ReturnConfig1







from .TeaserTag1 import TeaserTag1



class ProductPatch(BaseSchema):
    #  swagger.json

    
    category_slug = fields.Str(required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier1, required=False)
    
    size_guide = fields.Str(required=False)
    
    bulk_job_id = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    product_publish = fields.Nested(ProductPublish1, required=False)
    
    template_tag = fields.Str(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    action = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    variant_media = fields.Dict(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    currency = fields.Str(required=False)
    
    media = fields.List(fields.Nested(Media3, required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    change_request_id = fields.Raw(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    item_type = fields.Str(required=False)
    
    item_code = fields.Raw(required=False)
    
    requester = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    variants = fields.Dict(required=False)
    
    custom_order = fields.Nested(CustomOrder1, required=False)
    
    multi_size = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    teaser_tag = fields.Nested(TeaserTag1, required=False)
    
