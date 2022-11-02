"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


























class Item(BaseSchema):
    # Orders swagger.json

    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Int(required=False)
    
    department_id = fields.Int(required=False)
    
    l3_category = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    l3_category_name = fields.Str(required=False)
    

