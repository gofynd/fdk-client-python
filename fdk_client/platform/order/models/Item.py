"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Attributes import Attributes











































class Item(BaseSchema):
    #  swagger.json

    
    slug_key = fields.Str(required=False)
    
    l2_category_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    attributes = fields.Nested(Attributes, required=False)
    
    branch_url = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    webstore_product_url = fields.Str(required=False)
    
    brand = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    department_id = fields.Int(required=False)
    
    gender = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    l1_category_id = fields.Int(required=False)
    
    l2_category = fields.List(fields.Str(required=False), required=False)
    
    item_id = fields.Int(required=False)
    
    l3_category = fields.Int(required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    last_updated_at = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    l3_category_name = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    