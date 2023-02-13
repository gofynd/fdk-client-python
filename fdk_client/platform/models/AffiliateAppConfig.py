"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .AffiliateAppConfigMeta import AffiliateAppConfigMeta










class AffiliateAppConfig(BaseSchema):
    # OrderManage swagger.json

    
    secret = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    meta = fields.List(fields.Nested(AffiliateAppConfigMeta, required=False), required=False)
    
    name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    owner = fields.Str(required=False)
    
