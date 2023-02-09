"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .UserDetail import UserDetail





from .UserDetail import UserDetail











from .UserDetail import UserDetail











class DepartmentModel(BaseSchema):
    #  swagger.json

    
    verified_on = fields.Str(required=False)
    
    name = fields.Raw(required=False)
    
    created_on = fields.Str(required=False)
    
    _id = fields.Raw(required=False)
    
    modified_by = fields.Nested(UserDetail, required=False)
    
    modified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserDetail, required=False)
    
    slug = fields.Raw(required=False)
    
    synonyms = fields.List(fields.Raw(required=False), required=False)
    
    priority_order = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserDetail, required=False)
    
    uid = fields.Int(required=False)
    
    logo = fields.Raw(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    _cls = fields.Raw(required=False)
    
