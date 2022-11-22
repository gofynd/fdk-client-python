"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductInGroup import ProductInGroup









from .UserDetail import UserDetail















from .UserDetail import UserDetail





from .UserDetail import UserDetail


class ProductGroupingModel(BaseSchema):
    # Catalog swagger.json

    
    products = fields.List(fields.Nested(ProductInGroup, required=False), required=False)
    
    logo = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Raw(required=False)
    
    modified_by = fields.Nested(UserDetail, required=False)
    
    choice = fields.Raw(required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    verified_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    page_visibility = fields.List(fields.Raw(required=False), required=False)
    
    slug = fields.Raw(required=False)
    
    company_id = fields.Int(required=False)
    
    created_by = fields.Nested(UserDetail, required=False)
    
    _id = fields.Raw(required=False)
    
    created_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserDetail, required=False)
    

