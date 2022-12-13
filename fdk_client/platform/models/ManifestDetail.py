"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .ManifestDetailMeta import ManifestDetailMeta

from .ManifestFilter import ManifestFilter




class ManifestDetail(BaseSchema):
    # Order swagger.json

    
    manifest_id = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    user_id = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    meta = fields.Nested(ManifestDetailMeta, required=False)
    
    filters = fields.Nested(ManifestFilter, required=False)
    
    is_active = fields.Boolean(required=False)
    

