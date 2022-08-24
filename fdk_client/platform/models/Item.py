"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














































class Item(BaseSchema):
    # Order swagger.json

    
    size = fields.Str(required=False)
    
    department_id = fields.Int(required=False)
    
    brand_id = fields.Int(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    color = fields.Str(required=False)
    
    brand = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    last_updated_at = fields.Int(required=False)
    
    gender = fields.Str(required=False)
    
    l3_category = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    l2_category = fields.List(fields.Str(required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    slug_key = fields.Str(required=False)
    
    l3_category_name = fields.Str(required=False)
    
    webstore_product_url = fields.Str(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    branch_url = fields.Str(required=False)
    

