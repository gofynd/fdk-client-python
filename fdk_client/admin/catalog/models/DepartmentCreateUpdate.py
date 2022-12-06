"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


























class DepartmentCreateUpdate(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    platforms = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    priority_order = fields.Int(required=False)
    
    _cls = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
