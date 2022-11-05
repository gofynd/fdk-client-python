"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .UserDetail import UserDetail

from .UserDetail import UserDetail





from .UserDetail import UserDetail






















class DepartmentModel(BaseSchema):
    # Catalog swagger.json

    
    priority_order = fields.Int(required=False)
    
    verified_by = fields.Nested(UserDetail, required=False)
    
    created_by = fields.Nested(UserDetail, required=False)
    
    slug = fields.Raw(required=False)
    
    logo = fields.Str(required=False)
    
    modified_by = fields.Nested(UserDetail, required=False)
    
    verified_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    _cls = fields.Raw(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Raw(required=False)
    
    modified_on = fields.Str(required=False)
    
    synonyms = fields.List(fields.Raw(required=False), required=False)
    
    _id = fields.Raw(required=False)
    
    created_on = fields.Str(required=False)
    

