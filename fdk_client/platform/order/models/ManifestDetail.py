"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ManifestFilter import ManifestFilter







from .ManifestDetailMeta import ManifestDetailMeta













class ManifestDetail(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    created_by = fields.Str(required=False)
    
    filters = fields.Nested(ManifestFilter, required=False)
    
    company_id = fields.Int(required=False)
    
    user_id = fields.Int(required=False)
    
    meta = fields.Nested(ManifestDetailMeta, required=False)
    
    created_at = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    manifest_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
