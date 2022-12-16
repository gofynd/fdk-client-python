"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






























class PlatformItem(BaseSchema):
    #  swagger.json

    
    l3_category = fields.Int(required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    department_id = fields.Int(required=False)
    
    color = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    id = fields.Int(required=False)
    
    l3_category_name = fields.Str(required=False)
    
    images = fields.List(fields.Str(required=False), required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    