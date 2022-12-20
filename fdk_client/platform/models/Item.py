"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





































from .Attributes import Attributes












class Item(BaseSchema):
    # Order swagger.json

    
    l3_category = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    l3_category_name = fields.Str(required=False)
    
    l1_category_id = fields.Int(required=False)
    
    l2_category = fields.List(fields.Str(required=False), required=False)
    
    brand_id = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Str(required=False)
    
    l2_category_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    color = fields.Str(required=False)
    
    last_updated_at = fields.Str(required=False)
    
    branch_url = fields.Str(required=False)
    
    attributes = fields.Nested(Attributes, required=False)
    
    gender = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    webstore_product_url = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    department_id = fields.Int(required=False)
    

