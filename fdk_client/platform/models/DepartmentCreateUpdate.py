"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class DepartmentCreateUpdate(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    platforms = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    priority_order = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    _cls = fields.Str(required=False)
    

