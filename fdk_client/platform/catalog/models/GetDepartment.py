"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















from .UserSerializer import UserSerializer









from .UserSerializer import UserSerializer





class GetDepartment(BaseSchema):
    #  swagger.json

    
    search = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    page_size = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    priority_order = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    page_no = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    slug = fields.Str(required=False)
    
