"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class AppConfigurationsSort(BaseSchema):
    # Catalog swagger.json

    
    is_default = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    default_key = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    key = fields.Str(required=False)
    

