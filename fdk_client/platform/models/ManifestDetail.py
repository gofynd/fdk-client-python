"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .ManifestDetailMeta import ManifestDetailMeta











from .ManifestFilter import ManifestFilter


class ManifestDetail(BaseSchema):
    # Orders swagger.json

    
    is_active = fields.Boolean(required=False)
    
    company_id = fields.Int(required=False)
    
    user_id = fields.Int(required=False)
    
    created_by = fields.Str(required=False)
    
    meta = fields.Nested(ManifestDetailMeta, required=False)
    
    created_at = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    filters = fields.Nested(ManifestFilter, required=False)
    

