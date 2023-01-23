"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



















from .ProductBundleItem import ProductBundleItem






class ProductBundleUpdateRequest(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    products = fields.List(fields.Nested(ProductBundleItem, required=False), required=False)
    
    choice = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

