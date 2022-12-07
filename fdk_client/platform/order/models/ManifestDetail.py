"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .ManifestDetailMeta import ManifestDetailMeta







from .ManifestFilter import ManifestFilter











class ManifestDetail(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    company_id = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    meta = fields.Nested(ManifestDetailMeta, required=False)
    
    status = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    
    filters = fields.Nested(ManifestFilter, required=False)
    
    id = fields.Int(required=False)
    
    user_id = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
