"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class DepartmentCreateUpdate(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    platforms = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    _cls = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

