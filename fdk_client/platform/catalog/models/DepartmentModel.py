"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
























from .UserDetail import UserDetail





from .UserDetail import UserDetail







from .UserDetail import UserDetail



class DepartmentModel(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    _cls = fields.Raw(required=False)
    
    uid = fields.Int(required=False)
    
    priority_order = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Raw(required=False)
    
    modified_on = fields.Str(required=False)
    
    slug = fields.Raw(required=False)
    
    synonyms = fields.List(fields.Raw(required=False), required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserDetail, required=False)
    
    logo = fields.Str(required=False)
    
    verified_by = fields.Nested(UserDetail, required=False)
    
    created_on = fields.Str(required=False)
    
    _id = fields.Raw(required=False)
    
    created_by = fields.Nested(UserDetail, required=False)
    
