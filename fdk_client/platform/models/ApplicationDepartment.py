"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class ApplicationDepartment(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    

