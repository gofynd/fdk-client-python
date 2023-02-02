"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















from .Trader import Trader



















from .ProductPublish import ProductPublish



















from .ReturnConfig import ReturnConfig





from .TaxIdentifier import TaxIdentifier



from .Media1 import Media1







from .TeaserTag import TeaserTag









from .NetQuantity import NetQuantity









from .CustomOrder import CustomOrder



class ProductCreateUpdateSchemaV2(BaseSchema):
    #  swagger.json

    
    bulk_job_id = fields.Str(required=False)
    
    item_code = fields.Raw(required=False)
    
    template_tag = fields.Str(required=False)
    
    name = fields.Raw(required=False)
    
    is_set = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    variant_group = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader, required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    requester = fields.Str(required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    size_guide = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    product_publish = fields.Nested(ProductPublish, required=False)
    
    multi_size = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    variant_media = fields.Dict(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    variants = fields.Dict(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    brand_uid = fields.Int(required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier, required=False)
    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    category_slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    teaser_tag = fields.Nested(TeaserTag, required=False)
    
    short_description = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    change_request_id = fields.Raw(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    item_type = fields.Str(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    custom_order = fields.Nested(CustomOrder, required=False)
    
