"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .Trader1 import Trader1

















from .ProductPublish1 import ProductPublish1



from .CustomOrder1 import CustomOrder1





from .TaxIdentifier1 import TaxIdentifier1



















from .Media3 import Media3











from .TeaserTag1 import TeaserTag1





from .NetQuantity import NetQuantity











from .ReturnConfig1 import ReturnConfig1











class ProductPatch(BaseSchema):
    #  swagger.json

    
    short_description = fields.Str(required=False)
    
    requester = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    size_guide = fields.Str(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    item_code = fields.Raw(required=False)
    
    variant_media = fields.Dict(required=False)
    
    item_type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    change_request_id = fields.Raw(required=False)
    
    product_publish = fields.Nested(ProductPublish1, required=False)
    
    custom_order = fields.Nested(CustomOrder1, required=False)
    
    company_id = fields.Int(required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier1, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    template_tag = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    action = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    multi_size = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    media = fields.List(fields.Nested(Media3, required=False), required=False)
    
    description = fields.Str(required=False)
    
    variants = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    bulk_job_id = fields.Str(required=False)
    
    teaser_tag = fields.Nested(TeaserTag1, required=False)
    
    brand_uid = fields.Int(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    name = fields.Str(required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    category_slug = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
