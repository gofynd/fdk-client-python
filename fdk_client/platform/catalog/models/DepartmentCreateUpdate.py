"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


























class DepartmentCreateUpdate(BaseSchema):
    #  swagger.json

    
    _cls = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    priority_order = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Str(required=False)
    
    platforms = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
