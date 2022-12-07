"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ManifestFilter import ManifestFilter



from .ManifestDetailMeta import ManifestDetailMeta

















class ManifestDetail(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Str(required=False)
    
    filters = fields.Nested(ManifestFilter, required=False)
    
    meta = fields.Nested(ManifestDetailMeta, required=False)
    
    status = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    
    user_id = fields.Int(required=False)
    
