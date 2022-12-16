"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .ManifestFilter import ManifestFilter





class GeneratedManifestItem(BaseSchema):
    #  swagger.json

    
    created_by = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    filters = fields.Nested(ManifestFilter, required=False)
    
    status = fields.Str(required=False)
    