"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .Media3 import Media3





from .CustomOrder1 import CustomOrder1















from .NetQuantity import NetQuantity













from .ProductPublish1 import ProductPublish1







from .Trader1 import Trader1



from .TaxIdentifier1 import TaxIdentifier1





















from .ReturnConfig2 import ReturnConfig2





from .TeaserTag1 import TeaserTag1













class ProductPatch(BaseSchema):
    #  swagger.json

    
    description = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    media = fields.List(fields.Nested(Media3, required=False), required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    custom_order = fields.Nested(CustomOrder1, required=False)
    
    short_description = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    bulk_job_id = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    template_tag = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    requester = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    variant_media = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    change_request_id = fields.Raw(required=False)
    
    product_publish = fields.Nested(ProductPublish1, required=False)
    
    action = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier1, required=False)
    
    variants = fields.Dict(required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    category_slug = fields.Str(required=False)
    
    size_guide = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    item_type = fields.Str(required=False)
    
    teaser_tag = fields.Nested(TeaserTag1, required=False)
    
    multi_size = fields.Boolean(required=False)
    
    item_code = fields.Raw(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
