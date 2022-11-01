"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












































class ProductDetails(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Raw(required=False)
    
    is_set = fields.Boolean(required=False)
    
    slug = fields.Raw(required=False)
    
    template_tag = fields.Raw(required=False)
    
    brand_uid = fields.Int(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    country_of_origin = fields.Raw(required=False)
    
    item_code = fields.Raw(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    rating_count = fields.Int(required=False)
    
    description = fields.Raw(required=False)
    
    highlights = fields.List(fields.Raw(required=False), required=False)
    
    media = fields.List(fields.Dict(required=False), required=False)
    
    hsn_code = fields.Int(required=False)
    
    grouped_attributes = fields.Dict(required=False)
    
    short_description = fields.Raw(required=False)
    
    image_nature = fields.Raw(required=False)
    
    identifier = fields.Dict(required=False)
    
    rating = fields.Float(required=False)
    
    images = fields.List(fields.Raw(required=False), required=False)
    

