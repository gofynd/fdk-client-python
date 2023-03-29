"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class PlatformItem(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    l3_category = fields.Int(required=False)
    
    department_id = fields.Int(required=False)
    
    l3_category_name = fields.Str(required=False)
    
    images = fields.List(fields.Str(required=False), required=False)
    
    can_return = fields.Boolean(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    size = fields.Str(required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Int(required=False)
    
    color = fields.Str(required=False)
    

