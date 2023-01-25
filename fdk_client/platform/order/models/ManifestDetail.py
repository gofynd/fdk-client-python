"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ManifestDetailMeta import ManifestDetailMeta







from .ManifestFilter import ManifestFilter















class ManifestDetail(BaseSchema):
    #  swagger.json

    
    manifest_id = fields.Str(required=False)
    
    meta = fields.Nested(ManifestDetailMeta, required=False)
    
    uid = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    filters = fields.Nested(ManifestFilter, required=False)
    
    created_by = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    user_id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
