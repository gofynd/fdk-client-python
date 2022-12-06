"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .ManifestFilter import ManifestFilter




class GeneratedManifestItem(BaseSchema):
    # Order swagger.json

    
    manifest_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    filters = fields.Nested(ManifestFilter, required=False)
    
    created_at = fields.Str(required=False)
    

