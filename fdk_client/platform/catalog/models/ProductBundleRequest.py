"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






























from .ProductBundleItem import ProductBundleItem



class ProductBundleRequest(BaseSchema):
    #  swagger.json

    
    logo = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    choice = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    products = fields.List(fields.Nested(ProductBundleItem, required=False), required=False)
    
